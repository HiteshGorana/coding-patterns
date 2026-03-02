# 16) File/Media Systems

## Basics
File/media systems handle storage, processing, and delivery of large binary assets.

Core components:
- Object storage concepts (S3-like)
- Uploads: multipart, resumable uploads
- Image/video processing pipelines
- CDN for media delivery
- Signed URLs and access control

## How It Works
- Upload large files in chunks.
- Store immutable objects with metadata.
- Process media asynchronously (resize/transcode).
- Serve via CDN with access controls.

```text
Client Upload -> Object Store -> Processing Jobs -> CDN -> Viewer
```

Cause-effect idea:
- Direct app-server file proxying -> high bandwidth cost and bottlenecks.
- Missing signed URL expiry -> unauthorized reuse risk.

## Simple Example
Video platform:
- Client uploads with resumable chunks.
- Worker transcodes to 1080p/720p variants.
- CDN serves nearest edge copy.

Analogy: Object storage is a warehouse; CDN is a network of local pickup centers.

## Why and What-If Questions
- Why multipart upload?
  - Improves reliability for large files over unstable networks.
- What if transcode job fails?
  - Retry with DLQ and notify user on persistent failure.
- What if viral content spikes traffic?
  - CDN absorbs global read load.

## Practical Applications
- User-generated content platforms.
- Document management systems.
- Streaming and media publishing products.

## Compare With Related Ideas
- Object storage vs block storage: object API and scale vs low-level disk semantics.
- Public objects vs signed URLs: simplicity vs controlled temporary access.

## Retention Tips
- Remember the lifecycle: `upload -> store -> process -> deliver`.
- Track media KPIs: upload success, processing latency, CDN hit ratio.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
