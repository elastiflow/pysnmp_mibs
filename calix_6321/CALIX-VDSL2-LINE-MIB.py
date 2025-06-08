# SNMP MIB module (CALIX-VDSL2-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-VDSL2-LINE-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:36:06 2025
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

(c7,) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "c7")

(Xdsl2Band,
 Xdsl2BandUs,
 Xdsl2BitsAlloc,
 Xdsl2BpscResult,
 Xdsl2CarMask,
 Xdsl2ChAtmStatus,
 Xdsl2ChInitPolicy,
 Xdsl2ChInpReport,
 Xdsl2ChPtmStatus,
 Xdsl2ConfPmsForce,
 Xdsl2Direction,
 Xdsl2InitResult,
 Xdsl2LastTransmittedState,
 Xdsl2LdsfResult,
 Xdsl2LineBpsc,
 Xdsl2LineCeFlag,
 Xdsl2LineClassMask,
 Xdsl2LineLdsf,
 Xdsl2LineLimitMask,
 Xdsl2LinePmMode,
 Xdsl2LineProfiles,
 Xdsl2LinePsdMaskSelectUs,
 Xdsl2LineReset,
 Xdsl2LineSnrMode,
 Xdsl2LineStatus,
 Xdsl2LineTxRefVnDs,
 Xdsl2LineTxRefVnUs,
 Xdsl2LineUs0Disable,
 Xdsl2LineUs0Mask,
 Xdsl2MaxBer,
 Xdsl2MrefPsdDs,
 Xdsl2MrefPsdUs,
 Xdsl2OperationModes,
 Xdsl2PowerMngState,
 Xdsl2PsdMaskDs,
 Xdsl2PsdMaskUs,
 Xdsl2RaMode,
 Xdsl2RfiBands,
 Xdsl2ScMaskDs,
 Xdsl2ScMaskUs,
 Xdsl2SymbolProtection,
 Xdsl2SymbolProtection8,
 Xdsl2TransmissionModeType,
 Xdsl2Tssi,
 Xdsl2Unit,
 Xdsl2UpboKLF) = mibBuilder.importSymbols(
    "CALIX-VDSL2-LINE-TC",
    "Xdsl2Band",
    "Xdsl2BandUs",
    "Xdsl2BitsAlloc",
    "Xdsl2BpscResult",
    "Xdsl2CarMask",
    "Xdsl2ChAtmStatus",
    "Xdsl2ChInitPolicy",
    "Xdsl2ChInpReport",
    "Xdsl2ChPtmStatus",
    "Xdsl2ConfPmsForce",
    "Xdsl2Direction",
    "Xdsl2InitResult",
    "Xdsl2LastTransmittedState",
    "Xdsl2LdsfResult",
    "Xdsl2LineBpsc",
    "Xdsl2LineCeFlag",
    "Xdsl2LineClassMask",
    "Xdsl2LineLdsf",
    "Xdsl2LineLimitMask",
    "Xdsl2LinePmMode",
    "Xdsl2LineProfiles",
    "Xdsl2LinePsdMaskSelectUs",
    "Xdsl2LineReset",
    "Xdsl2LineSnrMode",
    "Xdsl2LineStatus",
    "Xdsl2LineTxRefVnDs",
    "Xdsl2LineTxRefVnUs",
    "Xdsl2LineUs0Disable",
    "Xdsl2LineUs0Mask",
    "Xdsl2MaxBer",
    "Xdsl2MrefPsdDs",
    "Xdsl2MrefPsdUs",
    "Xdsl2OperationModes",
    "Xdsl2PowerMngState",
    "Xdsl2PsdMaskDs",
    "Xdsl2PsdMaskUs",
    "Xdsl2RaMode",
    "Xdsl2RfiBands",
    "Xdsl2ScMaskDs",
    "Xdsl2ScMaskUs",
    "Xdsl2SymbolProtection",
    "Xdsl2SymbolProtection8",
    "Xdsl2TransmissionModeType",
    "Xdsl2Tssi",
    "Xdsl2Unit",
    "Xdsl2UpboKLF")

(HCPerfTimeElapsed,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfTimeElapsed")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vdsl2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    vdsl2MIB.setRevisions(
        ("2009-05-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xdsl2Objects_ObjectIdentity = ObjectIdentity
xdsl2Objects = _Xdsl2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1)
)
_Xdsl2Line_ObjectIdentity = ObjectIdentity
xdsl2Line = _Xdsl2Line_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1)
)
_Xdsl2LineTable_Object = MibTable
xdsl2LineTable = _Xdsl2LineTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineTable.setStatus("current")
_Xdsl2LineEntry_Object = MibTableRow
xdsl2LineEntry = _Xdsl2LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1)
)
xdsl2LineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2LineEntry.setStatus("current")


class _Xdsl2LineConfTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineConfTemplate based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LineConfTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineConfTemplate_Object = MibTableColumn
xdsl2LineConfTemplate = _Xdsl2LineConfTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 1),
    _Xdsl2LineConfTemplate_Type()
)
xdsl2LineConfTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineConfTemplate.setStatus("current")


class _Xdsl2LineConfFallbackTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineConfFallbackTemplate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LineConfFallbackTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineConfFallbackTemplate_Object = MibTableColumn
xdsl2LineConfFallbackTemplate = _Xdsl2LineConfFallbackTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 2),
    _Xdsl2LineConfFallbackTemplate_Type()
)
xdsl2LineConfFallbackTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineConfFallbackTemplate.setStatus("current")


class _Xdsl2LineAlarmConfTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineAlarmConfTemplate based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LineAlarmConfTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineAlarmConfTemplate_Object = MibTableColumn
xdsl2LineAlarmConfTemplate = _Xdsl2LineAlarmConfTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 3),
    _Xdsl2LineAlarmConfTemplate_Type()
)
xdsl2LineAlarmConfTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfTemplate.setStatus("current")


class _Xdsl2LineCmndConfPmsf_Type(Xdsl2ConfPmsForce):
    """Custom type xdsl2LineCmndConfPmsf based on Xdsl2ConfPmsForce"""
    defaultValue = 0


_Xdsl2LineCmndConfPmsf_Type.__name__ = "Xdsl2ConfPmsForce"
_Xdsl2LineCmndConfPmsf_Object = MibTableColumn
xdsl2LineCmndConfPmsf = _Xdsl2LineCmndConfPmsf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 4),
    _Xdsl2LineCmndConfPmsf_Type()
)
xdsl2LineCmndConfPmsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfPmsf.setStatus("current")


class _Xdsl2LineCmndConfLdsf_Type(Xdsl2LineLdsf):
    """Custom type xdsl2LineCmndConfLdsf based on Xdsl2LineLdsf"""
    defaultValue = 0


_Xdsl2LineCmndConfLdsf_Type.__name__ = "Xdsl2LineLdsf"
_Xdsl2LineCmndConfLdsf_Object = MibTableColumn
xdsl2LineCmndConfLdsf = _Xdsl2LineCmndConfLdsf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 5),
    _Xdsl2LineCmndConfLdsf_Type()
)
xdsl2LineCmndConfLdsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfLdsf.setStatus("current")


class _Xdsl2LineCmndConfLdsfFailReason_Type(Xdsl2LdsfResult):
    """Custom type xdsl2LineCmndConfLdsfFailReason based on Xdsl2LdsfResult"""
    defaultValue = 1


_Xdsl2LineCmndConfLdsfFailReason_Type.__name__ = "Xdsl2LdsfResult"
_Xdsl2LineCmndConfLdsfFailReason_Object = MibTableColumn
xdsl2LineCmndConfLdsfFailReason = _Xdsl2LineCmndConfLdsfFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 6),
    _Xdsl2LineCmndConfLdsfFailReason_Type()
)
xdsl2LineCmndConfLdsfFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfLdsfFailReason.setStatus("current")


class _Xdsl2LineCmndConfBpsc_Type(Xdsl2LineBpsc):
    """Custom type xdsl2LineCmndConfBpsc based on Xdsl2LineBpsc"""
    defaultValue = 1


_Xdsl2LineCmndConfBpsc_Type.__name__ = "Xdsl2LineBpsc"
_Xdsl2LineCmndConfBpsc_Object = MibTableColumn
xdsl2LineCmndConfBpsc = _Xdsl2LineCmndConfBpsc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 7),
    _Xdsl2LineCmndConfBpsc_Type()
)
xdsl2LineCmndConfBpsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfBpsc.setStatus("current")


class _Xdsl2LineCmndConfBpscFailReason_Type(Xdsl2BpscResult):
    """Custom type xdsl2LineCmndConfBpscFailReason based on Xdsl2BpscResult"""
    defaultValue = 1


_Xdsl2LineCmndConfBpscFailReason_Type.__name__ = "Xdsl2BpscResult"
_Xdsl2LineCmndConfBpscFailReason_Object = MibTableColumn
xdsl2LineCmndConfBpscFailReason = _Xdsl2LineCmndConfBpscFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 8),
    _Xdsl2LineCmndConfBpscFailReason_Type()
)
xdsl2LineCmndConfBpscFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfBpscFailReason.setStatus("current")
_Xdsl2LineCmndConfBpscRequests_Type = Counter32
_Xdsl2LineCmndConfBpscRequests_Object = MibTableColumn
xdsl2LineCmndConfBpscRequests = _Xdsl2LineCmndConfBpscRequests_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 9),
    _Xdsl2LineCmndConfBpscRequests_Type()
)
xdsl2LineCmndConfBpscRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfBpscRequests.setStatus("current")


class _Xdsl2LineCmndAutomodeColdStart_Type(TruthValue):
    """Custom type xdsl2LineCmndAutomodeColdStart based on TruthValue"""
    defaultValue = 2


_Xdsl2LineCmndAutomodeColdStart_Type.__name__ = "TruthValue"
_Xdsl2LineCmndAutomodeColdStart_Object = MibTableColumn
xdsl2LineCmndAutomodeColdStart = _Xdsl2LineCmndAutomodeColdStart_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 10),
    _Xdsl2LineCmndAutomodeColdStart_Type()
)
xdsl2LineCmndAutomodeColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndAutomodeColdStart.setStatus("current")


class _Xdsl2LineCmndConfReset_Type(Xdsl2LineReset):
    """Custom type xdsl2LineCmndConfReset based on Xdsl2LineReset"""
    defaultValue = 1


_Xdsl2LineCmndConfReset_Type.__name__ = "Xdsl2LineReset"
_Xdsl2LineCmndConfReset_Object = MibTableColumn
xdsl2LineCmndConfReset = _Xdsl2LineCmndConfReset_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 11),
    _Xdsl2LineCmndConfReset_Type()
)
xdsl2LineCmndConfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfReset.setStatus("current")


class _Xdsl2LineStatusActTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineStatusActTemplate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LineStatusActTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineStatusActTemplate_Object = MibTableColumn
xdsl2LineStatusActTemplate = _Xdsl2LineStatusActTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 12),
    _Xdsl2LineStatusActTemplate_Type()
)
xdsl2LineStatusActTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActTemplate.setStatus("current")


class _Xdsl2LineStatusXtuTransSys_Type(Xdsl2TransmissionModeType):
    """Custom type xdsl2LineStatusXtuTransSys based on Xdsl2TransmissionModeType"""
    defaultBinValue = "0"


_Xdsl2LineStatusXtuTransSys_Type.__name__ = "Xdsl2TransmissionModeType"
_Xdsl2LineStatusXtuTransSys_Object = MibTableColumn
xdsl2LineStatusXtuTransSys = _Xdsl2LineStatusXtuTransSys_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 13),
    _Xdsl2LineStatusXtuTransSys_Type()
)
xdsl2LineStatusXtuTransSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusXtuTransSys.setStatus("current")


class _Xdsl2LineStatusPwrMngState_Type(Xdsl2PowerMngState):
    """Custom type xdsl2LineStatusPwrMngState based on Xdsl2PowerMngState"""
    defaultValue = 4


_Xdsl2LineStatusPwrMngState_Type.__name__ = "Xdsl2PowerMngState"
_Xdsl2LineStatusPwrMngState_Object = MibTableColumn
xdsl2LineStatusPwrMngState = _Xdsl2LineStatusPwrMngState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 14),
    _Xdsl2LineStatusPwrMngState_Type()
)
xdsl2LineStatusPwrMngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusPwrMngState.setStatus("current")


class _Xdsl2LineStatusInitResult_Type(Xdsl2InitResult):
    """Custom type xdsl2LineStatusInitResult based on Xdsl2InitResult"""
    defaultValue = 0


_Xdsl2LineStatusInitResult_Type.__name__ = "Xdsl2InitResult"
_Xdsl2LineStatusInitResult_Object = MibTableColumn
xdsl2LineStatusInitResult = _Xdsl2LineStatusInitResult_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 15),
    _Xdsl2LineStatusInitResult_Type()
)
xdsl2LineStatusInitResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusInitResult.setStatus("current")


class _Xdsl2LineStatusLastStateDs_Type(Xdsl2LastTransmittedState):
    """Custom type xdsl2LineStatusLastStateDs based on Xdsl2LastTransmittedState"""
    defaultValue = 0


_Xdsl2LineStatusLastStateDs_Type.__name__ = "Xdsl2LastTransmittedState"
_Xdsl2LineStatusLastStateDs_Object = MibTableColumn
xdsl2LineStatusLastStateDs = _Xdsl2LineStatusLastStateDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 16),
    _Xdsl2LineStatusLastStateDs_Type()
)
xdsl2LineStatusLastStateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusLastStateDs.setStatus("current")


