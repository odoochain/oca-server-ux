import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-server-ux",
    description="Meta package for oca-server-ux Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-announcement>=15.0dev,<15.1dev',
        'odoo-addon-barcode_action>=15.0dev,<15.1dev',
        'odoo-addon-base_archive_date>=15.0dev,<15.1dev',
        'odoo-addon-base_cancel_confirm>=15.0dev,<15.1dev',
        'odoo-addon-base_custom_filter>=15.0dev,<15.1dev',
        'odoo-addon-base_duplicate_security_group>=15.0dev,<15.1dev',
        'odoo-addon-base_export_manager>=15.0dev,<15.1dev',
        'odoo-addon-base_field_deprecated>=15.0dev,<15.1dev',
        'odoo-addon-base_import_security_group>=15.0dev,<15.1dev',
        'odoo-addon-base_menu_visibility_restriction>=15.0dev,<15.1dev',
        'odoo-addon-base_optional_quick_create>=15.0dev,<15.1dev',
        'odoo-addon-base_recurrence>=15.0dev,<15.1dev',
        'odoo-addon-base_revision>=15.0dev,<15.1dev',
        'odoo-addon-base_search_custom_field_filter>=15.0dev,<15.1dev',
        'odoo-addon-base_substate>=15.0dev,<15.1dev',
        'odoo-addon-base_technical_features>=15.0dev,<15.1dev',
        'odoo-addon-base_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-base_tier_validation_formula>=15.0dev,<15.1dev',
        'odoo-addon-base_tier_validation_forward>=15.0dev,<15.1dev',
        'odoo-addon-base_tier_validation_report>=15.0dev,<15.1dev',
        'odoo-addon-base_tier_validation_server_action>=15.0dev,<15.1dev',
        'odoo-addon-chained_swapper>=15.0dev,<15.1dev',
        'odoo-addon-date_range>=15.0dev,<15.1dev',
        'odoo-addon-default_multi_user>=15.0dev,<15.1dev',
        'odoo-addon-document_quick_access>=15.0dev,<15.1dev',
        'odoo-addon-document_quick_access_folder_auto_classification>=15.0dev,<15.1dev',
        'odoo-addon-filter_multi_user>=15.0dev,<15.1dev',
        'odoo-addon-mass_editing>=15.0dev,<15.1dev',
        'odoo-addon-multi_step_wizard>=15.0dev,<15.1dev',
        'odoo-addon-sequence_reset_period>=15.0dev,<15.1dev',
        'odoo-addon-web_archive_date>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
