import functools

import pytest
import numpy as np
import pandas as pd
import torch

import tdfl
from tdfl import array as ar
import utils

devices = ["cpu"]
if torch.cuda.is_available():
    devices.append("cuda")
# if torch.backends.mps.is_available() and torch.backends.mps.is_built():
#     devices.append("mps")


@pytest.fixture
def xfail_cut(request):
    keys = ["right", "bins"]
    fixturevalues = {k: request.getfixturevalue(k) for k in keys}

    if fixturevalues["right"] and not isinstance(
        fixturevalues["bins"], pd.IntervalIndex
    ):
        request.node.add_marker(
            pytest.mark.xfail(
                raises=NotImplementedError, strict=True, reason="Not Implemented"
            )
        )


@pytest.mark.parametrize(
    "df0_long",
    [
        (3, 100, 3, "abc", 20),
    ],
    indirect=True,
)
@pytest.mark.parametrize("column", ["a", "c", "d"])
@pytest.mark.parametrize(
    "bins",
    [
        pytest.param(
            5,
            marks=pytest.mark.xfail(
                raises=NotImplementedError, strict=True, reason="Not Implemented"
            ),
        ),
        np.linspace(-2, 2, num=10),
        pd.interval_range(-2, 2, closed="left"),
        pytest.param(
            pd.interval_range(-2, 2, closed="right"),
            marks=pytest.mark.xfail(
                raises=NotImplementedError, strict=True, reason="Not Implemented"
            ),
        ),
    ],
)
@pytest.mark.parametrize("right", [True, False])
@pytest.mark.parametrize(
    "labels",
    [
        None,
        False,
        pytest.param(
            ["hi"],
            marks=pytest.mark.xfail(
                raises=NotImplementedError, strict=True, reason="Not Implemented"
            ),
        ),
    ],
)
@pytest.mark.parametrize("retbins", [False, True])
@pytest.mark.parametrize("missing_rep", [np.nan, -1])
@pytest.mark.parametrize("device", devices)
@pytest.mark.usefixtures("xfail_cut")
def test_cut(df0_long, column, bins, right, labels, retbins, missing_rep, device):
    tdf = df0_long.to(device)
    df = tdf.to_pandas()

    output = tdfl.cut(
        tdf[column],
        bins,
        right=right,
        labels=labels,
        retbins=retbins,
        missing_rep=missing_rep,
    )
    expected = pd.cut(df[column], bins, right=right, labels=labels, retbins=retbins)

    if retbins:
        output, output_bins = output
        expected, expected_bins = expected
        if isinstance(expected_bins, pd.IntervalIndex):
            assert (output_bins == expected_bins).all()
        else:
            np.testing.assert_allclose(
                ar.Array(output_bins).detach().cpu().numpy(), expected_bins
            )

    if labels is None:
        expected = pd.IntervalIndex(expected).mid
        if expected.isna().any():
            expected = expected.fillna(missing_rep)
    elif labels is False and isinstance(bins, pd.IntervalIndex):
        expected = expected.cat.codes
        if (expected == -1).any():
            expected = expected.astype(float)
            expected[expected == -1] = missing_rep
    else:
        if expected.isna().any():
            expected = expected.fillna(missing_rep)

    np.testing.assert_allclose(
        ar.Array(output).detach().cpu().numpy(), expected.to_numpy()
    )


@pytest.mark.parametrize("kind", ["numpy", "torch", "dict", "list", "dataframe"])
def test_init(kind):
    if kind == "numpy":
        data = np.array([[1, 2], [3, 4], [5, 6]])
        expected = {"a": np.array([1, 3, 5]), "b": np.array([2, 4, 6])}
    elif kind == "torch":
        data = torch.tensor([[1, 2], [3, 4], [5, 6]])
        expected = {"a": torch.tensor([1, 3, 5]), "b": torch.tensor([2, 4, 6])}
    elif kind == "list":
        data = [np.array([1, 3, 5]), torch.tensor([2, 4, 6])]
        expected = {"a": np.array([1, 3, 5]), "b": torch.tensor([2, 4, 6])}
    elif kind == "dict":
        data = {"a": np.array([1, 3, 5]), "b": torch.tensor([2, 4, 6])}
        expected = {"a": np.array([1, 3, 5]), "b": torch.tensor([2, 4, 6])}
    elif kind == "dataframe":
        data = tdfl.DataFrame({"a": np.array([1, 3, 5]), "b": torch.tensor([2, 4, 6])})
        expected = {"a": np.array([1, 3, 5]), "b": torch.tensor([2, 4, 6])}

    columns = ["a", "b"] if kind in ["numpy", "torch", "list"] else None
    out = tdfl.DataFrame(data, columns=columns)

    assert out.columns == ["a", "b"]
    assert (out["a"] == expected["a"]).all()
    assert (out["b"] == expected["b"]).all()