class _Xdsl2LineStatusLastStateUs_Type(Xdsl2LastTransmittedState):
    """Custom type xdsl2LineStatusLastStateUs based on Xdsl2LastTransmittedState"""
    defaultValue = 100


_Xdsl2LineStatusLastStateUs_Type.__name__ = "Xdsl2LastTransmittedState"
_Xdsl2LineStatusLastStateUs_Object = MibTableColumn
xdsl2LineStatusLastStateUs = _Xdsl2LineStatusLastStateUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 17),
    _Xdsl2LineStatusLastStateUs_Type()
)
xdsl2LineStatusLastStateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusLastStateUs.setStatus("current")


class _Xdsl2LineStatusXtur_Type(Xdsl2LineStatus):
    """Custom type xdsl2LineStatusXtur based on Xdsl2LineStatus"""
    defaultBinValue = "1"


_Xdsl2LineStatusXtur_Type.__name__ = "Xdsl2LineStatus"
_Xdsl2LineStatusXtur_Object = MibTableColumn
xdsl2LineStatusXtur = _Xdsl2LineStatusXtur_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 18),
    _Xdsl2LineStatusXtur_Type()
)
xdsl2LineStatusXtur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusXtur.setStatus("current")


class _Xdsl2LineStatusXtuc_Type(Xdsl2LineStatus):
    """Custom type xdsl2LineStatusXtuc based on Xdsl2LineStatus"""
    defaultBinValue = "1"


_Xdsl2LineStatusXtuc_Type.__name__ = "Xdsl2LineStatus"
_Xdsl2LineStatusXtuc_Object = MibTableColumn
xdsl2LineStatusXtuc = _Xdsl2LineStatusXtuc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 19),
    _Xdsl2LineStatusXtuc_Type()
)
xdsl2LineStatusXtuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusXtuc.setStatus("current")


class _Xdsl2LineStatusAttainableRateDs_Type(Unsigned32):
    """Custom type xdsl2LineStatusAttainableRateDs based on Unsigned32"""
    defaultValue = 0


_Xdsl2LineStatusAttainableRateDs_Type.__name__ = "Unsigned32"
_Xdsl2LineStatusAttainableRateDs_Object = MibTableColumn
xdsl2LineStatusAttainableRateDs = _Xdsl2LineStatusAttainableRateDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 20),
    _Xdsl2LineStatusAttainableRateDs_Type()
)
xdsl2LineStatusAttainableRateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateDs.setUnits("bits/second")


class _Xdsl2LineStatusAttainableRateUs_Type(Unsigned32):
    """Custom type xdsl2LineStatusAttainableRateUs based on Unsigned32"""
    defaultValue = 0


_Xdsl2LineStatusAttainableRateUs_Type.__name__ = "Unsigned32"
_Xdsl2LineStatusAttainableRateUs_Object = MibTableColumn
xdsl2LineStatusAttainableRateUs = _Xdsl2LineStatusAttainableRateUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 21),
    _Xdsl2LineStatusAttainableRateUs_Type()
)
xdsl2LineStatusAttainableRateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateUs.setUnits("bits/second")


class _Xdsl2LineStatusActPsdDs_Type(Integer32):
    """Custom type xdsl2LineStatusActPsdDs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActPsdDs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActPsdDs_Object = MibTableColumn
xdsl2LineStatusActPsdDs = _Xdsl2LineStatusActPsdDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 22),
    _Xdsl2LineStatusActPsdDs_Type()
)
xdsl2LineStatusActPsdDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdDs.setUnits("0.1 dBm/Hz")


class _Xdsl2LineStatusActPsdUs_Type(Integer32):
    """Custom type xdsl2LineStatusActPsdUs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActPsdUs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActPsdUs_Object = MibTableColumn
xdsl2LineStatusActPsdUs = _Xdsl2LineStatusActPsdUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 23),
    _Xdsl2LineStatusActPsdUs_Type()
)
xdsl2LineStatusActPsdUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdUs.setUnits("0.1 dBm/Hz")


class _Xdsl2LineStatusActAtpDs_Type(Integer32):
    """Custom type xdsl2LineStatusActAtpDs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActAtpDs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActAtpDs_Object = MibTableColumn
xdsl2LineStatusActAtpDs = _Xdsl2LineStatusActAtpDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 24),
    _Xdsl2LineStatusActAtpDs_Type()
)
xdsl2LineStatusActAtpDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpDs.setUnits("0.1 dBm")


class _Xdsl2LineStatusActAtpUs_Type(Integer32):
    """Custom type xdsl2LineStatusActAtpUs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActAtpUs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActAtpUs_Object = MibTableColumn
xdsl2LineStatusActAtpUs = _Xdsl2LineStatusActAtpUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 25),
    _Xdsl2LineStatusActAtpUs_Type()
)
xdsl2LineStatusActAtpUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpUs.setUnits("0.1 dBm")


class _Xdsl2LineStatusActProfile_Type(Xdsl2LineProfiles):
    """Custom type xdsl2LineStatusActProfile based on Xdsl2LineProfiles"""
    defaultBinValue = "0"


_Xdsl2LineStatusActProfile_Type.__name__ = "Xdsl2LineProfiles"
_Xdsl2LineStatusActProfile_Object = MibTableColumn
xdsl2LineStatusActProfile = _Xdsl2LineStatusActProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 26),
    _Xdsl2LineStatusActProfile_Type()
)
xdsl2LineStatusActProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActProfile.setStatus("current")


class _Xdsl2LineStatusActLimitMask_Type(Xdsl2LineLimitMask):
    """Custom type xdsl2LineStatusActLimitMask based on Xdsl2LineLimitMask"""
    defaultBinValue = "0"


_Xdsl2LineStatusActLimitMask_Type.__name__ = "Xdsl2LineLimitMask"
_Xdsl2LineStatusActLimitMask_Object = MibTableColumn
xdsl2LineStatusActLimitMask = _Xdsl2LineStatusActLimitMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 27),
    _Xdsl2LineStatusActLimitMask_Type()
)
xdsl2LineStatusActLimitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActLimitMask.setStatus("current")


class _Xdsl2LineStatusActUs0Mask_Type(Xdsl2LineUs0Mask):
    """Custom type xdsl2LineStatusActUs0Mask based on Xdsl2LineUs0Mask"""
    defaultBinValue = "0"


_Xdsl2LineStatusActUs0Mask_Type.__name__ = "Xdsl2LineUs0Mask"
_Xdsl2LineStatusActUs0Mask_Object = MibTableColumn
xdsl2LineStatusActUs0Mask = _Xdsl2LineStatusActUs0Mask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 28),
    _Xdsl2LineStatusActUs0Mask_Type()
)
xdsl2LineStatusActUs0Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActUs0Mask.setStatus("current")


class _Xdsl2LineStatusActSnrModeDs_Type(Xdsl2LineSnrMode):
    """Custom type xdsl2LineStatusActSnrModeDs based on Xdsl2LineSnrMode"""
    defaultValue = 1


_Xdsl2LineStatusActSnrModeDs_Type.__name__ = "Xdsl2LineSnrMode"
_Xdsl2LineStatusActSnrModeDs_Object = MibTableColumn
xdsl2LineStatusActSnrModeDs = _Xdsl2LineStatusActSnrModeDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 29),
    _Xdsl2LineStatusActSnrModeDs_Type()
)
xdsl2LineStatusActSnrModeDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActSnrModeDs.setStatus("current")


class _Xdsl2LineStatusActSnrModeUs_Type(Xdsl2LineSnrMode):
    """Custom type xdsl2LineStatusActSnrModeUs based on Xdsl2LineSnrMode"""
    defaultValue = 1


_Xdsl2LineStatusActSnrModeUs_Type.__name__ = "Xdsl2LineSnrMode"
_Xdsl2LineStatusActSnrModeUs_Object = MibTableColumn
xdsl2LineStatusActSnrModeUs = _Xdsl2LineStatusActSnrModeUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 30),
    _Xdsl2LineStatusActSnrModeUs_Type()
)
xdsl2LineStatusActSnrModeUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActSnrModeUs.setStatus("current")


class _Xdsl2LineStatusElectricalLength_Type(Unsigned32):
    """Custom type xdsl2LineStatusElectricalLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_Xdsl2LineStatusElectricalLength_Type.__name__ = "Unsigned32"
_Xdsl2LineStatusElectricalLength_Object = MibTableColumn
xdsl2LineStatusElectricalLength = _Xdsl2LineStatusElectricalLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 31),
    _Xdsl2LineStatusElectricalLength_Type()
)
xdsl2LineStatusElectricalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusElectricalLength.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusElectricalLength.setUnits("0.1 dB")
_Xdsl2LineStatusTssiDs_Type = Xdsl2Tssi
_Xdsl2LineStatusTssiDs_Object = MibTableColumn
xdsl2LineStatusTssiDs = _Xdsl2LineStatusTssiDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 32),
    _Xdsl2LineStatusTssiDs_Type()
)
xdsl2LineStatusTssiDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTssiDs.setStatus("current")
_Xdsl2LineStatusTssiUs_Type = Xdsl2Tssi
_Xdsl2LineStatusTssiUs_Object = MibTableColumn
xdsl2LineStatusTssiUs = _Xdsl2LineStatusTssiUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 33),
    _Xdsl2LineStatusTssiUs_Type()
)
xdsl2LineStatusTssiUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTssiUs.setStatus("current")
_Xdsl2LineStatusMrefPsdDs_Type = Xdsl2MrefPsdDs
_Xdsl2LineStatusMrefPsdDs_Object = MibTableColumn
xdsl2LineStatusMrefPsdDs = _Xdsl2LineStatusMrefPsdDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 34),
    _Xdsl2LineStatusMrefPsdDs_Type()
)
xdsl2LineStatusMrefPsdDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusMrefPsdDs.setStatus("current")
_Xdsl2LineStatusMrefPsdUs_Type = Xdsl2MrefPsdUs
_Xdsl2LineStatusMrefPsdUs_Object = MibTableColumn
xdsl2LineStatusMrefPsdUs = _Xdsl2LineStatusMrefPsdUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 35),
    _Xdsl2LineStatusMrefPsdUs_Type()
)
xdsl2LineStatusMrefPsdUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusMrefPsdUs.setStatus("current")


class _Xdsl2LineStatusTrellisDs_Type(TruthValue):
    """Custom type xdsl2LineStatusTrellisDs based on TruthValue"""
    defaultValue = 2


_Xdsl2LineStatusTrellisDs_Type.__name__ = "TruthValue"
_Xdsl2LineStatusTrellisDs_Object = MibTableColumn
xdsl2LineStatusTrellisDs = _Xdsl2LineStatusTrellisDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 36),
    _Xdsl2LineStatusTrellisDs_Type()
)
xdsl2LineStatusTrellisDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTrellisDs.setStatus("current")


class _Xdsl2LineStatusTrellisUs_Type(TruthValue):
    """Custom type xdsl2LineStatusTrellisUs based on TruthValue"""
    defaultValue = 2


_Xdsl2LineStatusTrellisUs_Type.__name__ = "TruthValue"
_Xdsl2LineStatusTrellisUs_Object = MibTableColumn
xdsl2LineStatusTrellisUs = _Xdsl2LineStatusTrellisUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 37),
    _Xdsl2LineStatusTrellisUs_Type()
)
xdsl2LineStatusTrellisUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTrellisUs.setStatus("current")


class _Xdsl2LineStatusActualCe_Type(Unsigned32):
    """Custom type xdsl2LineStatusActualCe based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_Xdsl2LineStatusActualCe_Type.__name__ = "Unsigned32"
_Xdsl2LineStatusActualCe_Object = MibTableColumn
xdsl2LineStatusActualCe = _Xdsl2LineStatusActualCe_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 1, 1, 38),
    _Xdsl2LineStatusActualCe_Type()
)
xdsl2LineStatusActualCe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActualCe.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActualCe.setUnits("N/32 samples")
_Xdsl2LineBandTable_Object = MibTable
xdsl2LineBandTable = _Xdsl2LineBandTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2LineBandTable.setStatus("current")
_Xdsl2LineBandEntry_Object = MibTableRow
xdsl2LineBandEntry = _Xdsl2LineBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 2, 1)
)
xdsl2LineBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2LineBand"),
)
if mibBuilder.loadTexts:
    xdsl2LineBandEntry.setStatus("current")
_Xdsl2LineBand_Type = Xdsl2Band
_Xdsl2LineBand_Object = MibTableColumn
xdsl2LineBand = _Xdsl2LineBand_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 2, 1, 1),
    _Xdsl2LineBand_Type()
)
xdsl2LineBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LineBand.setStatus("current")


class _Xdsl2LineBandStatusLnAtten_Type(Unsigned32):
    """Custom type xdsl2LineBandStatusLnAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusLnAtten_Type.__name__ = "Unsigned32"
_Xdsl2LineBandStatusLnAtten_Object = MibTableColumn
xdsl2LineBandStatusLnAtten = _Xdsl2LineBandStatusLnAtten_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 2, 1, 2),
    _Xdsl2LineBandStatusLnAtten_Type()
)
xdsl2LineBandStatusLnAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusLnAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusLnAtten.setUnits("0.1 dB")


class _Xdsl2LineBandStatusSigAtten_Type(Unsigned32):
    """Custom type xdsl2LineBandStatusSigAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusSigAtten_Type.__name__ = "Unsigned32"
