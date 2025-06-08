# SNMP MIB module (TIMETRA-SAS-OAM-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-OAM-TEST-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:16 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(TAdaptationRule,) = mibBuilder.importSymbols(
    "TIMETRA-SAS-QOS-MIB",
    "TAdaptationRule")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(Dot1PPriority,
 IpAddressPrefixLength,
 SdpBindId,
 TDSCPNameOrEmpty,
 TFCName,
 TItemDescription,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TProfile,
 TmnxAdminState,
 TmnxBgpRouteTarget,
 TmnxEncapVal,
 TmnxPortID,
 TmnxPwGlobalIdOrZero,
 TmnxServId,
 TmnxSpokeSdpIdOrZero,
 TmnxStrSapId,
 TmnxTunnelID,
 TmnxTunnelType,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID,
 TmnxVcId,
 TmnxVcIdOrNone,
 TmnxVcType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "SdpBindId",
    "TDSCPNameOrEmpty",
    "TFCName",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TProfile",
    "TmnxAdminState",
    "TmnxBgpRouteTarget",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxPwGlobalIdOrZero",
    "TmnxServId",
    "TmnxSpokeSdpIdOrZero",
    "TmnxStrSapId",
    "TmnxTunnelID",
    "TmnxTunnelType",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID",
    "TmnxVcId",
    "TmnxVcIdOrNone",
    "TmnxVcType")


# MODULE-IDENTITY

timetraSASOamTestMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    timetraSASOamTestMIBModule.setRevisions(
        ("1912-10-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TTestHdCIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )



class TTestHdPIRRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSASOamTestConformance_ObjectIdentity = ObjectIdentity
tmnxSASOamTestConformance = _TmnxSASOamTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 17)
)
_TmnxTestHdProfConformance_ObjectIdentity = ObjectIdentity
tmnxTestHdProfConformance = _TmnxTestHdProfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 17, 1)
)
_TmnxTestHdObjsGroups_ObjectIdentity = ObjectIdentity
tmnxTestHdObjsGroups = _TmnxTestHdObjsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 17, 1, 1)
)
_TmnxSASOamTestObjs_ObjectIdentity = ObjectIdentity
tmnxSASOamTestObjs = _TmnxSASOamTestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17)
)
_TmnxTestHdProfObjects_ObjectIdentity = ObjectIdentity
tmnxTestHdProfObjects = _TmnxTestHdProfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1)
)
_TmnxTestHdProfTable_Object = MibTable
tmnxTestHdProfTable = _TmnxTestHdProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxTestHdProfTable.setStatus("current")
_TmnxTestHdProfEntry_Object = MibTableRow
tmnxTestHdProfEntry = _TmnxTestHdProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1)
)
tmnxTestHdProfEntry.setIndexNames(
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfIndex"),
)
if mibBuilder.loadTexts:
    tmnxTestHdProfEntry.setStatus("current")


class _TmnxTestHdProfIndex_Type(Integer32):
    """Custom type tmnxTestHdProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxTestHdProfIndex_Type.__name__ = "Integer32"
_TmnxTestHdProfIndex_Object = MibTableColumn
tmnxTestHdProfIndex = _TmnxTestHdProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 1),
    _TmnxTestHdProfIndex_Type()
)
tmnxTestHdProfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdProfIndex.setStatus("current")
_TmnxTestHdProfRowStatus_Type = RowStatus
_TmnxTestHdProfRowStatus_Object = MibTableColumn
tmnxTestHdProfRowStatus = _TmnxTestHdProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 2),
    _TmnxTestHdProfRowStatus_Type()
)
tmnxTestHdProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfRowStatus.setStatus("current")


class _TmnxTestHdProfDescription_Type(TItemDescription):
    """Custom type tmnxTestHdProfDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxTestHdProfDescription_Type.__name__ = "TItemDescription"
_TmnxTestHdProfDescription_Object = MibTableColumn
tmnxTestHdProfDescription = _TmnxTestHdProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 3),
    _TmnxTestHdProfDescription_Type()
)
tmnxTestHdProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfDescription.setStatus("current")


class _TmnxTestHdProfCIRAdaptation_Type(TAdaptationRule):
    """Custom type tmnxTestHdProfCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TmnxTestHdProfCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TmnxTestHdProfCIRAdaptation_Object = MibTableColumn
tmnxTestHdProfCIRAdaptation = _TmnxTestHdProfCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 4),
    _TmnxTestHdProfCIRAdaptation_Type()
)
tmnxTestHdProfCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfCIRAdaptation.setStatus("current")
_TmnxTestHdProfOperCIR_Type = TTestHdCIRRate
_TmnxTestHdProfOperCIR_Object = MibTableColumn
tmnxTestHdProfOperCIR = _TmnxTestHdProfOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 5),
    _TmnxTestHdProfOperCIR_Type()
)
tmnxTestHdProfOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdProfOperCIR.setStatus("current")


class _TmnxTestHdProfCIR_Type(TTestHdCIRRate):
    """Custom type tmnxTestHdProfCIR based on TTestHdCIRRate"""
    defaultValue = 1000


_TmnxTestHdProfCIR_Type.__name__ = "TTestHdCIRRate"
_TmnxTestHdProfCIR_Object = MibTableColumn
tmnxTestHdProfCIR = _TmnxTestHdProfCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 6),
    _TmnxTestHdProfCIR_Type()
)
tmnxTestHdProfCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfCIR.setStatus("deprecated")


class _TmnxTestHdProfDurHr_Type(Integer32):
    """Custom type tmnxTestHdProfDurHr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_TmnxTestHdProfDurHr_Type.__name__ = "Integer32"
_TmnxTestHdProfDurHr_Object = MibTableColumn
tmnxTestHdProfDurHr = _TmnxTestHdProfDurHr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 8),
    _TmnxTestHdProfDurHr_Type()
)
tmnxTestHdProfDurHr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfDurHr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdProfDurHr.setUnits("hours")


class _TmnxTestHdProfDurMin_Type(Integer32):
    """Custom type tmnxTestHdProfDurMin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TmnxTestHdProfDurMin_Type.__name__ = "Integer32"
_TmnxTestHdProfDurMin_Object = MibTableColumn
tmnxTestHdProfDurMin = _TmnxTestHdProfDurMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 9),
    _TmnxTestHdProfDurMin_Type()
)
tmnxTestHdProfDurMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfDurMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdProfDurMin.setUnits("minutes")


class _TmnxTestHdProfDurSec_Type(Integer32):
    """Custom type tmnxTestHdProfDurSec based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TmnxTestHdProfDurSec_Type.__name__ = "Integer32"
_TmnxTestHdProfDurSec_Object = MibTableColumn
tmnxTestHdProfDurSec = _TmnxTestHdProfDurSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 10),
    _TmnxTestHdProfDurSec_Type()
)
tmnxTestHdProfDurSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfDurSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdProfDurSec.setUnits("seconds")


class _TmnxTestHdProfFrameSize_Type(Integer32):
    """Custom type tmnxTestHdProfFrameSize based on Integer32"""
    defaultValue = 1514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9212),
    )


_TmnxTestHdProfFrameSize_Type.__name__ = "Integer32"
_TmnxTestHdProfFrameSize_Object = MibTableColumn
tmnxTestHdProfFrameSize = _TmnxTestHdProfFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 11),
    _TmnxTestHdProfFrameSize_Type()
)
tmnxTestHdProfFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfFrameSize.setStatus("current")


class _TmnxTestHdProfTrapEnable_Type(TruthValue):
    """Custom type tmnxTestHdProfTrapEnable based on TruthValue"""
    defaultValue = 2


_TmnxTestHdProfTrapEnable_Type.__name__ = "TruthValue"
_TmnxTestHdProfTrapEnable_Object = MibTableColumn
tmnxTestHdProfTrapEnable = _TmnxTestHdProfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 13),
    _TmnxTestHdProfTrapEnable_Type()
)
tmnxTestHdProfTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfTrapEnable.setStatus("current")
_TmnxTestHdLastChanged_Type = TimeStamp
_TmnxTestHdLastChanged_Object = MibTableColumn
tmnxTestHdLastChanged = _TmnxTestHdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 14),
    _TmnxTestHdLastChanged_Type()
)
tmnxTestHdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdLastChanged.setStatus("current")


class _TmnxTestHdProfAdminCIR_Type(TTestHdCIRRate):
    """Custom type tmnxTestHdProfAdminCIR based on TTestHdCIRRate"""
    defaultValue = 1000


_TmnxTestHdProfAdminCIR_Type.__name__ = "TTestHdCIRRate"
_TmnxTestHdProfAdminCIR_Object = MibTableColumn
tmnxTestHdProfAdminCIR = _TmnxTestHdProfAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 15),
    _TmnxTestHdProfAdminCIR_Type()
)
tmnxTestHdProfAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfAdminCIR.setStatus("current")


class _TmnxTestHdProfAdminPIR_Type(TTestHdPIRRate):
    """Custom type tmnxTestHdProfAdminPIR based on TTestHdPIRRate"""
    defaultValue = -1


