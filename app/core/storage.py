from functools import lru_cache

import boto3
from botocore.config import Config

from app.core.config import get_settings


@lru_cache
def _client():
    s = get_settings()
    return boto3.client(
        "s3",
        endpoint_url=s.s3_endpoint_url,
        region_name=s.s3_region,
        aws_access_key_id=s.s3_access_key,
        aws_secret_access_key=s.s3_secret_key,
        # MinIO·Supabase 모두 path-style 주소(endpoint/bucket/key)를 쓴다
        config=Config(s3={"addressing_style": "path"}, retries={"max_attempts": 2}),
    )


def put_object(key: str, data: bytes, content_type: str) -> str:
    """객체를 저장하고 공개 URL을 돌려준다."""
    s = get_settings()
    _client().put_object(Bucket=s.s3_bucket, Key=key, Body=data, ContentType=content_type)
    return f"{s.s3_public_base_url}/{key}"


def delete_object(key: str) -> None:
    _client().delete_object(Bucket=get_settings().s3_bucket, Key=key)