def test_getitem():
    df = tdfl.DataFrame(
        {
            "a": torch.tensor([1, 2, 3, 4]),
            "b": np.array([5, 6, 7, 8]),
        }
    )
    assert (df["a"] == torch.tensor([1, 2, 3, 4])).all()
    assert (df["b"] == np.array([5, 6, 7, 8])).all()
    assert (df[["a", "b"]] == df).all()
    assert df[:, 1] == [torch.tensor(2), np.array(6)]
    assert (
        df[:, 1:3] == tdfl.DataFrame({"a": torch.tensor([2, 3]), "b": np.array([6, 7])})
    ).all()


@pytest.mark.parametrize("length", [None, 1, 4])
@pytest.mark.parametrize("kind", [None, "numpy", "torch"])
def test_setitem_column(length, kind):
    df = tdfl.DataFrame({"a": torch.tensor([1, 2, 3, 4])})

    b = 2
    expected_0 = np.array([2, 2, 2, 2])
    expected_1 = np.array([2, 3, 2, 2])
    if length is not None:
        b = [b] * length

    if kind == "numpy":
        b = np.array(b)

    elif kind == "torch":
        b = torch.tensor(b)
        expected_0 = torch.tensor(expected_0)
        expected_1 = torch.tensor(expected_1)

    df["b"] = b
    assert (df["b"] == expected_0).all()
    # check that we did not copy data if no broadcasting is performed
    if length != 4:
        pass
    elif kind == "torch":
        assert df["b"].untyped_storage().data_ptr() == b.untyped_storage().data_ptr()
    elif kind == "numpy":
        assert np.may_share_memory(df["b"], b)

    df["b", 1] = 3
    assert (df["b"] == expected_1).all()


@pytest.mark.parametrize("column_idx", [slice(None), ["a", "b"]])
@pytest.mark.parametrize("length", [None, 1, 2])
@pytest.mark.parametrize("kind", [None, "numpy", "torch"])
def test_setitem_row(column_idx, length, kind):
    df = tdfl.DataFrame(
        {
            "a": torch.tensor([1, 2, 3, 4]),
            "b": np.array([5, 6, 7, 8]),
        }
    )
    item = 10
    if length is not None:
        item = [item] * length
    if kind == "numpy":
        item = np.array(item)
    elif kind == "torch":
        item = torch.tensor(item)

    df[column_idx, 1] = item
    assert (df["a"] == torch.tensor([1, 10, 3, 4])).all()
    assert (df["b"] == np.array([5, 10, 7, 8])).all()


@pytest.mark.parametrize("column_idx", [slice(None), ["a", "b"]])
@pytest.mark.parametrize("row_idx", [None, slice(None), [0, 1, 2, 3]])
@pytest.mark.parametrize("shape", [None, (2,), (1, 4), (2, 4)])
@pytest.mark.parametrize("kind", [None, "numpy", "torch"])
def test_setitem_2d(column_idx, row_idx, shape, kind):
    df = tdfl.DataFrame(
        {
            "a": torch.tensor([1, 2, 3, 4]),
            "b": np.array([5, 6, 7, 8]),
        }
    )
    item = 10
    if shape == (2,):
        item = [item] * 2
    elif shape is not None:
        item = [[item] * shape[1]] * shape[0]
    if kind == "numpy":
        item = np.array(item)
    elif kind == "torch":
        item = torch.tensor(item)

    idx = (column_idx, row_idx) if row_idx is not None else column_idx
    df[idx] = item
    if row_idx is not None:
        assert (df["a"] == torch.tensor([10, 10, 10, 10])).all()
        assert (df["b"] == np.array([10, 10, 10, 10])).all()
    else:
        if kind is None or kind == "numpy":
            expected = np.full((2, 4), 10)
        else:
            expected = torch.full((2, 4), 10)
        assert (df["a"] == expected[0]).all()
        assert (df["b"] == expected[1]).all()