_TmnxTestHdProfAdminPIR_Type.__name__ = "TTestHdPIRRate"
_TmnxTestHdProfAdminPIR_Object = MibTableColumn
tmnxTestHdProfAdminPIR = _TmnxTestHdProfAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 16),
    _TmnxTestHdProfAdminPIR_Type()
)
tmnxTestHdProfAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfAdminPIR.setStatus("current")
_TmnxTestHdProfOperPIR_Type = TTestHdPIRRate
_TmnxTestHdProfOperPIR_Object = MibTableColumn
tmnxTestHdProfOperPIR = _TmnxTestHdProfOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 17),
    _TmnxTestHdProfOperPIR_Type()
)
tmnxTestHdProfOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdProfOperPIR.setStatus("current")


class _TmnxTestHdProfDot1pIn_Type(Dot1PPriority):
    """Custom type tmnxTestHdProfDot1pIn based on Dot1PPriority"""
    defaultValue = -1


_TmnxTestHdProfDot1pIn_Type.__name__ = "Dot1PPriority"
_TmnxTestHdProfDot1pIn_Object = MibTableColumn
tmnxTestHdProfDot1pIn = _TmnxTestHdProfDot1pIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 18),
    _TmnxTestHdProfDot1pIn_Type()
)
tmnxTestHdProfDot1pIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfDot1pIn.setStatus("current")


class _TmnxTestHdProfDot1pOut_Type(Dot1PPriority):
    """Custom type tmnxTestHdProfDot1pOut based on Dot1PPriority"""
    defaultValue = -1


_TmnxTestHdProfDot1pOut_Type.__name__ = "Dot1PPriority"
_TmnxTestHdProfDot1pOut_Object = MibTableColumn
tmnxTestHdProfDot1pOut = _TmnxTestHdProfDot1pOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 19),
    _TmnxTestHdProfDot1pOut_Type()
)
tmnxTestHdProfDot1pOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdProfDot1pOut.setStatus("current")
_TmnxTestHdProfActiveTests_Type = OctetString
_TmnxTestHdProfActiveTests_Object = MibTableColumn
tmnxTestHdProfActiveTests = _TmnxTestHdProfActiveTests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 20),
    _TmnxTestHdProfActiveTests_Type()
)
tmnxTestHdProfActiveTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdProfActiveTests.setStatus("current")
_TmnxTestHdProfCompetedTests_Type = OctetString
_TmnxTestHdProfCompetedTests_Object = MibTableColumn
tmnxTestHdProfCompetedTests = _TmnxTestHdProfCompetedTests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 1, 1, 21),
    _TmnxTestHdProfCompetedTests_Type()
)
tmnxTestHdProfCompetedTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdProfCompetedTests.setStatus("current")
_TmnxTestHdPayLdTable_Object = MibTable
tmnxTestHdPayLdTable = _TmnxTestHdPayLdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxTestHdPayLdTable.setStatus("current")
_TmnxTestHdPayLdEntry_Object = MibTableRow
tmnxTestHdPayLdEntry = _TmnxTestHdPayLdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1)
)
tmnxTestHdPayLdEntry.setIndexNames(
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfIndex"),
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdIndex"),
)
if mibBuilder.loadTexts:
    tmnxTestHdPayLdEntry.setStatus("current")


class _TmnxTestHdPayLdIndex_Type(Integer32):
    """Custom type tmnxTestHdPayLdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTestHdPayLdIndex_Type.__name__ = "Integer32"
_TmnxTestHdPayLdIndex_Object = MibTableColumn
tmnxTestHdPayLdIndex = _TmnxTestHdPayLdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 1),
    _TmnxTestHdPayLdIndex_Type()
)
tmnxTestHdPayLdIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdIndex.setStatus("current")
_TmnxTestHdPayLdRowStatus_Type = RowStatus
_TmnxTestHdPayLdRowStatus_Object = MibTableColumn
tmnxTestHdPayLdRowStatus = _TmnxTestHdPayLdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 2),
    _TmnxTestHdPayLdRowStatus_Type()
)
tmnxTestHdPayLdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdRowStatus.setStatus("current")


class _TmnxTestHdPayLdDesc_Type(TItemDescription):
    """Custom type tmnxTestHdPayLdDesc based on TItemDescription"""
    defaultHexValue = ""


_TmnxTestHdPayLdDesc_Type.__name__ = "TItemDescription"
_TmnxTestHdPayLdDesc_Object = MibTableColumn
tmnxTestHdPayLdDesc = _TmnxTestHdPayLdDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 3),
    _TmnxTestHdPayLdDesc_Type()
)
tmnxTestHdPayLdDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdDesc.setStatus("current")


class _TmnxTestHdPayLddataPattrn_Type(OctetString):
    """Custom type tmnxTestHdPayLddataPattrn based on OctetString"""
    defaultValue = OctetString("a1b2c3d4e5f6")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxTestHdPayLddataPattrn_Type.__name__ = "OctetString"
_TmnxTestHdPayLddataPattrn_Object = MibTableColumn
tmnxTestHdPayLddataPattrn = _TmnxTestHdPayLddataPattrn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 4),
    _TmnxTestHdPayLddataPattrn_Type()
)
tmnxTestHdPayLddataPattrn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLddataPattrn.setStatus("current")
_TmnxTestHdPayLdSrcIpv4Addr_Type = IpAddress
_TmnxTestHdPayLdSrcIpv4Addr_Object = MibTableColumn
tmnxTestHdPayLdSrcIpv4Addr = _TmnxTestHdPayLdSrcIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 5),
    _TmnxTestHdPayLdSrcIpv4Addr_Type()
)
tmnxTestHdPayLdSrcIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdSrcIpv4Addr.setStatus("current")
_TmnxTestHdPayLdDstIpv4Addr_Type = IpAddress
_TmnxTestHdPayLdDstIpv4Addr_Object = MibTableColumn
tmnxTestHdPayLdDstIpv4Addr = _TmnxTestHdPayLdDstIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 6),
    _TmnxTestHdPayLdDstIpv4Addr_Type()
)
tmnxTestHdPayLdDstIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdDstIpv4Addr.setStatus("current")


class _TmnxTestHdPayLdDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tmnxTestHdPayLdDSCP based on TDSCPNameOrEmpty"""
    defaultValue = OctetString("be")


_TmnxTestHdPayLdDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TmnxTestHdPayLdDSCP_Object = MibTableColumn
tmnxTestHdPayLdDSCP = _TmnxTestHdPayLdDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 7),
    _TmnxTestHdPayLdDSCP_Type()
)
tmnxTestHdPayLdDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdDSCP.setStatus("current")


class _TmnxTestHdPayLdIpProto_Type(Integer32):
    """Custom type tmnxTestHdPayLdIpProto based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxTestHdPayLdIpProto_Type.__name__ = "Integer32"
_TmnxTestHdPayLdIpProto_Object = MibTableColumn
tmnxTestHdPayLdIpProto = _TmnxTestHdPayLdIpProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 8),
    _TmnxTestHdPayLdIpProto_Type()
)
tmnxTestHdPayLdIpProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdIpProto.setStatus("current")


class _TmnxTestHdPayLdIpTos_Type(Integer32):
    """Custom type tmnxTestHdPayLdIpTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TmnxTestHdPayLdIpTos_Type.__name__ = "Integer32"
_TmnxTestHdPayLdIpTos_Object = MibTableColumn
tmnxTestHdPayLdIpTos = _TmnxTestHdPayLdIpTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 9),
    _TmnxTestHdPayLdIpTos_Type()
)
tmnxTestHdPayLdIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdIpTos.setStatus("current")


class _TmnxTestHdPayLdIpTTL_Type(Integer32):
    """Custom type tmnxTestHdPayLdIpTTL based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxTestHdPayLdIpTTL_Type.__name__ = "Integer32"
_TmnxTestHdPayLdIpTTL_Object = MibTableColumn
tmnxTestHdPayLdIpTTL = _TmnxTestHdPayLdIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 10),
    _TmnxTestHdPayLdIpTTL_Type()
)
tmnxTestHdPayLdIpTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdIpTTL.setStatus("current")


class _TmnxTestHdPayLdSrcMac_Type(MacAddress):
    """Custom type tmnxTestHdPayLdSrcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxTestHdPayLdSrcMac_Type.__name__ = "MacAddress"
_TmnxTestHdPayLdSrcMac_Object = MibTableColumn
tmnxTestHdPayLdSrcMac = _TmnxTestHdPayLdSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 11),
    _TmnxTestHdPayLdSrcMac_Type()
)
tmnxTestHdPayLdSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdSrcMac.setStatus("current")


class _TmnxTestHdPayLdDstMac_Type(MacAddress):
    """Custom type tmnxTestHdPayLdDstMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxTestHdPayLdDstMac_Type.__name__ = "MacAddress"
_TmnxTestHdPayLdDstMac_Object = MibTableColumn
tmnxTestHdPayLdDstMac = _TmnxTestHdPayLdDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 12),
    _TmnxTestHdPayLdDstMac_Type()
)
tmnxTestHdPayLdDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdDstMac.setStatus("current")


class _TmnxTestHdPayLdSrcPort_Type(Integer32):
    """Custom type tmnxTestHdPayLdSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxTestHdPayLdSrcPort_Type.__name__ = "Integer32"