_Xdsl2LineBandStatusSigAtten_Object = MibTableColumn
xdsl2LineBandStatusSigAtten = _Xdsl2LineBandStatusSigAtten_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 2, 1, 3),
    _Xdsl2LineBandStatusSigAtten_Type()
)
xdsl2LineBandStatusSigAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSigAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSigAtten.setUnits("0.1 dB")


class _Xdsl2LineBandStatusSnrMargin_Type(Integer32):
    """Custom type xdsl2LineBandStatusSnrMargin based on Integer32"""
    defaultValue = 2147483646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusSnrMargin_Type.__name__ = "Integer32"
_Xdsl2LineBandStatusSnrMargin_Object = MibTableColumn
xdsl2LineBandStatusSnrMargin = _Xdsl2LineBandStatusSnrMargin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 1, 2, 1, 4),
    _Xdsl2LineBandStatusSnrMargin_Type()
)
xdsl2LineBandStatusSnrMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSnrMargin.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSnrMargin.setUnits("0.1 dB")
_Xdsl2Status_ObjectIdentity = ObjectIdentity
xdsl2Status = _Xdsl2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2)
)
_Xdsl2LineSegmentTable_Object = MibTable
xdsl2LineSegmentTable = _Xdsl2LineSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineSegmentTable.setStatus("current")
_Xdsl2LineSegmentEntry_Object = MibTableRow
xdsl2LineSegmentEntry = _Xdsl2LineSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 1, 1)
)
xdsl2LineSegmentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2LineSegmentDirection"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2LineSegment"),
)
if mibBuilder.loadTexts:
    xdsl2LineSegmentEntry.setStatus("current")
_Xdsl2LineSegmentDirection_Type = Xdsl2Direction
_Xdsl2LineSegmentDirection_Object = MibTableColumn
xdsl2LineSegmentDirection = _Xdsl2LineSegmentDirection_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 1, 1, 1),
    _Xdsl2LineSegmentDirection_Type()
)
xdsl2LineSegmentDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LineSegmentDirection.setStatus("current")


class _Xdsl2LineSegment_Type(Unsigned32):
    """Custom type xdsl2LineSegment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Xdsl2LineSegment_Type.__name__ = "Unsigned32"
_Xdsl2LineSegment_Object = MibTableColumn
xdsl2LineSegment = _Xdsl2LineSegment_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 1, 1, 2),
    _Xdsl2LineSegment_Type()
)
xdsl2LineSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LineSegment.setStatus("current")
_Xdsl2LineSegmentBitsAlloc_Type = Xdsl2BitsAlloc
_Xdsl2LineSegmentBitsAlloc_Object = MibTableColumn
xdsl2LineSegmentBitsAlloc = _Xdsl2LineSegmentBitsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 1, 1, 3),
    _Xdsl2LineSegmentBitsAlloc_Type()
)
xdsl2LineSegmentBitsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentBitsAlloc.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineSegmentBitsAlloc.setUnits("bits")
_Xdsl2LineSegmentRowStatus_Type = RowStatus
_Xdsl2LineSegmentRowStatus_Object = MibTableColumn
xdsl2LineSegmentRowStatus = _Xdsl2LineSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 1, 1, 4),
    _Xdsl2LineSegmentRowStatus_Type()
)
xdsl2LineSegmentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineSegmentRowStatus.setStatus("current")
_Xdsl2ChannelStatusTable_Object = MibTable
xdsl2ChannelStatusTable = _Xdsl2ChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xdsl2ChannelStatusTable.setStatus("current")
_Xdsl2ChannelStatusEntry_Object = MibTableRow
xdsl2ChannelStatusEntry = _Xdsl2ChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1)
)
xdsl2ChannelStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2ChStatusUnit"),
)
if mibBuilder.loadTexts:
    xdsl2ChannelStatusEntry.setStatus("current")
_Xdsl2ChStatusUnit_Type = Xdsl2Unit
_Xdsl2ChStatusUnit_Object = MibTableColumn
xdsl2ChStatusUnit = _Xdsl2ChStatusUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 1),
    _Xdsl2ChStatusUnit_Type()
)
xdsl2ChStatusUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2ChStatusUnit.setStatus("current")


class _Xdsl2ChStatusActDataRate_Type(Unsigned32):
    """Custom type xdsl2ChStatusActDataRate based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChStatusActDataRate_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusActDataRate_Object = MibTableColumn
xdsl2ChStatusActDataRate = _Xdsl2ChStatusActDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 2),
    _Xdsl2ChStatusActDataRate_Type()
)
xdsl2ChStatusActDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDataRate.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDataRate.setUnits("bits/second")


class _Xdsl2ChStatusPrevDataRate_Type(Unsigned32):
    """Custom type xdsl2ChStatusPrevDataRate based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChStatusPrevDataRate_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusPrevDataRate_Object = MibTableColumn
xdsl2ChStatusPrevDataRate = _Xdsl2ChStatusPrevDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 3),
    _Xdsl2ChStatusPrevDataRate_Type()
)
xdsl2ChStatusPrevDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusPrevDataRate.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusPrevDataRate.setUnits("bits/second")


class _Xdsl2ChStatusActDelay_Type(Unsigned32):
    """Custom type xdsl2ChStatusActDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8176),
    )


_Xdsl2ChStatusActDelay_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusActDelay_Object = MibTableColumn
xdsl2ChStatusActDelay = _Xdsl2ChStatusActDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 4),
    _Xdsl2ChStatusActDelay_Type()
)
xdsl2ChStatusActDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDelay.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDelay.setUnits("milliseconds")


class _Xdsl2ChStatusActInp_Type(Unsigned32):
    """Custom type xdsl2ChStatusActInp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2ChStatusActInp_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusActInp_Object = MibTableColumn
xdsl2ChStatusActInp = _Xdsl2ChStatusActInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 5),
    _Xdsl2ChStatusActInp_Type()
)
xdsl2ChStatusActInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusActInp.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusActInp.setUnits("0.1 symbols")


class _Xdsl2ChStatusInpReport_Type(Xdsl2ChInpReport):
    """Custom type xdsl2ChStatusInpReport based on Xdsl2ChInpReport"""
    defaultValue = 1


_Xdsl2ChStatusInpReport_Type.__name__ = "Xdsl2ChInpReport"
_Xdsl2ChStatusInpReport_Object = MibTableColumn
xdsl2ChStatusInpReport = _Xdsl2ChStatusInpReport_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 6),
    _Xdsl2ChStatusInpReport_Type()
)
xdsl2ChStatusInpReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusInpReport.setStatus("current")


class _Xdsl2ChStatusNFec_Type(Unsigned32):
    """Custom type xdsl2ChStatusNFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2ChStatusNFec_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusNFec_Object = MibTableColumn
xdsl2ChStatusNFec = _Xdsl2ChStatusNFec_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 7),
    _Xdsl2ChStatusNFec_Type()
)
xdsl2ChStatusNFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusNFec.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusNFec.setUnits("bytes")


class _Xdsl2ChStatusRFec_Type(Unsigned32):
    """Custom type xdsl2ChStatusRFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Xdsl2ChStatusRFec_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusRFec_Object = MibTableColumn
xdsl2ChStatusRFec = _Xdsl2ChStatusRFec_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 8),
    _Xdsl2ChStatusRFec_Type()
)
xdsl2ChStatusRFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusRFec.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusRFec.setUnits("bits")


class _Xdsl2ChStatusLSymb_Type(Unsigned32):
    """Custom type xdsl2ChStatusLSymb based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xdsl2ChStatusLSymb_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusLSymb_Object = MibTableColumn
xdsl2ChStatusLSymb = _Xdsl2ChStatusLSymb_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 9),
    _Xdsl2ChStatusLSymb_Type()
)
xdsl2ChStatusLSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusLSymb.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusLSymb.setUnits("bits")


class _Xdsl2ChStatusIntlvDepth_Type(Unsigned32):
    """Custom type xdsl2ChStatusIntlvDepth based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Xdsl2ChStatusIntlvDepth_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusIntlvDepth_Object = MibTableColumn
xdsl2ChStatusIntlvDepth = _Xdsl2ChStatusIntlvDepth_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 10),
    _Xdsl2ChStatusIntlvDepth_Type()
)
xdsl2ChStatusIntlvDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusIntlvDepth.setStatus("current")


class _Xdsl2ChStatusIntlvBlock_Type(Unsigned32):
    """Custom type xdsl2ChStatusIntlvBlock based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 255),
    )


_Xdsl2ChStatusIntlvBlock_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusIntlvBlock_Object = MibTableColumn
xdsl2ChStatusIntlvBlock = _Xdsl2ChStatusIntlvBlock_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 11),
    _Xdsl2ChStatusIntlvBlock_Type()
)
xdsl2ChStatusIntlvBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusIntlvBlock.setStatus("current")


class _Xdsl2ChStatusLPath_Type(Unsigned32):
    """Custom type xdsl2ChStatusLPath based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xdsl2ChStatusLPath_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusLPath_Object = MibTableColumn
xdsl2ChStatusLPath = _Xdsl2ChStatusLPath_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 12),
    _Xdsl2ChStatusLPath_Type()
)
xdsl2ChStatusLPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusLPath.setStatus("current")


class _Xdsl2ChStatusAtmStatus_Type(Xdsl2ChAtmStatus):
    """Custom type xdsl2ChStatusAtmStatus based on Xdsl2ChAtmStatus"""
    defaultBinValue = "1"


_Xdsl2ChStatusAtmStatus_Type.__name__ = "Xdsl2ChAtmStatus"
_Xdsl2ChStatusAtmStatus_Object = MibTableColumn
xdsl2ChStatusAtmStatus = _Xdsl2ChStatusAtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 13),
    _Xdsl2ChStatusAtmStatus_Type()
)
xdsl2ChStatusAtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusAtmStatus.setStatus("current")


class _Xdsl2ChStatusPtmStatus_Type(Xdsl2ChPtmStatus):
    """Custom type xdsl2ChStatusPtmStatus based on Xdsl2ChPtmStatus"""
    defaultBinValue = "1"


_Xdsl2ChStatusPtmStatus_Type.__name__ = "Xdsl2ChPtmStatus"
_Xdsl2ChStatusPtmStatus_Object = MibTableColumn
xdsl2ChStatusPtmStatus = _Xdsl2ChStatusPtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 2, 1, 14),
    _Xdsl2ChStatusPtmStatus_Type()
)
xdsl2ChStatusPtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusPtmStatus.setStatus("current")
_Xdsl2SCStatusTable_Object = MibTable
xdsl2SCStatusTable = _Xdsl2SCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    xdsl2SCStatusTable.setStatus("current")
_Xdsl2SCStatusEntry_Object = MibTableRow
xdsl2SCStatusEntry = _Xdsl2SCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1)
)
xdsl2SCStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2SCStatusDirection"),
)
if mibBuilder.loadTexts:
    xdsl2SCStatusEntry.setStatus("current")
_Xdsl2SCStatusDirection_Type = Xdsl2Direction
_Xdsl2SCStatusDirection_Object = MibTableColumn
xdsl2SCStatusDirection = _Xdsl2SCStatusDirection_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 1),
    _Xdsl2SCStatusDirection_Type()
)
xdsl2SCStatusDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2SCStatusDirection.setStatus("current")


class _Xdsl2SCStatusLinScale_Type(Unsigned32):
    """Custom type xdsl2SCStatusLinScale based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusLinScale_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLinScale_Object = MibTableColumn
xdsl2SCStatusLinScale = _Xdsl2SCStatusLinScale_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 2),
    _Xdsl2SCStatusLinScale_Type()
)
xdsl2SCStatusLinScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLinScale.setStatus("current")


class _Xdsl2SCStatusLinScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusLinScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusLinScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLinScGroupSize_Object = MibTableColumn
xdsl2SCStatusLinScGroupSize = _Xdsl2SCStatusLinScGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 3),
    _Xdsl2SCStatusLinScGroupSize_Type()
)
xdsl2SCStatusLinScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLinScGroupSize.setStatus("current")


class _Xdsl2SCStatusLogMt_Type(Unsigned32):
    """Custom type xdsl2SCStatusLogMt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusLogMt_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLogMt_Object = MibTableColumn
xdsl2SCStatusLogMt = _Xdsl2SCStatusLogMt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 4),
    _Xdsl2SCStatusLogMt_Type()
)
xdsl2SCStatusLogMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLogMt.setStatus("current")


class _Xdsl2SCStatusLogScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusLogScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusLogScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLogScGroupSize_Object = MibTableColumn
xdsl2SCStatusLogScGroupSize = _Xdsl2SCStatusLogScGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 5),
    _Xdsl2SCStatusLogScGroupSize_Type()
)
xdsl2SCStatusLogScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLogScGroupSize.setStatus("current")


class _Xdsl2SCStatusQlnMt_Type(Unsigned32):
    """Custom type xdsl2SCStatusQlnMt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusQlnMt_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusQlnMt_Object = MibTableColumn
xdsl2SCStatusQlnMt = _Xdsl2SCStatusQlnMt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 6),
    _Xdsl2SCStatusQlnMt_Type()
)
xdsl2SCStatusQlnMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusQlnMt.setStatus("current")


class _Xdsl2SCStatusQlnScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusQlnScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusQlnScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusQlnScGroupSize_Object = MibTableColumn
xdsl2SCStatusQlnScGroupSize = _Xdsl2SCStatusQlnScGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 7),
    _Xdsl2SCStatusQlnScGroupSize_Type()
)
xdsl2SCStatusQlnScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusQlnScGroupSize.setStatus("current")


