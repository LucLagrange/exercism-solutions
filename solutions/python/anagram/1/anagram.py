def find_anagrams(word, candidates):

    print(f"Target word is: {word}")

    # Converts word into letters
    target_letters = list(word.lower())
    target_letters.sort()

    # For each candidate:
    # Convert into letters
    # Check against the target letters
    # If we have the same letters (regardless of the case)

    anagrams = []
    for candidate in candidates:

        candidate_letters = list(candidate.lower())
        candidate_letters.sort()

        if (
            candidate_letters == target_letters
            and not word.lower() == candidate.lower()
        ):
            anagrams.append(candidate)
            print(f"Match found: {candidate}")

    return anagrams