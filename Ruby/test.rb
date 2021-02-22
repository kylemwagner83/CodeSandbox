# ruby test.rb

def count_ones(matrix)
  ones = 0
  for x in matrix
    for y in x
      if y == 1
        ones += 1
      end
    end
  end
  return ones
end




matrix = [
  [1, 2, 3],
  [0, 2, 1],
  [5, 7, 33]
]

print count_ones(matrix)