_TmnxTestHdPayLdSrcPort_Object = MibTableColumn
tmnxTestHdPayLdSrcPort = _TmnxTestHdPayLdSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 13),
    _TmnxTestHdPayLdSrcPort_Type()
)
tmnxTestHdPayLdSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdSrcPort.setStatus("current")


class _TmnxTestHdPayLdDstPort_Type(Integer32):
    """Custom type tmnxTestHdPayLdDstPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxTestHdPayLdDstPort_Type.__name__ = "Integer32"
_TmnxTestHdPayLdDstPort_Object = MibTableColumn
tmnxTestHdPayLdDstPort = _TmnxTestHdPayLdDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 14),
    _TmnxTestHdPayLdDstPort_Type()
)
tmnxTestHdPayLdDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdDstPort.setStatus("current")
_TmnxTestHdPayLdLastChanged_Type = TimeStamp
_TmnxTestHdPayLdLastChanged_Object = MibTableColumn
tmnxTestHdPayLdLastChanged = _TmnxTestHdPayLdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 15),
    _TmnxTestHdPayLdLastChanged_Type()
)
tmnxTestHdPayLdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdLastChanged.setStatus("current")


class _TmnxTestHdPayLdType_Type(Integer32):
    """Custom type tmnxTestHdPayLdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tcp-ipv4", 1),
          ("l2", 2),
          ("udp-ipv4", 3),
          ("ipv4", 4))
    )


_TmnxTestHdPayLdType_Type.__name__ = "Integer32"
_TmnxTestHdPayLdType_Object = MibTableColumn
tmnxTestHdPayLdType = _TmnxTestHdPayLdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 16),
    _TmnxTestHdPayLdType_Type()
)
tmnxTestHdPayLdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdType.setStatus("current")


class _TmnxTestHdPayLdVTagOne_Type(Integer32):
    """Custom type tmnxTestHdPayLdVTagOne based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_TmnxTestHdPayLdVTagOne_Type.__name__ = "Integer32"
_TmnxTestHdPayLdVTagOne_Object = MibTableColumn
tmnxTestHdPayLdVTagOne = _TmnxTestHdPayLdVTagOne_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 17),
    _TmnxTestHdPayLdVTagOne_Type()
)
tmnxTestHdPayLdVTagOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdVTagOne.setStatus("current")


class _TmnxTestHdPayLdVTagOneTpid_Type(Unsigned32):
    """Custom type tmnxTestHdPayLdVTagOneTpid based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxTestHdPayLdVTagOneTpid_Type.__name__ = "Unsigned32"
_TmnxTestHdPayLdVTagOneTpid_Object = MibTableColumn
tmnxTestHdPayLdVTagOneTpid = _TmnxTestHdPayLdVTagOneTpid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 18),
    _TmnxTestHdPayLdVTagOneTpid_Type()
)
tmnxTestHdPayLdVTagOneTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdVTagOneTpid.setStatus("current")


class _TmnxTestHdPayLdVTagOneDot1p_Type(Dot1PPriority):
    """Custom type tmnxTestHdPayLdVTagOneDot1p based on Dot1PPriority"""
    defaultValue = 0


_TmnxTestHdPayLdVTagOneDot1p_Type.__name__ = "Dot1PPriority"
_TmnxTestHdPayLdVTagOneDot1p_Object = MibTableColumn
tmnxTestHdPayLdVTagOneDot1p = _TmnxTestHdPayLdVTagOneDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 19),
    _TmnxTestHdPayLdVTagOneDot1p_Type()
)
tmnxTestHdPayLdVTagOneDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdVTagOneDot1p.setStatus("current")


class _TmnxTestHdPayLdVTagTwo_Type(Integer32):
    """Custom type tmnxTestHdPayLdVTagTwo based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_TmnxTestHdPayLdVTagTwo_Type.__name__ = "Integer32"
_TmnxTestHdPayLdVTagTwo_Object = MibTableColumn
tmnxTestHdPayLdVTagTwo = _TmnxTestHdPayLdVTagTwo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 20),
    _TmnxTestHdPayLdVTagTwo_Type()
)
tmnxTestHdPayLdVTagTwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdVTagTwo.setStatus("current")


class _TmnxTestHdPayLdVTagTwoTpid_Type(Unsigned32):
    """Custom type tmnxTestHdPayLdVTagTwoTpid based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxTestHdPayLdVTagTwoTpid_Type.__name__ = "Unsigned32"
_TmnxTestHdPayLdVTagTwoTpid_Object = MibTableColumn
tmnxTestHdPayLdVTagTwoTpid = _TmnxTestHdPayLdVTagTwoTpid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 21),
    _TmnxTestHdPayLdVTagTwoTpid_Type()
)
tmnxTestHdPayLdVTagTwoTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdVTagTwoTpid.setStatus("current")


class _TmnxTestHdPayLdVTagTwoDot1p_Type(Dot1PPriority):
    """Custom type tmnxTestHdPayLdVTagTwoDot1p based on Dot1PPriority"""
    defaultValue = 0


_TmnxTestHdPayLdVTagTwoDot1p_Type.__name__ = "Dot1PPriority"
_TmnxTestHdPayLdVTagTwoDot1p_Object = MibTableColumn
tmnxTestHdPayLdVTagTwoDot1p = _TmnxTestHdPayLdVTagTwoDot1p_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 22),
    _TmnxTestHdPayLdVTagTwoDot1p_Type()
)
tmnxTestHdPayLdVTagTwoDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdVTagTwoDot1p.setStatus("current")


class _TmnxTestHdPayLdEthertype_Type(Unsigned32):
    """Custom type tmnxTestHdPayLdEthertype based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxTestHdPayLdEthertype_Type.__name__ = "Unsigned32"
_TmnxTestHdPayLdEthertype_Object = MibTableColumn
tmnxTestHdPayLdEthertype = _TmnxTestHdPayLdEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 2, 1, 23),
    _TmnxTestHdPayLdEthertype_Type()
)
tmnxTestHdPayLdEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdEthertype.setStatus("current")
_TmnxTestHdAccCritTable_Object = MibTable
tmnxTestHdAccCritTable = _TmnxTestHdAccCritTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxTestHdAccCritTable.setStatus("current")
_TmnxTestHdAccCritEntry_Object = MibTableRow
tmnxTestHdAccCritEntry = _TmnxTestHdAccCritEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1)
)
tmnxTestHdAccCritEntry.setIndexNames(
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfIndex"),
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritIndex"),
)
if mibBuilder.loadTexts:
    tmnxTestHdAccCritEntry.setStatus("current")


class _TmnxTestHdAccCritIndex_Type(Integer32):
    """Custom type tmnxTestHdAccCritIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTestHdAccCritIndex_Type.__name__ = "Integer32"
_TmnxTestHdAccCritIndex_Object = MibTableColumn
tmnxTestHdAccCritIndex = _TmnxTestHdAccCritIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 1),
    _TmnxTestHdAccCritIndex_Type()
)
tmnxTestHdAccCritIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritIndex.setStatus("current")
_TmnxTestHdAccCritRowStatus_Type = RowStatus
_TmnxTestHdAccCritRowStatus_Object = MibTableColumn
tmnxTestHdAccCritRowStatus = _TmnxTestHdAccCritRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 2),
    _TmnxTestHdAccCritRowStatus_Type()
)
tmnxTestHdAccCritRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritRowStatus.setStatus("current")


class _TmnxTestHdAccCritJittrRiseThres_Type(Integer32):
    """Custom type tmnxTestHdAccCritJittrRiseThres based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdAccCritJittrRiseThres_Type.__name__ = "Integer32"
_TmnxTestHdAccCritJittrRiseThres_Object = MibTableColumn
tmnxTestHdAccCritJittrRiseThres = _TmnxTestHdAccCritJittrRiseThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 3),
    _TmnxTestHdAccCritJittrRiseThres_Type()
)
tmnxTestHdAccCritJittrRiseThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritJittrRiseThres.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritJittrRiseThres.setUnits("microseconds")


class _TmnxTestHdAccCritLatRiseThres_Type(Integer32):
    """Custom type tmnxTestHdAccCritLatRiseThres based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdAccCritLatRiseThres_Type.__name__ = "Integer32"
_TmnxTestHdAccCritLatRiseThres_Object = MibTableColumn
tmnxTestHdAccCritLatRiseThres = _TmnxTestHdAccCritLatRiseThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 4),
    _TmnxTestHdAccCritLatRiseThres_Type()
)
tmnxTestHdAccCritLatRiseThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLatRiseThres.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLatRiseThres.setUnits("microseconds")