class _Xdsl2SCStatusSnrMtime_Type(Unsigned32):
    """Custom type xdsl2SCStatusSnrMtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusSnrMtime_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusSnrMtime_Object = MibTableColumn
xdsl2SCStatusSnrMtime = _Xdsl2SCStatusSnrMtime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 8),
    _Xdsl2SCStatusSnrMtime_Type()
)
xdsl2SCStatusSnrMtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSnrMtime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSnrMtime.setUnits("symbols")


class _Xdsl2SCStatusSnrScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusSnrScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusSnrScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusSnrScGroupSize_Object = MibTableColumn
xdsl2SCStatusSnrScGroupSize = _Xdsl2SCStatusSnrScGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 9),
    _Xdsl2SCStatusSnrScGroupSize_Type()
)
xdsl2SCStatusSnrScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSnrScGroupSize.setStatus("current")
_Xdsl2SCStatusAttainableRate_Type = Unsigned32
_Xdsl2SCStatusAttainableRate_Object = MibTableColumn
xdsl2SCStatusAttainableRate = _Xdsl2SCStatusAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 10),
    _Xdsl2SCStatusAttainableRate_Type()
)
xdsl2SCStatusAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusAttainableRate.setUnits("bits/second")
_Xdsl2SCStatusRowStatus_Type = RowStatus
_Xdsl2SCStatusRowStatus_Object = MibTableColumn
xdsl2SCStatusRowStatus = _Xdsl2SCStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 3, 1, 11),
    _Xdsl2SCStatusRowStatus_Type()
)
xdsl2SCStatusRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2SCStatusRowStatus.setStatus("current")
_Xdsl2SCStatusBandTable_Object = MibTable
xdsl2SCStatusBandTable = _Xdsl2SCStatusBandTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    xdsl2SCStatusBandTable.setStatus("current")
_Xdsl2SCStatusBandEntry_Object = MibTableRow
xdsl2SCStatusBandEntry = _Xdsl2SCStatusBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 4, 1)
)
xdsl2SCStatusBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2SCStatusBand"),
)
if mibBuilder.loadTexts:
    xdsl2SCStatusBandEntry.setStatus("current")
_Xdsl2SCStatusBand_Type = Xdsl2Band
_Xdsl2SCStatusBand_Object = MibTableColumn
xdsl2SCStatusBand = _Xdsl2SCStatusBand_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 4, 1, 1),
    _Xdsl2SCStatusBand_Type()
)
xdsl2SCStatusBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2SCStatusBand.setStatus("current")


class _Xdsl2SCStatusBandLnAtten_Type(Unsigned32):
    """Custom type xdsl2SCStatusBandLnAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusBandLnAtten_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusBandLnAtten_Object = MibTableColumn
xdsl2SCStatusBandLnAtten = _Xdsl2SCStatusBandLnAtten_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 4, 1, 2),
    _Xdsl2SCStatusBandLnAtten_Type()
)
xdsl2SCStatusBandLnAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandLnAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandLnAtten.setUnits("0.1 dB")


class _Xdsl2SCStatusBandSigAtten_Type(Unsigned32):
    """Custom type xdsl2SCStatusBandSigAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusBandSigAtten_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusBandSigAtten_Object = MibTableColumn
xdsl2SCStatusBandSigAtten = _Xdsl2SCStatusBandSigAtten_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 4, 1, 3),
    _Xdsl2SCStatusBandSigAtten_Type()
)
xdsl2SCStatusBandSigAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSigAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSigAtten.setUnits("0.1 dB")
_Xdsl2SCStatusSegmentTable_Object = MibTable
xdsl2SCStatusSegmentTable = _Xdsl2SCStatusSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentTable.setStatus("current")
_Xdsl2SCStatusSegmentEntry_Object = MibTableRow
xdsl2SCStatusSegmentEntry = _Xdsl2SCStatusSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1)
)
xdsl2SCStatusSegmentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2SCStatusDirection"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2SCStatusSegment"),
)
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentEntry.setStatus("current")


class _Xdsl2SCStatusSegment_Type(Unsigned32):
    """Custom type xdsl2SCStatusSegment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Xdsl2SCStatusSegment_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusSegment_Object = MibTableColumn
xdsl2SCStatusSegment = _Xdsl2SCStatusSegment_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 1),
    _Xdsl2SCStatusSegment_Type()
)
xdsl2SCStatusSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegment.setStatus("current")


class _Xdsl2SCStatusSegmentLinReal_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentLinReal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentLinReal_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentLinReal_Object = MibTableColumn
xdsl2SCStatusSegmentLinReal = _Xdsl2SCStatusSegmentLinReal_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 2),
    _Xdsl2SCStatusSegmentLinReal_Type()
)
xdsl2SCStatusSegmentLinReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLinReal.setStatus("current")


class _Xdsl2SCStatusSegmentLinImg_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentLinImg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentLinImg_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentLinImg_Object = MibTableColumn
xdsl2SCStatusSegmentLinImg = _Xdsl2SCStatusSegmentLinImg_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 3),
    _Xdsl2SCStatusSegmentLinImg_Type()
)
xdsl2SCStatusSegmentLinImg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLinImg.setStatus("current")


class _Xdsl2SCStatusSegmentLog_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentLog_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentLog_Object = MibTableColumn
xdsl2SCStatusSegmentLog = _Xdsl2SCStatusSegmentLog_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 4),
    _Xdsl2SCStatusSegmentLog_Type()
)
xdsl2SCStatusSegmentLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLog.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLog.setUnits("dB")


class _Xdsl2SCStatusSegmentQln_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentQln based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Xdsl2SCStatusSegmentQln_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentQln_Object = MibTableColumn
xdsl2SCStatusSegmentQln = _Xdsl2SCStatusSegmentQln_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 5),
    _Xdsl2SCStatusSegmentQln_Type()
)
xdsl2SCStatusSegmentQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentQln.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentQln.setUnits("dBm/Hz")


class _Xdsl2SCStatusSegmentSnr_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentSnr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Xdsl2SCStatusSegmentSnr_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentSnr_Object = MibTableColumn
xdsl2SCStatusSegmentSnr = _Xdsl2SCStatusSegmentSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 6),
    _Xdsl2SCStatusSegmentSnr_Type()
)
xdsl2SCStatusSegmentSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentSnr.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentSnr.setUnits("0.5 dB")
_Xdsl2SCStatusSegmentBitsAlloc_Type = Xdsl2BitsAlloc
_Xdsl2SCStatusSegmentBitsAlloc_Object = MibTableColumn
xdsl2SCStatusSegmentBitsAlloc = _Xdsl2SCStatusSegmentBitsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 7),
    _Xdsl2SCStatusSegmentBitsAlloc_Type()
)
xdsl2SCStatusSegmentBitsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentBitsAlloc.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentBitsAlloc.setUnits("bits")


class _Xdsl2SCStatusSegmentGainAlloc_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentGainAlloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentGainAlloc_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentGainAlloc_Object = MibTableColumn
xdsl2SCStatusSegmentGainAlloc = _Xdsl2SCStatusSegmentGainAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 2, 5, 1, 8),
    _Xdsl2SCStatusSegmentGainAlloc_Type()
)
xdsl2SCStatusSegmentGainAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentGainAlloc.setStatus("current")
_Xdsl2Inventory_ObjectIdentity = ObjectIdentity
xdsl2Inventory = _Xdsl2Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3)
)
_Xdsl2LineInventoryTable_Object = MibTable
xdsl2LineInventoryTable = _Xdsl2LineInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineInventoryTable.setStatus("current")
_Xdsl2LineInventoryEntry_Object = MibTableRow
xdsl2LineInventoryEntry = _Xdsl2LineInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1)
)
xdsl2LineInventoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2LInvUnit"),
)
if mibBuilder.loadTexts:
    xdsl2LineInventoryEntry.setStatus("current")
_Xdsl2LInvUnit_Type = Xdsl2Unit
_Xdsl2LInvUnit_Object = MibTableColumn
xdsl2LInvUnit = _Xdsl2LInvUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1, 1),
    _Xdsl2LInvUnit_Type()
)
xdsl2LInvUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LInvUnit.setStatus("current")


class _Xdsl2LInvG994VendorId_Type(OctetString):
    """Custom type xdsl2LInvG994VendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Xdsl2LInvG994VendorId_Type.__name__ = "OctetString"
_Xdsl2LInvG994VendorId_Object = MibTableColumn
xdsl2LInvG994VendorId = _Xdsl2LInvG994VendorId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1, 2),
    _Xdsl2LInvG994VendorId_Type()
)
xdsl2LInvG994VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvG994VendorId.setStatus("current")


class _Xdsl2LInvSystemVendorId_Type(OctetString):
    """Custom type xdsl2LInvSystemVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Xdsl2LInvSystemVendorId_Type.__name__ = "OctetString"
_Xdsl2LInvSystemVendorId_Object = MibTableColumn
xdsl2LInvSystemVendorId = _Xdsl2LInvSystemVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1, 3),
    _Xdsl2LInvSystemVendorId_Type()
)
xdsl2LInvSystemVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvSystemVendorId.setStatus("current")


class _Xdsl2LInvVersionNumber_Type(OctetString):
    """Custom type xdsl2LInvVersionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xdsl2LInvVersionNumber_Type.__name__ = "OctetString"
_Xdsl2LInvVersionNumber_Object = MibTableColumn
xdsl2LInvVersionNumber = _Xdsl2LInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1, 4),
    _Xdsl2LInvVersionNumber_Type()
)
xdsl2LInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvVersionNumber.setStatus("current")


class _Xdsl2LInvSerialNumber_Type(OctetString):
    """Custom type xdsl2LInvSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LInvSerialNumber_Type.__name__ = "OctetString"
_Xdsl2LInvSerialNumber_Object = MibTableColumn
xdsl2LInvSerialNumber = _Xdsl2LInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1, 5),
    _Xdsl2LInvSerialNumber_Type()
)
xdsl2LInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvSerialNumber.setStatus("current")


class _Xdsl2LInvSelfTestResult_Type(Unsigned32):
    """Custom type xdsl2LInvSelfTestResult based on Unsigned32"""
    defaultValue = 0


_Xdsl2LInvSelfTestResult_Type.__name__ = "Unsigned32"
_Xdsl2LInvSelfTestResult_Object = MibTableColumn
xdsl2LInvSelfTestResult = _Xdsl2LInvSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1, 6),
    _Xdsl2LInvSelfTestResult_Type()
)
xdsl2LInvSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvSelfTestResult.setStatus("current")
_Xdsl2LInvTransmissionCapabilities_Type = Xdsl2TransmissionModeType
_Xdsl2LInvTransmissionCapabilities_Object = MibTableColumn
xdsl2LInvTransmissionCapabilities = _Xdsl2LInvTransmissionCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 3, 1, 1, 7),
    _Xdsl2LInvTransmissionCapabilities_Type()
)
xdsl2LInvTransmissionCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvTransmissionCapabilities.setStatus("current")
_Xdsl2PM_ObjectIdentity = ObjectIdentity
xdsl2PM = _Xdsl2PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4)
)
_Xdsl2PMLine_ObjectIdentity = ObjectIdentity
xdsl2PMLine = _Xdsl2PMLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1)
)
_Xdsl2PMLineCurrTable_Object = MibTable
xdsl2PMLineCurrTable = _Xdsl2PMLineCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2PMLineCurrTable.setStatus("current")
_Xdsl2PMLineCurrEntry_Object = MibTableRow
xdsl2PMLineCurrEntry = _Xdsl2PMLineCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1)
)
xdsl2PMLineCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMLCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineCurrEntry.setStatus("current")
_Xdsl2PMLCurrUnit_Type = Xdsl2Unit
_Xdsl2PMLCurrUnit_Object = MibTableColumn
xdsl2PMLCurrUnit = _Xdsl2PMLCurrUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 1),
    _Xdsl2PMLCurrUnit_Type()
)
xdsl2PMLCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLCurrUnit.setStatus("current")


class _Xdsl2PMLCurr15MValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr15MValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLCurr15MValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr15MValidIntervals_Object = MibTableColumn
xdsl2PMLCurr15MValidIntervals = _Xdsl2PMLCurr15MValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 2),
    _Xdsl2PMLCurr15MValidIntervals_Type()
)
xdsl2PMLCurr15MValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MValidIntervals.setStatus("current")


