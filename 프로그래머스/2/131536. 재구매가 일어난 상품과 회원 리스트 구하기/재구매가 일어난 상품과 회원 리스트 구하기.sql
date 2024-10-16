-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
# 데이터를 묶어서  같은 회원이 동일한 상품을 재구매한 경우를 찾기
GROUP BY USER_ID, PRODUCT_ID
HAVING count(*) >=2
ORDER BY USER_ID , PRODUCT_ID desc;