class _TmnxTestHdAccCritLossRiseThres_Type(Integer32):
    """Custom type tmnxTestHdAccCritLossRiseThres based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxTestHdAccCritLossRiseThres_Type.__name__ = "Integer32"
_TmnxTestHdAccCritLossRiseThres_Object = MibTableColumn
tmnxTestHdAccCritLossRiseThres = _TmnxTestHdAccCritLossRiseThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 5),
    _TmnxTestHdAccCritLossRiseThres_Type()
)
tmnxTestHdAccCritLossRiseThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLossRiseThres.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLossRiseThres.setUnits("10000th of a percent")
_TmnxTestHdAccCritLastChanged_Type = TimeStamp
_TmnxTestHdAccCritLastChanged_Object = MibTableColumn
tmnxTestHdAccCritLastChanged = _TmnxTestHdAccCritLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 6),
    _TmnxTestHdAccCritLastChanged_Type()
)
tmnxTestHdAccCritLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLastChanged.setStatus("current")


class _TmnxTestHdAccCritLossRiseThresIn_Type(Integer32):
    """Custom type tmnxTestHdAccCritLossRiseThresIn based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxTestHdAccCritLossRiseThresIn_Type.__name__ = "Integer32"
_TmnxTestHdAccCritLossRiseThresIn_Object = MibTableColumn
tmnxTestHdAccCritLossRiseThresIn = _TmnxTestHdAccCritLossRiseThresIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 7),
    _TmnxTestHdAccCritLossRiseThresIn_Type()
)
tmnxTestHdAccCritLossRiseThresIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLossRiseThresIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLossRiseThresIn.setUnits("10000th of a percent")


class _TmnxTestHdAccCritLossRiseThresOut_Type(Integer32):
    """Custom type tmnxTestHdAccCritLossRiseThresOut based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxTestHdAccCritLossRiseThresOut_Type.__name__ = "Integer32"
_TmnxTestHdAccCritLossRiseThresOut_Object = MibTableColumn
tmnxTestHdAccCritLossRiseThresOut = _TmnxTestHdAccCritLossRiseThresOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 8),
    _TmnxTestHdAccCritLossRiseThresOut_Type()
)
tmnxTestHdAccCritLossRiseThresOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLossRiseThresOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLossRiseThresOut.setUnits("10000th of a percent")


class _TmnxTestHdAccCritCirThres_Type(Integer32):
    """Custom type tmnxTestHdAccCritCirThres based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxTestHdAccCritCirThres_Type.__name__ = "Integer32"
_TmnxTestHdAccCritCirThres_Object = MibTableColumn
tmnxTestHdAccCritCirThres = _TmnxTestHdAccCritCirThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 9),
    _TmnxTestHdAccCritCirThres_Type()
)
tmnxTestHdAccCritCirThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritCirThres.setStatus("current")


class _TmnxTestHdAccCritPirThres_Type(Integer32):
    """Custom type tmnxTestHdAccCritPirThres based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000000),
    )


_TmnxTestHdAccCritPirThres_Type.__name__ = "Integer32"
_TmnxTestHdAccCritPirThres_Object = MibTableColumn
tmnxTestHdAccCritPirThres = _TmnxTestHdAccCritPirThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 10),
    _TmnxTestHdAccCritPirThres_Type()
)
tmnxTestHdAccCritPirThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritPirThres.setStatus("current")


class _TmnxTestHdAccCritLatRiseThresIn_Type(Integer32):
    """Custom type tmnxTestHdAccCritLatRiseThresIn based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdAccCritLatRiseThresIn_Type.__name__ = "Integer32"
_TmnxTestHdAccCritLatRiseThresIn_Object = MibTableColumn
tmnxTestHdAccCritLatRiseThresIn = _TmnxTestHdAccCritLatRiseThresIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 11),
    _TmnxTestHdAccCritLatRiseThresIn_Type()
)
tmnxTestHdAccCritLatRiseThresIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLatRiseThresIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLatRiseThresIn.setUnits("microseconds")


class _TmnxTestHdAccCritLatRiseThresOut_Type(Integer32):
    """Custom type tmnxTestHdAccCritLatRiseThresOut based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdAccCritLatRiseThresOut_Type.__name__ = "Integer32"
_TmnxTestHdAccCritLatRiseThresOut_Object = MibTableColumn
tmnxTestHdAccCritLatRiseThresOut = _TmnxTestHdAccCritLatRiseThresOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 12),
    _TmnxTestHdAccCritLatRiseThresOut_Type()
)
tmnxTestHdAccCritLatRiseThresOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLatRiseThresOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritLatRiseThresOut.setUnits("microseconds")


class _TmnxTestHdAccCritJittrRiseThresIn_Type(Integer32):
    """Custom type tmnxTestHdAccCritJittrRiseThresIn based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdAccCritJittrRiseThresIn_Type.__name__ = "Integer32"
_TmnxTestHdAccCritJittrRiseThresIn_Object = MibTableColumn
tmnxTestHdAccCritJittrRiseThresIn = _TmnxTestHdAccCritJittrRiseThresIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 13),
    _TmnxTestHdAccCritJittrRiseThresIn_Type()
)
tmnxTestHdAccCritJittrRiseThresIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritJittrRiseThresIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritJittrRiseThresIn.setUnits("microseconds")


class _TmnxTestHdAccCritJittrRiseThresOut_Type(Integer32):
    """Custom type tmnxTestHdAccCritJittrRiseThresOut based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdAccCritJittrRiseThresOut_Type.__name__ = "Integer32"
_TmnxTestHdAccCritJittrRiseThresOut_Object = MibTableColumn
tmnxTestHdAccCritJittrRiseThresOut = _TmnxTestHdAccCritJittrRiseThresOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 3, 1, 14),
    _TmnxTestHdAccCritJittrRiseThresOut_Type()
)
tmnxTestHdAccCritJittrRiseThresOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritJittrRiseThresOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritJittrRiseThresOut.setUnits("microseconds")
_TmnxTestHdSessTable_Object = MibTable
tmnxTestHdSessTable = _TmnxTestHdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxTestHdSessTable.setStatus("current")
_TmnxTestHdSessEntry_Object = MibTableRow
tmnxTestHdSessEntry = _TmnxTestHdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1)
)
tmnxTestHdSessEntry.setIndexNames(
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessOwnerName"),
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessTestName"),
)
if mibBuilder.loadTexts:
    tmnxTestHdSessEntry.setStatus("current")


class _TmnxTestHdSessOwnerName_Type(SnmpAdminString):
    """Custom type tmnxTestHdSessOwnerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxTestHdSessOwnerName_Type.__name__ = "SnmpAdminString"
_TmnxTestHdSessOwnerName_Object = MibTableColumn
tmnxTestHdSessOwnerName = _TmnxTestHdSessOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 1),
    _TmnxTestHdSessOwnerName_Type()
)
tmnxTestHdSessOwnerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTestHdSessOwnerName.setStatus("current")


class _TmnxTestHdSessTestName_Type(SnmpAdminString):
    """Custom type tmnxTestHdSessTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxTestHdSessTestName_Type.__name__ = "SnmpAdminString"
_TmnxTestHdSessTestName_Object = MibTableColumn
tmnxTestHdSessTestName = _TmnxTestHdSessTestName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 2),
    _TmnxTestHdSessTestName_Type()
)
tmnxTestHdSessTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTestHdSessTestName.setStatus("current")
_TmnxTestHdSessStartTime_Type = DateAndTime
_TmnxTestHdSessStartTime_Object = MibTableColumn
tmnxTestHdSessStartTime = _TmnxTestHdSessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 3),
    _TmnxTestHdSessStartTime_Type()
)
tmnxTestHdSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessStartTime.setStatus("current")
_TmnxTestHdSessCompletedTime_Type = DateAndTime
_TmnxTestHdSessCompletedTime_Object = MibTableColumn
tmnxTestHdSessCompletedTime = _TmnxTestHdSessCompletedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 4),
    _TmnxTestHdSessCompletedTime_Type()
)
tmnxTestHdSessCompletedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessCompletedTime.setStatus("current")
_TmnxTestHdSessTotalTime_Type = Integer32
_TmnxTestHdSessTotalTime_Object = MibTableColumn
tmnxTestHdSessTotalTime = _TmnxTestHdSessTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 5),
    _TmnxTestHdSessTotalTime_Type()
)
tmnxTestHdSessTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessTotalTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdSessTotalTime.setUnits("seconds")
_TmnxTestHdSessFc_Type = TFCName
_TmnxTestHdSessFc_Object = MibTableColumn
tmnxTestHdSessFc = _TmnxTestHdSessFc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 6),
    _TmnxTestHdSessFc_Type()
)
tmnxTestHdSessFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessFc.setStatus("current")
_TmnxTestHdSessCompleted_Type = TruthValue
_TmnxTestHdSessCompleted_Object = MibTableColumn
tmnxTestHdSessCompleted = _TmnxTestHdSessCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 7),
    _TmnxTestHdSessCompleted_Type()
)
tmnxTestHdSessCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessCompleted.setStatus("current")
_TmnxTestHdSessStopped_Type = TruthValue
_TmnxTestHdSessStopped_Object = MibTableColumn
tmnxTestHdSessStopped = _TmnxTestHdSessStopped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 8),
    _TmnxTestHdSessStopped_Type()
)
tmnxTestHdSessStopped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessStopped.setStatus("current")


class _TmnxTestHdSessProfId_Type(Integer32):
    """Custom type tmnxTestHdSessProfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxTestHdSessProfId_Type.__name__ = "Integer32"
