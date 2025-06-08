# SNMP MIB module (CISCO-URWB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-URWB-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:39 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifNumber,
 ifTable) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifNumber",
    "ifTable")

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

ciscoUrwb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056)
)
if mibBuilder.loadTexts:
    ciscoUrwb.setRevisions(
        ("2022-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoUrwbInfo_ObjectIdentity = ObjectIdentity
ciscoUrwbInfo = _CiscoUrwbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11)
)


class _CiscoUrwbOperMode_Type(DisplayString):
    """Custom type ciscoUrwbOperMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbOperMode_Type.__name__ = "DisplayString"
_CiscoUrwbOperMode_Object = MibScalar
ciscoUrwbOperMode = _CiscoUrwbOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 1),
    _CiscoUrwbOperMode_Type()
)
ciscoUrwbOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbOperMode.setStatus("current")


class _CiscoUrwbModel_Type(DisplayString):
    """Custom type ciscoUrwbModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbModel_Type.__name__ = "DisplayString"
_CiscoUrwbModel_Object = MibScalar
ciscoUrwbModel = _CiscoUrwbModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 2),
    _CiscoUrwbModel_Type()
)
ciscoUrwbModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbModel.setStatus("current")


class _CiscoUrwbFwVersion_Type(DisplayString):
    """Custom type ciscoUrwbFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbFwVersion_Type.__name__ = "DisplayString"
_CiscoUrwbFwVersion_Object = MibScalar
ciscoUrwbFwVersion = _CiscoUrwbFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 3),
    _CiscoUrwbFwVersion_Type()
)
ciscoUrwbFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbFwVersion.setStatus("current")


class _CiscoUrwbWs1_Type(DisplayString):
    """Custom type ciscoUrwbWs1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbWs1_Type.__name__ = "DisplayString"
_CiscoUrwbWs1_Object = MibScalar
ciscoUrwbWs1 = _CiscoUrwbWs1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 4),
    _CiscoUrwbWs1_Type()
)
ciscoUrwbWs1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbWs1.setStatus("current")


class _CiscoUrwbWs2_Type(DisplayString):
    """Custom type ciscoUrwbWs2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbWs2_Type.__name__ = "DisplayString"
_CiscoUrwbWs2_Object = MibScalar
ciscoUrwbWs2 = _CiscoUrwbWs2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 5),
    _CiscoUrwbWs2_Type()
)
ciscoUrwbWs2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbWs2.setStatus("current")
_CiscoUrwbFreq1_Type = Integer32
_CiscoUrwbFreq1_Object = MibScalar
ciscoUrwbFreq1 = _CiscoUrwbFreq1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 6),
    _CiscoUrwbFreq1_Type()
)
ciscoUrwbFreq1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbFreq1.setStatus("current")
_CiscoUrwbChanWidth1_Type = Integer32
_CiscoUrwbChanWidth1_Object = MibScalar
ciscoUrwbChanWidth1 = _CiscoUrwbChanWidth1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 7),
    _CiscoUrwbChanWidth1_Type()
)
ciscoUrwbChanWidth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbChanWidth1.setStatus("current")
_CiscoUrwbFreq2_Type = Integer32
_CiscoUrwbFreq2_Object = MibScalar
ciscoUrwbFreq2 = _CiscoUrwbFreq2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 8),
    _CiscoUrwbFreq2_Type()
)
ciscoUrwbFreq2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbFreq2.setStatus("current")
_CiscoUrwbChanWidth2_Type = Integer32
_CiscoUrwbChanWidth2_Object = MibScalar
ciscoUrwbChanWidth2 = _CiscoUrwbChanWidth2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 9),
    _CiscoUrwbChanWidth2_Type()
)
ciscoUrwbChanWidth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbChanWidth2.setStatus("current")


class _CiscoUrwbName_Type(DisplayString):
    """Custom type ciscoUrwbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbName_Type.__name__ = "DisplayString"
_CiscoUrwbName_Object = MibScalar
ciscoUrwbName = _CiscoUrwbName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 10),
    _CiscoUrwbName_Type()
)
ciscoUrwbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbName.setStatus("current")
_CiscoUrwbMid_Type = IpAddress
_CiscoUrwbMid_Object = MibScalar
ciscoUrwbMid = _CiscoUrwbMid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 11),
    _CiscoUrwbMid_Type()
)
ciscoUrwbMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbMid.setStatus("current")


class _CiscoUrwbUptime_Type(DisplayString):
    """Custom type ciscoUrwbUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbUptime_Type.__name__ = "DisplayString"
_CiscoUrwbUptime_Object = MibScalar
ciscoUrwbUptime = _CiscoUrwbUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 12),
    _CiscoUrwbUptime_Type()
)
ciscoUrwbUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbUptime.setStatus("current")


class _CiscoUrwbSerial_Type(DisplayString):
    """Custom type ciscoUrwbSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbSerial_Type.__name__ = "DisplayString"
_CiscoUrwbSerial_Object = MibScalar
ciscoUrwbSerial = _CiscoUrwbSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 13),
    _CiscoUrwbSerial_Type()
)
ciscoUrwbSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbSerial.setStatus("current")


