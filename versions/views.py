from utils import response
from datetime import datetime
from versions.forms import VersionsForm

def view_enter_versions(request, enter_versions_template):
    return response(request, enter_versions_template, {'form':VersionsForm()})

def view_validate_versions(request, validate_versions_template, enter_versions_template):
    form = VersionsForm(request.POST)
    if form.is_valid():
        validated_versions = []
        versions_info = form.cleaned_data.get('versions')
        for (name, version_digits) in versions_info:
            version = {}
            version['name'] = name
            version['version'] = version_digits
            version['flag'] = _validate_version(name, version_digits)
            validated_versions.append(version)
        default_file_name = ''.join(('versions_',
                                     datetime.today().strftime('%Y_%b_%d'),
                                     '.txt'))
        return response(request, validate_versions_template, {'versions':validated_versions, 'default_file_name':default_file_name})
    return response(request, enter_versions_template, {'form':form})

def _validate_version(name, version_digits):
    return 'warning'

def view_generate_file(request, generate_versions_file_template):
    return response(request, generate_versions_file_template, {'form':form})
