from assertpy import assert_that, soft_assertions




class UserAsserts:

    @staticmethod
    def assert_get_user_response(expected_body, actual_body):
        response_id = actual_body.get('id', strict=False)
        assert_that(response_id, 'id of response').is_not_none()

        with soft_assertions():
            for k in expected_body:
                assert_that(expected_body[k], k).is_equal_to(actual_body[k])
