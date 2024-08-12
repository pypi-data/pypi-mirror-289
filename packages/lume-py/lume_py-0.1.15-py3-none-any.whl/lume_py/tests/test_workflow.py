import sys
import os
import pytest
import json
import httpx

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import lume_py

# Load target and source data from files
target_data_path = os.path.join(os.path.dirname(__file__), 'target.json')
with open(target_data_path, encoding='utf-8') as f:
    target_data = json.load(f)

source_data_path = os.path.join(os.path.dirname(__file__), 'source.json')
with open(source_data_path, encoding='utf-8') as f:
    source_data = json.load(f)


@pytest.mark.asyncio
async def test_pipeline_workflow():
    lume_py.set_api_key('222be6ab26bf6ea6bb86fffbb3880a67')
    
    # Print the payload to debug the structure
    print("Payload being sent for pipeline creation:", json.dumps(target_data, indent=2))
    
    # Attempt to create the pipeline
    try:
        pipeline = await lume_py.Pipeline.create(name="testingsdktwelve", description="test", target_schema=target_data)
        assert pipeline is not None
        assert pipeline.name == "testingsdktwelve"

        pipeline_id = pipeline.id
        fetched_pipeline = await lume_py.Pipeline.get_pipeline_by_id(pipeline_id)
        assert fetched_pipeline.id == pipeline_id

        updated_pipeline = await pipeline.update(name="updated_pipeline_test_twelve", description="A test pipeline updated")
        assert updated_pipeline.name == "updated_pipeline_test_twelve"

        paginated_pipelines = await pipeline.get_pipelines_data_page()
        assert paginated_pipelines is not None

        job = await lume_py.Job.create(pipeline_id=pipeline_id, source_data=source_data)
        assert job is not None

        job_result = await job.run()
        assert job_result is not None

    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        print(exc.response.json())
        raise

@pytest.mark.asyncio
async def test_pdf_workflow():
    lume_py.set_api_key('222be6ab26bf6ea6bb86fffbb3880a67')
    
    pdf_path = '/Users/aryanpanda/Downloads/PDF/Alaris/ADV/226583 (1).pdf'
    
    try:
        pdf_service = lume_py.PDF()
        extracted_pdf = await pdf_service.extract_pdf(pdf_path=pdf_path)
        assert extracted_pdf is not None

        adv_url = await pdf_service.get_adv_url(pdf_id='ebb5d33c-e7b9-464c-bc47-3776fa9c6c22')
        assert adv_url.startswith('https://')

        pdf_url = await pdf_service.get_pdf_url(pdf_id='509ae017-e566-4d1b-a451-87d96fe65f4c')
        assert pdf_url.startswith('https://')

    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        print(exc.response.json())
        raise

@pytest.mark.asyncio
async def test_result_workflow():
    lume_py.set_api_key('222be6ab26bf6ea6bb86fffbb3880a67')
    
    try:
        result = await lume_py.Result.get_results()
        assert result is not None

        spec = await result[0].get_spec()

        assert spec is not None

    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        print(exc.response.json())
        raise

@pytest.mark.asyncio
async def test_target_workflow():
    lume_py.set_api_key('222be6ab26bf6ea6bb86fffbb3880a67')
    
    try:
        target = await lume_py.Target.create(name='testing_target_sdk_4', filename='testing target sdk 3', target_schema=target_data)
        assert target is not None

        target_id = target.id
        fetched_target = await lume_py.Target.get_target_by_id(target_id)
        assert fetched_target is not None

        updated_target = await target.update(target_schema=target_data, name="updatedNew")
        
        assert updated_target is not None

    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        print(exc.response.json())
        raise

@pytest.mark.asyncio
async def test_workshop_workflow():
    lume_py.set_api_key('222be6ab26bf6ea6bb86fffbb3880a67')
    
    try:
        pipeline = await lume_py.Pipeline.get_pipeline_by_id('63e7ff0e-031d-48b6-9f58-b162e03f63a1')
        workshop = await pipeline.create_workshop()
        assert workshop is not None

    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        print(exc.response.json())
        raise


if __name__ == "__main__":
    pytest.main(["-v", __file__])
