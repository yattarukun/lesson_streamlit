import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import time

st.title('streamlit 超入門')


st.write('プログレスバーの表示')

latest_iteretion = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteretion.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)




left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition













# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい。',
#     list(range(1, 11))
# )

# 'あなたが好きな数字は、', option, 'です。'








# if st.checkbox('show image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='Kosa tops', use_column_width=True)










# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)


# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.line_chart(df)
# st.area_chart(df)

# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4], 
#     '2列目':[10, 20, 30, 40]
# })

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""