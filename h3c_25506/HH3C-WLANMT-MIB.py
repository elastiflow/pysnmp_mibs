# SNMP MIB module (HH3C-WLANMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-WLANMT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:44:46 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cWlanMt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157)
)
if mibBuilder.loadTexts:
    hh3cWlanMt.setRevisions(
        ("2014-09-28 17:47",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cWlanMtVCpuInfoGroup_ObjectIdentity = ObjectIdentity
hh3cWlanMtVCpuInfoGroup = _Hh3cWlanMtVCpuInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1)
)
_Hh3cWlanMtVCpuInfoTable_Object = MibTable
hh3cWlanMtVCpuInfoTable = _Hh3cWlanMtVCpuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanMtVCpuInfoTable.setStatus("current")
_Hh3cWlanMtVCpuInfoEntry_Object = MibTableRow
hh3cWlanMtVCpuInfoEntry = _Hh3cWlanMtVCpuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1, 1, 1)
)
hh3cWlanMtVCpuInfoEntry.setIndexNames(
    (0, "HH3C-WLANMT-MIB", "hh3cWlanMtVcpuID"),
)
if mibBuilder.loadTexts:
    hh3cWlanMtVCpuInfoEntry.setStatus("current")


class _Hh3cWlanMtVcpuID_Type(Unsigned32):
    """Custom type hh3cWlanMtVcpuID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cWlanMtVcpuID_Type.__name__ = "Unsigned32"
_Hh3cWlanMtVcpuID_Object = MibTableColumn
hh3cWlanMtVcpuID = _Hh3cWlanMtVcpuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1, 1, 1, 1),
    _Hh3cWlanMtVcpuID_Type()
)
hh3cWlanMtVcpuID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanMtVcpuID.setStatus("current")


class _Hh3cWlanMtVcpuUsage_Type(Unsigned32):
    """Custom type hh3cWlanMtVcpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cWlanMtVcpuUsage_Type.__name__ = "Unsigned32"
_Hh3cWlanMtVcpuUsage_Object = MibTableColumn
hh3cWlanMtVcpuUsage = _Hh3cWlanMtVcpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1, 1, 1, 2),
    _Hh3cWlanMtVcpuUsage_Type()
)
hh3cWlanMtVcpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWlanMtVcpuUsage.setStatus("current")
_Hh3cWlanMtVcpuRx_Type = Counter64
_Hh3cWlanMtVcpuRx_Object = MibTableColumn
hh3cWlanMtVcpuRx = _Hh3cWlanMtVcpuRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1, 1, 1, 3),
    _Hh3cWlanMtVcpuRx_Type()
)
hh3cWlanMtVcpuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWlanMtVcpuRx.setStatus("current")
_Hh3cWlanMtVcpuTx_Type = Counter64
_Hh3cWlanMtVcpuTx_Object = MibTableColumn
hh3cWlanMtVcpuTx = _Hh3cWlanMtVcpuTx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1, 1, 1, 4),
    _Hh3cWlanMtVcpuTx_Type()
)
hh3cWlanMtVcpuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWlanMtVcpuTx.setStatus("current")
_Hh3cWlanMtVcpuDrop_Type = Counter64
_Hh3cWlanMtVcpuDrop_Object = MibTableColumn
hh3cWlanMtVcpuDrop = _Hh3cWlanMtVcpuDrop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 1, 1, 1, 5),
    _Hh3cWlanMtVcpuDrop_Type()
)
hh3cWlanMtVcpuDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWlanMtVcpuDrop.setStatus("current")
_Hh3cWlanMtFrameToCpu_ObjectIdentity = ObjectIdentity
hh3cWlanMtFrameToCpu = _Hh3cWlanMtFrameToCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 2)
)
_Hh3cWlanMtToCpuTxFrameCnt_Type = Counter64
_Hh3cWlanMtToCpuTxFrameCnt_Object = MibScalar
hh3cWlanMtToCpuTxFrameCnt = _Hh3cWlanMtToCpuTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 2, 1),
    _Hh3cWlanMtToCpuTxFrameCnt_Type()
)
hh3cWlanMtToCpuTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWlanMtToCpuTxFrameCnt.setStatus("current")
_Hh3cWlanMtToCpuDropFrameCnt_Type = Counter64
_Hh3cWlanMtToCpuDropFrameCnt_Object = MibScalar
hh3cWlanMtToCpuDropFrameCnt = _Hh3cWlanMtToCpuDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157, 2, 2),
    _Hh3cWlanMtToCpuDropFrameCnt_Type()
)
hh3cWlanMtToCpuDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWlanMtToCpuDropFrameCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-WLANMT-MIB",
    **{"hh3cWlanMt": hh3cWlanMt,
       "hh3cWlanMtVCpuInfoGroup": hh3cWlanMtVCpuInfoGroup,
       "hh3cWlanMtVCpuInfoTable": hh3cWlanMtVCpuInfoTable,
       "hh3cWlanMtVCpuInfoEntry": hh3cWlanMtVCpuInfoEntry,
       "hh3cWlanMtVcpuID": hh3cWlanMtVcpuID,
       "hh3cWlanMtVcpuUsage": hh3cWlanMtVcpuUsage,
       "hh3cWlanMtVcpuRx": hh3cWlanMtVcpuRx,
       "hh3cWlanMtVcpuTx": hh3cWlanMtVcpuTx,
       "hh3cWlanMtVcpuDrop": hh3cWlanMtVcpuDrop,
       "hh3cWlanMtFrameToCpu": hh3cWlanMtFrameToCpu,
       "hh3cWlanMtToCpuTxFrameCnt": hh3cWlanMtToCpuTxFrameCnt,
       "hh3cWlanMtToCpuDropFrameCnt": hh3cWlanMtToCpuDropFrameCnt}
)
