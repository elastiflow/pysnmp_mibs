# SNMP MIB module (OPHYLINK-OSL6200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ophylink_42861/OPHYLINK-OSL6200-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:48:30 2025
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

(ophylinkProducts,) = mibBuilder.importSymbols(
    "OPHYLINK-MIB",
    "ophylinkProducts")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OphylinkOsl6200_ObjectIdentity = ObjectIdentity
ophylinkOsl6200 = _OphylinkOsl6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200.setStatus("current")
_OphylinkOsl6200SlotStatusTable_Object = MibTable
ophylinkOsl6200SlotStatusTable = _OphylinkOsl6200SlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 1)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotStatusTable.setStatus("current")
_OphylinkOsl6200SlotStatusEntry_Object = MibTableRow
ophylinkOsl6200SlotStatusEntry = _OphylinkOsl6200SlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 1, 1)
)
ophylinkOsl6200SlotStatusEntry.setIndexNames(
    (0, "OPHYLINK-OSL6200-MIB", "oSSSlotNum"),
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotStatusEntry.setStatus("current")


class _OSSSlotNum_Type(Integer32):
    """Custom type oSSSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_OSSSlotNum_Type.__name__ = "Integer32"
_OSSSlotNum_Object = MibTableColumn
oSSSlotNum = _OSSSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 1, 1, 1),
    _OSSSlotNum_Type()
)
oSSSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSSSlotNum.setStatus("current")
_OSSSlotStatus_Type = Integer32
_OSSSlotStatus_Object = MibTableColumn
oSSSlotStatus = _OSSSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 1, 1, 2),
    _OSSSlotStatus_Type()
)
oSSSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSSSlotStatus.setStatus("current")
_OphylinkOsl6200SlotBasicInfoTable_Object = MibTable
ophylinkOsl6200SlotBasicInfoTable = _OphylinkOsl6200SlotBasicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotBasicInfoTable.setStatus("current")
_OphylinkOsl6200SlotBasicInfoEntry_Object = MibTableRow
ophylinkOsl6200SlotBasicInfoEntry = _OphylinkOsl6200SlotBasicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1)
)
ophylinkOsl6200SlotBasicInfoEntry.setIndexNames(
    (0, "OPHYLINK-OSL6200-MIB", "osl6200SlotNum"),
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotBasicInfoEntry.setStatus("current")


class _Osl6200SlotNum_Type(Integer32):
    """Custom type osl6200SlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_Osl6200SlotNum_Type.__name__ = "Integer32"
_Osl6200SlotNum_Object = MibTableColumn
osl6200SlotNum = _Osl6200SlotNum_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 1),
    _Osl6200SlotNum_Type()
)
osl6200SlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotNum.setStatus("current")


class _Osl6200SlotReady_Type(Integer32):
    """Custom type osl6200SlotReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SlotReady_Type.__name__ = "Integer32"
_Osl6200SlotReady_Object = MibTableColumn
osl6200SlotReady = _Osl6200SlotReady_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 2),
    _Osl6200SlotReady_Type()
)
osl6200SlotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotReady.setStatus("current")
_Osl6200SlotType_Type = Integer32
_Osl6200SlotType_Object = MibTableColumn
osl6200SlotType = _Osl6200SlotType_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 3),
    _Osl6200SlotType_Type()
)
osl6200SlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotType.setStatus("current")


class _Osl6200SlotHwVer_Type(OctetString):
    """Custom type osl6200SlotHwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotHwVer_Type.__name__ = "OctetString"
_Osl6200SlotHwVer_Object = MibTableColumn
osl6200SlotHwVer = _Osl6200SlotHwVer_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 4),
    _Osl6200SlotHwVer_Type()
)
osl6200SlotHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotHwVer.setStatus("current")


class _Osl6200SlotSwVer_Type(OctetString):
    """Custom type osl6200SlotSwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotSwVer_Type.__name__ = "OctetString"
_Osl6200SlotSwVer_Object = MibTableColumn
osl6200SlotSwVer = _Osl6200SlotSwVer_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 5),
    _Osl6200SlotSwVer_Type()
)
osl6200SlotSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotSwVer.setStatus("current")


class _Osl6200SlotFwVer_Type(OctetString):
    """Custom type osl6200SlotFwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotFwVer_Type.__name__ = "OctetString"
_Osl6200SlotFwVer_Object = MibTableColumn
osl6200SlotFwVer = _Osl6200SlotFwVer_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 6),
    _Osl6200SlotFwVer_Type()
)
osl6200SlotFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotFwVer.setStatus("current")


class _Osl6200SlotModel_Type(OctetString):
    """Custom type osl6200SlotModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotModel_Type.__name__ = "OctetString"
_Osl6200SlotModel_Object = MibTableColumn
osl6200SlotModel = _Osl6200SlotModel_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 7),
    _Osl6200SlotModel_Type()
)
osl6200SlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotModel.setStatus("current")


class _Osl6200SlotSn_Type(OctetString):
    """Custom type osl6200SlotSn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotSn_Type.__name__ = "OctetString"
_Osl6200SlotSn_Object = MibTableColumn
osl6200SlotSn = _Osl6200SlotSn_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 8),
    _Osl6200SlotSn_Type()
)
osl6200SlotSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotSn.setStatus("current")


