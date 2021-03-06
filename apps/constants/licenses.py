from tower import ugettext_lazy as _lazy


# Built-in Licenses
class _LicenseBase(object):
    """Base class for built-in licenses."""
    icons = ''  # CSS classes. See zamboni.css for a list.
    some_rights = True


class LICENSE_COPYRIGHT(_LicenseBase):
    id = 1
    name = _lazy(u'All Rights Reserved')
    icons = 'copyr'
    some_rights = False
    url = None


class LICENSE_CC_BY(_LicenseBase):
    id = 2
    name = _lazy(u'Creative Commons Attribution 3.0')
    url = 'http://creativecommons.org/licenses/by/3.0/'
    icons = 'cc-attrib'


class LICENSE_CC_BY_NC(_LicenseBase):
    id = 3
    icons = 'cc-attrib cc-noncom'
    name = _lazy(u'Creative Commons Attribution-NonCommercial 3.0')
    url = 'http://creativecommons.org/licenses/by-nc/3.0/'


class LICENSE_CC_BY_NC_ND(_LicenseBase):
    id = 4
    icons = 'cc-attrib cc-noncom cc-noderiv'
    name = _lazy(u'Creative Commons Attribution-NonCommercial-NoDerivs 3.0')
    url = 'http://creativecommons.org/licenses/by-nc-nd/3.0/'


class LICENSE_CC_BY_NC_SA(_LicenseBase):
    id = 5
    icons = 'cc-attrib cc-noncom cc-share'
    name = _lazy(u'Creative Commons Attribution-NonCommercial-Share Alike 3.0')
    url = 'http://creativecommons.org/licenses/by-nc-sa/3.0/'


class LICENSE_CC_BY_ND(_LicenseBase):
    id = 6
    icons = 'cc-attrib cc-noderiv'
    name = _lazy(u'Creative Commons Attribution-NoDerivs 3.0')
    url = 'http://creativecommons.org/licenses/by-nd/3.0/'


class LICENSE_CC_BY_SA(_LicenseBase):
    id = 7
    icons = 'cc-attrib cc-share'
    name = _lazy(u'Creative Commons Attribution-ShareAlike 3.0')
    url = 'http://creativecommons.org/licenses/by-sa/3.0/'


PERSONA_LICENSES = (LICENSE_COPYRIGHT, LICENSE_CC_BY, LICENSE_CC_BY_NC,
                    LICENSE_CC_BY_NC_ND, LICENSE_CC_BY_NC_SA, LICENSE_CC_BY_ND,
                    LICENSE_CC_BY_SA)
PERSONA_LICENSES_CHOICES = [(l.id, l) for l in PERSONA_LICENSES]
PERSONA_LICENSES_IDS = dict(PERSONA_LICENSES_CHOICES)