@pytest.mark.parametrize(
    "query", ["a > 2", "b == 'b'", "a > 2 and b == 'b'", "a == @num"]
)
def test_query(query):
    num = 2  # noqa
    data = {"a": [4, 3, 2, 1], "b": ["a", "b", "c", "d"]}
    out = tdfl.DataFrame(data).query(query)
    expected = pd.DataFrame(data).query(query)
    pd.testing.assert_frame_equal(out.to_pandas(), expected.reset_index(drop=True))


@pytest.mark.parametrize(
    "ltdf, rtdf, on, left_on, right_on, suffixes, grads1, grads2",
    [
        (
            "df0",
            "df1a",
            None,
            None,
            None,
            ("_x", "_y"),
            (True, True, False, True, True, True),
            (True, False, False, True, True, False),
        ),
        (
            "df0",
            "df1a",
            ("a", "b"),
            None,
            None,
            ("_0", "_1"),
            (True, True, False, True, True, False, False, True),
            (True, False, False, True, True, False, False, False),
        ),
        (
            "df0",
            "df1b",
            None,
            None,
            None,
            ("_x", "_y"),
            (True, False, False, True, True, False, False),
            (True, False, False, True, True, False, False),
        ),
        (
            "df0",
            "df1b",
            None,
            ("a", "b"),
            ("b", "a"),
            ("_x", "_y"),
            (True, False, False, True, True, False, False, False, False),
            (True, False, False, True, True, False, False, False, False),
        ),
    ],
)
@pytest.mark.parametrize(
    "how",
    [
        "inner",
        "left",
        "right",
        "outer",
    ],
)
@pytest.mark.parametrize("sort", [True, False])
@pytest.mark.parametrize("indicator", [True, False])
@pytest.mark.parametrize("device", devices)
def test_merge(
    request,
    ltdf,
    rtdf,
    on,
    left_on,
    right_on,
    suffixes,
    how,
    sort,
    indicator,
    grads1,
    grads2,
    device,
):
    print(
        f"{ltdf=}, {rtdf=}, {on=}, {left_on=}, {right_on=}, {suffixes=}, {how=}, {sort=}, {indicator=}"
    )

    ltdf, rtdf = request.getfixturevalue(ltdf), request.getfixturevalue(rtdf)
    ldf, rdf = ltdf.to_pandas(), rtdf.to_pandas()

    ltdf, rtdf = ltdf.to(device), rtdf.to(device)

    tdf1 = ltdf.merge(
        rtdf,
        how=how,
        on=on,
        left_on=left_on,
        right_on=right_on,
        sort=sort,
        suffixes=suffixes,
        indicator=indicator,
    )
    tdf2 = ltdf.merge(
        rdf,
        how=how,
        on=on,
        left_on=left_on,
        right_on=right_on,
        sort=sort,
        suffixes=suffixes,
        indicator=indicator,
    )
    df = ldf.merge(
        rdf,
        how=how,
        on=on,
        left_on=left_on,
        right_on=right_on,
        sort=sort,
        suffixes=suffixes,
        indicator=indicator,
    )

    if indicator:
        df["_merge"] = df["_merge"].astype(str)

    # Currently the tests are designed so that float output type should always be float32.
    # Discrepancy arises when tensor columns are converted from int to float due to NaNs,
    # where pandas converts to float64 but typical pytorch convertion dictates that
    # such columns should be converted to float32.
    df1, df2 = df.copy(), df.copy()
    float64_cols = list(df1.select_dtypes(include="float64"))
    df1[float64_cols] = df1[float64_cols].astype("float32")

    pd.testing.assert_frame_equal(tdf1.to_pandas(), df1)
    pd.testing.assert_frame_equal(tdf2.to_pandas(), df2)

    if indicator:
        assert len(tdf1.columns) == len(tdf2.columns) == len(grads1) + 1
    else:
        assert len(tdf1.columns) == len(tdf2.columns) == len(grads2)

    for v1, v2, grad1, grad2 in zip(tdf1.values(), tdf2.values(), grads1, grads2):
        if isinstance(v1, torch.Tensor):
            assert v1.requires_grad is grad1
        if isinstance(v2, torch.Tensor):
            assert v2.requires_grad is grad2