class _Osl6200SlotManuDate_Type(OctetString):
    """Custom type osl6200SlotManuDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotManuDate_Type.__name__ = "OctetString"
_Osl6200SlotManuDate_Object = MibTableColumn
osl6200SlotManuDate = _Osl6200SlotManuDate_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 9),
    _Osl6200SlotManuDate_Type()
)
osl6200SlotManuDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotManuDate.setStatus("current")


class _Osl6200SlotManuVendor_Type(OctetString):
    """Custom type osl6200SlotManuVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotManuVendor_Type.__name__ = "OctetString"
_Osl6200SlotManuVendor_Object = MibTableColumn
osl6200SlotManuVendor = _Osl6200SlotManuVendor_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 10),
    _Osl6200SlotManuVendor_Type()
)
osl6200SlotManuVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotManuVendor.setStatus("current")


class _Osl6200SlotTemperature_Type(OctetString):
    """Custom type osl6200SlotTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Osl6200SlotTemperature_Type.__name__ = "OctetString"
_Osl6200SlotTemperature_Object = MibTableColumn
osl6200SlotTemperature = _Osl6200SlotTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 11),
    _Osl6200SlotTemperature_Type()
)
osl6200SlotTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotTemperature.setStatus("current")
if mibBuilder.loadTexts:
    osl6200SlotTemperature.setUnits("C")


class _Osl6200SlotPower1Status_Type(Integer32):
    """Custom type osl6200SlotPower1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SlotPower1Status_Type.__name__ = "Integer32"
_Osl6200SlotPower1Status_Object = MibTableColumn
osl6200SlotPower1Status = _Osl6200SlotPower1Status_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 12),
    _Osl6200SlotPower1Status_Type()
)
osl6200SlotPower1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotPower1Status.setStatus("current")


class _Osl6200SlotPower1Val_Type(OctetString):
    """Custom type osl6200SlotPower1Val based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotPower1Val_Type.__name__ = "OctetString"
_Osl6200SlotPower1Val_Object = MibTableColumn
osl6200SlotPower1Val = _Osl6200SlotPower1Val_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 13),
    _Osl6200SlotPower1Val_Type()
)
osl6200SlotPower1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotPower1Val.setStatus("current")
if mibBuilder.loadTexts:
    osl6200SlotPower1Val.setUnits("V")


class _Osl6200SlotPower2Status_Type(Integer32):
    """Custom type osl6200SlotPower2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SlotPower2Status_Type.__name__ = "Integer32"
_Osl6200SlotPower2Status_Object = MibTableColumn
osl6200SlotPower2Status = _Osl6200SlotPower2Status_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 14),
    _Osl6200SlotPower2Status_Type()
)
osl6200SlotPower2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotPower2Status.setStatus("current")


class _Osl6200SlotPower2Val_Type(OctetString):
    """Custom type osl6200SlotPower2Val based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotPower2Val_Type.__name__ = "OctetString"
_Osl6200SlotPower2Val_Object = MibTableColumn
osl6200SlotPower2Val = _Osl6200SlotPower2Val_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 15),
    _Osl6200SlotPower2Val_Type()
)
osl6200SlotPower2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotPower2Val.setStatus("current")
if mibBuilder.loadTexts:
    osl6200SlotPower2Val.setUnits("V")


class _Osl6200SlotPower3Status_Type(Integer32):
    """Custom type osl6200SlotPower3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SlotPower3Status_Type.__name__ = "Integer32"
_Osl6200SlotPower3Status_Object = MibTableColumn
osl6200SlotPower3Status = _Osl6200SlotPower3Status_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 16),
    _Osl6200SlotPower3Status_Type()
)
osl6200SlotPower3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotPower3Status.setStatus("current")


class _Osl6200SlotPower3Val_Type(OctetString):
    """Custom type osl6200SlotPower3Val based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotPower3Val_Type.__name__ = "OctetString"
_Osl6200SlotPower3Val_Object = MibTableColumn
osl6200SlotPower3Val = _Osl6200SlotPower3Val_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 17),
    _Osl6200SlotPower3Val_Type()
)
osl6200SlotPower3Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotPower3Val.setStatus("current")
if mibBuilder.loadTexts:
    osl6200SlotPower3Val.setUnits("V")
_Osl6200SlotDiagStatus_Type = Unsigned32
_Osl6200SlotDiagStatus_Object = MibTableColumn
osl6200SlotDiagStatus = _Osl6200SlotDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 18),
    _Osl6200SlotDiagStatus_Type()
)
osl6200SlotDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotDiagStatus.setStatus("current")
_Osl6200SlotPowerTotalNum_Type = Integer32
_Osl6200SlotPowerTotalNum_Object = MibTableColumn
osl6200SlotPowerTotalNum = _Osl6200SlotPowerTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 19),
    _Osl6200SlotPowerTotalNum_Type()
)
osl6200SlotPowerTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotPowerTotalNum.setStatus("current")


class _Osl6200SlotSwBuildDate_Type(OctetString):
    """Custom type osl6200SlotSwBuildDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SlotSwBuildDate_Type.__name__ = "OctetString"
