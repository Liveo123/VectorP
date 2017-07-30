import sys
from VectorP import VectorP

def main():
    """Test function for running the vector library.
    :returns: none
    """
    #vec1 = VectorP([8.218, -9.341])
    #vec2 = VectorP([-1.129, 2.111])
    
    #vec3 = VectorP([7.119, 8.215])
    #vec4 = VectorP([-8.223, 0.878])

    vec1 = VectorP([2, 2], 2)
    vec2 = VectorP([5, 6])

    print(vec1.magnitude())
    
    print(vec1.direction())

if __name__ == "__main__":
    main()
