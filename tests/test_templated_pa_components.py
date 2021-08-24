import unittest

from fds.analyticsapi.engines.api.templated_pa_components_api import TemplatedPAComponentsApi
from fds.analyticsapi.engines.api.unlinked_pa_templates_api import UnlinkedPATemplatesApi
from fds.analyticsapi.engines.model.templated_pa_component_parameters import TemplatedPAComponentParameters
from fds.analyticsapi.engines.model.templated_pa_component_parameters_root import TemplatedPAComponentParametersRoot
from fds.analyticsapi.engines.model.pa_component_data import PAComponentData
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pa_calculation_group import PACalculationGroup
from fds.analyticsapi.engines.model.pa_calculation_column import PACalculationColumn
from fds.analyticsapi.engines.model.templated_pa_component_summary import TemplatedPAComponentSummary
from fds.analyticsapi.engines.model.templated_pa_component_update_parameters import TemplatedPAComponentUpdateParameters
from fds.analyticsapi.engines.model.templated_pa_component_update_parameters_root import TemplatedPAComponentUpdateParametersRoot


from common_functions import CommonFunctions

class TestTemplatedPaComponents(unittest.TestCase):
    def setUp(self):
        self.templated_pa_components_api = TemplatedPAComponentsApi(CommonFunctions.build_api_client())
        self.unlinked_pa_templates_api = UnlinkedPATemplatesApi(CommonFunctions.build_api_client())

    def test_create_templated_pa_component(self):
        templates = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            directory = "Personal:UnlinkedPATemplates/"
        )
        parent_template_id = list(templates[0].data.keys())[0]

        templated_pa_component_parameters = TemplatedPAComponentParameters(
            directory="Personal:TemplatedPAComponents/",
            parent_template_id=parent_template_id,
            description="This is a templated PA component",
            component_data = PAComponentData(
                accounts = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "MSCI_USA:984000",
                        holdingsmode = "B&H")],
                benchmarks = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "DJGX:AMERICAS",
                        holdingsmode = "B&H")],
                columns = [
                    PACalculationColumn(
                        id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                        statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
                groups = [
                    PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
                currencyisocode = "USD",
                componentdetail = "GROUPS"
            )
        )

        templated_pa_component_parameters_root = TemplatedPAComponentParametersRoot(
            data = templated_pa_component_parameters
        )

        response = self.templated_pa_components_api.create_templated_pa_components(
            templated_pa_component_parameters_root = templated_pa_component_parameters_root)

        firstcomponent = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 201, "Response should be 201 - Success")
        self.assertEqual(type(response[0].data), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0].data[firstcomponent]),
            TemplatedPAComponentSummary, "Response should be of TemplatedPAComponentSummary type.")
        self.assertGreater(len(response[0].data), 0, "Response result should not be an empty list.")

    def test_update_templated_pa_component(self):
        # create templated PA component to use component id later
        templates = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            directory = "Personal:UnlinkedPATemplates/"
        )
        parent_template_id = list(templates[0].data.keys())[0]

        templated_pa_component_parameters = TemplatedPAComponentParameters(
            directory="Personal:TemplatedPAComponents/",
            parent_template_id=parent_template_id,
            description="This is a templated PA component",
            component_data = PAComponentData(
                accounts = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "MSCI_USA:984000",
                        holdingsmode = "B&H")],
                benchmarks = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "DJGX:AMERICAS",
                        holdingsmode = "B&H")],
                columns = [
                    PACalculationColumn(
                        id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                        statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
                groups = [
                    PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
                currencyisocode = "USD",
                componentdetail = "GROUPS"
            )
        )

        templated_pa_component_parameters_root = TemplatedPAComponentParametersRoot(
            data = templated_pa_component_parameters
        )

        components = self.templated_pa_components_api.create_templated_pa_components(
            templated_pa_component_parameters_root = templated_pa_component_parameters_root)

        component_id = list(components[0].data.keys())[0]

        # update templated PA component
        templated_pa_component_update_parameters = TemplatedPAComponentUpdateParameters(
            parent_template_id = parent_template_id,
            description = "This is an updated templated PA component",
            component_data = PAComponentData(
                accounts = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "MSCI_USA:984000",
                        holdingsmode = "B&H")],
                benchmarks = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "DJGX:AMERICAS",
                        holdingsmode = "B&H")],
                columns = [
                    PACalculationColumn(
                        id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                        statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
                groups = [
                    PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
                currencyisocode = "USD",
                componentdetail = "GROUPS"
            )
        )

        templated_pa_component_update_parameters_root = TemplatedPAComponentUpdateParametersRoot (
            data = templated_pa_component_update_parameters
        )

        response = self.templated_pa_components_api.update_templated_pa_components(
            id = component_id, templated_pa_component_update_parameters_root=templated_pa_component_update_parameters_root
        )

        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0].data[component_id]),
            TemplatedPAComponentSummary, "Response should be of TemplatedPAComponentSummary type.")
        self.assertGreater(len(response[0].data), 0, "Response result should not be an empty list.")

    def test_delete_templated_pa_component(self):
        # create templated PA component to use component id later
        templates = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            directory = "Personal:UnlinkedPATemplates/"
        )
        parent_template_id = list(templates[0].data.keys())[0]

        templated_pa_component_parameters = TemplatedPAComponentParameters(
            directory="Personal:TemplatedPAComponents/",
            parent_template_id=parent_template_id,
            description="This is a templated PA component",
            component_data = PAComponentData(
                accounts = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "MSCI_USA:984000",
                        holdingsmode = "B&H")],
                benchmarks = [
                    PAIdentifier(
                        id = "SPN:SP50",
                        holdingsmode = "B&H"),
                    PAIdentifier(
                        id = "DJGX:AMERICAS",
                        holdingsmode = "B&H")],
                columns = [
                    PACalculationColumn(
                        id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                        statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
                groups = [
                    PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
                currencyisocode = "USD",
                componentdetail = "GROUPS"
            )
        )

        templated_pa_component_parameters_root = TemplatedPAComponentParametersRoot(
            data = templated_pa_component_parameters
        )

        components = self.templated_pa_components_api.create_templated_pa_components(
            templated_pa_component_parameters_root = templated_pa_component_parameters_root)

        component_id = list(components[0].data.keys())[0]

        # delete templated PA component
        response = self.templated_pa_components_api.delete_templated_pa_components(
            id = component_id
        )

        self.assertEqual(response[1], 204, "Response should be 204 - Success")

if __name__ == '__main__':
    unittest.main()