_Osl6200SlotSwBuildDate_Object = MibTableColumn
osl6200SlotSwBuildDate = _Osl6200SlotSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 2, 1, 20),
    _Osl6200SlotSwBuildDate_Type()
)
osl6200SlotSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SlotSwBuildDate.setStatus("current")
_OphylinkOsl6200SlotCommCtrlTable_Object = MibTable
ophylinkOsl6200SlotCommCtrlTable = _OphylinkOsl6200SlotCommCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 3)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotCommCtrlTable.setStatus("current")
_OphylinkOsl6200SlotCommCtrlEntry_Object = MibTableRow
ophylinkOsl6200SlotCommCtrlEntry = _OphylinkOsl6200SlotCommCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 3, 1)
)
ophylinkOsl6200SlotCommCtrlEntry.setIndexNames(
    (0, "OPHYLINK-OSL6200-MIB", "osl6200SCCSlotNum"),
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotCommCtrlEntry.setStatus("current")


class _Osl6200SCCSlotNum_Type(Integer32):
    """Custom type osl6200SCCSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_Osl6200SCCSlotNum_Type.__name__ = "Integer32"
_Osl6200SCCSlotNum_Object = MibTableColumn
osl6200SCCSlotNum = _Osl6200SCCSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 3, 1, 1),
    _Osl6200SCCSlotNum_Type()
)
osl6200SCCSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SCCSlotNum.setStatus("current")


class _Osl6200SCCSaveCurrentConf_Type(Integer32):
    """Custom type osl6200SCCSaveCurrentConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Osl6200SCCSaveCurrentConf_Type.__name__ = "Integer32"
_Osl6200SCCSaveCurrentConf_Object = MibTableColumn
osl6200SCCSaveCurrentConf = _Osl6200SCCSaveCurrentConf_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 3, 1, 2),
    _Osl6200SCCSaveCurrentConf_Type()
)
osl6200SCCSaveCurrentConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osl6200SCCSaveCurrentConf.setStatus("current")


class _Osl6200SCCReset2Factory_Type(Integer32):
    """Custom type osl6200SCCReset2Factory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Osl6200SCCReset2Factory_Type.__name__ = "Integer32"
_Osl6200SCCReset2Factory_Object = MibTableColumn
osl6200SCCReset2Factory = _Osl6200SCCReset2Factory_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 3, 1, 3),
    _Osl6200SCCReset2Factory_Type()
)
osl6200SCCReset2Factory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osl6200SCCReset2Factory.setStatus("current")


class _Osl6200SCCReboot_Type(Integer32):
    """Custom type osl6200SCCReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Osl6200SCCReboot_Type.__name__ = "Integer32"
_Osl6200SCCReboot_Object = MibTableColumn
osl6200SCCReboot = _Osl6200SCCReboot_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 3, 1, 4),
    _Osl6200SCCReboot_Type()
)
osl6200SCCReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osl6200SCCReboot.setStatus("current")
_OphylinkOsl6200CommAlarm_ObjectIdentity = ObjectIdentity
ophylinkOsl6200CommAlarm = _OphylinkOsl6200CommAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200CommAlarm.setStatus("current")
_OphylinkOsl6200SystemAlarm_ObjectIdentity = ObjectIdentity
ophylinkOsl6200SystemAlarm = _OphylinkOsl6200SystemAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SystemAlarm.setStatus("current")


class _Osl6200TempAlarm_Type(Integer32):
    """Custom type osl6200TempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Osl6200TempAlarm_Type.__name__ = "Integer32"
_Osl6200TempAlarm_Object = MibScalar
osl6200TempAlarm = _Osl6200TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 1),
    _Osl6200TempAlarm_Type()
)
osl6200TempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200TempAlarm.setStatus("current")


class _Osl6200SystemPowerAAlarm_Type(Integer32):
    """Custom type osl6200SystemPowerAAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SystemPowerAAlarm_Type.__name__ = "Integer32"
_Osl6200SystemPowerAAlarm_Object = MibScalar
osl6200SystemPowerAAlarm = _Osl6200SystemPowerAAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 2),
    _Osl6200SystemPowerAAlarm_Type()
)
osl6200SystemPowerAAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SystemPowerAAlarm.setStatus("current")


class _Osl6200SystemPowerBAlarm_Type(Integer32):
    """Custom type osl6200SystemPowerBAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SystemPowerBAlarm_Type.__name__ = "Integer32"
_Osl6200SystemPowerBAlarm_Object = MibScalar
osl6200SystemPowerBAlarm = _Osl6200SystemPowerBAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 3),
    _Osl6200SystemPowerBAlarm_Type()
)
osl6200SystemPowerBAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SystemPowerBAlarm.setStatus("current")


class _Osl6200SystemPowerCAlarm_Type(Integer32):
    """Custom type osl6200SystemPowerCAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SystemPowerCAlarm_Type.__name__ = "Integer32"
_Osl6200SystemPowerCAlarm_Object = MibScalar
osl6200SystemPowerCAlarm = _Osl6200SystemPowerCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 4),
    _Osl6200SystemPowerCAlarm_Type()
)
osl6200SystemPowerCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SystemPowerCAlarm.setStatus("current")


