from cmath import exp
 
def fft(x):
    n = len(x)
    if n <= 1: return x
    e = fft(x[0::2])
    o =  fft(x[1::2])
    T= [exp(-2j*3.14159265359*k/N)*o[k] for i in range(n//2)]
    return [e[i] + T[i] for i in range(n//2)] + \
           [e[i] - T[i] for i in range(n//2)]

The convolution theorem states that under suitable conditions the Fourier transform of a convolution is the pointwise product of Fourier transforms.  This allows us to sa