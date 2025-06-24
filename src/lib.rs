use pyo3::prelude::*;
use uuid::Uuid;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// Returns a random UUID v4
#[pyfunction]
fn random_uuid_v4() -> Uuid {
    Uuid::new_v4()
}

/// A Python module implemented in Rust.
#[pymodule]
fn uuid_blake3(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(random_uuid_v4, m)?)?;
    Ok(())
}