class _Osl6200SystemFan1Alarm_Type(Integer32):
    """Custom type osl6200SystemFan1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SystemFan1Alarm_Type.__name__ = "Integer32"
_Osl6200SystemFan1Alarm_Object = MibScalar
osl6200SystemFan1Alarm = _Osl6200SystemFan1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 5),
    _Osl6200SystemFan1Alarm_Type()
)
osl6200SystemFan1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SystemFan1Alarm.setStatus("current")


class _Osl6200SystemFan2Alarm_Type(Integer32):
    """Custom type osl6200SystemFan2Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SystemFan2Alarm_Type.__name__ = "Integer32"
_Osl6200SystemFan2Alarm_Object = MibScalar
osl6200SystemFan2Alarm = _Osl6200SystemFan2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 6),
    _Osl6200SystemFan2Alarm_Type()
)
osl6200SystemFan2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SystemFan2Alarm.setStatus("current")


class _Osl6200SystemFan3Alarm_Type(Integer32):
    """Custom type osl6200SystemFan3Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SystemFan3Alarm_Type.__name__ = "Integer32"
_Osl6200SystemFan3Alarm_Object = MibScalar
osl6200SystemFan3Alarm = _Osl6200SystemFan3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 7),
    _Osl6200SystemFan3Alarm_Type()
)
osl6200SystemFan3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SystemFan3Alarm.setStatus("current")


class _Osl6200SystemFan4Alarm_Type(Integer32):
    """Custom type osl6200SystemFan4Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SystemFan4Alarm_Type.__name__ = "Integer32"
_Osl6200SystemFan4Alarm_Object = MibScalar
osl6200SystemFan4Alarm = _Osl6200SystemFan4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 8),
    _Osl6200SystemFan4Alarm_Type()
)
osl6200SystemFan4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SystemFan4Alarm.setStatus("current")


class _Osl6200CriticalAlarm_Type(Integer32):
    """Custom type osl6200CriticalAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200CriticalAlarm_Type.__name__ = "Integer32"
_Osl6200CriticalAlarm_Object = MibScalar
osl6200CriticalAlarm = _Osl6200CriticalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 9),
    _Osl6200CriticalAlarm_Type()
)
osl6200CriticalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200CriticalAlarm.setStatus("current")


class _Osl6200MajorAlarm_Type(Integer32):
    """Custom type osl6200MajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200MajorAlarm_Type.__name__ = "Integer32"
_Osl6200MajorAlarm_Object = MibScalar
osl6200MajorAlarm = _Osl6200MajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 10),
    _Osl6200MajorAlarm_Type()
)
osl6200MajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200MajorAlarm.setStatus("current")


class _Osl6200MinorAlarm_Type(Integer32):
    """Custom type osl6200MinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200MinorAlarm_Type.__name__ = "Integer32"
_Osl6200MinorAlarm_Object = MibScalar
osl6200MinorAlarm = _Osl6200MinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 1, 11),
    _Osl6200MinorAlarm_Type()
)
osl6200MinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200MinorAlarm.setStatus("current")
_OphylinkOsl6200SlotAlarmCommTable_Object = MibTable
ophylinkOsl6200SlotAlarmCommTable = _OphylinkOsl6200SlotAlarmCommTable_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotAlarmCommTable.setStatus("current")
_OphylinkOsl6200SlotAlarmCommEntry_Object = MibTableRow
ophylinkOsl6200SlotAlarmCommEntry = _OphylinkOsl6200SlotAlarmCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1)
)
ophylinkOsl6200SlotAlarmCommEntry.setIndexNames(
    (0, "OPHYLINK-OSL6200-MIB", "osl6200SACSlotNum"),
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotAlarmCommEntry.setStatus("current")


class _Osl6200SACSlotNum_Type(Integer32):
    """Custom type osl6200SACSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_Osl6200SACSlotNum_Type.__name__ = "Integer32"
_Osl6200SACSlotNum_Object = MibTableColumn
osl6200SACSlotNum = _Osl6200SACSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 1),
    _Osl6200SACSlotNum_Type()
)
osl6200SACSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SACSlotNum.setStatus("current")


class _Osl6200SACAlarmSummary_Type(Integer32):
    """Custom type osl6200SACAlarmSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SACAlarmSummary_Type.__name__ = "Integer32"
_Osl6200SACAlarmSummary_Object = MibTableColumn
osl6200SACAlarmSummary = _Osl6200SACAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 2),
    _Osl6200SACAlarmSummary_Type()
)
osl6200SACAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SACAlarmSummary.setStatus("current")
_Osl6200SACSlotStatusAlarm_Type = Integer32
_Osl6200SACSlotStatusAlarm_Object = MibTableColumn
osl6200SACSlotStatusAlarm = _Osl6200SACSlotStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 3),
    _Osl6200SACSlotStatusAlarm_Type()
)
osl6200SACSlotStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SACSlotStatusAlarm.setStatus("current")


class _Osl6200SACSlotTempAlarm_Type(Integer32):
    """Custom type osl6200SACSlotTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Osl6200SACSlotTempAlarm_Type.__name__ = "Integer32"
_Osl6200SACSlotTempAlarm_Object = MibTableColumn
osl6200SACSlotTempAlarm = _Osl6200SACSlotTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 4),
    _Osl6200SACSlotTempAlarm_Type()
)
osl6200SACSlotTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SACSlotTempAlarm.setStatus("current")