class _CiscoUrwbDate_Type(DisplayString):
    """Custom type ciscoUrwbDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbDate_Type.__name__ = "DisplayString"
_CiscoUrwbDate_Object = MibScalar
ciscoUrwbDate = _CiscoUrwbDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 14),
    _CiscoUrwbDate_Type()
)
ciscoUrwbDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbDate.setStatus("current")
_CiscoUrwbStaNum_Type = Integer32
_CiscoUrwbStaNum_Object = MibScalar
ciscoUrwbStaNum = _CiscoUrwbStaNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 20),
    _CiscoUrwbStaNum_Type()
)
ciscoUrwbStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaNum.setStatus("current")
_CiscoUrwbStaTable_Object = MibTable
ciscoUrwbStaTable = _CiscoUrwbStaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21)
)
if mibBuilder.loadTexts:
    ciscoUrwbStaTable.setStatus("current")
_CiscoUrwbStaEntry_Object = MibTableRow
ciscoUrwbStaEntry = _CiscoUrwbStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1)
)
ciscoUrwbStaEntry.setIndexNames(
    (0, "CISCO-URWB-MIB", "ciscoUrwbStaIndex"),
)
if mibBuilder.loadTexts:
    ciscoUrwbStaEntry.setStatus("current")


class _CiscoUrwbStaIndex_Type(Integer32):
    """Custom type ciscoUrwbStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CiscoUrwbStaIndex_Type.__name__ = "Integer32"
_CiscoUrwbStaIndex_Object = MibTableColumn
ciscoUrwbStaIndex = _CiscoUrwbStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 1),
    _CiscoUrwbStaIndex_Type()
)
ciscoUrwbStaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaIndex.setStatus("current")


class _CiscoUrwbLocalMacAddress_Type(DisplayString):
    """Custom type ciscoUrwbLocalMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbLocalMacAddress_Type.__name__ = "DisplayString"
_CiscoUrwbLocalMacAddress_Object = MibTableColumn
ciscoUrwbLocalMacAddress = _CiscoUrwbLocalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 2),
    _CiscoUrwbLocalMacAddress_Type()
)
ciscoUrwbLocalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbLocalMacAddress.setStatus("current")


class _CiscoUrwbStaMacAddress_Type(DisplayString):
    """Custom type ciscoUrwbStaMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbStaMacAddress_Type.__name__ = "DisplayString"
_CiscoUrwbStaMacAddress_Object = MibTableColumn
ciscoUrwbStaMacAddress = _CiscoUrwbStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 3),
    _CiscoUrwbStaMacAddress_Type()
)
ciscoUrwbStaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaMacAddress.setStatus("current")
_CiscoUrwbStaMid_Type = IpAddress
_CiscoUrwbStaMid_Object = MibTableColumn
ciscoUrwbStaMid = _CiscoUrwbStaMid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 4),
    _CiscoUrwbStaMid_Type()
)
ciscoUrwbStaMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaMid.setStatus("current")
_CiscoUrwbStaSignal_Type = Integer32
_CiscoUrwbStaSignal_Object = MibTableColumn
ciscoUrwbStaSignal = _CiscoUrwbStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 5),
    _CiscoUrwbStaSignal_Type()
)
ciscoUrwbStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaSignal.setStatus("current")
_CiscoUrwbStaRxBytes_Type = Counter32
_CiscoUrwbStaRxBytes_Object = MibTableColumn
ciscoUrwbStaRxBytes = _CiscoUrwbStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 6),
    _CiscoUrwbStaRxBytes_Type()
)
ciscoUrwbStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaRxBytes.setStatus("current")
_CiscoUrwbStaRxPkts_Type = Counter32
_CiscoUrwbStaRxPkts_Object = MibTableColumn
ciscoUrwbStaRxPkts = _CiscoUrwbStaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 7),
    _CiscoUrwbStaRxPkts_Type()
)
ciscoUrwbStaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaRxPkts.setStatus("current")
_CiscoUrwbStaRxRate_Type = Integer32
_CiscoUrwbStaRxRate_Object = MibTableColumn
ciscoUrwbStaRxRate = _CiscoUrwbStaRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 8),
    _CiscoUrwbStaRxRate_Type()
)
ciscoUrwbStaRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaRxRate.setStatus("current")


class _CiscoUrwbStaRxMcs_Type(DisplayString):
    """Custom type ciscoUrwbStaRxMcs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbStaRxMcs_Type.__name__ = "DisplayString"
_CiscoUrwbStaRxMcs_Object = MibTableColumn
ciscoUrwbStaRxMcs = _CiscoUrwbStaRxMcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 9),
    _CiscoUrwbStaRxMcs_Type()
)
ciscoUrwbStaRxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaRxMcs.setStatus("current")


class _CiscoUrwbStaRxMcsFlag_Type(DisplayString):
    """Custom type ciscoUrwbStaRxMcsFlag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbStaRxMcsFlag_Type.__name__ = "DisplayString"