_TmnxTestHdSessProfId_Object = MibTableColumn
tmnxTestHdSessProfId = _TmnxTestHdSessProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 9),
    _TmnxTestHdSessProfId_Type()
)
tmnxTestHdSessProfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessProfId.setStatus("current")


class _TmnxTestHdSessPayLdId_Type(Integer32):
    """Custom type tmnxTestHdSessPayLdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTestHdSessPayLdId_Type.__name__ = "Integer32"
_TmnxTestHdSessPayLdId_Object = MibTableColumn
tmnxTestHdSessPayLdId = _TmnxTestHdSessPayLdId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 10),
    _TmnxTestHdSessPayLdId_Type()
)
tmnxTestHdSessPayLdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessPayLdId.setStatus("current")


class _TmnxTestHdSessAccCritId_Type(Integer32):
    """Custom type tmnxTestHdSessAccCritId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTestHdSessAccCritId_Type.__name__ = "Integer32"
_TmnxTestHdSessAccCritId_Object = MibTableColumn
tmnxTestHdSessAccCritId = _TmnxTestHdSessAccCritId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 11),
    _TmnxTestHdSessAccCritId_Type()
)
tmnxTestHdSessAccCritId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessAccCritId.setStatus("current")
_TmnxTestHdSessSapPortId_Type = TmnxPortID
_TmnxTestHdSessSapPortId_Object = MibTableColumn
tmnxTestHdSessSapPortId = _TmnxTestHdSessSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 12),
    _TmnxTestHdSessSapPortId_Type()
)
tmnxTestHdSessSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessSapPortId.setStatus("current")
_TmnxTestHdSessSapEncapValue_Type = TmnxEncapVal
_TmnxTestHdSessSapEncapValue_Object = MibTableColumn
tmnxTestHdSessSapEncapValue = _TmnxTestHdSessSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 13),
    _TmnxTestHdSessSapEncapValue_Type()
)
tmnxTestHdSessSapEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessSapEncapValue.setStatus("current")
_TmnxTestHdSessTransCount_Type = Counter64
_TmnxTestHdSessTransCount_Object = MibTableColumn
tmnxTestHdSessTransCount = _TmnxTestHdSessTransCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 14),
    _TmnxTestHdSessTransCount_Type()
)
tmnxTestHdSessTransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessTransCount.setStatus("current")
_TmnxTestHdSessRecvCount_Type = Counter64
_TmnxTestHdSessRecvCount_Object = MibTableColumn
tmnxTestHdSessRecvCount = _TmnxTestHdSessRecvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 15),
    _TmnxTestHdSessRecvCount_Type()
)
tmnxTestHdSessRecvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessRecvCount.setStatus("current")
_TmnxTestHdSessMinLatency_Type = Counter64
_TmnxTestHdSessMinLatency_Object = MibTableColumn
tmnxTestHdSessMinLatency = _TmnxTestHdSessMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 16),
    _TmnxTestHdSessMinLatency_Type()
)
tmnxTestHdSessMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdSessMinLatency.setUnits("microseconds")
_TmnxTestHdSessMaxLatency_Type = Counter64
_TmnxTestHdSessMaxLatency_Object = MibTableColumn
tmnxTestHdSessMaxLatency = _TmnxTestHdSessMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 17),
    _TmnxTestHdSessMaxLatency_Type()
)
tmnxTestHdSessMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdSessMaxLatency.setUnits("microseconds")
_TmnxTestHdSessMeasuredLatency_Type = Counter64
_TmnxTestHdSessMeasuredLatency_Object = MibTableColumn
tmnxTestHdSessMeasuredLatency = _TmnxTestHdSessMeasuredLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 18),
    _TmnxTestHdSessMeasuredLatency_Type()
)
tmnxTestHdSessMeasuredLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessMeasuredLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdSessMeasuredLatency.setUnits("microseconds")
_TmnxTestHdSessMeasuredJitter_Type = Integer32
_TmnxTestHdSessMeasuredJitter_Object = MibTableColumn
tmnxTestHdSessMeasuredJitter = _TmnxTestHdSessMeasuredJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 4, 1, 19),
    _TmnxTestHdSessMeasuredJitter_Type()
)
tmnxTestHdSessMeasuredJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdSessMeasuredJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdSessMeasuredJitter.setUnits("microseconds")
_TmnxTestHdResultsTable_Object = MibTable
tmnxTestHdResultsTable = _TmnxTestHdResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxTestHdResultsTable.setStatus("current")
_TmnxTestHdResultsEntry_Object = MibTableRow
tmnxTestHdResultsEntry = _TmnxTestHdResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1)
)
tmnxTestHdResultsEntry.setIndexNames(
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdOwnerName"),
    (0, "TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdTestName"),
)
if mibBuilder.loadTexts:
    tmnxTestHdResultsEntry.setStatus("current")


class _TmnxTestHdOwnerName_Type(SnmpAdminString):
    """Custom type tmnxTestHdOwnerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxTestHdOwnerName_Type.__name__ = "SnmpAdminString"
_TmnxTestHdOwnerName_Object = MibTableColumn
tmnxTestHdOwnerName = _TmnxTestHdOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 1),
    _TmnxTestHdOwnerName_Type()
)
tmnxTestHdOwnerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTestHdOwnerName.setStatus("current")


class _TmnxTestHdTestName_Type(SnmpAdminString):
    """Custom type tmnxTestHdTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxTestHdTestName_Type.__name__ = "SnmpAdminString"
_TmnxTestHdTestName_Object = MibTableColumn
tmnxTestHdTestName = _TmnxTestHdTestName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 2),
    _TmnxTestHdTestName_Type()
)
tmnxTestHdTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTestHdTestName.setStatus("current")
_TmnxTestHdResProfId_Type = Integer32
_TmnxTestHdResProfId_Object = MibTableColumn
tmnxTestHdResProfId = _TmnxTestHdResProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 3),
    _TmnxTestHdResProfId_Type()
)
tmnxTestHdResProfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResProfId.setStatus("current")
_TmnxTestHdResProfPayLdId_Type = Integer32
_TmnxTestHdResProfPayLdId_Object = MibTableColumn
tmnxTestHdResProfPayLdId = _TmnxTestHdResProfPayLdId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 4),
    _TmnxTestHdResProfPayLdId_Type()
)
tmnxTestHdResProfPayLdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResProfPayLdId.setStatus("current")
_TmnxTestHdResProfAccCritId_Type = Integer32
_TmnxTestHdResProfAccCritId_Object = MibTableColumn
tmnxTestHdResProfAccCritId = _TmnxTestHdResProfAccCritId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 5),
    _TmnxTestHdResProfAccCritId_Type()
)
tmnxTestHdResProfAccCritId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResProfAccCritId.setStatus("current")
_TmnxTestHdResTransCount_Type = Counter64
_TmnxTestHdResTransCount_Object = MibTableColumn
tmnxTestHdResTransCount = _TmnxTestHdResTransCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 6),
    _TmnxTestHdResTransCount_Type()
)
tmnxTestHdResTransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResTransCount.setStatus("current")
_TmnxTestHdResRecvCount_Type = Counter64
_TmnxTestHdResRecvCount_Object = MibTableColumn
tmnxTestHdResRecvCount = _TmnxTestHdResRecvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 7),
    _TmnxTestHdResRecvCount_Type()
)
tmnxTestHdResRecvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResRecvCount.setStatus("current")
_TmnxTestHdResMeasuredThruput_Type = Integer32
_TmnxTestHdResMeasuredThruput_Object = MibTableColumn
tmnxTestHdResMeasuredThruput = _TmnxTestHdResMeasuredThruput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 8),
    _TmnxTestHdResMeasuredThruput_Type()
)
tmnxTestHdResMeasuredThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredThruput.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredThruput.setUnits("kbps")
_TmnxTestHdResMeasuredFLR_Type = Integer32
_TmnxTestHdResMeasuredFLR_Object = MibTableColumn
tmnxTestHdResMeasuredFLR = _TmnxTestHdResMeasuredFLR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 9),
    _TmnxTestHdResMeasuredFLR_Type()
)
tmnxTestHdResMeasuredFLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredFLR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredFLR.setUnits("10000th of a percent")
_TmnxTestHdResMeasuredLatency_Type = Counter64
_TmnxTestHdResMeasuredLatency_Object = MibTableColumn
tmnxTestHdResMeasuredLatency = _TmnxTestHdResMeasuredLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 10),
    _TmnxTestHdResMeasuredLatency_Type()
)
tmnxTestHdResMeasuredLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredLatency.setUnits("microseconds")


class _TmnxTestHdResLatencyAccptanceResult_Type(Integer32):
    """Custom type tmnxTestHdResLatencyAccptanceResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2),
          ("not-applicable", 3))
    )


_TmnxTestHdResLatencyAccptanceResult_Type.__name__ = "Integer32"
_TmnxTestHdResLatencyAccptanceResult_Object = MibTableColumn
tmnxTestHdResLatencyAccptanceResult = _TmnxTestHdResLatencyAccptanceResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 11),
    _TmnxTestHdResLatencyAccptanceResult_Type()
)
tmnxTestHdResLatencyAccptanceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResLatencyAccptanceResult.setStatus("current")
_TmnxTestHdResMeasuredJitter_Type = Integer32
_TmnxTestHdResMeasuredJitter_Object = MibTableColumn
tmnxTestHdResMeasuredJitter = _TmnxTestHdResMeasuredJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 12),
    _TmnxTestHdResMeasuredJitter_Type()
)
tmnxTestHdResMeasuredJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdResMeasuredJitter.setUnits("microseconds")


class _TmnxTestHdResJitterAccptanceResult_Type(Integer32):
    """Custom type tmnxTestHdResJitterAccptanceResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2),
          ("not-applicable", 3))
    )