class _Xdsl2PMLCurr15MInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr15MInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLCurr15MInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr15MInvalidIntervals_Object = MibTableColumn
xdsl2PMLCurr15MInvalidIntervals = _Xdsl2PMLCurr15MInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 3),
    _Xdsl2PMLCurr15MInvalidIntervals_Type()
)
xdsl2PMLCurr15MInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MInvalidIntervals.setStatus("current")
_Xdsl2PMLCurr15MTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMLCurr15MTimeElapsed_Object = MibTableColumn
xdsl2PMLCurr15MTimeElapsed = _Xdsl2PMLCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 4),
    _Xdsl2PMLCurr15MTimeElapsed_Type()
)
xdsl2PMLCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MTimeElapsed.setUnits("seconds")
_Xdsl2PMLCurr15MFecs_Type = Counter32
_Xdsl2PMLCurr15MFecs_Object = MibTableColumn
xdsl2PMLCurr15MFecs = _Xdsl2PMLCurr15MFecs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 5),
    _Xdsl2PMLCurr15MFecs_Type()
)
xdsl2PMLCurr15MFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MFecs.setUnits("seconds")
_Xdsl2PMLCurr15MEs_Type = Counter32
_Xdsl2PMLCurr15MEs_Object = MibTableColumn
xdsl2PMLCurr15MEs = _Xdsl2PMLCurr15MEs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 6),
    _Xdsl2PMLCurr15MEs_Type()
)
xdsl2PMLCurr15MEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MEs.setUnits("seconds")
_Xdsl2PMLCurr15MSes_Type = Counter32
_Xdsl2PMLCurr15MSes_Object = MibTableColumn
xdsl2PMLCurr15MSes = _Xdsl2PMLCurr15MSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 7),
    _Xdsl2PMLCurr15MSes_Type()
)
xdsl2PMLCurr15MSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MSes.setUnits("seconds")
_Xdsl2PMLCurr15MLoss_Type = Counter32
_Xdsl2PMLCurr15MLoss_Object = MibTableColumn
xdsl2PMLCurr15MLoss = _Xdsl2PMLCurr15MLoss_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 8),
    _Xdsl2PMLCurr15MLoss_Type()
)
xdsl2PMLCurr15MLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLoss.setUnits("seconds")
_Xdsl2PMLCurr15MUas_Type = Counter32
_Xdsl2PMLCurr15MUas_Object = MibTableColumn
xdsl2PMLCurr15MUas = _Xdsl2PMLCurr15MUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 9),
    _Xdsl2PMLCurr15MUas_Type()
)
xdsl2PMLCurr15MUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MUas.setUnits("seconds")


class _Xdsl2PMLCurr1DayValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLCurr1DayValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr1DayValidIntervals_Object = MibTableColumn
xdsl2PMLCurr1DayValidIntervals = _Xdsl2PMLCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 10),
    _Xdsl2PMLCurr1DayValidIntervals_Type()
)
xdsl2PMLCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayValidIntervals.setStatus("current")


class _Xdsl2PMLCurr1DayInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLCurr1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr1DayInvalidIntervals_Object = MibTableColumn
xdsl2PMLCurr1DayInvalidIntervals = _Xdsl2PMLCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 11),
    _Xdsl2PMLCurr1DayInvalidIntervals_Type()
)
xdsl2PMLCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayInvalidIntervals.setStatus("current")
_Xdsl2PMLCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMLCurr1DayTimeElapsed_Object = MibTableColumn
xdsl2PMLCurr1DayTimeElapsed = _Xdsl2PMLCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 12),
    _Xdsl2PMLCurr1DayTimeElapsed_Type()
)
xdsl2PMLCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayTimeElapsed.setUnits("seconds")
_Xdsl2PMLCurr1DayFecs_Type = Counter32
_Xdsl2PMLCurr1DayFecs_Object = MibTableColumn
xdsl2PMLCurr1DayFecs = _Xdsl2PMLCurr1DayFecs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 13),
    _Xdsl2PMLCurr1DayFecs_Type()
)
xdsl2PMLCurr1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayFecs.setUnits("seconds")
_Xdsl2PMLCurr1DayEs_Type = Counter32
_Xdsl2PMLCurr1DayEs_Object = MibTableColumn
xdsl2PMLCurr1DayEs = _Xdsl2PMLCurr1DayEs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 14),
    _Xdsl2PMLCurr1DayEs_Type()
)
xdsl2PMLCurr1DayEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayEs.setUnits("seconds")
_Xdsl2PMLCurr1DaySes_Type = Counter32
_Xdsl2PMLCurr1DaySes_Object = MibTableColumn
xdsl2PMLCurr1DaySes = _Xdsl2PMLCurr1DaySes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 15),
    _Xdsl2PMLCurr1DaySes_Type()
)
xdsl2PMLCurr1DaySes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DaySes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DaySes.setUnits("seconds")
_Xdsl2PMLCurr1DayLoss_Type = Counter32
_Xdsl2PMLCurr1DayLoss_Object = MibTableColumn
xdsl2PMLCurr1DayLoss = _Xdsl2PMLCurr1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 16),
    _Xdsl2PMLCurr1DayLoss_Type()
)
xdsl2PMLCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLoss.setUnits("seconds")
_Xdsl2PMLCurr1DayUas_Type = Counter32
_Xdsl2PMLCurr1DayUas_Object = MibTableColumn
xdsl2PMLCurr1DayUas = _Xdsl2PMLCurr1DayUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 1, 1, 17),
    _Xdsl2PMLCurr1DayUas_Type()
)
xdsl2PMLCurr1DayUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayUas.setUnits("seconds")
_Xdsl2PMLineInitCurrTable_Object = MibTable
xdsl2PMLineInitCurrTable = _Xdsl2PMLineInitCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrTable.setStatus("current")
_Xdsl2PMLineInitCurrEntry_Object = MibTableRow
xdsl2PMLineInitCurrEntry = _Xdsl2PMLineInitCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1)
)
xdsl2PMLineInitCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrEntry.setStatus("current")


class _Xdsl2PMLInitCurr15MValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr15MValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLInitCurr15MValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr15MValidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr15MValidIntervals = _Xdsl2PMLInitCurr15MValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 1),
    _Xdsl2PMLInitCurr15MValidIntervals_Type()
)
xdsl2PMLInitCurr15MValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MValidIntervals.setStatus("current")


class _Xdsl2PMLInitCurr15MInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr15MInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLInitCurr15MInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr15MInvalidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr15MInvalidIntervals = _Xdsl2PMLInitCurr15MInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 2),
    _Xdsl2PMLInitCurr15MInvalidIntervals_Type()
)
xdsl2PMLInitCurr15MInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MInvalidIntervals.setStatus("current")
_Xdsl2PMLInitCurr15MTimeElapsed_Type = Unsigned32
_Xdsl2PMLInitCurr15MTimeElapsed_Object = MibTableColumn
xdsl2PMLInitCurr15MTimeElapsed = _Xdsl2PMLInitCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 3),
    _Xdsl2PMLInitCurr15MTimeElapsed_Type()
)
xdsl2PMLInitCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MTimeElapsed.setUnits("seconds")
_Xdsl2PMLInitCurr15MFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MFullInits_Object = MibTableColumn
xdsl2PMLInitCurr15MFullInits = _Xdsl2PMLInitCurr15MFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 4),
    _Xdsl2PMLInitCurr15MFullInits_Type()
)
xdsl2PMLInitCurr15MFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MFullInits.setStatus("current")
_Xdsl2PMLInitCurr15MFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MFailedFullInits_Object = MibTableColumn
xdsl2PMLInitCurr15MFailedFullInits = _Xdsl2PMLInitCurr15MFailedFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 5),
    _Xdsl2PMLInitCurr15MFailedFullInits_Type()
)
xdsl2PMLInitCurr15MFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MFailedFullInits.setStatus("current")
_Xdsl2PMLInitCurr15MShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MShortInits_Object = MibTableColumn
xdsl2PMLInitCurr15MShortInits = _Xdsl2PMLInitCurr15MShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 6),
    _Xdsl2PMLInitCurr15MShortInits_Type()
)
xdsl2PMLInitCurr15MShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MShortInits.setStatus("current")
_Xdsl2PMLInitCurr15MFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MFailedShortInits_Object = MibTableColumn
xdsl2PMLInitCurr15MFailedShortInits = _Xdsl2PMLInitCurr15MFailedShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 7),
    _Xdsl2PMLInitCurr15MFailedShortInits_Type()
)
xdsl2PMLInitCurr15MFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MFailedShortInits.setStatus("current")


class _Xdsl2PMLInitCurr1DayValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLInitCurr1DayValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr1DayValidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr1DayValidIntervals = _Xdsl2PMLInitCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 8),
    _Xdsl2PMLInitCurr1DayValidIntervals_Type()
)
xdsl2PMLInitCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayValidIntervals.setStatus("current")


class _Xdsl2PMLInitCurr1DayInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLInitCurr1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr1DayInvalidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr1DayInvalidIntervals = _Xdsl2PMLInitCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 9),
    _Xdsl2PMLInitCurr1DayInvalidIntervals_Type()
)
xdsl2PMLInitCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayInvalidIntervals.setStatus("current")
_Xdsl2PMLInitCurr1DayTimeElapsed_Type = Unsigned32
_Xdsl2PMLInitCurr1DayTimeElapsed_Object = MibTableColumn
xdsl2PMLInitCurr1DayTimeElapsed = _Xdsl2PMLInitCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 10),
    _Xdsl2PMLInitCurr1DayTimeElapsed_Type()
)
xdsl2PMLInitCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayTimeElapsed.setUnits("seconds")
_Xdsl2PMLInitCurr1DayFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayFullInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayFullInits = _Xdsl2PMLInitCurr1DayFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 11),
    _Xdsl2PMLInitCurr1DayFullInits_Type()
)
xdsl2PMLInitCurr1DayFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayFullInits.setStatus("current")
_Xdsl2PMLInitCurr1DayFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayFailedFullInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayFailedFullInits = _Xdsl2PMLInitCurr1DayFailedFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 12),
    _Xdsl2PMLInitCurr1DayFailedFullInits_Type()
)
xdsl2PMLInitCurr1DayFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayFailedFullInits.setStatus("current")
_Xdsl2PMLInitCurr1DayShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayShortInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayShortInits = _Xdsl2PMLInitCurr1DayShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 13),
    _Xdsl2PMLInitCurr1DayShortInits_Type()
)
xdsl2PMLInitCurr1DayShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayShortInits.setStatus("current")
_Xdsl2PMLInitCurr1DayFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayFailedShortInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayFailedShortInits = _Xdsl2PMLInitCurr1DayFailedShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 2, 1, 14),
    _Xdsl2PMLInitCurr1DayFailedShortInits_Type()
)
xdsl2PMLInitCurr1DayFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayFailedShortInits.setStatus("current")
_Xdsl2PMLineHist15MinTable_Object = MibTable
xdsl2PMLineHist15MinTable = _Xdsl2PMLineHist15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist15MinTable.setStatus("current")
_Xdsl2PMLineHist15MinEntry_Object = MibTableRow
xdsl2PMLineHist15MinEntry = _Xdsl2PMLineHist15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1)
)
xdsl2PMLineHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMLHist15MUnit"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMLHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist15MinEntry.setStatus("current")
_Xdsl2PMLHist15MUnit_Type = Xdsl2Unit
_Xdsl2PMLHist15MUnit_Object = MibTableColumn
xdsl2PMLHist15MUnit = _Xdsl2PMLHist15MUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 1),
    _Xdsl2PMLHist15MUnit_Type()
)
xdsl2PMLHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MUnit.setStatus("current")


class _Xdsl2PMLHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMLHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMLHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLHist15MInterval_Object = MibTableColumn
xdsl2PMLHist15MInterval = _Xdsl2PMLHist15MInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 2),
    _Xdsl2PMLHist15MInterval_Type()
)
xdsl2PMLHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MInterval.setStatus("current")
_Xdsl2PMLHist15MMonitoredTime_Type = Unsigned32
_Xdsl2PMLHist15MMonitoredTime_Object = MibTableColumn
xdsl2PMLHist15MMonitoredTime = _Xdsl2PMLHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 3),
    _Xdsl2PMLHist15MMonitoredTime_Type()
)
xdsl2PMLHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MMonitoredTime.setUnits("seconds")
_Xdsl2PMLHist15MFecs_Type = Counter32
_Xdsl2PMLHist15MFecs_Object = MibTableColumn
xdsl2PMLHist15MFecs = _Xdsl2PMLHist15MFecs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 4),
    _Xdsl2PMLHist15MFecs_Type()
)
xdsl2PMLHist15MFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MFecs.setUnits("seconds")
_Xdsl2PMLHist15MEs_Type = Counter32
_Xdsl2PMLHist15MEs_Object = MibTableColumn
xdsl2PMLHist15MEs = _Xdsl2PMLHist15MEs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 5),
    _Xdsl2PMLHist15MEs_Type()
)
xdsl2PMLHist15MEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MEs.setUnits("seconds")
_Xdsl2PMLHist15MSes_Type = Counter32
_Xdsl2PMLHist15MSes_Object = MibTableColumn
xdsl2PMLHist15MSes = _Xdsl2PMLHist15MSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 6),
    _Xdsl2PMLHist15MSes_Type()
)
xdsl2PMLHist15MSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MSes.setUnits("seconds")
_Xdsl2PMLHist15MLoss_Type = Counter32
_Xdsl2PMLHist15MLoss_Object = MibTableColumn
xdsl2PMLHist15MLoss = _Xdsl2PMLHist15MLoss_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 7),
    _Xdsl2PMLHist15MLoss_Type()
)
xdsl2PMLHist15MLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLoss.setUnits("seconds")
_Xdsl2PMLHist15MUas_Type = Counter32
_Xdsl2PMLHist15MUas_Object = MibTableColumn
xdsl2PMLHist15MUas = _Xdsl2PMLHist15MUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 8),
    _Xdsl2PMLHist15MUas_Type()
)
xdsl2PMLHist15MUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MUas.setUnits("seconds")
_Xdsl2PMLHist15MValidInterval_Type = TruthValue
_Xdsl2PMLHist15MValidInterval_Object = MibTableColumn
xdsl2PMLHist15MValidInterval = _Xdsl2PMLHist15MValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 3, 1, 9),
    _Xdsl2PMLHist15MValidInterval_Type()
)
xdsl2PMLHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MValidInterval.setStatus("current")
_Xdsl2PMLineHist1DayTable_Object = MibTable
xdsl2PMLineHist1DayTable = _Xdsl2PMLineHist1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist1DayTable.setStatus("current")
_Xdsl2PMLineHist1DayEntry_Object = MibTableRow
xdsl2PMLineHist1DayEntry = _Xdsl2PMLineHist1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1)
)
xdsl2PMLineHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMLHist1DUnit"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMLHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist1DayEntry.setStatus("current")
_Xdsl2PMLHist1DUnit_Type = Xdsl2Unit
_Xdsl2PMLHist1DUnit_Object = MibTableColumn
xdsl2PMLHist1DUnit = _Xdsl2PMLHist1DUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 1),
    _Xdsl2PMLHist1DUnit_Type()
)
xdsl2PMLHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DUnit.setStatus("current")


