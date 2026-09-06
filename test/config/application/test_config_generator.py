from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.config.application.config_generator import ConfigGenerator
from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.shared.domain.config_repository import ConfigRepository
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestConfigGenerator:
    def test_should_generate_config(self) -> None:
        question_wizard = Mock(QuestionWizard)
        config_repository = Mock(ConfigRepository)
        config_generator = ConfigGenerator(question_wizard=question_wizard, repository=config_repository)
        config = ConfigSchemaMother.any()

        expect_call(question_wizard).run().returns(config)
        expect_call(config_repository).write(config)

        config_generator.execute()

        expect(question_wizard).to(have_been_satisfied)
        expect(config_repository).to(have_been_satisfied)
