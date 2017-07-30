
import pdb
import math
import numpy as np 


class VectorP(object):
    
    """ A class used to manipulate numpy vectors.

        Arg1 - coordinates - A numpy array used to hold the VectorP
        Arg2 - dataType - Datatype to convert to if necessary
                      0 - No conversion required
                      1 - Convert to int
                      2 - Convert to float
    """

    def __init__(self, coordinates, dataType = 0):
        try:
            
            if not coordinates:
                raise ValueError
            self.coordinates = np.array(coordinates)
            self.dimension = len(coordinates)
            
            # Convert coordinates if necessary
            if dataType == 1:
                self.coordinates =  self.coordinates.astype(np.int)
            elif dataType == 2:
                self.coordinates =  self.coordinates.astype(np.float)

            # Constants
            self.SQUARE = 2

        except ValueError:
            raise ValueError('The coordinates are not empty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector:{}'.format(self.coordinates)

    def __eq__(self, v):
        """ Finds the result of comparing the current object with the one passed in. 

        :arg1: v - The vector to compare with 
        :returns: True if they are the same, false if otherwise

        """
        return self.coordinates == v.coordinates

    def __add__(self, other):
        """ Finds the result of adding other vector to the self vector. 

        :arg1: other - The vector which is taken away from the self vector 
        :returns: self-coordinates - other

        """
        try:
            result = []
            for i in range(len(self.coordinates)):
                result.append(self.coordinates[i] + other.coordinates[i])
        
        except IndexError:
            raise IndexError('Ensure both of your vectors are the same size.')
        
        return(tuple(result))

    
    def __sub__(self, other):
        """ Finds the result of subtracting the other vector from the self vector. 

        :arg1: other - The vector which is taken away from the self vector 
        :returns: self-coordinates - other

        """
        try:
            result = []
            for i in range(len(self.coordinates)):
                result.append(self.coordinates[i] - other.coordinates[i])
                print("{}".format(result[i]))

        except IndexError:
            raise IndexError('Ensure both of your vectors are the same size.')
        
        return(tuple(result))
      

    def __mul__(self, scalar):
        """ Multiples each element of object vector with the argument

        :arg1: scalar - The floating point scalar to multiply with
        :returns: The resulting vector 

        """
        try:
            result = np.copy(self.coordinates)
            for i in range(len(result)):
                result[i] =  result[i] * (scalar + 0.0)
        except AttributeError:
            raise AttributeError('Ensure you are multiplying with a scalar, not a VectorP')
        return(result)


    def magnitude(self):
        """ Finds the magnitude of a vetor using pythag.
        :returns: the magnitude

        """
        result = 0

        # Add together the square of all of the vector coords...
        for c in self.coordinates:
            result += math.pow(c, self.SQUARE)

        # Return the pythag of the hypotenuse
        return math.sqrt(result)

    def direction(self):
        """ Use to find the unit vector for the vector, which is the canonical element.

        The unit vector is (1/|v|)*v
        :returns: The unit vector of this vector.

        """
        
        # First get the reciprocal of the magnitude...
        multiplier = 1/self.magnitude()
        print("multiplier = {}".format(multiplier))

        # now multiply by the vector itself and return
        
        return(multiplier * self.coordinates)