class _Xdsl2PMLHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMLHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMLHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLHist1DInterval_Object = MibTableColumn
xdsl2PMLHist1DInterval = _Xdsl2PMLHist1DInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 2),
    _Xdsl2PMLHist1DInterval_Type()
)
xdsl2PMLHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DInterval.setStatus("current")
_Xdsl2PMLHist1DMonitoredTime_Type = Unsigned32
_Xdsl2PMLHist1DMonitoredTime_Object = MibTableColumn
xdsl2PMLHist1DMonitoredTime = _Xdsl2PMLHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 3),
    _Xdsl2PMLHist1DMonitoredTime_Type()
)
xdsl2PMLHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DMonitoredTime.setUnits("seconds")
_Xdsl2PMLHist1DFecs_Type = Counter32
_Xdsl2PMLHist1DFecs_Object = MibTableColumn
xdsl2PMLHist1DFecs = _Xdsl2PMLHist1DFecs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 4),
    _Xdsl2PMLHist1DFecs_Type()
)
xdsl2PMLHist1DFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DFecs.setUnits("seconds")
_Xdsl2PMLHist1DEs_Type = Counter32
_Xdsl2PMLHist1DEs_Object = MibTableColumn
xdsl2PMLHist1DEs = _Xdsl2PMLHist1DEs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 5),
    _Xdsl2PMLHist1DEs_Type()
)
xdsl2PMLHist1DEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DEs.setUnits("seconds")
_Xdsl2PMLHist1DSes_Type = Counter32
_Xdsl2PMLHist1DSes_Object = MibTableColumn
xdsl2PMLHist1DSes = _Xdsl2PMLHist1DSes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 6),
    _Xdsl2PMLHist1DSes_Type()
)
xdsl2PMLHist1DSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DSes.setUnits("seconds")
_Xdsl2PMLHist1DLoss_Type = Counter32
_Xdsl2PMLHist1DLoss_Object = MibTableColumn
xdsl2PMLHist1DLoss = _Xdsl2PMLHist1DLoss_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 7),
    _Xdsl2PMLHist1DLoss_Type()
)
xdsl2PMLHist1DLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLoss.setUnits("seconds")
_Xdsl2PMLHist1DUas_Type = Counter32
_Xdsl2PMLHist1DUas_Object = MibTableColumn
xdsl2PMLHist1DUas = _Xdsl2PMLHist1DUas_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 8),
    _Xdsl2PMLHist1DUas_Type()
)
xdsl2PMLHist1DUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DUas.setUnits("seconds")
_Xdsl2PMLHist1DValidInterval_Type = TruthValue
_Xdsl2PMLHist1DValidInterval_Object = MibTableColumn
xdsl2PMLHist1DValidInterval = _Xdsl2PMLHist1DValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 4, 1, 9),
    _Xdsl2PMLHist1DValidInterval_Type()
)
xdsl2PMLHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DValidInterval.setStatus("current")
_Xdsl2PMLineInitHist15MinTable_Object = MibTable
xdsl2PMLineInitHist15MinTable = _Xdsl2PMLineInitHist15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinTable.setStatus("current")
_Xdsl2PMLineInitHist15MinEntry_Object = MibTableRow
xdsl2PMLineInitHist15MinEntry = _Xdsl2PMLineInitHist15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1)
)
xdsl2PMLineInitHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMLInitHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinEntry.setStatus("current")


class _Xdsl2PMLInitHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMLInitHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMLInitHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitHist15MInterval_Object = MibTableColumn
xdsl2PMLInitHist15MInterval = _Xdsl2PMLInitHist15MInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1, 1),
    _Xdsl2PMLInitHist15MInterval_Type()
)
xdsl2PMLInitHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MInterval.setStatus("current")
_Xdsl2PMLInitHist15MMonitoredTime_Type = Unsigned32
_Xdsl2PMLInitHist15MMonitoredTime_Object = MibTableColumn
xdsl2PMLInitHist15MMonitoredTime = _Xdsl2PMLInitHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1, 2),
    _Xdsl2PMLInitHist15MMonitoredTime_Type()
)
xdsl2PMLInitHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MMonitoredTime.setUnits("seconds")
_Xdsl2PMLInitHist15MFullInits_Type = Unsigned32
_Xdsl2PMLInitHist15MFullInits_Object = MibTableColumn
xdsl2PMLInitHist15MFullInits = _Xdsl2PMLInitHist15MFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1, 3),
    _Xdsl2PMLInitHist15MFullInits_Type()
)
xdsl2PMLInitHist15MFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MFullInits.setStatus("current")
_Xdsl2PMLInitHist15MFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitHist15MFailedFullInits_Object = MibTableColumn
xdsl2PMLInitHist15MFailedFullInits = _Xdsl2PMLInitHist15MFailedFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1, 4),
    _Xdsl2PMLInitHist15MFailedFullInits_Type()
)
xdsl2PMLInitHist15MFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MFailedFullInits.setStatus("current")
_Xdsl2PMLInitHist15MShortInits_Type = Unsigned32
_Xdsl2PMLInitHist15MShortInits_Object = MibTableColumn
xdsl2PMLInitHist15MShortInits = _Xdsl2PMLInitHist15MShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1, 5),
    _Xdsl2PMLInitHist15MShortInits_Type()
)
xdsl2PMLInitHist15MShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MShortInits.setStatus("current")
_Xdsl2PMLInitHist15MFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitHist15MFailedShortInits_Object = MibTableColumn
xdsl2PMLInitHist15MFailedShortInits = _Xdsl2PMLInitHist15MFailedShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1, 6),
    _Xdsl2PMLInitHist15MFailedShortInits_Type()
)
xdsl2PMLInitHist15MFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MFailedShortInits.setStatus("current")
_Xdsl2PMLInitHist15MValidInterval_Type = TruthValue
_Xdsl2PMLInitHist15MValidInterval_Object = MibTableColumn
xdsl2PMLInitHist15MValidInterval = _Xdsl2PMLInitHist15MValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 5, 1, 7),
    _Xdsl2PMLInitHist15MValidInterval_Type()
)
xdsl2PMLInitHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MValidInterval.setStatus("current")
_Xdsl2PMLineInitHist1DayTable_Object = MibTable
xdsl2PMLineInitHist1DayTable = _Xdsl2PMLineInitHist1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayTable.setStatus("current")
_Xdsl2PMLineInitHist1DayEntry_Object = MibTableRow
xdsl2PMLineInitHist1DayEntry = _Xdsl2PMLineInitHist1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1)
)
xdsl2PMLineInitHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMLInitHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayEntry.setStatus("current")


class _Xdsl2PMLInitHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMLInitHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMLInitHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitHist1DInterval_Object = MibTableColumn
xdsl2PMLInitHist1DInterval = _Xdsl2PMLInitHist1DInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1, 1),
    _Xdsl2PMLInitHist1DInterval_Type()
)
xdsl2PMLInitHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DInterval.setStatus("current")
_Xdsl2PMLInitHist1DMonitoredTime_Type = Unsigned32
_Xdsl2PMLInitHist1DMonitoredTime_Object = MibTableColumn
xdsl2PMLInitHist1DMonitoredTime = _Xdsl2PMLInitHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1, 2),
    _Xdsl2PMLInitHist1DMonitoredTime_Type()
)
xdsl2PMLInitHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DMonitoredTime.setUnits("seconds")
_Xdsl2PMLInitHist1DFullInits_Type = Unsigned32
_Xdsl2PMLInitHist1DFullInits_Object = MibTableColumn
xdsl2PMLInitHist1DFullInits = _Xdsl2PMLInitHist1DFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1, 3),
    _Xdsl2PMLInitHist1DFullInits_Type()
)
xdsl2PMLInitHist1DFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DFullInits.setStatus("current")
_Xdsl2PMLInitHist1DFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitHist1DFailedFullInits_Object = MibTableColumn
xdsl2PMLInitHist1DFailedFullInits = _Xdsl2PMLInitHist1DFailedFullInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1, 4),
    _Xdsl2PMLInitHist1DFailedFullInits_Type()
)
xdsl2PMLInitHist1DFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DFailedFullInits.setStatus("current")
_Xdsl2PMLInitHist1DShortInits_Type = Unsigned32
_Xdsl2PMLInitHist1DShortInits_Object = MibTableColumn
xdsl2PMLInitHist1DShortInits = _Xdsl2PMLInitHist1DShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1, 5),
    _Xdsl2PMLInitHist1DShortInits_Type()
)
xdsl2PMLInitHist1DShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DShortInits.setStatus("current")
_Xdsl2PMLInitHist1DFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitHist1DFailedShortInits_Object = MibTableColumn
xdsl2PMLInitHist1DFailedShortInits = _Xdsl2PMLInitHist1DFailedShortInits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1, 6),
    _Xdsl2PMLInitHist1DFailedShortInits_Type()
)
xdsl2PMLInitHist1DFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DFailedShortInits.setStatus("current")
_Xdsl2PMLInitHist1DValidInterval_Type = TruthValue
_Xdsl2PMLInitHist1DValidInterval_Object = MibTableColumn
xdsl2PMLInitHist1DValidInterval = _Xdsl2PMLInitHist1DValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 1, 6, 1, 7),
    _Xdsl2PMLInitHist1DValidInterval_Type()
)
xdsl2PMLInitHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DValidInterval.setStatus("current")
_Xdsl2PMChannel_ObjectIdentity = ObjectIdentity
xdsl2PMChannel = _Xdsl2PMChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2)
)
_Xdsl2PMChCurrTable_Object = MibTable
xdsl2PMChCurrTable = _Xdsl2PMChCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2PMChCurrTable.setStatus("current")
_Xdsl2PMChCurrEntry_Object = MibTableRow
xdsl2PMChCurrEntry = _Xdsl2PMChCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1)
)
xdsl2PMChCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMChCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2PMChCurrEntry.setStatus("current")
_Xdsl2PMChCurrUnit_Type = Xdsl2Unit
_Xdsl2PMChCurrUnit_Object = MibTableColumn
xdsl2PMChCurrUnit = _Xdsl2PMChCurrUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 1),
    _Xdsl2PMChCurrUnit_Type()
)
xdsl2PMChCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChCurrUnit.setStatus("current")


class _Xdsl2PMChCurr15MValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr15MValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMChCurr15MValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr15MValidIntervals_Object = MibTableColumn
xdsl2PMChCurr15MValidIntervals = _Xdsl2PMChCurr15MValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 2),
    _Xdsl2PMChCurr15MValidIntervals_Type()
)
xdsl2PMChCurr15MValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MValidIntervals.setStatus("current")


class _Xdsl2PMChCurr15MInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr15MInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMChCurr15MInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr15MInvalidIntervals_Object = MibTableColumn
xdsl2PMChCurr15MInvalidIntervals = _Xdsl2PMChCurr15MInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 3),
    _Xdsl2PMChCurr15MInvalidIntervals_Type()
)
xdsl2PMChCurr15MInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MInvalidIntervals.setStatus("current")
_Xdsl2PMChCurr15MTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMChCurr15MTimeElapsed_Object = MibTableColumn
xdsl2PMChCurr15MTimeElapsed = _Xdsl2PMChCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 4),
    _Xdsl2PMChCurr15MTimeElapsed_Type()
)
xdsl2PMChCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MTimeElapsed.setUnits("seconds")
_Xdsl2PMChCurr15MCodingViolations_Type = Unsigned32
_Xdsl2PMChCurr15MCodingViolations_Object = MibTableColumn
xdsl2PMChCurr15MCodingViolations = _Xdsl2PMChCurr15MCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 5),
    _Xdsl2PMChCurr15MCodingViolations_Type()
)
xdsl2PMChCurr15MCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MCodingViolations.setStatus("current")
_Xdsl2PMChCurr15MCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChCurr15MCorrectedBlocks_Object = MibTableColumn
xdsl2PMChCurr15MCorrectedBlocks = _Xdsl2PMChCurr15MCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 6),
    _Xdsl2PMChCurr15MCorrectedBlocks_Type()
)
xdsl2PMChCurr15MCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MCorrectedBlocks.setStatus("current")


class _Xdsl2PMChCurr1DayValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMChCurr1DayValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr1DayValidIntervals_Object = MibTableColumn
xdsl2PMChCurr1DayValidIntervals = _Xdsl2PMChCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 7),
    _Xdsl2PMChCurr1DayValidIntervals_Type()
)
xdsl2PMChCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayValidIntervals.setStatus("current")