_CiscoUrwbStaRxMcsFlag_Object = MibTableColumn
ciscoUrwbStaRxMcsFlag = _CiscoUrwbStaRxMcsFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 10),
    _CiscoUrwbStaRxMcsFlag_Type()
)
ciscoUrwbStaRxMcsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaRxMcsFlag.setStatus("current")
_CiscoUrwbStaTxBytes_Type = Counter32
_CiscoUrwbStaTxBytes_Object = MibTableColumn
ciscoUrwbStaTxBytes = _CiscoUrwbStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 11),
    _CiscoUrwbStaTxBytes_Type()
)
ciscoUrwbStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaTxBytes.setStatus("current")
_CiscoUrwbStaTxPkts_Type = Counter32
_CiscoUrwbStaTxPkts_Object = MibTableColumn
ciscoUrwbStaTxPkts = _CiscoUrwbStaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 12),
    _CiscoUrwbStaTxPkts_Type()
)
ciscoUrwbStaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaTxPkts.setStatus("current")
_CiscoUrwbStaTxFail_Type = Counter32
_CiscoUrwbStaTxFail_Object = MibTableColumn
ciscoUrwbStaTxFail = _CiscoUrwbStaTxFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 13),
    _CiscoUrwbStaTxFail_Type()
)
ciscoUrwbStaTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaTxFail.setStatus("current")
_CiscoUrwbStaTxRetry_Type = Counter32
_CiscoUrwbStaTxRetry_Object = MibTableColumn
ciscoUrwbStaTxRetry = _CiscoUrwbStaTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 14),
    _CiscoUrwbStaTxRetry_Type()
)
ciscoUrwbStaTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaTxRetry.setStatus("current")
_CiscoUrwbStaTxRate_Type = Integer32
_CiscoUrwbStaTxRate_Object = MibTableColumn
ciscoUrwbStaTxRate = _CiscoUrwbStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 15),
    _CiscoUrwbStaTxRate_Type()
)
ciscoUrwbStaTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaTxRate.setStatus("current")


class _CiscoUrwbStaTxMcs_Type(DisplayString):
    """Custom type ciscoUrwbStaTxMcs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbStaTxMcs_Type.__name__ = "DisplayString"
_CiscoUrwbStaTxMcs_Object = MibTableColumn
ciscoUrwbStaTxMcs = _CiscoUrwbStaTxMcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 16),
    _CiscoUrwbStaTxMcs_Type()
)
ciscoUrwbStaTxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaTxMcs.setStatus("current")


class _CiscoUrwbStaTxMcsFlag_Type(DisplayString):
    """Custom type ciscoUrwbStaTxMcsFlag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbStaTxMcsFlag_Type.__name__ = "DisplayString"
_CiscoUrwbStaTxMcsFlag_Object = MibTableColumn
ciscoUrwbStaTxMcsFlag = _CiscoUrwbStaTxMcsFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 21, 1, 17),
    _CiscoUrwbStaTxMcsFlag_Type()
)
ciscoUrwbStaTxMcsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaTxMcsFlag.setStatus("current")
_CiscoUrwbTputNum_Type = Integer32
_CiscoUrwbTputNum_Object = MibScalar
ciscoUrwbTputNum = _CiscoUrwbTputNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 22),
    _CiscoUrwbTputNum_Type()
)
ciscoUrwbTputNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTputNum.setStatus("current")
_CiscoUrwbTputTable_Object = MibTable
ciscoUrwbTputTable = _CiscoUrwbTputTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 23)
)
if mibBuilder.loadTexts:
    ciscoUrwbTputTable.setStatus("current")
_CiscoUrwbTputEntry_Object = MibTableRow
ciscoUrwbTputEntry = _CiscoUrwbTputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 23, 1)
)
ciscoUrwbTputEntry.setIndexNames(
    (0, "CISCO-URWB-MIB", "ciscoUrwbTputIndex"),
)
if mibBuilder.loadTexts:
    ciscoUrwbTputEntry.setStatus("current")


class _CiscoUrwbTputIndex_Type(Integer32):
    """Custom type ciscoUrwbTputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CiscoUrwbTputIndex_Type.__name__ = "Integer32"
_CiscoUrwbTputIndex_Object = MibTableColumn
ciscoUrwbTputIndex = _CiscoUrwbTputIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 23, 1, 1),
    _CiscoUrwbTputIndex_Type()
)
ciscoUrwbTputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTputIndex.setStatus("current")


class _CiscoUrwbTputIface_Type(Integer32):
    """Custom type ciscoUrwbTputIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wired", 1),
          ("wireless1", 2),
          ("wireless2", 3))
    )


_CiscoUrwbTputIface_Type.__name__ = "Integer32"
_CiscoUrwbTputIface_Object = MibTableColumn
ciscoUrwbTputIface = _CiscoUrwbTputIface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 23, 1, 2),
    _CiscoUrwbTputIface_Type()
)
ciscoUrwbTputIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTputIface.setStatus("current")
_CiscoUrwbTputTx_Type = Counter32
_CiscoUrwbTputTx_Object = MibTableColumn
ciscoUrwbTputTx = _CiscoUrwbTputTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 23, 1, 3),
    _CiscoUrwbTputTx_Type()
)
ciscoUrwbTputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTputTx.setStatus("current")
_CiscoUrwbTputRx_Type = Counter32
_CiscoUrwbTputRx_Object = MibTableColumn
ciscoUrwbTputRx = _CiscoUrwbTputRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 23, 1, 4),
    _CiscoUrwbTputRx_Type()
)
ciscoUrwbTputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTputRx.setStatus("current")