_TmnxTestHdResJitterAccptanceResult_Type.__name__ = "Integer32"
_TmnxTestHdResJitterAccptanceResult_Object = MibTableColumn
tmnxTestHdResJitterAccptanceResult = _TmnxTestHdResJitterAccptanceResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 13),
    _TmnxTestHdResJitterAccptanceResult_Type()
)
tmnxTestHdResJitterAccptanceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResJitterAccptanceResult.setStatus("current")
_TmnxTestHdResSapPortId_Type = TmnxPortID
_TmnxTestHdResSapPortId_Object = MibTableColumn
tmnxTestHdResSapPortId = _TmnxTestHdResSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 14),
    _TmnxTestHdResSapPortId_Type()
)
tmnxTestHdResSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResSapPortId.setStatus("current")
_TmnxTestHdResSapEncapValue_Type = TmnxEncapVal
_TmnxTestHdResSapEncapValue_Object = MibTableColumn
tmnxTestHdResSapEncapValue = _TmnxTestHdResSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 15),
    _TmnxTestHdResSapEncapValue_Type()
)
tmnxTestHdResSapEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResSapEncapValue.setStatus("current")


class _TmnxTestHdResFLRAccptanceResult_Type(Integer32):
    """Custom type tmnxTestHdResFLRAccptanceResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2),
          ("not-applicable", 3))
    )


_TmnxTestHdResFLRAccptanceResult_Type.__name__ = "Integer32"
_TmnxTestHdResFLRAccptanceResult_Object = MibTableColumn
tmnxTestHdResFLRAccptanceResult = _TmnxTestHdResFLRAccptanceResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 16),
    _TmnxTestHdResFLRAccptanceResult_Type()
)
tmnxTestHdResFLRAccptanceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResFLRAccptanceResult.setStatus("current")
_TmnxTestHdResMinLatency_Type = Counter64
_TmnxTestHdResMinLatency_Object = MibTableColumn
tmnxTestHdResMinLatency = _TmnxTestHdResMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 17),
    _TmnxTestHdResMinLatency_Type()
)
tmnxTestHdResMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdResMinLatency.setUnits("microseconds")
_TmnxTestHdResMaxLatency_Type = Counter64
_TmnxTestHdResMaxLatency_Object = MibTableColumn
tmnxTestHdResMaxLatency = _TmnxTestHdResMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 5, 1, 18),
    _TmnxTestHdResMaxLatency_Type()
)
tmnxTestHdResMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTestHdResMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdResMaxLatency.setUnits("microseconds")
_TmnxTestHdProfScalarObjs_ObjectIdentity = ObjectIdentity
tmnxTestHdProfScalarObjs = _TmnxTestHdProfScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6)
)


class _TmnxTestHdName_Type(SnmpAdminString):
    """Custom type tmnxTestHdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxTestHdName_Type.__name__ = "SnmpAdminString"
_TmnxTestHdName_Object = MibScalar
tmnxTestHdName = _TmnxTestHdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 1),
    _TmnxTestHdName_Type()
)
tmnxTestHdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdName.setStatus("current")


class _TmnxTestHdOwner_Type(SnmpAdminString):
    """Custom type tmnxTestHdOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxTestHdOwner_Type.__name__ = "SnmpAdminString"
_TmnxTestHdOwner_Object = MibScalar
tmnxTestHdOwner = _TmnxTestHdOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 2),
    _TmnxTestHdOwner_Type()
)
tmnxTestHdOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdOwner.setStatus("current")
_TmnxTestHdStartTime_Type = DateAndTime
_TmnxTestHdStartTime_Object = MibScalar
tmnxTestHdStartTime = _TmnxTestHdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 3),
    _TmnxTestHdStartTime_Type()
)
tmnxTestHdStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdStartTime.setStatus("current")
_TmnxTestHdElapsedTime_Type = Integer32
_TmnxTestHdElapsedTime_Object = MibScalar
tmnxTestHdElapsedTime = _TmnxTestHdElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 4),
    _TmnxTestHdElapsedTime_Type()
)
tmnxTestHdElapsedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdElapsedTime.setUnits("seconds")


class _TmnxTestHdFc_Type(TFCName):
    """Custom type tmnxTestHdFc based on TFCName"""
    defaultValue = OctetString("be")


_TmnxTestHdFc_Type.__name__ = "TFCName"
_TmnxTestHdFc_Object = MibScalar
tmnxTestHdFc = _TmnxTestHdFc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 5),
    _TmnxTestHdFc_Type()
)
tmnxTestHdFc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdFc.setStatus("current")


class _TmnxTestHdAvgLatency_Type(Integer32):
    """Custom type tmnxTestHdAvgLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdAvgLatency_Type.__name__ = "Integer32"
_TmnxTestHdAvgLatency_Object = MibScalar
tmnxTestHdAvgLatency = _TmnxTestHdAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 6),
    _TmnxTestHdAvgLatency_Type()
)
tmnxTestHdAvgLatency.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdAvgLatency.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdAvgLatency.setUnits("microseconds")


class _TmnxTestHdFrLossRatio_Type(Integer32):
    """Custom type tmnxTestHdFrLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_TmnxTestHdFrLossRatio_Type.__name__ = "Integer32"
_TmnxTestHdFrLossRatio_Object = MibScalar
tmnxTestHdFrLossRatio = _TmnxTestHdFrLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 7),
    _TmnxTestHdFrLossRatio_Type()
)
tmnxTestHdFrLossRatio.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdFrLossRatio.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdFrLossRatio.setUnits("10000th of a percent")


class _TmnxTestHdJitter_Type(Integer32):
    """Custom type tmnxTestHdJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483000),
    )


_TmnxTestHdJitter_Type.__name__ = "Integer32"
_TmnxTestHdJitter_Object = MibScalar
tmnxTestHdJitter = _TmnxTestHdJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 8),
    _TmnxTestHdJitter_Type()
)
tmnxTestHdJitter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTestHdJitter.setUnits("microseconds")
_TmnxTestHdDsiredThrpt_Type = Integer32
_TmnxTestHdDsiredThrpt_Object = MibScalar
tmnxTestHdDsiredThrpt = _TmnxTestHdDsiredThrpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 9),
    _TmnxTestHdDsiredThrpt_Type()
)
tmnxTestHdDsiredThrpt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdDsiredThrpt.setStatus("current")
_TmnxTestHdAchvdThrpt_Type = Integer32
_TmnxTestHdAchvdThrpt_Object = MibScalar
tmnxTestHdAchvdThrpt = _TmnxTestHdAchvdThrpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 10),
    _TmnxTestHdAchvdThrpt_Type()
)
tmnxTestHdAchvdThrpt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdAchvdThrpt.setStatus("current")
_TmnxTestHdCompleted_Type = TruthValue
_TmnxTestHdCompleted_Object = MibScalar
tmnxTestHdCompleted = _TmnxTestHdCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 11),
    _TmnxTestHdCompleted_Type()
)
tmnxTestHdCompleted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdCompleted.setStatus("current")
_TmnxTestHdStopped_Type = TruthValue
_TmnxTestHdStopped_Object = MibScalar
tmnxTestHdStopped = _TmnxTestHdStopped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 12),
    _TmnxTestHdStopped_Type()
)
tmnxTestHdStopped.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdStopped.setStatus("current")


class _TmnxTestHdTestStatus_Type(Integer32):
    """Custom type tmnxTestHdTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2),
          ("not-available", 3))
    )


_TmnxTestHdTestStatus_Type.__name__ = "Integer32"
_TmnxTestHdTestStatus_Object = MibScalar
tmnxTestHdTestStatus = _TmnxTestHdTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 13),
    _TmnxTestHdTestStatus_Type()
)
tmnxTestHdTestStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdTestStatus.setStatus("current")
_TmnxTestHdCompletedTime_Type = DateAndTime
_TmnxTestHdCompletedTime_Object = MibScalar
tmnxTestHdCompletedTime = _TmnxTestHdCompletedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 14),
    _TmnxTestHdCompletedTime_Type()
)
tmnxTestHdCompletedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTestHdCompletedTime.setStatus("current")
_TmnxTestHdSapPortId_Type = TmnxPortID
_TmnxTestHdSapPortId_Object = MibScalar
tmnxTestHdSapPortId = _TmnxTestHdSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 15),
    _TmnxTestHdSapPortId_Type()
)
tmnxTestHdSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdSapPortId.setStatus("current")
_TmnxTestHdSapEncapValue_Type = TmnxEncapVal
_TmnxTestHdSapEncapValue_Object = MibScalar
tmnxTestHdSapEncapValue = _TmnxTestHdSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 16),
    _TmnxTestHdSapEncapValue_Type()
)
tmnxTestHdSapEncapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdSapEncapValue.setStatus("current")


class _TmnxTestHdAdminStatus_Type(Integer32):
    """Custom type tmnxTestHdAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TmnxTestHdAdminStatus_Type.__name__ = "Integer32"