class _Xdsl2PMChCurr1DayInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMChCurr1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr1DayInvalidIntervals_Object = MibTableColumn
xdsl2PMChCurr1DayInvalidIntervals = _Xdsl2PMChCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 8),
    _Xdsl2PMChCurr1DayInvalidIntervals_Type()
)
xdsl2PMChCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayInvalidIntervals.setStatus("current")
_Xdsl2PMChCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMChCurr1DayTimeElapsed_Object = MibTableColumn
xdsl2PMChCurr1DayTimeElapsed = _Xdsl2PMChCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 9),
    _Xdsl2PMChCurr1DayTimeElapsed_Type()
)
xdsl2PMChCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayTimeElapsed.setUnits("seconds")
_Xdsl2PMChCurr1DayCodingViolations_Type = Unsigned32
_Xdsl2PMChCurr1DayCodingViolations_Object = MibTableColumn
xdsl2PMChCurr1DayCodingViolations = _Xdsl2PMChCurr1DayCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 10),
    _Xdsl2PMChCurr1DayCodingViolations_Type()
)
xdsl2PMChCurr1DayCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayCodingViolations.setStatus("current")
_Xdsl2PMChCurr1DayCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChCurr1DayCorrectedBlocks_Object = MibTableColumn
xdsl2PMChCurr1DayCorrectedBlocks = _Xdsl2PMChCurr1DayCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 1, 1, 11),
    _Xdsl2PMChCurr1DayCorrectedBlocks_Type()
)
xdsl2PMChCurr1DayCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayCorrectedBlocks.setStatus("current")
_Xdsl2PMChHist15MinTable_Object = MibTable
xdsl2PMChHist15MinTable = _Xdsl2PMChHist15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    xdsl2PMChHist15MinTable.setStatus("current")
_Xdsl2PMChHist15MinEntry_Object = MibTableRow
xdsl2PMChHist15MinEntry = _Xdsl2PMChHist15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2, 1)
)
xdsl2PMChHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMChHist15MUnit"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMChHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMChHist15MinEntry.setStatus("current")
_Xdsl2PMChHist15MUnit_Type = Xdsl2Unit
_Xdsl2PMChHist15MUnit_Object = MibTableColumn
xdsl2PMChHist15MUnit = _Xdsl2PMChHist15MUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2, 1, 1),
    _Xdsl2PMChHist15MUnit_Type()
)
xdsl2PMChHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MUnit.setStatus("current")


class _Xdsl2PMChHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMChHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMChHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMChHist15MInterval_Object = MibTableColumn
xdsl2PMChHist15MInterval = _Xdsl2PMChHist15MInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2, 1, 2),
    _Xdsl2PMChHist15MInterval_Type()
)
xdsl2PMChHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MInterval.setStatus("current")
_Xdsl2PMChHist15MMonitoredTime_Type = Unsigned32
_Xdsl2PMChHist15MMonitoredTime_Object = MibTableColumn
xdsl2PMChHist15MMonitoredTime = _Xdsl2PMChHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2, 1, 3),
    _Xdsl2PMChHist15MMonitoredTime_Type()
)
xdsl2PMChHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MMonitoredTime.setUnits("seconds")
_Xdsl2PMChHist15MCodingViolations_Type = Unsigned32
_Xdsl2PMChHist15MCodingViolations_Object = MibTableColumn
xdsl2PMChHist15MCodingViolations = _Xdsl2PMChHist15MCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2, 1, 4),
    _Xdsl2PMChHist15MCodingViolations_Type()
)
xdsl2PMChHist15MCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MCodingViolations.setStatus("current")
_Xdsl2PMChHist15MCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChHist15MCorrectedBlocks_Object = MibTableColumn
xdsl2PMChHist15MCorrectedBlocks = _Xdsl2PMChHist15MCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2, 1, 5),
    _Xdsl2PMChHist15MCorrectedBlocks_Type()
)
xdsl2PMChHist15MCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MCorrectedBlocks.setStatus("current")
_Xdsl2PMChHist15MValidInterval_Type = TruthValue
_Xdsl2PMChHist15MValidInterval_Object = MibTableColumn
xdsl2PMChHist15MValidInterval = _Xdsl2PMChHist15MValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 2, 1, 6),
    _Xdsl2PMChHist15MValidInterval_Type()
)
xdsl2PMChHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MValidInterval.setStatus("current")
_Xdsl2PMChHist1DTable_Object = MibTable
xdsl2PMChHist1DTable = _Xdsl2PMChHist1DTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    xdsl2PMChHist1DTable.setStatus("current")
_Xdsl2PMChHist1DEntry_Object = MibTableRow
xdsl2PMChHist1DEntry = _Xdsl2PMChHist1DEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3, 1)
)
xdsl2PMChHist1DEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMChHist1DUnit"),
    (0, "CALIX-VDSL2-LINE-MIB", "xdsl2PMChHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMChHist1DEntry.setStatus("current")
_Xdsl2PMChHist1DUnit_Type = Xdsl2Unit
_Xdsl2PMChHist1DUnit_Object = MibTableColumn
xdsl2PMChHist1DUnit = _Xdsl2PMChHist1DUnit_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3, 1, 1),
    _Xdsl2PMChHist1DUnit_Type()
)
xdsl2PMChHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DUnit.setStatus("current")