class _CiscoUrwbLoad1_Type(DisplayString):
    """Custom type ciscoUrwbLoad1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbLoad1_Type.__name__ = "DisplayString"
_CiscoUrwbLoad1_Object = MibScalar
ciscoUrwbLoad1 = _CiscoUrwbLoad1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 25),
    _CiscoUrwbLoad1_Type()
)
ciscoUrwbLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbLoad1.setStatus("current")


class _CiscoUrwbLoad5_Type(DisplayString):
    """Custom type ciscoUrwbLoad5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbLoad5_Type.__name__ = "DisplayString"
_CiscoUrwbLoad5_Object = MibScalar
ciscoUrwbLoad5 = _CiscoUrwbLoad5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 26),
    _CiscoUrwbLoad5_Type()
)
ciscoUrwbLoad5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbLoad5.setStatus("current")


class _CiscoUrwbLoad15_Type(DisplayString):
    """Custom type ciscoUrwbLoad15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbLoad15_Type.__name__ = "DisplayString"
_CiscoUrwbLoad15_Object = MibScalar
ciscoUrwbLoad15 = _CiscoUrwbLoad15_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 27),
    _CiscoUrwbLoad15_Type()
)
ciscoUrwbLoad15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbLoad15.setStatus("current")
_CiscoUrwbTemperature_Type = Integer32
_CiscoUrwbTemperature_Object = MibScalar
ciscoUrwbTemperature = _CiscoUrwbTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 28),
    _CiscoUrwbTemperature_Type()
)
ciscoUrwbTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTemperature.setStatus("current")


class _CiscoUrwbSoftwareStatus_Type(Integer32):
    """Custom type ciscoUrwbSoftwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 0),
          ("normal", 1))
    )


_CiscoUrwbSoftwareStatus_Type.__name__ = "Integer32"
_CiscoUrwbSoftwareStatus_Object = MibScalar
ciscoUrwbSoftwareStatus = _CiscoUrwbSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 29),
    _CiscoUrwbSoftwareStatus_Type()
)
ciscoUrwbSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbSoftwareStatus.setStatus("current")
_CiscoUrwbGenericHwFail_ObjectIdentity = ObjectIdentity
ciscoUrwbGenericHwFail = _CiscoUrwbGenericHwFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 30)
)


class _CiscoUrwbGenericHwFailTime_Type(DisplayString):
    """Custom type ciscoUrwbGenericHwFailTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbGenericHwFailTime_Type.__name__ = "DisplayString"
_CiscoUrwbGenericHwFailTime_Object = MibScalar
ciscoUrwbGenericHwFailTime = _CiscoUrwbGenericHwFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 30, 1),
    _CiscoUrwbGenericHwFailTime_Type()
)
ciscoUrwbGenericHwFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbGenericHwFailTime.setStatus("current")
_CiscoUrwbGenericHwFailCode_Type = Integer32
_CiscoUrwbGenericHwFailCode_Object = MibScalar
ciscoUrwbGenericHwFailCode = _CiscoUrwbGenericHwFailCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 30, 2),
    _CiscoUrwbGenericHwFailCode_Type()
)
ciscoUrwbGenericHwFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbGenericHwFailCode.setStatus("current")


class _CiscoUrwbGenericHwFailInfo_Type(DisplayString):
    """Custom type ciscoUrwbGenericHwFailInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbGenericHwFailInfo_Type.__name__ = "DisplayString"
