from flask_wtf import FlaskForm
from wtforms import FormField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from descriptions import features


class ModelForm(FlaskForm):
    model = SelectField(
        label="Select the Model",
        choices=[(0, "Isolation Forest"), (1, "AutoEncoder")],
        coerce=int,
        validators=[DataRequired()],
    )


class DataForm(FlaskForm):
    duration = IntegerField(
        label=features[0][0],
        description=features[0][1],
        validators=[
            DataRequired(),
            NumberRange(min=0, max=10_000, message=features[0][2]),
        ],
    )

    protocol_type = SelectField(
        label=features[1][0],
        description=features[1][1],
        choices=[("tcp", "TCP"), ("udp", "UDP"), ("icmp", "ICMP")],
        validators=[DataRequired()],
    )

    service = SelectField(
        label=features[2][0],
        description=features[2][1],
        choices=sorted(
            [
                ("http", "http"),
                ("smtp", "smtp"),
                ("domain_u", "domain_u"),
                ("auth", "auth"),
                ("finger", "finger"),
                ("telnet", "telnet"),
                ("eco_i", "eco_i"),
                ("ftp", "ftp"),
                ("ntp_u", "ntp_u"),
                ("ecr_i", "ecr_i"),
                ("other", "other"),
                ("urp_i", "urp_i"),
                ("private", "private"),
                ("pop_3", "pop_3"),
                ("ftp_data", "ftp_data"),
                ("netstat", "netstat"),
                ("daytime", "daytime"),
                ("ssh", "ssh"),
                ("echo", "echo"),
                ("time", "time"),
                ("name", "name"),
                ("whois", "whois"),
                ("domain", "domain"),
                ("mtp", "mtp"),
                ("gopher", "gopher"),
                ("remote_job", "remote_job"),
                ("rje", "rje"),
                ("ctf", "ctf"),
                ("supdup", "supdup"),
                ("link", "link"),
                ("systat", "systat"),
                ("discard", "discard"),
                ("X11", "X11"),
                ("shell", "shell"),
                ("login", "login"),
                ("imap4", "imap4"),
                ("nntp", "nntp"),
                ("uucp", "uucp"),
                ("pm_dump", "pm_dump"),
                ("IRC", "IRC"),
                ("Z39_50", "Z39_50"),
                ("netbios_dgm", "netbios_dgm"),
                ("ldap", "ldap"),
                ("sunrpc", "sunrpc"),
                ("courier", "courier"),
                ("exec", "exec"),
                ("bgp", "bgp"),
                ("csnet_ns", "csnet_ns"),
                ("http_443", "http_443"),
                ("klogin", "klogin"),
                ("printer", "printer"),
                ("netbios_ssn", "netbios_ssn"),
                ("pop_2", "pop_2"),
                ("nnsp", "nnsp"),
                ("efs", "efs"),
                ("hostnames", "hostnames"),
                ("uucp_path", "uucp_path"),
                ("sql_net", "sql_net"),
                ("vmnet", "vmnet"),
                ("iso_tsap", "iso_tsap"),
                ("netbios_ns", "netbios_ns"),
                ("kshell", "kshell"),
                ("urh_i", "urh_i"),
                ("http_2784", "http_2784"),
                ("harvest", "harvest"),
                ("aol", "aol"),
                ("tftp_u", "tftp_u"),
                ("http_8001", "http_8001"),
                ("tim_i", "tim_i"),
                ("red_i", "red_i"),
            ],
            key=lambda x: x[1],
        ),
        validators=[DataRequired()],
    )

    src_bytes = IntegerField(
        label=features[3][0],
        description=features[3][1],
        validators=[
            DataRequired(),
            NumberRange(min=0, max=1_500_000, message=features[3][2]),
        ],
    )

    dst_bytes = IntegerField(
        label=features[4][0],
        description=features[4][1],
        validators=[
            DataRequired(),
            NumberRange(min=0, max=1_500_000, message=features[4][2]),
        ],
    )

    logged_in = SelectField(
        label=features[5][0],
        description=features[5][1],
        choices=[(1, "Yes"), (0, "No")],
        coerce=int,
        validators=[DataRequired()],
    )

    count = IntegerField(
        label=features[6][0],
        description=features[6][1],
        validators=[
            DataRequired(),
            NumberRange(min=0, max=511, message=features[6][2]),
        ],
    )

    srv_count = IntegerField(
        label=features[7][0],
        description=features[7][1],
        validators=[
            DataRequired(),
            NumberRange(min=0, max=511, message=features[7][2]),
        ],
    )

    dst_host_count = IntegerField(
        label=features[8][0],
        description=features[8][1],
        validators=[
            DataRequired(),
            NumberRange(min=0, max=255, message=features[8][2]),
        ],
    )

    dst_host_srv_count = IntegerField(
        label=features[9][0],
        description=features[9][1],
        validators=[
            DataRequired(),
            NumberRange(min=0, max=255, message=features[9][2]),
        ],
    )


class Form(FlaskForm):
    model = FormField(ModelForm)
    data = FormField(DataForm)

    submit = SubmitField(label="Predict")
