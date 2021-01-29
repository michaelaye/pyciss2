# Index
> Tools to retrieve the PDS index for Cassini ISS image data.


```python
get_index_dir()
```




    PosixPath('/home/maye/big_drive/planetary_data/pyciss/indexes')



```python
df = ring_summary_index()
```

```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>VOLUME_ID</th>
      <th>FILE_SPECIFICATION_NAME</th>
      <th>OPUS_ID</th>
      <th>MINIMUM_RIGHT_ASCENSION</th>
      <th>MAXIMUM_RIGHT_ASCENSION</th>
      <th>MINIMUM_DECLINATION</th>
      <th>MAXIMUM_DECLINATION</th>
      <th>MINIMUM_RING_RADIUS</th>
      <th>MAXIMUM_RING_RADIUS</th>
      <th>FINEST_RING_INTERCEPT_RESOLUTION</th>
      <th>...</th>
      <th>RING_CENTER_DISTANCE</th>
      <th>SUB_SOLAR_RING_LONGITUDE</th>
      <th>SUB_OBSERVER_RING_LONGITUDE</th>
      <th>RING_CENTER_PHASE_ANGLE</th>
      <th>RING_CENTER_INCIDENCE_ANGLE</th>
      <th>RING_CENTER_NORTH_BASED_INCIDENCE_ANGLE</th>
      <th>RING_CENTER_EMISSION_ANGLE</th>
      <th>RING_CENTER_NORTH_BASED_EMISSION_ANGLE</th>
      <th>SOLAR_RING_OPENING_ANGLE</th>
      <th>OBSERVER_RING_OPENING_ANGLE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>COISS_2001</td>
      <td>data/1454725799_1455008789/N1454725799_1.LBL</td>
      <td>co-iss-n1454725799</td>
      <td>35.528398</td>
      <td>35.905555</td>
      <td>9.719637</td>
      <td>10.091212</td>
      <td>205899.335</td>
      <td>1098621.586</td>
      <td>419.01370</td>
      <td>...</td>
      <td>7.087500e+07</td>
      <td>284.523</td>
      <td>215.951</td>
      <td>64.070</td>
      <td>64.589</td>
      <td>115.411</td>
      <td>73.676</td>
      <td>106.324</td>
      <td>-25.411</td>
      <td>-16.324</td>
    </tr>
    <tr>
      <th>1</th>
      <td>COISS_2001</td>
      <td>data/1454725799_1455008789/N1454726579_1.LBL</td>
      <td>co-iss-n1454726579</td>
      <td>36.662898</td>
      <td>37.039038</td>
      <td>9.590114</td>
      <td>9.960833</td>
      <td>721136.155</td>
      <td>1745689.307</td>
      <td>421.97145</td>
      <td>...</td>
      <td>7.087085e+07</td>
      <td>284.524</td>
      <td>215.951</td>
      <td>64.070</td>
      <td>64.589</td>
      <td>115.411</td>
      <td>73.676</td>
      <td>106.324</td>
      <td>-25.411</td>
      <td>-16.324</td>
    </tr>
    <tr>
      <th>2</th>
      <td>COISS_2001</td>
      <td>data/1454725799_1455008789/N1454727359_1.LBL</td>
      <td>co-iss-n1454727359</td>
      <td>36.928066</td>
      <td>37.304334</td>
      <td>9.879593</td>
      <td>10.250110</td>
      <td>1042341.438</td>
      <td>2186830.920</td>
      <td>414.79041</td>
      <td>...</td>
      <td>7.086670e+07</td>
      <td>284.524</td>
      <td>215.951</td>
      <td>64.071</td>
      <td>64.589</td>
      <td>115.411</td>
      <td>73.676</td>
      <td>106.324</td>
      <td>-25.411</td>
      <td>-16.324</td>
    </tr>
    <tr>
      <th>3</th>
      <td>COISS_2001</td>
      <td>data/1454725799_1455008789/N1454728139_1.LBL</td>
      <td>co-iss-n1454728139</td>
      <td>28.100420</td>
      <td>28.479618</td>
      <td>6.224709</td>
      <td>6.601574</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>7.086256e+07</td>
      <td>284.524</td>
      <td>215.951</td>
      <td>64.071</td>
      <td>64.589</td>
      <td>115.411</td>
      <td>73.676</td>
      <td>106.324</td>
      <td>-25.411</td>
      <td>-16.324</td>
    </tr>
    <tr>
      <th>4</th>
      <td>COISS_2001</td>
      <td>data/1454725799_1455008789/N1454728919_1.LBL</td>
      <td>co-iss-n1454728919</td>
      <td>37.981418</td>
      <td>38.357791</td>
      <td>10.611947</td>
      <td>10.981697</td>
      <td>3865717.589</td>
      <td>3905151.343</td>
      <td>405.91234</td>
      <td>...</td>
      <td>7.085841e+07</td>
      <td>284.525</td>
      <td>215.951</td>
      <td>64.071</td>
      <td>64.589</td>
      <td>115.411</td>
      <td>73.676</td>
      <td>106.324</td>
      <td>-25.411</td>
      <td>-16.324</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 59 columns</p>
</div>



```python
read_ring_images_index().info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 117692 entries, 2321 to 407222
    Columns: 140 entries, FILE_NAME to STANDARD_DATA_PRODUCT_ID
    dtypes: datetime64[ns](7), float64(70), int64(20), object(43)
    memory usage: 126.6+ MB


```python
clearnacs = get_clearnacs_ring_images()
clearnacs.info()
```

    'isotime' column does not exist. Leaving index as it is.
    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 73271 entries, 2321 to 407222
    Columns: 140 entries, FILE_NAME to STANDARD_DATA_PRODUCT_ID
    dtypes: datetime64[ns](7), float64(70), int64(20), object(43)
    memory usage: 78.8+ MB


```python
filter_for_ringspan(clearnacs, 500).info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 134 entries, 13326 to 398037
    Columns: 140 entries, FILE_NAME to STANDARD_DATA_PRODUCT_ID
    dtypes: datetime64[ns](7), float64(70), int64(20), object(43)
    memory usage: 147.6+ KB


```python
from nbdev.export import notebook2script; notebook2script()
```

    Converted 00_io.ipynb.
    Converted 01_opusapi.ipynb.
    Converted 02_pipeline.ipynb.
    Converted 03_ringutils.ipynb.
    Converted 04_plotting.ipynb.
    Converted 05_index.ipynb.
    Converted 06_ringcube.ipynb.
    Converted index.ipynb.
    Converted to_be_implemented.ipynb.