_CiscoUrwbGenericHwFailInfo_Object = MibScalar
ciscoUrwbGenericHwFailInfo = _CiscoUrwbGenericHwFailInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 30, 3),
    _CiscoUrwbGenericHwFailInfo_Type()
)
ciscoUrwbGenericHwFailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbGenericHwFailInfo.setStatus("current")
_CiscoUrwbDetectedRadars_Type = Integer32
_CiscoUrwbDetectedRadars_Object = MibScalar
ciscoUrwbDetectedRadars = _CiscoUrwbDetectedRadars_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 31),
    _CiscoUrwbDetectedRadars_Type()
)
ciscoUrwbDetectedRadars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbDetectedRadars.setStatus("current")
_CiscoUrwbLastConfId_Type = Integer32
_CiscoUrwbLastConfId_Object = MibScalar
ciscoUrwbLastConfId = _CiscoUrwbLastConfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 32),
    _CiscoUrwbLastConfId_Type()
)
ciscoUrwbLastConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbLastConfId.setStatus("current")
_CiscoUrwbGenericHwFailLogFile_Type = Integer32
_CiscoUrwbGenericHwFailLogFile_Object = MibScalar
ciscoUrwbGenericHwFailLogFile = _CiscoUrwbGenericHwFailLogFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 33),
    _CiscoUrwbGenericHwFailLogFile_Type()
)
ciscoUrwbGenericHwFailLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoUrwbGenericHwFailLogFile.setStatus("current")
_CiscoUrwbTracksideConn_ObjectIdentity = ObjectIdentity
ciscoUrwbTracksideConn = _CiscoUrwbTracksideConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 40)
)
_CiscoUrwbTracksideConnStatic_Type = IpAddress
_CiscoUrwbTracksideConnStatic_Object = MibScalar
ciscoUrwbTracksideConnStatic = _CiscoUrwbTracksideConnStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 40, 1),
    _CiscoUrwbTracksideConnStatic_Type()
)
ciscoUrwbTracksideConnStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTracksideConnStatic.setStatus("current")
_CiscoUrwbTracksideConnMobile_Type = IpAddress
_CiscoUrwbTracksideConnMobile_Object = MibScalar
ciscoUrwbTracksideConnMobile = _CiscoUrwbTracksideConnMobile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 40, 2),
    _CiscoUrwbTracksideConnMobile_Type()
)
ciscoUrwbTracksideConnMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTracksideConnMobile.setStatus("current")
_CiscoUrwbTracksideConnMobilePrimary_Type = IpAddress
_CiscoUrwbTracksideConnMobilePrimary_Object = MibScalar
ciscoUrwbTracksideConnMobilePrimary = _CiscoUrwbTracksideConnMobilePrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 40, 3),
    _CiscoUrwbTracksideConnMobilePrimary_Type()
)
ciscoUrwbTracksideConnMobilePrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTracksideConnMobilePrimary.setStatus("current")
_CiscoUrwbTracksideConnRssi_Type = Integer32
_CiscoUrwbTracksideConnRssi_Object = MibScalar
ciscoUrwbTracksideConnRssi = _CiscoUrwbTracksideConnRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 40, 4),
    _CiscoUrwbTracksideConnRssi_Type()
)
ciscoUrwbTracksideConnRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTracksideConnRssi.setStatus("current")
_CiscoUrwbVehicleInfo_ObjectIdentity = ObjectIdentity
ciscoUrwbVehicleInfo = _CiscoUrwbVehicleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 41)
)
_CiscoUrwbTrainHead_Type = IpAddress
_CiscoUrwbTrainHead_Object = MibScalar
ciscoUrwbTrainHead = _CiscoUrwbTrainHead_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 41, 1),
    _CiscoUrwbTrainHead_Type()
)
ciscoUrwbTrainHead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTrainHead.setStatus("current")
_CiscoUrwbTrainTail_Type = IpAddress
_CiscoUrwbTrainTail_Object = MibScalar
ciscoUrwbTrainTail = _CiscoUrwbTrainTail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 41, 2),
    _CiscoUrwbTrainTail_Type()
)
ciscoUrwbTrainTail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTrainTail.setStatus("current")
_CiscoUrwbOnboardMobiles_Type = Integer32
_CiscoUrwbOnboardMobiles_Object = MibScalar
ciscoUrwbOnboardMobiles = _CiscoUrwbOnboardMobiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 11, 41, 3),
    _CiscoUrwbOnboardMobiles_Type()
)
ciscoUrwbOnboardMobiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbOnboardMobiles.setStatus("current")
_CiscoUrwbTraps_ObjectIdentity = ObjectIdentity
ciscoUrwbTraps = _CiscoUrwbTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 12)
)
_CiscoUrwbExperimental_ObjectIdentity = ObjectIdentity
ciscoUrwbExperimental = _CiscoUrwbExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 13)
)
_CiscoUrwbMobilityInfo_ObjectIdentity = ObjectIdentity
ciscoUrwbMobilityInfo = _CiscoUrwbMobilityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 14)
)
_CiscoUrwbMobileIp_Type = IpAddress
_CiscoUrwbMobileIp_Object = MibScalar
ciscoUrwbMobileIp = _CiscoUrwbMobileIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 14, 1),
    _CiscoUrwbMobileIp_Type()
)
ciscoUrwbMobileIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbMobileIp.setStatus("current")
_CiscoUrwbStaticIp_Type = IpAddress
_CiscoUrwbStaticIp_Object = MibScalar
ciscoUrwbStaticIp = _CiscoUrwbStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 14, 2),
    _CiscoUrwbStaticIp_Type()
)
ciscoUrwbStaticIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaticIp.setStatus("current")
_CiscoUrwbMobileMid_Type = IpAddress
_CiscoUrwbMobileMid_Object = MibScalar
ciscoUrwbMobileMid = _CiscoUrwbMobileMid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 14, 3),
    _CiscoUrwbMobileMid_Type()
)
ciscoUrwbMobileMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbMobileMid.setStatus("current")
_CiscoUrwbStaticMid_Type = IpAddress
_CiscoUrwbStaticMid_Object = MibScalar
ciscoUrwbStaticMid = _CiscoUrwbStaticMid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 14, 4),
    _CiscoUrwbStaticMid_Type()
)
ciscoUrwbStaticMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbStaticMid.setStatus("current")
_CiscoUrwbHandoffSeq_Type = Counter32
_CiscoUrwbHandoffSeq_Object = MibScalar
ciscoUrwbHandoffSeq = _CiscoUrwbHandoffSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 14, 7),
    _CiscoUrwbHandoffSeq_Type()
)
ciscoUrwbHandoffSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbHandoffSeq.setStatus("current")
_CiscoUrwbFailInfo_ObjectIdentity = ObjectIdentity
ciscoUrwbFailInfo = _CiscoUrwbFailInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 15)
)
_CiscoUrwbMeshId_Type = IpAddress
_CiscoUrwbMeshId_Object = MibScalar
ciscoUrwbMeshId = _CiscoUrwbMeshId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 15, 1),
    _CiscoUrwbMeshId_Type()
)
ciscoUrwbMeshId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbMeshId.setStatus("current")