class _Xdsl2PMChHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMChHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMChHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMChHist1DInterval_Object = MibTableColumn
xdsl2PMChHist1DInterval = _Xdsl2PMChHist1DInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3, 1, 2),
    _Xdsl2PMChHist1DInterval_Type()
)
xdsl2PMChHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DInterval.setStatus("current")
_Xdsl2PMChHist1DMonitoredTime_Type = Unsigned32
_Xdsl2PMChHist1DMonitoredTime_Object = MibTableColumn
xdsl2PMChHist1DMonitoredTime = _Xdsl2PMChHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3, 1, 3),
    _Xdsl2PMChHist1DMonitoredTime_Type()
)
xdsl2PMChHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DMonitoredTime.setUnits("seconds")
_Xdsl2PMChHist1DCodingViolations_Type = Unsigned32
_Xdsl2PMChHist1DCodingViolations_Object = MibTableColumn
xdsl2PMChHist1DCodingViolations = _Xdsl2PMChHist1DCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3, 1, 4),
    _Xdsl2PMChHist1DCodingViolations_Type()
)
xdsl2PMChHist1DCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DCodingViolations.setStatus("current")
_Xdsl2PMChHist1DCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChHist1DCorrectedBlocks_Object = MibTableColumn
xdsl2PMChHist1DCorrectedBlocks = _Xdsl2PMChHist1DCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3, 1, 5),
    _Xdsl2PMChHist1DCorrectedBlocks_Type()
)
xdsl2PMChHist1DCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DCorrectedBlocks.setStatus("current")
_Xdsl2PMChHist1DValidInterval_Type = TruthValue
_Xdsl2PMChHist1DValidInterval_Object = MibTableColumn
xdsl2PMChHist1DValidInterval = _Xdsl2PMChHist1DValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 8, 1, 4, 2, 3, 1, 6),
    _Xdsl2PMChHist1DValidInterval_Type()
)
xdsl2PMChHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DValidInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-VDSL2-LINE-MIB",
    **{"vdsl2MIB": vdsl2MIB,
       "xdsl2Objects": xdsl2Objects,
       "xdsl2Line": xdsl2Line,
       "xdsl2LineTable": xdsl2LineTable,
       "xdsl2LineEntry": xdsl2LineEntry,
       "xdsl2LineConfTemplate": xdsl2LineConfTemplate,
       "xdsl2LineConfFallbackTemplate": xdsl2LineConfFallbackTemplate,
       "xdsl2LineAlarmConfTemplate": xdsl2LineAlarmConfTemplate,
       "xdsl2LineCmndConfPmsf": xdsl2LineCmndConfPmsf,
       "xdsl2LineCmndConfLdsf": xdsl2LineCmndConfLdsf,
       "xdsl2LineCmndConfLdsfFailReason": xdsl2LineCmndConfLdsfFailReason,
       "xdsl2LineCmndConfBpsc": xdsl2LineCmndConfBpsc,
       "xdsl2LineCmndConfBpscFailReason": xdsl2LineCmndConfBpscFailReason,
       "xdsl2LineCmndConfBpscRequests": xdsl2LineCmndConfBpscRequests,
       "xdsl2LineCmndAutomodeColdStart": xdsl2LineCmndAutomodeColdStart,
       "xdsl2LineCmndConfReset": xdsl2LineCmndConfReset,
       "xdsl2LineStatusActTemplate": xdsl2LineStatusActTemplate,
       "xdsl2LineStatusXtuTransSys": xdsl2LineStatusXtuTransSys,
       "xdsl2LineStatusPwrMngState": xdsl2LineStatusPwrMngState,
       "xdsl2LineStatusInitResult": xdsl2LineStatusInitResult,
       "xdsl2LineStatusLastStateDs": xdsl2LineStatusLastStateDs,
       "xdsl2LineStatusLastStateUs": xdsl2LineStatusLastStateUs,
       "xdsl2LineStatusXtur": xdsl2LineStatusXtur,
       "xdsl2LineStatusXtuc": xdsl2LineStatusXtuc,
       "xdsl2LineStatusAttainableRateDs": xdsl2LineStatusAttainableRateDs,
       "xdsl2LineStatusAttainableRateUs": xdsl2LineStatusAttainableRateUs,
       "xdsl2LineStatusActPsdDs": xdsl2LineStatusActPsdDs,
       "xdsl2LineStatusActPsdUs": xdsl2LineStatusActPsdUs,
       "xdsl2LineStatusActAtpDs": xdsl2LineStatusActAtpDs,
       "xdsl2LineStatusActAtpUs": xdsl2LineStatusActAtpUs,
       "xdsl2LineStatusActProfile": xdsl2LineStatusActProfile,
       "xdsl2LineStatusActLimitMask": xdsl2LineStatusActLimitMask,
       "xdsl2LineStatusActUs0Mask": xdsl2LineStatusActUs0Mask,
       "xdsl2LineStatusActSnrModeDs": xdsl2LineStatusActSnrModeDs,
       "xdsl2LineStatusActSnrModeUs": xdsl2LineStatusActSnrModeUs,
       "xdsl2LineStatusElectricalLength": xdsl2LineStatusElectricalLength,
       "xdsl2LineStatusTssiDs": xdsl2LineStatusTssiDs,
       "xdsl2LineStatusTssiUs": xdsl2LineStatusTssiUs,
       "xdsl2LineStatusMrefPsdDs": xdsl2LineStatusMrefPsdDs,
       "xdsl2LineStatusMrefPsdUs": xdsl2LineStatusMrefPsdUs,
       "xdsl2LineStatusTrellisDs": xdsl2LineStatusTrellisDs,
       "xdsl2LineStatusTrellisUs": xdsl2LineStatusTrellisUs,
       "xdsl2LineStatusActualCe": xdsl2LineStatusActualCe,
       "xdsl2LineBandTable": xdsl2LineBandTable,
       "xdsl2LineBandEntry": xdsl2LineBandEntry,
       "xdsl2LineBand": xdsl2LineBand,
       "xdsl2LineBandStatusLnAtten": xdsl2LineBandStatusLnAtten,
       "xdsl2LineBandStatusSigAtten": xdsl2LineBandStatusSigAtten,
       "xdsl2LineBandStatusSnrMargin": xdsl2LineBandStatusSnrMargin,
       "xdsl2Status": xdsl2Status,
       "xdsl2LineSegmentTable": xdsl2LineSegmentTable,
       "xdsl2LineSegmentEntry": xdsl2LineSegmentEntry,
       "xdsl2LineSegmentDirection": xdsl2LineSegmentDirection,
       "xdsl2LineSegment": xdsl2LineSegment,
       "xdsl2LineSegmentBitsAlloc": xdsl2LineSegmentBitsAlloc,
       "xdsl2LineSegmentRowStatus": xdsl2LineSegmentRowStatus,
       "xdsl2ChannelStatusTable": xdsl2ChannelStatusTable,
       "xdsl2ChannelStatusEntry": xdsl2ChannelStatusEntry,
       "xdsl2ChStatusUnit": xdsl2ChStatusUnit,
       "xdsl2ChStatusActDataRate": xdsl2ChStatusActDataRate,
       "xdsl2ChStatusPrevDataRate": xdsl2ChStatusPrevDataRate,
       "xdsl2ChStatusActDelay": xdsl2ChStatusActDelay,
       "xdsl2ChStatusActInp": xdsl2ChStatusActInp,
       "xdsl2ChStatusInpReport": xdsl2ChStatusInpReport,
       "xdsl2ChStatusNFec": xdsl2ChStatusNFec,
       "xdsl2ChStatusRFec": xdsl2ChStatusRFec,
       "xdsl2ChStatusLSymb": xdsl2ChStatusLSymb,
       "xdsl2ChStatusIntlvDepth": xdsl2ChStatusIntlvDepth,
       "xdsl2ChStatusIntlvBlock": xdsl2ChStatusIntlvBlock,
       "xdsl2ChStatusLPath": xdsl2ChStatusLPath,
       "xdsl2ChStatusAtmStatus": xdsl2ChStatusAtmStatus,
       "xdsl2ChStatusPtmStatus": xdsl2ChStatusPtmStatus,
       "xdsl2SCStatusTable": xdsl2SCStatusTable,
       "xdsl2SCStatusEntry": xdsl2SCStatusEntry,
       "xdsl2SCStatusDirection": xdsl2SCStatusDirection,
       "xdsl2SCStatusLinScale": xdsl2SCStatusLinScale,
       "xdsl2SCStatusLinScGroupSize": xdsl2SCStatusLinScGroupSize,
       "xdsl2SCStatusLogMt": xdsl2SCStatusLogMt,
       "xdsl2SCStatusLogScGroupSize": xdsl2SCStatusLogScGroupSize,
       "xdsl2SCStatusQlnMt": xdsl2SCStatusQlnMt,
       "xdsl2SCStatusQlnScGroupSize": xdsl2SCStatusQlnScGroupSize,
       "xdsl2SCStatusSnrMtime": xdsl2SCStatusSnrMtime,
       "xdsl2SCStatusSnrScGroupSize": xdsl2SCStatusSnrScGroupSize,
       "xdsl2SCStatusAttainableRate": xdsl2SCStatusAttainableRate,
       "xdsl2SCStatusRowStatus": xdsl2SCStatusRowStatus,
       "xdsl2SCStatusBandTable": xdsl2SCStatusBandTable,
       "xdsl2SCStatusBandEntry": xdsl2SCStatusBandEntry,
       "xdsl2SCStatusBand": xdsl2SCStatusBand,
       "xdsl2SCStatusBandLnAtten": xdsl2SCStatusBandLnAtten,
       "xdsl2SCStatusBandSigAtten": xdsl2SCStatusBandSigAtten,
       "xdsl2SCStatusSegmentTable": xdsl2SCStatusSegmentTable,
       "xdsl2SCStatusSegmentEntry": xdsl2SCStatusSegmentEntry,
       "xdsl2SCStatusSegment": xdsl2SCStatusSegment,
       "xdsl2SCStatusSegmentLinReal": xdsl2SCStatusSegmentLinReal,
       "xdsl2SCStatusSegmentLinImg": xdsl2SCStatusSegmentLinImg,
       "xdsl2SCStatusSegmentLog": xdsl2SCStatusSegmentLog,
       "xdsl2SCStatusSegmentQln": xdsl2SCStatusSegmentQln,
       "xdsl2SCStatusSegmentSnr": xdsl2SCStatusSegmentSnr,
       "xdsl2SCStatusSegmentBitsAlloc": xdsl2SCStatusSegmentBitsAlloc,
       "xdsl2SCStatusSegmentGainAlloc": xdsl2SCStatusSegmentGainAlloc,
       "xdsl2Inventory": xdsl2Inventory,
       "xdsl2LineInventoryTable": xdsl2LineInventoryTable,
       "xdsl2LineInventoryEntry": xdsl2LineInventoryEntry,
       "xdsl2LInvUnit": xdsl2LInvUnit,
       "xdsl2LInvG994VendorId": xdsl2LInvG994VendorId,
       "xdsl2LInvSystemVendorId": xdsl2LInvSystemVendorId,
       "xdsl2LInvVersionNumber": xdsl2LInvVersionNumber,
       "xdsl2LInvSerialNumber": xdsl2LInvSerialNumber,
       "xdsl2LInvSelfTestResult": xdsl2LInvSelfTestResult,
       "xdsl2LInvTransmissionCapabilities": xdsl2LInvTransmissionCapabilities,
       "xdsl2PM": xdsl2PM,
       "xdsl2PMLine": xdsl2PMLine,
       "xdsl2PMLineCurrTable": xdsl2PMLineCurrTable,
       "xdsl2PMLineCurrEntry": xdsl2PMLineCurrEntry,
       "xdsl2PMLCurrUnit": xdsl2PMLCurrUnit,
       "xdsl2PMLCurr15MValidIntervals": xdsl2PMLCurr15MValidIntervals,
       "xdsl2PMLCurr15MInvalidIntervals": xdsl2PMLCurr15MInvalidIntervals,
       "xdsl2PMLCurr15MTimeElapsed": xdsl2PMLCurr15MTimeElapsed,
       "xdsl2PMLCurr15MFecs": xdsl2PMLCurr15MFecs,
       "xdsl2PMLCurr15MEs": xdsl2PMLCurr15MEs,
       "xdsl2PMLCurr15MSes": xdsl2PMLCurr15MSes,
       "xdsl2PMLCurr15MLoss": xdsl2PMLCurr15MLoss,
       "xdsl2PMLCurr15MUas": xdsl2PMLCurr15MUas,
       "xdsl2PMLCurr1DayValidIntervals": xdsl2PMLCurr1DayValidIntervals,
       "xdsl2PMLCurr1DayInvalidIntervals": xdsl2PMLCurr1DayInvalidIntervals,
       "xdsl2PMLCurr1DayTimeElapsed": xdsl2PMLCurr1DayTimeElapsed,
       "xdsl2PMLCurr1DayFecs": xdsl2PMLCurr1DayFecs,
       "xdsl2PMLCurr1DayEs": xdsl2PMLCurr1DayEs,
       "xdsl2PMLCurr1DaySes": xdsl2PMLCurr1DaySes,
       "xdsl2PMLCurr1DayLoss": xdsl2PMLCurr1DayLoss,
       "xdsl2PMLCurr1DayUas": xdsl2PMLCurr1DayUas,
       "xdsl2PMLineInitCurrTable": xdsl2PMLineInitCurrTable,
       "xdsl2PMLineInitCurrEntry": xdsl2PMLineInitCurrEntry,
       "xdsl2PMLInitCurr15MValidIntervals": xdsl2PMLInitCurr15MValidIntervals,
       "xdsl2PMLInitCurr15MInvalidIntervals": xdsl2PMLInitCurr15MInvalidIntervals,
       "xdsl2PMLInitCurr15MTimeElapsed": xdsl2PMLInitCurr15MTimeElapsed,
       "xdsl2PMLInitCurr15MFullInits": xdsl2PMLInitCurr15MFullInits,
       "xdsl2PMLInitCurr15MFailedFullInits": xdsl2PMLInitCurr15MFailedFullInits,
       "xdsl2PMLInitCurr15MShortInits": xdsl2PMLInitCurr15MShortInits,
       "xdsl2PMLInitCurr15MFailedShortInits": xdsl2PMLInitCurr15MFailedShortInits,
       "xdsl2PMLInitCurr1DayValidIntervals": xdsl2PMLInitCurr1DayValidIntervals,
       "xdsl2PMLInitCurr1DayInvalidIntervals": xdsl2PMLInitCurr1DayInvalidIntervals,
       "xdsl2PMLInitCurr1DayTimeElapsed": xdsl2PMLInitCurr1DayTimeElapsed,
       "xdsl2PMLInitCurr1DayFullInits": xdsl2PMLInitCurr1DayFullInits,
       "xdsl2PMLInitCurr1DayFailedFullInits": xdsl2PMLInitCurr1DayFailedFullInits,
       "xdsl2PMLInitCurr1DayShortInits": xdsl2PMLInitCurr1DayShortInits,
       "xdsl2PMLInitCurr1DayFailedShortInits": xdsl2PMLInitCurr1DayFailedShortInits,
       "xdsl2PMLineHist15MinTable": xdsl2PMLineHist15MinTable,
       "xdsl2PMLineHist15MinEntry": xdsl2PMLineHist15MinEntry,
       "xdsl2PMLHist15MUnit": xdsl2PMLHist15MUnit,
       "xdsl2PMLHist15MInterval": xdsl2PMLHist15MInterval,
       "xdsl2PMLHist15MMonitoredTime": xdsl2PMLHist15MMonitoredTime,
       "xdsl2PMLHist15MFecs": xdsl2PMLHist15MFecs,
       "xdsl2PMLHist15MEs": xdsl2PMLHist15MEs,
       "xdsl2PMLHist15MSes": xdsl2PMLHist15MSes,
       "xdsl2PMLHist15MLoss": xdsl2PMLHist15MLoss,
       "xdsl2PMLHist15MUas": xdsl2PMLHist15MUas,
       "xdsl2PMLHist15MValidInterval": xdsl2PMLHist15MValidInterval,
       "xdsl2PMLineHist1DayTable": xdsl2PMLineHist1DayTable,
       "xdsl2PMLineHist1DayEntry": xdsl2PMLineHist1DayEntry,
       "xdsl2PMLHist1DUnit": xdsl2PMLHist1DUnit,
       "xdsl2PMLHist1DInterval": xdsl2PMLHist1DInterval,
       "xdsl2PMLHist1DMonitoredTime": xdsl2PMLHist1DMonitoredTime,
       "xdsl2PMLHist1DFecs": xdsl2PMLHist1DFecs,
       "xdsl2PMLHist1DEs": xdsl2PMLHist1DEs,
       "xdsl2PMLHist1DSes": xdsl2PMLHist1DSes,
       "xdsl2PMLHist1DLoss": xdsl2PMLHist1DLoss,
       "xdsl2PMLHist1DUas": xdsl2PMLHist1DUas,
       "xdsl2PMLHist1DValidInterval": xdsl2PMLHist1DValidInterval,
       "xdsl2PMLineInitHist15MinTable": xdsl2PMLineInitHist15MinTable,
       "xdsl2PMLineInitHist15MinEntry": xdsl2PMLineInitHist15MinEntry,
       "xdsl2PMLInitHist15MInterval": xdsl2PMLInitHist15MInterval,
       "xdsl2PMLInitHist15MMonitoredTime": xdsl2PMLInitHist15MMonitoredTime,
       "xdsl2PMLInitHist15MFullInits": xdsl2PMLInitHist15MFullInits,
       "xdsl2PMLInitHist15MFailedFullInits": xdsl2PMLInitHist15MFailedFullInits,
       "xdsl2PMLInitHist15MShortInits": xdsl2PMLInitHist15MShortInits,
       "xdsl2PMLInitHist15MFailedShortInits": xdsl2PMLInitHist15MFailedShortInits,
       "xdsl2PMLInitHist15MValidInterval": xdsl2PMLInitHist15MValidInterval,
       "xdsl2PMLineInitHist1DayTable": xdsl2PMLineInitHist1DayTable,
       "xdsl2PMLineInitHist1DayEntry": xdsl2PMLineInitHist1DayEntry,
       "xdsl2PMLInitHist1DInterval": xdsl2PMLInitHist1DInterval,
       "xdsl2PMLInitHist1DMonitoredTime": xdsl2PMLInitHist1DMonitoredTime,
       "xdsl2PMLInitHist1DFullInits": xdsl2PMLInitHist1DFullInits,
       "xdsl2PMLInitHist1DFailedFullInits": xdsl2PMLInitHist1DFailedFullInits,
       "xdsl2PMLInitHist1DShortInits": xdsl2PMLInitHist1DShortInits,
       "xdsl2PMLInitHist1DFailedShortInits": xdsl2PMLInitHist1DFailedShortInits,
       "xdsl2PMLInitHist1DValidInterval": xdsl2PMLInitHist1DValidInterval,
       "xdsl2PMChannel": xdsl2PMChannel,
       "xdsl2PMChCurrTable": xdsl2PMChCurrTable,
       "xdsl2PMChCurrEntry": xdsl2PMChCurrEntry,
       "xdsl2PMChCurrUnit": xdsl2PMChCurrUnit,
       "xdsl2PMChCurr15MValidIntervals": xdsl2PMChCurr15MValidIntervals,
       "xdsl2PMChCurr15MInvalidIntervals": xdsl2PMChCurr15MInvalidIntervals,
       "xdsl2PMChCurr15MTimeElapsed": xdsl2PMChCurr15MTimeElapsed,
       "xdsl2PMChCurr15MCodingViolations": xdsl2PMChCurr15MCodingViolations,
       "xdsl2PMChCurr15MCorrectedBlocks": xdsl2PMChCurr15MCorrectedBlocks,
       "xdsl2PMChCurr1DayValidIntervals": xdsl2PMChCurr1DayValidIntervals,
       "xdsl2PMChCurr1DayInvalidIntervals": xdsl2PMChCurr1DayInvalidIntervals,
       "xdsl2PMChCurr1DayTimeElapsed": xdsl2PMChCurr1DayTimeElapsed,
       "xdsl2PMChCurr1DayCodingViolations": xdsl2PMChCurr1DayCodingViolations,
       "xdsl2PMChCurr1DayCorrectedBlocks": xdsl2PMChCurr1DayCorrectedBlocks,
       "xdsl2PMChHist15MinTable": xdsl2PMChHist15MinTable,
       "xdsl2PMChHist15MinEntry": xdsl2PMChHist15MinEntry,
       "xdsl2PMChHist15MUnit": xdsl2PMChHist15MUnit,
       "xdsl2PMChHist15MInterval": xdsl2PMChHist15MInterval,
       "xdsl2PMChHist15MMonitoredTime": xdsl2PMChHist15MMonitoredTime,
       "xdsl2PMChHist15MCodingViolations": xdsl2PMChHist15MCodingViolations,
       "xdsl2PMChHist15MCorrectedBlocks": xdsl2PMChHist15MCorrectedBlocks,
       "xdsl2PMChHist15MValidInterval": xdsl2PMChHist15MValidInterval,
       "xdsl2PMChHist1DTable": xdsl2PMChHist1DTable,
       "xdsl2PMChHist1DEntry": xdsl2PMChHist1DEntry,
       "xdsl2PMChHist1DUnit": xdsl2PMChHist1DUnit,
       "xdsl2PMChHist1DInterval": xdsl2PMChHist1DInterval,
       "xdsl2PMChHist1DMonitoredTime": xdsl2PMChHist1DMonitoredTime,
       "xdsl2PMChHist1DCodingViolations": xdsl2PMChHist1DCodingViolations,
       "xdsl2PMChHist1DCorrectedBlocks": xdsl2PMChHist1DCorrectedBlocks,
       "xdsl2PMChHist1DValidInterval": xdsl2PMChHist1DValidInterval}
)