class _Osl6200SACPower1Alarm_Type(Integer32):
    """Custom type osl6200SACPower1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SACPower1Alarm_Type.__name__ = "Integer32"
_Osl6200SACPower1Alarm_Object = MibTableColumn
osl6200SACPower1Alarm = _Osl6200SACPower1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 5),
    _Osl6200SACPower1Alarm_Type()
)
osl6200SACPower1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SACPower1Alarm.setStatus("current")


class _Osl6200SACPower2Alarm_Type(Integer32):
    """Custom type osl6200SACPower2Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SACPower2Alarm_Type.__name__ = "Integer32"
_Osl6200SACPower2Alarm_Object = MibTableColumn
osl6200SACPower2Alarm = _Osl6200SACPower2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 6),
    _Osl6200SACPower2Alarm_Type()
)
osl6200SACPower2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SACPower2Alarm.setStatus("current")


class _Osl6200SACPower3Alarm_Type(Integer32):
    """Custom type osl6200SACPower3Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Osl6200SACPower3Alarm_Type.__name__ = "Integer32"
_Osl6200SACPower3Alarm_Object = MibTableColumn
osl6200SACPower3Alarm = _Osl6200SACPower3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 7),
    _Osl6200SACPower3Alarm_Type()
)
osl6200SACPower3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SACPower3Alarm.setStatus("current")


class _Osl6200SACSlotTempHighThld_Type(OctetString):
    """Custom type osl6200SACSlotTempHighThld based on OctetString"""
    defaultValue = OctetString("85")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SACSlotTempHighThld_Type.__name__ = "OctetString"
_Osl6200SACSlotTempHighThld_Object = MibTableColumn
osl6200SACSlotTempHighThld = _Osl6200SACSlotTempHighThld_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 8),
    _Osl6200SACSlotTempHighThld_Type()
)
osl6200SACSlotTempHighThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osl6200SACSlotTempHighThld.setStatus("current")
if mibBuilder.loadTexts:
    osl6200SACSlotTempHighThld.setUnits("C")


class _Osl6200SACSlotTempLowThld_Type(OctetString):
    """Custom type osl6200SACSlotTempLowThld based on OctetString"""
    defaultValue = OctetString("-5")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Osl6200SACSlotTempLowThld_Type.__name__ = "OctetString"
_Osl6200SACSlotTempLowThld_Object = MibTableColumn
osl6200SACSlotTempLowThld = _Osl6200SACSlotTempLowThld_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 4, 2, 1, 9),
    _Osl6200SACSlotTempLowThld_Type()
)
osl6200SACSlotTempLowThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osl6200SACSlotTempLowThld.setStatus("current")
if mibBuilder.loadTexts:
    osl6200SACSlotTempLowThld.setUnits("C")
_OphylinkOsl6200CommNotifications_ObjectIdentity = ObjectIdentity
ophylinkOsl6200CommNotifications = _OphylinkOsl6200CommNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200CommNotifications.setStatus("current")
_OphylinkOsl6200LedStatus_ObjectIdentity = ObjectIdentity
ophylinkOsl6200LedStatus = _OphylinkOsl6200LedStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200LedStatus.setStatus("current")
_OphylinkOsl6200PanelLeds_ObjectIdentity = ObjectIdentity
ophylinkOsl6200PanelLeds = _OphylinkOsl6200PanelLeds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200PanelLeds.setStatus("current")
_OphylinkOsl6200LedPwrA_Type = Integer32
_OphylinkOsl6200LedPwrA_Object = MibScalar
ophylinkOsl6200LedPwrA = _OphylinkOsl6200LedPwrA_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 1),
    _OphylinkOsl6200LedPwrA_Type()
)
ophylinkOsl6200LedPwrA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedPwrA.setStatus("current")
_OphylinkOsl6200LedPwrB_Type = Integer32
_OphylinkOsl6200LedPwrB_Object = MibScalar
ophylinkOsl6200LedPwrB = _OphylinkOsl6200LedPwrB_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 2),
    _OphylinkOsl6200LedPwrB_Type()
)
ophylinkOsl6200LedPwrB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedPwrB.setStatus("current")
_OphylinkOsl6200LedPwrC_Type = Integer32
_OphylinkOsl6200LedPwrC_Object = MibScalar
ophylinkOsl6200LedPwrC = _OphylinkOsl6200LedPwrC_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 3),
    _OphylinkOsl6200LedPwrC_Type()
)
ophylinkOsl6200LedPwrC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedPwrC.setStatus("current")
_OphylinkOsl6200LedOAMA_Type = Integer32
_OphylinkOsl6200LedOAMA_Object = MibScalar
ophylinkOsl6200LedOAMA = _OphylinkOsl6200LedOAMA_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 4),
    _OphylinkOsl6200LedOAMA_Type()
)
ophylinkOsl6200LedOAMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedOAMA.setStatus("current")
_OphylinkOsl6200LedOAMB_Type = Integer32
_OphylinkOsl6200LedOAMB_Object = MibScalar
ophylinkOsl6200LedOAMB = _OphylinkOsl6200LedOAMB_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 5),
    _OphylinkOsl6200LedOAMB_Type()
)
ophylinkOsl6200LedOAMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedOAMB.setStatus("current")
_OphylinkOsl6200LedFan_Type = Integer32
_OphylinkOsl6200LedFan_Object = MibScalar
ophylinkOsl6200LedFan = _OphylinkOsl6200LedFan_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 6),
    _OphylinkOsl6200LedFan_Type()
)
ophylinkOsl6200LedFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedFan.setStatus("current")
_OphylinkOsl6200LedCritical_Type = Integer32
_OphylinkOsl6200LedCritical_Object = MibScalar
ophylinkOsl6200LedCritical = _OphylinkOsl6200LedCritical_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 7),
    _OphylinkOsl6200LedCritical_Type()
)
ophylinkOsl6200LedCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedCritical.setStatus("current")
_OphylinkOsl6200LedMajor_Type = Integer32
_OphylinkOsl6200LedMajor_Object = MibScalar
ophylinkOsl6200LedMajor = _OphylinkOsl6200LedMajor_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 8),
    _OphylinkOsl6200LedMajor_Type()
)
ophylinkOsl6200LedMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedMajor.setStatus("current")
_OphylinkOsl6200LedMinor_Type = Integer32
_OphylinkOsl6200LedMinor_Object = MibScalar
ophylinkOsl6200LedMinor = _OphylinkOsl6200LedMinor_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 1, 9),
    _OphylinkOsl6200LedMinor_Type()
)
ophylinkOsl6200LedMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ophylinkOsl6200LedMinor.setStatus("current")
_OphylinkOsl6200SlotCommLedStatusTable_Object = MibTable
ophylinkOsl6200SlotCommLedStatusTable = _OphylinkOsl6200SlotCommLedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotCommLedStatusTable.setStatus("current")
_OphylinkOsl6200SlotCommLedStatusEntry_Object = MibTableRow
ophylinkOsl6200SlotCommLedStatusEntry = _OphylinkOsl6200SlotCommLedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2, 1)
)
ophylinkOsl6200SlotCommLedStatusEntry.setIndexNames(
    (0, "OPHYLINK-OSL6200-MIB", "osl6200SCLSSlotNum"),
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotCommLedStatusEntry.setStatus("current")


class _Osl6200SCLSSlotNum_Type(Integer32):
    """Custom type osl6200SCLSSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_Osl6200SCLSSlotNum_Type.__name__ = "Integer32"