class _CiscoUrwbTimestamp_Type(DisplayString):
    """Custom type ciscoUrwbTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbTimestamp_Type.__name__ = "DisplayString"
_CiscoUrwbTimestamp_Object = MibScalar
ciscoUrwbTimestamp = _CiscoUrwbTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 15, 2),
    _CiscoUrwbTimestamp_Type()
)
ciscoUrwbTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTimestamp.setStatus("current")
_CiscoUrwbErrorCode_Type = Integer32
_CiscoUrwbErrorCode_Object = MibScalar
ciscoUrwbErrorCode = _CiscoUrwbErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 15, 3),
    _CiscoUrwbErrorCode_Type()
)
ciscoUrwbErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbErrorCode.setStatus("current")


class _CiscoUrwbAdditionalInfo_Type(DisplayString):
    """Custom type ciscoUrwbAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbAdditionalInfo_Type.__name__ = "DisplayString"
_CiscoUrwbAdditionalInfo_Object = MibScalar
ciscoUrwbAdditionalInfo = _CiscoUrwbAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 15, 4),
    _CiscoUrwbAdditionalInfo_Type()
)
ciscoUrwbAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbAdditionalInfo.setStatus("current")
_CiscoUrwbFailSshLoginInfo_ObjectIdentity = ObjectIdentity
ciscoUrwbFailSshLoginInfo = _CiscoUrwbFailSshLoginInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 16)
)


class _CiscoUrwbFailSshLoginFlag_Type(Integer32):
    """Custom type ciscoUrwbFailSshLoginFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid-username", 1),
          ("invalid-passwd", 2))
    )


_CiscoUrwbFailSshLoginFlag_Type.__name__ = "Integer32"
_CiscoUrwbFailSshLoginFlag_Object = MibScalar
ciscoUrwbFailSshLoginFlag = _CiscoUrwbFailSshLoginFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 16, 1),
    _CiscoUrwbFailSshLoginFlag_Type()
)
ciscoUrwbFailSshLoginFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbFailSshLoginFlag.setStatus("current")


class _CiscoUrwbFailSshLoginUser_Type(DisplayString):
    """Custom type ciscoUrwbFailSshLoginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbFailSshLoginUser_Type.__name__ = "DisplayString"
_CiscoUrwbFailSshLoginUser_Object = MibScalar
ciscoUrwbFailSshLoginUser = _CiscoUrwbFailSshLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 16, 2),
    _CiscoUrwbFailSshLoginUser_Type()
)
ciscoUrwbFailSshLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbFailSshLoginUser.setStatus("current")
_CiscoUrwbFailWebLoginInfo_ObjectIdentity = ObjectIdentity
ciscoUrwbFailWebLoginInfo = _CiscoUrwbFailWebLoginInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 17)
)


