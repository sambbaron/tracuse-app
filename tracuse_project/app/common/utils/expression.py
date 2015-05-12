"""Expression Language for Setting Element Values"""

import os

from django.conf import settings
from django.template.loader import render_to_string


def expr_django_template(expr_string, data_dict,
                         save_template=False, template_name="", template_dir=""):
    """Convert django template string expression into value

    Temporary template file is created and optionally destroyed
    Template must be 'recognized' by django in order to render

    Arguments:
        expr_string (string): In, django template language
        data_dict (dict): 'context' dictionary for template engine
        save_template (boolean, default=False):
            Option to delete temporary template file
        template_name (string, optional, default="expr.html"):
            Optional template name
        template_dir (string, optional, default=django template path):
            Directory to save temporary template

    Returns:
        rendered string
    """
    if not template_name:
        template_name = "expr.html"

    template_path = os.path.join(settings.TEMPLATE_PATH,
                                 template_dir,
                                 template_name
                                 )

    with open(template_path, "w") as f:
        f.write(expr_string)

    template_result = render_to_string(template_name, data_dict)

    if not save_template:
        os.remove(template_path)

    return template_result
