from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from strawberry.fastapi import BaseContext

from phoenix.core.model_schema import Model
from phoenix.server.api.dataloaders import (
    AnnotationSummaryDataLoader,
    AverageExperimentRunLatencyDataLoader,
    CacheForDataLoaders,
    DatasetExampleRevisionsDataLoader,
    DatasetExampleSpansDataLoader,
    DocumentEvaluationsDataLoader,
    DocumentEvaluationSummaryDataLoader,
    DocumentRetrievalMetricsDataLoader,
    EvaluationSummaryDataLoader,
    ExperimentAnnotationSummaryDataLoader,
    ExperimentErrorRatesDataLoader,
    ExperimentRunCountsDataLoader,
    ExperimentSequenceNumberDataLoader,
    LatencyMsQuantileDataLoader,
    MinStartOrMaxEndTimeDataLoader,
    ProjectByNameDataLoader,
    RecordCountDataLoader,
    SpanAnnotationsDataLoader,
    SpanDatasetExamplesDataLoader,
    SpanDescendantsDataLoader,
    SpanEvaluationsDataLoader,
    SpanProjectsDataLoader,
    TokenCountDataLoader,
    TraceEvaluationsDataLoader,
    TraceRowIdsDataLoader,
)
from phoenix.server.dml_event import DmlEvent
from phoenix.server.types import CanGetLastUpdatedAt, CanPutItem, DbSessionFactory


@dataclass
class DataLoaders:
    average_experiment_run_latency: AverageExperimentRunLatencyDataLoader
    dataset_example_revisions: DatasetExampleRevisionsDataLoader
    dataset_example_spans: DatasetExampleSpansDataLoader
    document_evaluation_summaries: DocumentEvaluationSummaryDataLoader
    document_evaluations: DocumentEvaluationsDataLoader
    document_retrieval_metrics: DocumentRetrievalMetricsDataLoader
    annotation_summaries: AnnotationSummaryDataLoader
    evaluation_summaries: EvaluationSummaryDataLoader
    experiment_annotation_summaries: ExperimentAnnotationSummaryDataLoader
    experiment_error_rates: ExperimentErrorRatesDataLoader
    experiment_run_counts: ExperimentRunCountsDataLoader
    experiment_sequence_number: ExperimentSequenceNumberDataLoader
    latency_ms_quantile: LatencyMsQuantileDataLoader
    min_start_or_max_end_times: MinStartOrMaxEndTimeDataLoader
    record_counts: RecordCountDataLoader
    span_annotations: SpanAnnotationsDataLoader
    span_dataset_examples: SpanDatasetExamplesDataLoader
    span_descendants: SpanDescendantsDataLoader
    span_evaluations: SpanEvaluationsDataLoader
    span_projects: SpanProjectsDataLoader
    token_counts: TokenCountDataLoader
    trace_evaluations: TraceEvaluationsDataLoader
    trace_row_ids: TraceRowIdsDataLoader
    project_by_name: ProjectByNameDataLoader


class _NoOp:
    def get(self, *args: Any, **kwargs: Any) -> Any: ...
    def put(self, *args: Any, **kwargs: Any) -> Any: ...


@dataclass
class Context(BaseContext):
    db: DbSessionFactory
    data_loaders: DataLoaders
    cache_for_dataloaders: Optional[CacheForDataLoaders]
    model: Model
    export_path: Path
    last_updated_at: CanGetLastUpdatedAt = _NoOp()
    event_queue: CanPutItem[DmlEvent] = _NoOp()
    corpus: Optional[Model] = None
    read_only: bool = False
