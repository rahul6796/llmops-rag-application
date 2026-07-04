
from pathlib import Path
import re


TIMESTAMP_PATTERN = re.compile(
    r"^\d{2}:\d{2}:\d{2}(?:\.\d+)?\s+-->\s+\d{2}:\d{2}:\d{2}(?:\.\d+)?$"
)



def clean_transcript_text(transcript: str) -> str:

    """
    Remove timestamp line from the transcripts and return only the spoken text.
    """

    lines = transcript.splitlines()
    cleaned_text = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if TIMESTAMP_PATTERN.match(stripped):
            continue
        cleaned_text.append(stripped)
    return "\n".join(cleaned_text)


def load_and_clean_transcripts(original_path: Path | str,
                               new_path: Path | str):

    ORIGINAL_PATH  = Path(original_path) 
    NEW_PATH =  Path(new_path)


    # create a new directory
    NEW_PATH.mkdir(parents=True, exist_ok=True)

    # load all the transcripts file:
    transcripts = ORIGINAL_PATH.glob(pattern="*.txt")

    for transcript_path in transcripts:

        # read all the content = 
        file_content = transcript_path.read_text(encoding='utf-8')

        # clean the text
        cleaned_text = clean_transcript_text(transcript=file_content)

        # save the all the content on the same filename and different location

        file_name = transcript_path.name

        output_path  = NEW_PATH / file_name
        print(output_path)

        output_path.write_text(data = cleaned_text, 
                               encoding='utf-8')
        



if __name__ == "__main__":

    load_and_clean_transcripts(
        original_path=Path('./transcripts'),
        new_path=Path('./cleaned-transcripts')
    )












