class Mortal

  def initialize
    @dead = false
    @sticky = true
  end

  def die
    @dead = true
  end
  
end

class Man < Mortal

end

@socrates = Man.new

@socrates.is_a?(Mortal) #should return true
