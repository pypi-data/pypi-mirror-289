(function_declaration
  modifiers: (modifiers 
    (annotation
      (user_type 
        (type_identifier) @annotation.test)))
  (simple_identifier) @test.name
  (function_value_parameters)
  (function_body) @test.body) @test.method
  (#eq? @annotation.test "Test")


(import_header) @import