class _CiscoUrwbFailWebLoginUser_Type(DisplayString):
    """Custom type ciscoUrwbFailWebLoginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoUrwbFailWebLoginUser_Type.__name__ = "DisplayString"
_CiscoUrwbFailWebLoginUser_Object = MibScalar
ciscoUrwbFailWebLoginUser = _CiscoUrwbFailWebLoginUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 17, 1),
    _CiscoUrwbFailWebLoginUser_Type()
)
ciscoUrwbFailWebLoginUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbFailWebLoginUser.setStatus("current")
_CiscoUrwbHeadInfo_ObjectIdentity = ObjectIdentity
ciscoUrwbHeadInfo = _CiscoUrwbHeadInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 18)
)
_CiscoUrwbHeadMid_Type = IpAddress
_CiscoUrwbHeadMid_Object = MibScalar
ciscoUrwbHeadMid = _CiscoUrwbHeadMid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 18, 1),
    _CiscoUrwbHeadMid_Type()
)
ciscoUrwbHeadMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbHeadMid.setStatus("current")
_CiscoUrwbTailMid_Type = IpAddress
_CiscoUrwbTailMid_Object = MibScalar
ciscoUrwbTailMid = _CiscoUrwbTailMid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 18, 2),
    _CiscoUrwbTailMid_Type()
)
ciscoUrwbTailMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoUrwbTailMid.setStatus("current")

# Managed Objects groups


# Notification objects

ciscoUrwbNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 12, 1)
)
ciscoUrwbNotif.setObjects(
      *(("CISCO-URWB-MIB", "ciscoUrwbOperMode"),
        ("CISCO-URWB-MIB", "ciscoUrwbModel"),
        ("CISCO-URWB-MIB", "ciscoUrwbFwVersion"),
        ("CISCO-URWB-MIB", "ciscoUrwbWs1"),
        ("CISCO-URWB-MIB", "ciscoUrwbWs2"),
        ("CISCO-URWB-MIB", "ciscoUrwbFreq1"),
        ("CISCO-URWB-MIB", "ciscoUrwbChanWidth1"),
        ("CISCO-URWB-MIB", "ciscoUrwbFreq2"),
        ("CISCO-URWB-MIB", "ciscoUrwbChanWidth2"),
        ("CISCO-URWB-MIB", "ciscoUrwbName"),
        ("CISCO-URWB-MIB", "ciscoUrwbMid"),
        ("CISCO-URWB-MIB", "ciscoUrwbUptime"),
        ("CISCO-URWB-MIB", "ciscoUrwbSerial"),
        ("CISCO-URWB-MIB", "ciscoUrwbDate"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaNum"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaIndex"),
        ("CISCO-URWB-MIB", "ciscoUrwbLocalMacAddress"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaMacAddress"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaMid"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaSignal"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaRxBytes"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaRxPackets"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaRxRate"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaRxMcs"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaRxMcsFlag"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaTxBytes"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaTxPkts"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaTxFail"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaTxRetry"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaTxRate"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaTxMcs"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaTxMcsFlag"),
        ("CISCO-URWB-MIB", "ciscoUrwbTputNum"),
        ("CISCO-URWB-MIB", "ciscoUrwbTputIndex"),
        ("CISCO-URWB-MIB", "ciscoUrwbTputIface"),
        ("CISCO-URWB-MIB", "ciscoUrwbTputRx"),
        ("CISCO-URWB-MIB", "ciscoUrwbTputTx"),
        ("CISCO-URWB-MIB", "ciscoUrwbLoad1"),
        ("CISCO-URWB-MIB", "ciscoUrwbLoad5"),
        ("CISCO-URWB-MIB", "ciscoUrwbLoad15"))
)
if mibBuilder.loadTexts:
    ciscoUrwbNotif.setStatus(
        "current"
    )

ciscoUrwbHandoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 12, 2)
)
ciscoUrwbHandoff.setObjects(
      *(("CISCO-URWB-MIB", "ciscoUrwbMobileIp"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaticIp"),
        ("CISCO-URWB-MIB", "ciscoUrwbMobileMid"),
        ("CISCO-URWB-MIB", "ciscoUrwbStaticMid"),
        ("CISCO-URWB-MIB", "ciscoUrwbHandoffSeq"))
)
if mibBuilder.loadTexts:
    ciscoUrwbHandoff.setStatus(
        "current"
    )

ciscoUrwbFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 12, 3)
)
ciscoUrwbFail.setObjects(
      *(("CISCO-URWB-MIB", "ciscoUrwbMeshId"),
        ("CISCO-URWB-MIB", "ciscoUrwbTimestamp"),
        ("CISCO-URWB-MIB", "ciscoUrwbErrorCode"),
        ("CISCO-URWB-MIB", "ciscoUrwbAdditionalInfo"))
)
if mibBuilder.loadTexts:
    ciscoUrwbFail.setStatus(
        "current"
    )

ciscoUrwbFailSshLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 12, 4)
)
ciscoUrwbFailSshLogin.setObjects(
    ("CISCO-URWB-MIB", "ciscoUrwbFailSshLoginUser")
)
if mibBuilder.loadTexts:
    ciscoUrwbFailSshLogin.setStatus(
        "current"
    )

ciscoUrwbFailWebLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 12, 5)
)
ciscoUrwbFailWebLogin.setObjects(
    ("CISCO-URWB-MIB", "ciscoUrwbFailWebLoginUser")
)
if mibBuilder.loadTexts:
    ciscoUrwbFailWebLogin.setStatus(
        "current"
    )

ciscoUrwbHeadDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1056, 12, 6)
)
ciscoUrwbHeadDetect.setObjects(
      *(("CISCO-URWB-MIB", "ciscoUrwbHeadMid"),
        ("CISCO-URWB-MIB", "ciscoUrwbTailMid"))
)
if mibBuilder.loadTexts:
    ciscoUrwbHeadDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-URWB-MIB",
    **{"ciscoUrwb": ciscoUrwb,
       "ciscoUrwbInfo": ciscoUrwbInfo,
       "ciscoUrwbOperMode": ciscoUrwbOperMode,
       "ciscoUrwbModel": ciscoUrwbModel,
       "ciscoUrwbFwVersion": ciscoUrwbFwVersion,
       "ciscoUrwbWs1": ciscoUrwbWs1,
       "ciscoUrwbWs2": ciscoUrwbWs2,
       "ciscoUrwbFreq1": ciscoUrwbFreq1,
       "ciscoUrwbChanWidth1": ciscoUrwbChanWidth1,
       "ciscoUrwbFreq2": ciscoUrwbFreq2,
       "ciscoUrwbChanWidth2": ciscoUrwbChanWidth2,
       "ciscoUrwbName": ciscoUrwbName,
       "ciscoUrwbMid": ciscoUrwbMid,
       "ciscoUrwbUptime": ciscoUrwbUptime,
       "ciscoUrwbSerial": ciscoUrwbSerial,
       "ciscoUrwbDate": ciscoUrwbDate,
       "ciscoUrwbStaNum": ciscoUrwbStaNum,
       "ciscoUrwbStaTable": ciscoUrwbStaTable,
       "ciscoUrwbStaEntry": ciscoUrwbStaEntry,
       "ciscoUrwbStaIndex": ciscoUrwbStaIndex,
       "ciscoUrwbLocalMacAddress": ciscoUrwbLocalMacAddress,
       "ciscoUrwbStaMacAddress": ciscoUrwbStaMacAddress,
       "ciscoUrwbStaMid": ciscoUrwbStaMid,
       "ciscoUrwbStaSignal": ciscoUrwbStaSignal,
       "ciscoUrwbStaRxBytes": ciscoUrwbStaRxBytes,
       "ciscoUrwbStaRxPkts": ciscoUrwbStaRxPkts,
       "ciscoUrwbStaRxRate": ciscoUrwbStaRxRate,
       "ciscoUrwbStaRxMcs": ciscoUrwbStaRxMcs,
       "ciscoUrwbStaRxMcsFlag": ciscoUrwbStaRxMcsFlag,
       "ciscoUrwbStaTxBytes": ciscoUrwbStaTxBytes,
       "ciscoUrwbStaTxPkts": ciscoUrwbStaTxPkts,
       "ciscoUrwbStaTxFail": ciscoUrwbStaTxFail,
       "ciscoUrwbStaTxRetry": ciscoUrwbStaTxRetry,
       "ciscoUrwbStaTxRate": ciscoUrwbStaTxRate,
       "ciscoUrwbStaTxMcs": ciscoUrwbStaTxMcs,
       "ciscoUrwbStaTxMcsFlag": ciscoUrwbStaTxMcsFlag,
       "ciscoUrwbTputNum": ciscoUrwbTputNum,
       "ciscoUrwbTputTable": ciscoUrwbTputTable,
       "ciscoUrwbTputEntry": ciscoUrwbTputEntry,
       "ciscoUrwbTputIndex": ciscoUrwbTputIndex,
       "ciscoUrwbTputIface": ciscoUrwbTputIface,
       "ciscoUrwbTputTx": ciscoUrwbTputTx,
       "ciscoUrwbTputRx": ciscoUrwbTputRx,
       "ciscoUrwbLoad1": ciscoUrwbLoad1,
       "ciscoUrwbLoad5": ciscoUrwbLoad5,
       "ciscoUrwbLoad15": ciscoUrwbLoad15,
       "ciscoUrwbTemperature": ciscoUrwbTemperature,
       "ciscoUrwbSoftwareStatus": ciscoUrwbSoftwareStatus,
       "ciscoUrwbGenericHwFail": ciscoUrwbGenericHwFail,
       "ciscoUrwbGenericHwFailTime": ciscoUrwbGenericHwFailTime,
       "ciscoUrwbGenericHwFailCode": ciscoUrwbGenericHwFailCode,
       "ciscoUrwbGenericHwFailInfo": ciscoUrwbGenericHwFailInfo,
       "ciscoUrwbDetectedRadars": ciscoUrwbDetectedRadars,
       "ciscoUrwbLastConfId": ciscoUrwbLastConfId,
       "ciscoUrwbGenericHwFailLogFile": ciscoUrwbGenericHwFailLogFile,
       "ciscoUrwbTracksideConn": ciscoUrwbTracksideConn,
       "ciscoUrwbTracksideConnStatic": ciscoUrwbTracksideConnStatic,
       "ciscoUrwbTracksideConnMobile": ciscoUrwbTracksideConnMobile,
       "ciscoUrwbTracksideConnMobilePrimary": ciscoUrwbTracksideConnMobilePrimary,
       "ciscoUrwbTracksideConnRssi": ciscoUrwbTracksideConnRssi,
       "ciscoUrwbVehicleInfo": ciscoUrwbVehicleInfo,
       "ciscoUrwbTrainHead": ciscoUrwbTrainHead,
       "ciscoUrwbTrainTail": ciscoUrwbTrainTail,
       "ciscoUrwbOnboardMobiles": ciscoUrwbOnboardMobiles,
       "ciscoUrwbTraps": ciscoUrwbTraps,
       "ciscoUrwbNotif": ciscoUrwbNotif,
       "ciscoUrwbHandoff": ciscoUrwbHandoff,
       "ciscoUrwbFail": ciscoUrwbFail,
       "ciscoUrwbFailSshLogin": ciscoUrwbFailSshLogin,
       "ciscoUrwbFailWebLogin": ciscoUrwbFailWebLogin,
       "ciscoUrwbHeadDetect": ciscoUrwbHeadDetect,
       "ciscoUrwbExperimental": ciscoUrwbExperimental,
       "ciscoUrwbMobilityInfo": ciscoUrwbMobilityInfo,
       "ciscoUrwbMobileIp": ciscoUrwbMobileIp,
       "ciscoUrwbStaticIp": ciscoUrwbStaticIp,
       "ciscoUrwbMobileMid": ciscoUrwbMobileMid,
       "ciscoUrwbStaticMid": ciscoUrwbStaticMid,
       "ciscoUrwbHandoffSeq": ciscoUrwbHandoffSeq,
       "ciscoUrwbFailInfo": ciscoUrwbFailInfo,
       "ciscoUrwbMeshId": ciscoUrwbMeshId,
       "ciscoUrwbTimestamp": ciscoUrwbTimestamp,
       "ciscoUrwbErrorCode": ciscoUrwbErrorCode,
       "ciscoUrwbAdditionalInfo": ciscoUrwbAdditionalInfo,
       "ciscoUrwbFailSshLoginInfo": ciscoUrwbFailSshLoginInfo,
       "ciscoUrwbFailSshLoginFlag": ciscoUrwbFailSshLoginFlag,
       "ciscoUrwbFailSshLoginUser": ciscoUrwbFailSshLoginUser,
       "ciscoUrwbFailWebLoginInfo": ciscoUrwbFailWebLoginInfo,
       "ciscoUrwbFailWebLoginUser": ciscoUrwbFailWebLoginUser,
       "ciscoUrwbHeadInfo": ciscoUrwbHeadInfo,
       "ciscoUrwbHeadMid": ciscoUrwbHeadMid,
       "ciscoUrwbTailMid": ciscoUrwbTailMid}
)