_Osl6200SCLSSlotNum_Object = MibTableColumn
osl6200SCLSSlotNum = _Osl6200SCLSSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2, 1, 1),
    _Osl6200SCLSSlotNum_Type()
)
osl6200SCLSSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SCLSSlotNum.setStatus("current")
_Osl6200SCLSSlotLedPwr_Type = Integer32
_Osl6200SCLSSlotLedPwr_Object = MibTableColumn
osl6200SCLSSlotLedPwr = _Osl6200SCLSSlotLedPwr_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2, 1, 2),
    _Osl6200SCLSSlotLedPwr_Type()
)
osl6200SCLSSlotLedPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SCLSSlotLedPwr.setStatus("current")
_Osl6200SCLSSlotLedAlm_Type = Integer32
_Osl6200SCLSSlotLedAlm_Object = MibTableColumn
osl6200SCLSSlotLedAlm = _Osl6200SCLSSlotLedAlm_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2, 1, 3),
    _Osl6200SCLSSlotLedAlm_Type()
)
osl6200SCLSSlotLedAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SCLSSlotLedAlm.setStatus("current")
_Osl6200SCLSSlotLedRun_Type = Integer32
_Osl6200SCLSSlotLedRun_Object = MibTableColumn
osl6200SCLSSlotLedRun = _Osl6200SCLSSlotLedRun_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2, 1, 4),
    _Osl6200SCLSSlotLedRun_Type()
)
osl6200SCLSSlotLedRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SCLSSlotLedRun.setStatus("current")
_Osl6200SCLSSlotLedFault_Type = Integer32
_Osl6200SCLSSlotLedFault_Object = MibTableColumn
osl6200SCLSSlotLedFault = _Osl6200SCLSSlotLedFault_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2, 1, 5),
    _Osl6200SCLSSlotLedFault_Type()
)
osl6200SCLSSlotLedFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SCLSSlotLedFault.setStatus("current")
_Osl6200SCLSSlotLedAct_Type = Integer32
_Osl6200SCLSSlotLedAct_Object = MibTableColumn
osl6200SCLSSlotLedAct = _Osl6200SCLSSlotLedAct_Object(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 6, 2, 1, 6),
    _Osl6200SCLSSlotLedAct_Type()
)
osl6200SCLSSlotLedAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osl6200SCLSSlotLedAct.setStatus("current")

# Managed Objects groups


# Notification objects

ophylinkOsl6200SysTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 1)
)
ophylinkOsl6200SysTemperatureEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200TempAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysTemperatureEvent.setStatus(
        "current"
    )

ophylinkOsl6200SysPowerAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 2)
)
ophylinkOsl6200SysPowerAEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SystemPowerAAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysPowerAEvent.setStatus(
        "current"
    )

ophylinkOsl6200SysPowerBEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 3)
)
ophylinkOsl6200SysPowerBEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SystemPowerBAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysPowerBEvent.setStatus(
        "current"
    )

ophylinkOsl6200SysPowerCEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 4)
)
ophylinkOsl6200SysPowerCEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SystemPowerCAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysPowerCEvent.setStatus(
        "current"
    )

