# WARNING: creates infinite loop (paradox)

def this_statement
  this_statement == false
end

this_statement
