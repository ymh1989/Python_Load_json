## Loading ELS, DLS data from json by using Python

### Environment

- CPU : Intel(R) Core(TM) i5-6400 @ 2.7GHZ
- RAM : DDR3L 16GB PC3-12800
- [Python 3.5](https://www.python.org/), [requests](https://docs.python.org/3.5/library/ctypes.html), [pandas](http://pandas.pydata.org/)

### Example

- Loads json(JavaScript Object Notation) Equity Linked Securities(ELS), Derivatives Linked Securities(DLS) data from [DART](https://dart.fss.or.kr/)
- Note that all contents which can cause security issues are removed(i.e. issuer_name).
