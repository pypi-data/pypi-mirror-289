
class platform:

    # check for the platform type and use that information to search files specific to that platform

    models = ['PA-54', 'PA-70', 'PA-7500']

    def check_platform(str):
        result = False
        for model in  platform.models:
            if model in str:
                result = True

        return result
    