_TmnxTestHdAdminStatus_Object = MibScalar
tmnxTestHdAdminStatus = _TmnxTestHdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 17),
    _TmnxTestHdAdminStatus_Type()
)
tmnxTestHdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdAdminStatus.setStatus("current")


class _TmnxTestHdProfId_Type(Integer32):
    """Custom type tmnxTestHdProfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxTestHdProfId_Type.__name__ = "Integer32"
_TmnxTestHdProfId_Object = MibScalar
tmnxTestHdProfId = _TmnxTestHdProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 18),
    _TmnxTestHdProfId_Type()
)
tmnxTestHdProfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdProfId.setStatus("current")


class _TmnxTestHdAccCritId_Type(Integer32):
    """Custom type tmnxTestHdAccCritId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTestHdAccCritId_Type.__name__ = "Integer32"
_TmnxTestHdAccCritId_Object = MibScalar
tmnxTestHdAccCritId = _TmnxTestHdAccCritId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 19),
    _TmnxTestHdAccCritId_Type()
)
tmnxTestHdAccCritId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdAccCritId.setStatus("current")


class _TmnxTestHdPayLdId_Type(Integer32):
    """Custom type tmnxTestHdPayLdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxTestHdPayLdId_Type.__name__ = "Integer32"
_TmnxTestHdPayLdId_Object = MibScalar
tmnxTestHdPayLdId = _TmnxTestHdPayLdId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 20),
    _TmnxTestHdPayLdId_Type()
)
tmnxTestHdPayLdId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdPayLdId.setStatus("current")
_TmnxTestHdColorAware_Type = TruthValue
_TmnxTestHdColorAware_Object = MibScalar
tmnxTestHdColorAware = _TmnxTestHdColorAware_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 1, 6, 21),
    _TmnxTestHdColorAware_Type()
)
tmnxTestHdColorAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTestHdColorAware.setStatus("current")
_TmnxTestHdProfNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxTestHdProfNotifyObjs = _TmnxTestHdProfNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 17, 2)
)
_TmnxSASOamNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSASOamNotifyPrefix = _TmnxSASOamNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 3)
)
_TmnxSASOamNotifications_ObjectIdentity = ObjectIdentity
tmnxSASOamNotifications = _TmnxSASOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 3, 1)
)

# Managed Objects groups

tmnxTestHdObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 17, 1, 1, 1)
)
tmnxTestHdObjsV5v0Group.setObjects(
      *(("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritIndex"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritJittrRiseThres"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritLastChanged"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritLatRiseThres"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritLossRiseThres"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritRowStatus"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAchvdThrpt"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAdminStatus"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAvgLatency"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdCompleted"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdCompletedTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdDsiredThrpt"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdElapsedTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdFc"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdFrLossRatio"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdJitter"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdLastChanged"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdName"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdOwner"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdDSCP"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdDesc"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdDstIpv4Addr"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdDstMac"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdDstPort"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdEthertype"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdIndex"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdIpProto"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdIpTTL"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdIpTos"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdLastChanged"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdRowStatus"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdSrcIpv4Addr"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdSrcMac"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdSrcPort"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdType"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdVTagOne"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdVTagOneDot1p"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdVTagOneTpid"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdVTagTwo"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdVTagTwoDot1p"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdVTagTwoTpid"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLddataPattrn"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfAdminCIR"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfOperCIR"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfCIR"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfCIRAdaptation"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfDescription"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfDurHr"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfDurMin"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfDurSec"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfFrameSize"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfIndex"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfRowStatus"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfTrapEnable"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResFLRAccptanceResult"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResJitterAccptanceResult"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResLatencyAccptanceResult"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResMaxLatency"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResMeasuredFLR"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResMeasuredJitter"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResMeasuredLatency"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResMeasuredThruput"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResMinLatency"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResProfAccCritId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResProfId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResProfPayLdId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResRecvCount"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResSapEncapValue"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResSapPortId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdResTransCount"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSapEncapValue"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSapPortId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessAccCritId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessCompleted"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessCompletedTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessFc"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessPayLdId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessProfId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessSapEncapValue"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessSapPortId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessStartTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessStopped"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSessTotalTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdStartTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdStopped"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdTestStatus"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritLossRiseThresIn"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritLossRiseThresOut"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritCirThres"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritPirThres"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritLatRiseThresIn"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritLatRiseThresOut"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritJittrRiseThresIn"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritJittrRiseThresOut"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfDot1pIn"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfDot1pOut"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfOperPIR"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfAdminPIR"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdColorAware"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfActiveTests"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfCompetedTests"))
)
if mibBuilder.loadTexts:
    tmnxTestHdObjsV5v0Group.setStatus("current")


# Notification objects

tmnxOamTestHeadTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 3, 1, 1)
)
tmnxOamTestHeadTestCompleted.setObjects(
      *(("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdName"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdOwner"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdStartTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdCompletedTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdElapsedTime"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdProfIndex"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAccCritIndex"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdPayLdIndex"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSapPortId"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdSapEncapValue"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdFc"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdDsiredThrpt"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdCompleted"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdStopped"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdTestStatus"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAvgLatency"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdFrLossRatio"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdJitter"),
        ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxTestHdAchvdThrpt"))
)
if mibBuilder.loadTexts:
    tmnxOamTestHeadTestCompleted.setStatus(
        "current"
    )


# Notifications groups

tmnxTestHdNotifyV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 17, 1, 1, 2)
)
tmnxTestHdNotifyV5v0Group.setObjects(
    ("TIMETRA-SAS-OAM-TEST-MIB", "tmnxOamTestHeadTestCompleted")
)
if mibBuilder.loadTexts:
    tmnxTestHdNotifyV5v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-OAM-TEST-MIB",
    **{"TTestHdCIRRate": TTestHdCIRRate,
       "TTestHdPIRRate": TTestHdPIRRate,
       "timetraSASOamTestMIBModule": timetraSASOamTestMIBModule,
       "tmnxSASOamTestConformance": tmnxSASOamTestConformance,
       "tmnxTestHdProfConformance": tmnxTestHdProfConformance,
       "tmnxTestHdObjsGroups": tmnxTestHdObjsGroups,
       "tmnxTestHdObjsV5v0Group": tmnxTestHdObjsV5v0Group,
       "tmnxTestHdNotifyV5v0Group": tmnxTestHdNotifyV5v0Group,
       "tmnxSASOamTestObjs": tmnxSASOamTestObjs,
       "tmnxTestHdProfObjects": tmnxTestHdProfObjects,
       "tmnxTestHdProfTable": tmnxTestHdProfTable,
       "tmnxTestHdProfEntry": tmnxTestHdProfEntry,
       "tmnxTestHdProfIndex": tmnxTestHdProfIndex,
       "tmnxTestHdProfRowStatus": tmnxTestHdProfRowStatus,
       "tmnxTestHdProfDescription": tmnxTestHdProfDescription,
       "tmnxTestHdProfCIRAdaptation": tmnxTestHdProfCIRAdaptation,
       "tmnxTestHdProfOperCIR": tmnxTestHdProfOperCIR,
       "tmnxTestHdProfCIR": tmnxTestHdProfCIR,
       "tmnxTestHdProfDurHr": tmnxTestHdProfDurHr,
       "tmnxTestHdProfDurMin": tmnxTestHdProfDurMin,
       "tmnxTestHdProfDurSec": tmnxTestHdProfDurSec,
       "tmnxTestHdProfFrameSize": tmnxTestHdProfFrameSize,
       "tmnxTestHdProfTrapEnable": tmnxTestHdProfTrapEnable,
       "tmnxTestHdLastChanged": tmnxTestHdLastChanged,
       "tmnxTestHdProfAdminCIR": tmnxTestHdProfAdminCIR,
       "tmnxTestHdProfAdminPIR": tmnxTestHdProfAdminPIR,
       "tmnxTestHdProfOperPIR": tmnxTestHdProfOperPIR,
       "tmnxTestHdProfDot1pIn": tmnxTestHdProfDot1pIn,
       "tmnxTestHdProfDot1pOut": tmnxTestHdProfDot1pOut,
       "tmnxTestHdProfActiveTests": tmnxTestHdProfActiveTests,
       "tmnxTestHdProfCompetedTests": tmnxTestHdProfCompetedTests,
       "tmnxTestHdPayLdTable": tmnxTestHdPayLdTable,
       "tmnxTestHdPayLdEntry": tmnxTestHdPayLdEntry,
       "tmnxTestHdPayLdIndex": tmnxTestHdPayLdIndex,
       "tmnxTestHdPayLdRowStatus": tmnxTestHdPayLdRowStatus,
       "tmnxTestHdPayLdDesc": tmnxTestHdPayLdDesc,
       "tmnxTestHdPayLddataPattrn": tmnxTestHdPayLddataPattrn,
       "tmnxTestHdPayLdSrcIpv4Addr": tmnxTestHdPayLdSrcIpv4Addr,
       "tmnxTestHdPayLdDstIpv4Addr": tmnxTestHdPayLdDstIpv4Addr,
       "tmnxTestHdPayLdDSCP": tmnxTestHdPayLdDSCP,
       "tmnxTestHdPayLdIpProto": tmnxTestHdPayLdIpProto,
       "tmnxTestHdPayLdIpTos": tmnxTestHdPayLdIpTos,
       "tmnxTestHdPayLdIpTTL": tmnxTestHdPayLdIpTTL,
       "tmnxTestHdPayLdSrcMac": tmnxTestHdPayLdSrcMac,
       "tmnxTestHdPayLdDstMac": tmnxTestHdPayLdDstMac,
       "tmnxTestHdPayLdSrcPort": tmnxTestHdPayLdSrcPort,
       "tmnxTestHdPayLdDstPort": tmnxTestHdPayLdDstPort,
       "tmnxTestHdPayLdLastChanged": tmnxTestHdPayLdLastChanged,
       "tmnxTestHdPayLdType": tmnxTestHdPayLdType,
       "tmnxTestHdPayLdVTagOne": tmnxTestHdPayLdVTagOne,
       "tmnxTestHdPayLdVTagOneTpid": tmnxTestHdPayLdVTagOneTpid,
       "tmnxTestHdPayLdVTagOneDot1p": tmnxTestHdPayLdVTagOneDot1p,
       "tmnxTestHdPayLdVTagTwo": tmnxTestHdPayLdVTagTwo,
       "tmnxTestHdPayLdVTagTwoTpid": tmnxTestHdPayLdVTagTwoTpid,
       "tmnxTestHdPayLdVTagTwoDot1p": tmnxTestHdPayLdVTagTwoDot1p,
       "tmnxTestHdPayLdEthertype": tmnxTestHdPayLdEthertype,
       "tmnxTestHdAccCritTable": tmnxTestHdAccCritTable,
       "tmnxTestHdAccCritEntry": tmnxTestHdAccCritEntry,
       "tmnxTestHdAccCritIndex": tmnxTestHdAccCritIndex,
       "tmnxTestHdAccCritRowStatus": tmnxTestHdAccCritRowStatus,
       "tmnxTestHdAccCritJittrRiseThres": tmnxTestHdAccCritJittrRiseThres,
       "tmnxTestHdAccCritLatRiseThres": tmnxTestHdAccCritLatRiseThres,
       "tmnxTestHdAccCritLossRiseThres": tmnxTestHdAccCritLossRiseThres,
       "tmnxTestHdAccCritLastChanged": tmnxTestHdAccCritLastChanged,
       "tmnxTestHdAccCritLossRiseThresIn": tmnxTestHdAccCritLossRiseThresIn,
       "tmnxTestHdAccCritLossRiseThresOut": tmnxTestHdAccCritLossRiseThresOut,
       "tmnxTestHdAccCritCirThres": tmnxTestHdAccCritCirThres,
       "tmnxTestHdAccCritPirThres": tmnxTestHdAccCritPirThres,
       "tmnxTestHdAccCritLatRiseThresIn": tmnxTestHdAccCritLatRiseThresIn,
       "tmnxTestHdAccCritLatRiseThresOut": tmnxTestHdAccCritLatRiseThresOut,
       "tmnxTestHdAccCritJittrRiseThresIn": tmnxTestHdAccCritJittrRiseThresIn,
       "tmnxTestHdAccCritJittrRiseThresOut": tmnxTestHdAccCritJittrRiseThresOut,
       "tmnxTestHdSessTable": tmnxTestHdSessTable,
       "tmnxTestHdSessEntry": tmnxTestHdSessEntry,
       "tmnxTestHdSessOwnerName": tmnxTestHdSessOwnerName,
       "tmnxTestHdSessTestName": tmnxTestHdSessTestName,
       "tmnxTestHdSessStartTime": tmnxTestHdSessStartTime,
       "tmnxTestHdSessCompletedTime": tmnxTestHdSessCompletedTime,
       "tmnxTestHdSessTotalTime": tmnxTestHdSessTotalTime,
       "tmnxTestHdSessFc": tmnxTestHdSessFc,
       "tmnxTestHdSessCompleted": tmnxTestHdSessCompleted,
       "tmnxTestHdSessStopped": tmnxTestHdSessStopped,
       "tmnxTestHdSessProfId": tmnxTestHdSessProfId,
       "tmnxTestHdSessPayLdId": tmnxTestHdSessPayLdId,
       "tmnxTestHdSessAccCritId": tmnxTestHdSessAccCritId,
       "tmnxTestHdSessSapPortId": tmnxTestHdSessSapPortId,
       "tmnxTestHdSessSapEncapValue": tmnxTestHdSessSapEncapValue,
       "tmnxTestHdSessTransCount": tmnxTestHdSessTransCount,
       "tmnxTestHdSessRecvCount": tmnxTestHdSessRecvCount,
       "tmnxTestHdSessMinLatency": tmnxTestHdSessMinLatency,
       "tmnxTestHdSessMaxLatency": tmnxTestHdSessMaxLatency,
       "tmnxTestHdSessMeasuredLatency": tmnxTestHdSessMeasuredLatency,
       "tmnxTestHdSessMeasuredJitter": tmnxTestHdSessMeasuredJitter,
       "tmnxTestHdResultsTable": tmnxTestHdResultsTable,
       "tmnxTestHdResultsEntry": tmnxTestHdResultsEntry,
       "tmnxTestHdOwnerName": tmnxTestHdOwnerName,
       "tmnxTestHdTestName": tmnxTestHdTestName,
       "tmnxTestHdResProfId": tmnxTestHdResProfId,
       "tmnxTestHdResProfPayLdId": tmnxTestHdResProfPayLdId,
       "tmnxTestHdResProfAccCritId": tmnxTestHdResProfAccCritId,
       "tmnxTestHdResTransCount": tmnxTestHdResTransCount,
       "tmnxTestHdResRecvCount": tmnxTestHdResRecvCount,
       "tmnxTestHdResMeasuredThruput": tmnxTestHdResMeasuredThruput,
       "tmnxTestHdResMeasuredFLR": tmnxTestHdResMeasuredFLR,
       "tmnxTestHdResMeasuredLatency": tmnxTestHdResMeasuredLatency,
       "tmnxTestHdResLatencyAccptanceResult": tmnxTestHdResLatencyAccptanceResult,
       "tmnxTestHdResMeasuredJitter": tmnxTestHdResMeasuredJitter,
       "tmnxTestHdResJitterAccptanceResult": tmnxTestHdResJitterAccptanceResult,
       "tmnxTestHdResSapPortId": tmnxTestHdResSapPortId,
       "tmnxTestHdResSapEncapValue": tmnxTestHdResSapEncapValue,
       "tmnxTestHdResFLRAccptanceResult": tmnxTestHdResFLRAccptanceResult,
       "tmnxTestHdResMinLatency": tmnxTestHdResMinLatency,
       "tmnxTestHdResMaxLatency": tmnxTestHdResMaxLatency,
       "tmnxTestHdProfScalarObjs": tmnxTestHdProfScalarObjs,
       "tmnxTestHdName": tmnxTestHdName,
       "tmnxTestHdOwner": tmnxTestHdOwner,
       "tmnxTestHdStartTime": tmnxTestHdStartTime,
       "tmnxTestHdElapsedTime": tmnxTestHdElapsedTime,
       "tmnxTestHdFc": tmnxTestHdFc,
       "tmnxTestHdAvgLatency": tmnxTestHdAvgLatency,
       "tmnxTestHdFrLossRatio": tmnxTestHdFrLossRatio,
       "tmnxTestHdJitter": tmnxTestHdJitter,
       "tmnxTestHdDsiredThrpt": tmnxTestHdDsiredThrpt,
       "tmnxTestHdAchvdThrpt": tmnxTestHdAchvdThrpt,
       "tmnxTestHdCompleted": tmnxTestHdCompleted,
       "tmnxTestHdStopped": tmnxTestHdStopped,
       "tmnxTestHdTestStatus": tmnxTestHdTestStatus,
       "tmnxTestHdCompletedTime": tmnxTestHdCompletedTime,
       "tmnxTestHdSapPortId": tmnxTestHdSapPortId,
       "tmnxTestHdSapEncapValue": tmnxTestHdSapEncapValue,
       "tmnxTestHdAdminStatus": tmnxTestHdAdminStatus,
       "tmnxTestHdProfId": tmnxTestHdProfId,
       "tmnxTestHdAccCritId": tmnxTestHdAccCritId,
       "tmnxTestHdPayLdId": tmnxTestHdPayLdId,
       "tmnxTestHdColorAware": tmnxTestHdColorAware,
       "tmnxTestHdProfNotifyObjs": tmnxTestHdProfNotifyObjs,
       "tmnxSASOamNotifyPrefix": tmnxSASOamNotifyPrefix,
       "tmnxSASOamNotifications": tmnxSASOamNotifications,
       "tmnxOamTestHeadTestCompleted": tmnxOamTestHeadTestCompleted}
)
