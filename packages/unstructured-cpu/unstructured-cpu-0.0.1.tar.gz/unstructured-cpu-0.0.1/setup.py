"""
setup.py

unstructured-cpu - pre-processing tools for unstructured data without GPU dependencies

Copyright 2022 Unstructured Technologies, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import List, Optional, Union
from setuptools import find_packages, setup
from unstructured.__version__ import __version__

def load_requirements(file_list: Optional[Union[str, List[str]]] = None) -> List[str]:
    if file_list is None:
        file_list = ["requirements/sigrid/base.in"]
    if isinstance(file_list, str):
        file_list = [file_list]
    requirements: List[str] = []
    for file in file_list:
        with open(file, encoding="utf-8") as f:
            requirements.extend(f.readlines())
    requirements = [
        req.strip() for req in requirements
        if req.strip() and not req.startswith("#") and not req.startswith("-")
    ]
    return requirements

# Load all requirements
all_requirements = load_requirements([
    "requirements/sigrid/base.in",
    "requirements/sigrid/extra-csv.in",
    "requirements/sigrid/extra-docx.in",
    "requirements/sigrid/extra-epub.in",
    "requirements/sigrid/extra-pdf-image.in",
    "requirements/sigrid/extra-markdown.in",
    "requirements/sigrid/extra-msg.in",
    "requirements/sigrid/extra-odt.in",
    "requirements/sigrid/extra-pandoc.in",
    "requirements/sigrid/extra-pptx.in",
    "requirements/sigrid/extra-xlsx.in",
    "requirements/sigrid/huggingface.in",
    "requirements/sigrid/extra-paddleocr.in",
    "requirements/sigrid/ingest/airtable.in",
    "requirements/sigrid/ingest/astra.in",
    "requirements/sigrid/ingest/azure.in",
    "requirements/sigrid/ingest/azure-cognitive-search.in",
    "requirements/sigrid/ingest/biomed.in",
    "requirements/sigrid/ingest/box.in",
    "requirements/sigrid/ingest/chroma.in",
    "requirements/sigrid/ingest/clarifai.in",
    "requirements/sigrid/ingest/confluence.in",
    "requirements/sigrid/ingest/delta-table.in",
    "requirements/sigrid/ingest/discord.in",
    "requirements/sigrid/ingest/dropbox.in",
    "requirements/sigrid/ingest/elasticsearch.in",
    "requirements/sigrid/ingest/gcs.in",
    "requirements/sigrid/ingest/github.in",
    "requirements/sigrid/ingest/gitlab.in",
    "requirements/sigrid/ingest/google-drive.in",
    "requirements/sigrid/ingest/hubspot.in",
    "requirements/sigrid/ingest/jira.in",
    "requirements/sigrid/ingest/kafka.in",
    "requirements/sigrid/ingest/mongodb.in",
    "requirements/sigrid/ingest/notion.in",
    "requirements/sigrid/ingest/onedrive.in",
    "requirements/sigrid/ingest/opensearch.in",
    "requirements/sigrid/ingest/outlook.in",
    "requirements/sigrid/ingest/pinecone.in",
    "requirements/sigrid/ingest/postgres.in",
    "requirements/sigrid/ingest/qdrant.in",
    "requirements/sigrid/ingest/reddit.in",
    "requirements/sigrid/ingest/s3.in",
    "requirements/sigrid/ingest/sharepoint.in",
    "requirements/sigrid/ingest/salesforce.in",
    "requirements/sigrid/ingest/sftp.in",
    "requirements/sigrid/ingest/slack.in",
    "requirements/sigrid/ingest/wikipedia.in",
    "requirements/sigrid/ingest/weaviate.in",
    "requirements/sigrid/ingest/embed-huggingface.in",
    "requirements/sigrid/ingest/embed-octoai.in",
    "requirements/sigrid/ingest/embed-vertexai.in",
    "requirements/sigrid/ingest/embed-voyageai.in",
    "requirements/sigrid/ingest/embed-openai.in",
    "requirements/sigrid/ingest/embed-aws-bedrock.in",
    "requirements/sigrid/ingest/databricks-volumes.in",
])

# Remove duplicates while preserving order
all_requirements = list(dict.fromkeys(all_requirements))

setup(
    name="unstructured-cpu",
    version=__version__,
    description="No more headache on cuda for unstructured data processing",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sigrid Jin",
    author_email="sigrid.jinhyung@gmail.com",
    url="https://github.com/Unstructured-IO/unstructured",
    packages=find_packages(),
    install_requires=all_requirements,
    entry_points={
        "console_scripts": ["unstructured-ingest=unstructured.ingest.main:main"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9.0,<3.13",
    license="Apache-2.0",
    keywords="NLP PDF HTML CV XML parsing preprocessing",
    package_data={"unstructured": ["nlp/*.txt", "py.typed"]},
)