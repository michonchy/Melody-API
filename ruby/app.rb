require 'json'

def handler(event:, context:)
    res = {
        text: 'Rubyからこんにちは'
      }
    { statusCode: 200, body: JSON.generate(res) }
end