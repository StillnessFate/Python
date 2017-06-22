def flatten_alpha(iamge) :
    alpha = iamge.split()[-1]  # Pull off the alpha layer
    alpha_bytes = alpha.tobytes()  # Original 8-bit alpha
    checked = []  # Create a new array to store the cleaned up alpha layer bytes
    # Walk through all pixels and set them either to 0 for transparent or 255 for opaque fancy pants
    transparent = 128  # change to suit your tolerance for what is and is not transparent

    for pixel in range(0, len(alpha_bytes)) :
        if alpha_bytes[pixel] < transparent:
            checked.append(0)  # Transparent
        else:
            checked.append(255)  # Opaque

    mask = Image.frombytes('L', iamge.size, bytes(checked))
    iamge.putalpha(mask)