ophylinkOsl6200SysFan1Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 5)
)
ophylinkOsl6200SysFan1Event.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SystemFan1Alarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysFan1Event.setStatus(
        "current"
    )

ophylinkOsl6200SysFan2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 6)
)
ophylinkOsl6200SysFan2Event.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SystemFan2Alarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysFan2Event.setStatus(
        "current"
    )

ophylinkOsl6200SysFan3Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 7)
)
ophylinkOsl6200SysFan3Event.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SystemFan3Alarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysFan3Event.setStatus(
        "current"
    )

ophylinkOsl6200SysFan4Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 8)
)
ophylinkOsl6200SysFan4Event.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SystemFan4Alarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SysFan4Event.setStatus(
        "current"
    )

ophylinkOsl6200SlotTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 9)
)
ophylinkOsl6200SlotTemperatureEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SACSlotTempAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotTemperatureEvent.setStatus(
        "current"
    )

ophylinkOsl6200SlotPower1Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 10)
)
ophylinkOsl6200SlotPower1Event.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SACPower1Alarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotPower1Event.setStatus(
        "current"
    )

ophylinkOsl6200SlotPower2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 11)
)
ophylinkOsl6200SlotPower2Event.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SACPower2Alarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotPower2Event.setStatus(
        "current"
    )

ophylinkOsl6200SlotPower3Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 12)
)
ophylinkOsl6200SlotPower3Event.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SACPower3Alarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotPower3Event.setStatus(
        "current"
    )

ophylinkOsl6200SlotStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 13)
)
ophylinkOsl6200SlotStatusEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200SACSlotStatusAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200SlotStatusEvent.setStatus(
        "current"
    )

ophylinkOsl6200CriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 14)
)
ophylinkOsl6200CriticalEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200CriticalAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200CriticalEvent.setStatus(
        "current"
    )

ophylinkOsl6200MajorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 15)
)
ophylinkOsl6200MajorEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200MinorAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200MajorEvent.setStatus(
        "current"
    )