@pytest.mark.parametrize(
    "ltdf, rtdf, suffixes, grads",
    [
        (
            "df0",
            "df1a",
            ("_x", "_y"),
            (True, False, False, True, True, False, True, False, False, True),
        ),
        (
            "df0",
            "df1b",
            ("_0", "_1"),
            (True, False, False, True, True, False, False, False, False),
        ),
    ],
)
@pytest.mark.parametrize("sort", [True, False])
@pytest.mark.parametrize("indicator", [True, False])
@pytest.mark.parametrize("device", devices)
def test_merge_cross(request, ltdf, rtdf, suffixes, sort, indicator, grads, device):
    how = "cross"

    ltdf, rtdf = request.getfixturevalue(ltdf), request.getfixturevalue(rtdf)
    ldf, rdf = ltdf.to_pandas(), rtdf.to_pandas()

    ltdf, rtdf = ltdf.to(device), rtdf.to(device)

    tdf = ltdf.merge(rtdf, how=how, sort=sort, suffixes=suffixes, indicator=indicator)
    df = ldf.merge(rdf, how=how, sort=sort, suffixes=suffixes, indicator=indicator)

    if indicator:
        df["_merge"] = df["_merge"].astype(str)

    pd.testing.assert_frame_equal(tdf.to_pandas(), df)
    for v, grad in zip(tdf.values(), grads):
        if isinstance(v, torch.Tensor):
            assert v.requires_grad == grad


@pytest.mark.parametrize(
    "df0_long",
    [
        (2, 100, 3, "abc", 20),
    ],
    indirect=True,
)
@pytest.mark.parametrize(
    "groupby",
    [
        "a",
        "b",
        "c",
        "d",
        ["b", "c"],
        ["c", "d"],
        ["b", "c", "d"],
    ],
)
@pytest.mark.parametrize(
    "columns, func, kwargs, requires_grad",
    [
        ("a", "mean", None, {"a"}),
        ("d", "sum", None, set()),
        ("c", "count", None, set()),
        ("a", "var", None, {"a"}),
        ("a", "std", None, {"a"}),
        ("a", "sem", None, {"a"}),
        ("a", "min", None, {"a"}),
        ("a", "max", None, {"a"}),
        ("a", "median", None, {"a"}),
        ("a", ["mean", "sum"], None, {"mean", "sum"}),
        ("a", ["mean", "sum"], {"hi": "count"}, None),  # xfail, cannot provide both
        ("a", None, {"hi": "mean"}, {"hi"}),
        ("a", None, {"hi": "mean", "bye": "sum"}, {"hi", "bye"}),
        ("a", None, None, None),  # xfail, must provide something
        (
            None,
            None,
            {"hi": ("a", "mean"), "bye": ("d", "sum"), "byebye": ("c", "count")},
            {"hi"},
        ),
        (None, None, {"hi": ("a", "mean")}, {"hi"}),
        (None, None, None, None),  # xfail, must provide something
    ],
)
@pytest.mark.parametrize("dropna", [True, False])
@pytest.mark.parametrize("sort", [True, False])
@pytest.mark.parametrize("device", devices)
def test_groupby_agg(
    df0_long, groupby, columns, func, kwargs, sort, dropna, device, requires_grad
):
    if columns is None and func is not None:
        raise RuntimeError()

    if kwargs is None:
        kwargs = {}

    tdf = df0_long.to(device)
    df = tdf.to_pandas()

    tg = tdf.groupby(groupby, sort=sort, dropna=dropna, device=device)
    g = df.groupby(groupby, as_index=False, sort=sort, dropna=dropna)

    if columns is None:
        output = functools.partial(tg.agg, **kwargs)
        expected = functools.partial(g.agg, **kwargs)
    else:
        output = functools.partial(tg[columns].agg, func=func, **kwargs)
        expected = functools.partial(g[columns].agg, func=func, **kwargs)

    def assert_equal(output, expected, sort=sort, requires_grad=requires_grad):
        for k in requires_grad:
            assert output[k].requires_grad
        output, expected = output.to_pandas(), expected.reset_index(drop=True)
        if not sort:
            output, expected = output.sort_values(
                list(output.columns)
            ), expected.sort_values(list(expected.columns))
            output, expected = output.reset_index(drop=True), expected.reset_index(
                drop=True
            )
        pd.testing.assert_frame_equal(output, expected)

    utils.assert_equal_or_equal_error_type(output, expected, assert_equal)