ophylinkOsl6200MinorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42861, 3, 4, 5, 16)
)
ophylinkOsl6200MinorEvent.setObjects(
    ("OPHYLINK-OSL6200-MIB", "osl6200MajorAlarm")
)
if mibBuilder.loadTexts:
    ophylinkOsl6200MinorEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPHYLINK-OSL6200-MIB",
    **{"ophylinkOsl6200": ophylinkOsl6200,
       "ophylinkOsl6200SlotStatusTable": ophylinkOsl6200SlotStatusTable,
       "ophylinkOsl6200SlotStatusEntry": ophylinkOsl6200SlotStatusEntry,
       "oSSSlotNum": oSSSlotNum,
       "oSSSlotStatus": oSSSlotStatus,
       "ophylinkOsl6200SlotBasicInfoTable": ophylinkOsl6200SlotBasicInfoTable,
       "ophylinkOsl6200SlotBasicInfoEntry": ophylinkOsl6200SlotBasicInfoEntry,
       "osl6200SlotNum": osl6200SlotNum,
       "osl6200SlotReady": osl6200SlotReady,
       "osl6200SlotType": osl6200SlotType,
       "osl6200SlotHwVer": osl6200SlotHwVer,
       "osl6200SlotSwVer": osl6200SlotSwVer,
       "osl6200SlotFwVer": osl6200SlotFwVer,
       "osl6200SlotModel": osl6200SlotModel,
       "osl6200SlotSn": osl6200SlotSn,
       "osl6200SlotManuDate": osl6200SlotManuDate,
       "osl6200SlotManuVendor": osl6200SlotManuVendor,
       "osl6200SlotTemperature": osl6200SlotTemperature,
       "osl6200SlotPower1Status": osl6200SlotPower1Status,
       "osl6200SlotPower1Val": osl6200SlotPower1Val,
       "osl6200SlotPower2Status": osl6200SlotPower2Status,
       "osl6200SlotPower2Val": osl6200SlotPower2Val,
       "osl6200SlotPower3Status": osl6200SlotPower3Status,
       "osl6200SlotPower3Val": osl6200SlotPower3Val,
       "osl6200SlotDiagStatus": osl6200SlotDiagStatus,
       "osl6200SlotPowerTotalNum": osl6200SlotPowerTotalNum,
       "osl6200SlotSwBuildDate": osl6200SlotSwBuildDate,
       "ophylinkOsl6200SlotCommCtrlTable": ophylinkOsl6200SlotCommCtrlTable,
       "ophylinkOsl6200SlotCommCtrlEntry": ophylinkOsl6200SlotCommCtrlEntry,
       "osl6200SCCSlotNum": osl6200SCCSlotNum,
       "osl6200SCCSaveCurrentConf": osl6200SCCSaveCurrentConf,
       "osl6200SCCReset2Factory": osl6200SCCReset2Factory,
       "osl6200SCCReboot": osl6200SCCReboot,
       "ophylinkOsl6200CommAlarm": ophylinkOsl6200CommAlarm,
       "ophylinkOsl6200SystemAlarm": ophylinkOsl6200SystemAlarm,
       "osl6200TempAlarm": osl6200TempAlarm,
       "osl6200SystemPowerAAlarm": osl6200SystemPowerAAlarm,
       "osl6200SystemPowerBAlarm": osl6200SystemPowerBAlarm,
       "osl6200SystemPowerCAlarm": osl6200SystemPowerCAlarm,
       "osl6200SystemFan1Alarm": osl6200SystemFan1Alarm,
       "osl6200SystemFan2Alarm": osl6200SystemFan2Alarm,
       "osl6200SystemFan3Alarm": osl6200SystemFan3Alarm,
       "osl6200SystemFan4Alarm": osl6200SystemFan4Alarm,
       "osl6200CriticalAlarm": osl6200CriticalAlarm,
       "osl6200MajorAlarm": osl6200MajorAlarm,
       "osl6200MinorAlarm": osl6200MinorAlarm,
       "ophylinkOsl6200SlotAlarmCommTable": ophylinkOsl6200SlotAlarmCommTable,
       "ophylinkOsl6200SlotAlarmCommEntry": ophylinkOsl6200SlotAlarmCommEntry,
       "osl6200SACSlotNum": osl6200SACSlotNum,
       "osl6200SACAlarmSummary": osl6200SACAlarmSummary,
       "osl6200SACSlotStatusAlarm": osl6200SACSlotStatusAlarm,
       "osl6200SACSlotTempAlarm": osl6200SACSlotTempAlarm,
       "osl6200SACPower1Alarm": osl6200SACPower1Alarm,
       "osl6200SACPower2Alarm": osl6200SACPower2Alarm,
       "osl6200SACPower3Alarm": osl6200SACPower3Alarm,
       "osl6200SACSlotTempHighThld": osl6200SACSlotTempHighThld,
       "osl6200SACSlotTempLowThld": osl6200SACSlotTempLowThld,
       "ophylinkOsl6200CommNotifications": ophylinkOsl6200CommNotifications,
       "ophylinkOsl6200SysTemperatureEvent": ophylinkOsl6200SysTemperatureEvent,
       "ophylinkOsl6200SysPowerAEvent": ophylinkOsl6200SysPowerAEvent,
       "ophylinkOsl6200SysPowerBEvent": ophylinkOsl6200SysPowerBEvent,
       "ophylinkOsl6200SysPowerCEvent": ophylinkOsl6200SysPowerCEvent,
       "ophylinkOsl6200SysFan1Event": ophylinkOsl6200SysFan1Event,
       "ophylinkOsl6200SysFan2Event": ophylinkOsl6200SysFan2Event,
       "ophylinkOsl6200SysFan3Event": ophylinkOsl6200SysFan3Event,
       "ophylinkOsl6200SysFan4Event": ophylinkOsl6200SysFan4Event,
       "ophylinkOsl6200SlotTemperatureEvent": ophylinkOsl6200SlotTemperatureEvent,
       "ophylinkOsl6200SlotPower1Event": ophylinkOsl6200SlotPower1Event,
       "ophylinkOsl6200SlotPower2Event": ophylinkOsl6200SlotPower2Event,
       "ophylinkOsl6200SlotPower3Event": ophylinkOsl6200SlotPower3Event,
       "ophylinkOsl6200SlotStatusEvent": ophylinkOsl6200SlotStatusEvent,
       "ophylinkOsl6200CriticalEvent": ophylinkOsl6200CriticalEvent,
       "ophylinkOsl6200MajorEvent": ophylinkOsl6200MajorEvent,
       "ophylinkOsl6200MinorEvent": ophylinkOsl6200MinorEvent,
       "ophylinkOsl6200LedStatus": ophylinkOsl6200LedStatus,
       "ophylinkOsl6200PanelLeds": ophylinkOsl6200PanelLeds,
       "ophylinkOsl6200LedPwrA": ophylinkOsl6200LedPwrA,
       "ophylinkOsl6200LedPwrB": ophylinkOsl6200LedPwrB,
       "ophylinkOsl6200LedPwrC": ophylinkOsl6200LedPwrC,
       "ophylinkOsl6200LedOAMA": ophylinkOsl6200LedOAMA,
       "ophylinkOsl6200LedOAMB": ophylinkOsl6200LedOAMB,
       "ophylinkOsl6200LedFan": ophylinkOsl6200LedFan,
       "ophylinkOsl6200LedCritical": ophylinkOsl6200LedCritical,
       "ophylinkOsl6200LedMajor": ophylinkOsl6200LedMajor,
       "ophylinkOsl6200LedMinor": ophylinkOsl6200LedMinor,
       "ophylinkOsl6200SlotCommLedStatusTable": ophylinkOsl6200SlotCommLedStatusTable,
       "ophylinkOsl6200SlotCommLedStatusEntry": ophylinkOsl6200SlotCommLedStatusEntry,
       "osl6200SCLSSlotNum": osl6200SCLSSlotNum,
       "osl6200SCLSSlotLedPwr": osl6200SCLSSlotLedPwr,
       "osl6200SCLSSlotLedAlm": osl6200SCLSSlotLedAlm,
       "osl6200SCLSSlotLedRun": osl6200SCLSSlotLedRun,
       "osl6200SCLSSlotLedFault": osl6200SCLSSlotLedFault,
       "osl6200SCLSSlotLedAct": osl6200SCLSSlotLedAct}
)
