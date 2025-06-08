# SNMP MIB module (TIMETRA-PIM-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-PIM-NG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:40 2025
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardHwIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardHwIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxMcacLagPortsDown,
 tmnxMcacLevelId) = mibBuilder.importSymbols(
    "TIMETRA-MCAST-CAC-MIB",
    "tmnxMcacLagPortsDown",
    "tmnxMcacLevelId")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(IpAddressPrefixLength,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxMulticastAddrFamily,
 TmnxOperState,
 TmnxServId,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxMulticastAddrFamily",
    "TmnxOperState",
    "TmnxServId",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraPimNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 50)
)
if mibBuilder.loadTexts:
    timetraPimNgMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxPimNgConformance_ObjectIdentity = ObjectIdentity
tmnxPimNgConformance = _TmnxPimNgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50)
)
_TmnxPimNgCompliances_ObjectIdentity = ObjectIdentity
tmnxPimNgCompliances = _TmnxPimNgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1)
)
_TmnxPimNgGroups_ObjectIdentity = ObjectIdentity
tmnxPimNgGroups = _TmnxPimNgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2)
)
_TmnxPimNgObjs_ObjectIdentity = ObjectIdentity
tmnxPimNgObjs = _TmnxPimNgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50)
)
_VRtrPimNgProtocolObjs_ObjectIdentity = ObjectIdentity
vRtrPimNgProtocolObjs = _VRtrPimNgProtocolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1)
)
_VRtrPimNgGeneralTableLstChanged_Type = TimeStamp
_VRtrPimNgGeneralTableLstChanged_Object = MibScalar
vRtrPimNgGeneralTableLstChanged = _VRtrPimNgGeneralTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 1),
    _VRtrPimNgGeneralTableLstChanged_Type()
)
vRtrPimNgGeneralTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGeneralTableLstChanged.setStatus("current")
_VRtrPimNgGeneralTable_Object = MibTable
vRtrPimNgGeneralTable = _VRtrPimNgGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2)
)
if mibBuilder.loadTexts:
    vRtrPimNgGeneralTable.setStatus("current")
_VRtrPimNgGeneralEntry_Object = MibTableRow
vRtrPimNgGeneralEntry = _VRtrPimNgGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1)
)
vRtrPimNgGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrPimNgGeneralEntry.setStatus("current")
_VRtrPimNgGenRowLastChanged_Type = TimeStamp
_VRtrPimNgGenRowLastChanged_Object = MibTableColumn
vRtrPimNgGenRowLastChanged = _VRtrPimNgGenRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 1),
    _VRtrPimNgGenRowLastChanged_Type()
)
vRtrPimNgGenRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenRowLastChanged.setStatus("current")


class _VRtrPimNgGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgGenAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrPimNgGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgGenAdminState_Object = MibTableColumn
vRtrPimNgGenAdminState = _VRtrPimNgGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 2),
    _VRtrPimNgGenAdminState_Type()
)
vRtrPimNgGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenAdminState.setStatus("current")
_VRtrPimNgGenOperState_Type = TmnxOperState
_VRtrPimNgGenOperState_Object = MibTableColumn
vRtrPimNgGenOperState = _VRtrPimNgGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 3),
    _VRtrPimNgGenOperState_Type()
)
vRtrPimNgGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenOperState.setStatus("current")


class _VRtrPimNgGenCreateInterfaces_Type(Integer32):
    """Custom type vRtrPimNgGenCreateInterfaces based on Integer32"""
    defaultValue = 4

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
        *(("ies", 1),
          ("non-ies", 2),
          ("all", 3),
          ("none", 4))
    )


_VRtrPimNgGenCreateInterfaces_Type.__name__ = "Integer32"
_VRtrPimNgGenCreateInterfaces_Object = MibTableColumn
vRtrPimNgGenCreateInterfaces = _VRtrPimNgGenCreateInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 4),
    _VRtrPimNgGenCreateInterfaces_Type()
)
vRtrPimNgGenCreateInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenCreateInterfaces.setStatus("current")
_VRtrPimNgGenMaxMdts_Type = Integer32
_VRtrPimNgGenMaxMdts_Object = MibTableColumn
vRtrPimNgGenMaxMdts = _VRtrPimNgGenMaxMdts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 5),
    _VRtrPimNgGenMaxMdts_Type()
)
vRtrPimNgGenMaxMdts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenMaxMdts.setStatus("current")


class _VRtrPimNgGenNonDrAttractTraffic_Type(TruthValue):
    """Custom type vRtrPimNgGenNonDrAttractTraffic based on TruthValue"""
    defaultValue = 2


_VRtrPimNgGenNonDrAttractTraffic_Type.__name__ = "TruthValue"
_VRtrPimNgGenNonDrAttractTraffic_Object = MibTableColumn
vRtrPimNgGenNonDrAttractTraffic = _VRtrPimNgGenNonDrAttractTraffic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 6),
    _VRtrPimNgGenNonDrAttractTraffic_Type()
)
vRtrPimNgGenNonDrAttractTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenNonDrAttractTraffic.setStatus("current")


class _VRtrPimNgGenEcmpBalance_Type(TruthValue):
    """Custom type vRtrPimNgGenEcmpBalance based on TruthValue"""
    defaultValue = 1


_VRtrPimNgGenEcmpBalance_Type.__name__ = "TruthValue"
_VRtrPimNgGenEcmpBalance_Object = MibTableColumn
vRtrPimNgGenEcmpBalance = _VRtrPimNgGenEcmpBalance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 7),
    _VRtrPimNgGenEcmpBalance_Type()
)
vRtrPimNgGenEcmpBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpBalance.setStatus("current")


class _VRtrPimNgGenEcmpBalanceHoldTime_Type(Unsigned32):
    """Custom type vRtrPimNgGenEcmpBalanceHoldTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrPimNgGenEcmpBalanceHoldTime_Type.__name__ = "Unsigned32"
_VRtrPimNgGenEcmpBalanceHoldTime_Object = MibTableColumn
vRtrPimNgGenEcmpBalanceHoldTime = _VRtrPimNgGenEcmpBalanceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 8),
    _VRtrPimNgGenEcmpBalanceHoldTime_Type()
)
vRtrPimNgGenEcmpBalanceHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpBalanceHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpBalanceHoldTime.setUnits("minutes")
_VRtrPimNgGenEcmpReBlncInProg_Type = TruthValue
_VRtrPimNgGenEcmpReBlncInProg_Object = MibTableColumn
vRtrPimNgGenEcmpReBlncInProg = _VRtrPimNgGenEcmpReBlncInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 9),
    _VRtrPimNgGenEcmpReBlncInProg_Type()
)
vRtrPimNgGenEcmpReBlncInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpReBlncInProg.setStatus("current")
_VRtrPimNgGenEcmpLastReBlncTime_Type = TimeStamp
_VRtrPimNgGenEcmpLastReBlncTime_Object = MibTableColumn
vRtrPimNgGenEcmpLastReBlncTime = _VRtrPimNgGenEcmpLastReBlncTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 10),
    _VRtrPimNgGenEcmpLastReBlncTime_Type()
)
vRtrPimNgGenEcmpLastReBlncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpLastReBlncTime.setStatus("current")


class _VRtrPimNgGenEcmpRebalanceType_Type(Integer32):
    """Custom type vRtrPimNgGenEcmpRebalanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggered", 1),
          ("operatorForced", 2))
    )


_VRtrPimNgGenEcmpRebalanceType_Type.__name__ = "Integer32"
_VRtrPimNgGenEcmpRebalanceType_Object = MibTableColumn
vRtrPimNgGenEcmpRebalanceType = _VRtrPimNgGenEcmpRebalanceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 11),
    _VRtrPimNgGenEcmpRebalanceType_Type()
)
vRtrPimNgGenEcmpRebalanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpRebalanceType.setStatus("current")
_VRtrPimNgGenEcmpOptThreshold_Type = Unsigned32
_VRtrPimNgGenEcmpOptThreshold_Object = MibTableColumn
vRtrPimNgGenEcmpOptThreshold = _VRtrPimNgGenEcmpOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 12),
    _VRtrPimNgGenEcmpOptThreshold_Type()
)
vRtrPimNgGenEcmpOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpOptThreshold.setStatus("obsolete")


class _VRtrPimNgGenEcmpNextBalanceTime_Type(Unsigned32):
    """Custom type vRtrPimNgGenEcmpNextBalanceTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_VRtrPimNgGenEcmpNextBalanceTime_Type.__name__ = "Unsigned32"
_VRtrPimNgGenEcmpNextBalanceTime_Object = MibTableColumn
vRtrPimNgGenEcmpNextBalanceTime = _VRtrPimNgGenEcmpNextBalanceTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 13),
    _VRtrPimNgGenEcmpNextBalanceTime_Type()
)
vRtrPimNgGenEcmpNextBalanceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpNextBalanceTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpNextBalanceTime.setUnits("seconds")


class _VRtrPimNgGenLagUsageOptimize_Type(TruthValue):
    """Custom type vRtrPimNgGenLagUsageOptimize based on TruthValue"""
    defaultValue = 2


_VRtrPimNgGenLagUsageOptimize_Type.__name__ = "TruthValue"
_VRtrPimNgGenLagUsageOptimize_Object = MibTableColumn
vRtrPimNgGenLagUsageOptimize = _VRtrPimNgGenLagUsageOptimize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 14),
    _VRtrPimNgGenLagUsageOptimize_Type()
)
vRtrPimNgGenLagUsageOptimize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenLagUsageOptimize.setStatus("current")


class _VRtrPimNgGenEcmpHashingEnabled_Type(TruthValue):
    """Custom type vRtrPimNgGenEcmpHashingEnabled based on TruthValue"""
    defaultValue = 2


_VRtrPimNgGenEcmpHashingEnabled_Type.__name__ = "TruthValue"
_VRtrPimNgGenEcmpHashingEnabled_Object = MibTableColumn
vRtrPimNgGenEcmpHashingEnabled = _VRtrPimNgGenEcmpHashingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 15),
    _VRtrPimNgGenEcmpHashingEnabled_Type()
)
vRtrPimNgGenEcmpHashingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenEcmpHashingEnabled.setStatus("current")


class _VRtrPimNgGenEnableMdtSpt_Type(TruthValue):
    """Custom type vRtrPimNgGenEnableMdtSpt based on TruthValue"""
    defaultValue = 2


_VRtrPimNgGenEnableMdtSpt_Type.__name__ = "TruthValue"
_VRtrPimNgGenEnableMdtSpt_Object = MibTableColumn
vRtrPimNgGenEnableMdtSpt = _VRtrPimNgGenEnableMdtSpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 16),
    _VRtrPimNgGenEnableMdtSpt_Type()
)
vRtrPimNgGenEnableMdtSpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenEnableMdtSpt.setStatus("current")


class _VRtrPimNgGenRpfVectorFlags_Type(Bits):
    """Custom type vRtrPimNgGenRpfVectorFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("mvpn", 0),
          ("core", 1))
    )

_VRtrPimNgGenRpfVectorFlags_Type.__name__ = "Bits"
_VRtrPimNgGenRpfVectorFlags_Object = MibTableColumn
vRtrPimNgGenRpfVectorFlags = _VRtrPimNgGenRpfVectorFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 2, 1, 17),
    _VRtrPimNgGenRpfVectorFlags_Type()
)
vRtrPimNgGenRpfVectorFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgGenRpfVectorFlags.setStatus("current")
_VRtrPimNgAFGenTableLstChanged_Type = TimeStamp
_VRtrPimNgAFGenTableLstChanged_Object = MibScalar
vRtrPimNgAFGenTableLstChanged = _VRtrPimNgAFGenTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 3),
    _VRtrPimNgAFGenTableLstChanged_Type()
)
vRtrPimNgAFGenTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenTableLstChanged.setStatus("current")
_VRtrPimNgAFGenTable_Object = MibTable
vRtrPimNgAFGenTable = _VRtrPimNgAFGenTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4)
)
if mibBuilder.loadTexts:
    vRtrPimNgAFGenTable.setStatus("current")
_VRtrPimNgAFGenEntry_Object = MibTableRow
vRtrPimNgAFGenEntry = _VRtrPimNgAFGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1)
)
vRtrPimNgAFGenEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    vRtrPimNgAFGenEntry.setStatus("current")
_VRtrPimNgAFGenAFType_Type = TmnxMulticastAddrFamily
_VRtrPimNgAFGenAFType_Object = MibTableColumn
vRtrPimNgAFGenAFType = _VRtrPimNgAFGenAFType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 1),
    _VRtrPimNgAFGenAFType_Type()
)
vRtrPimNgAFGenAFType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenAFType.setStatus("current")


class _VRtrPimNgAFGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgAFGenAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrPimNgAFGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgAFGenAdminState_Object = MibTableColumn
vRtrPimNgAFGenAdminState = _VRtrPimNgAFGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 2),
    _VRtrPimNgAFGenAdminState_Type()
)
vRtrPimNgAFGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenAdminState.setStatus("current")
_VRtrPimNgAFGenOperState_Type = TmnxOperState
_VRtrPimNgAFGenOperState_Object = MibTableColumn
vRtrPimNgAFGenOperState = _VRtrPimNgAFGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 3),
    _VRtrPimNgAFGenOperState_Type()
)
vRtrPimNgAFGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenOperState.setStatus("current")


class _VRtrPimNgAFGenCBSRPriority_Type(Integer32):
    """Custom type vRtrPimNgAFGenCBSRPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimNgAFGenCBSRPriority_Type.__name__ = "Integer32"
_VRtrPimNgAFGenCBSRPriority_Object = MibTableColumn
vRtrPimNgAFGenCBSRPriority = _VRtrPimNgAFGenCBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 4),
    _VRtrPimNgAFGenCBSRPriority_Type()
)
vRtrPimNgAFGenCBSRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCBSRPriority.setStatus("current")
_VRtrPimNgAFGenCBSRAddressType_Type = InetAddressType
_VRtrPimNgAFGenCBSRAddressType_Object = MibTableColumn
vRtrPimNgAFGenCBSRAddressType = _VRtrPimNgAFGenCBSRAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 5),
    _VRtrPimNgAFGenCBSRAddressType_Type()
)
vRtrPimNgAFGenCBSRAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCBSRAddressType.setStatus("current")


class _VRtrPimNgAFGenCBSRAddress_Type(InetAddress):
    """Custom type vRtrPimNgAFGenCBSRAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFGenCBSRAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAFGenCBSRAddress_Object = MibTableColumn
vRtrPimNgAFGenCBSRAddress = _VRtrPimNgAFGenCBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 6),
    _VRtrPimNgAFGenCBSRAddress_Type()
)
vRtrPimNgAFGenCBSRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCBSRAddress.setStatus("current")


class _VRtrPimNgAFGenCBSRAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgAFGenCBSRAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrPimNgAFGenCBSRAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgAFGenCBSRAdminState_Object = MibTableColumn
vRtrPimNgAFGenCBSRAdminState = _VRtrPimNgAFGenCBSRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 7),
    _VRtrPimNgAFGenCBSRAdminState_Type()
)
vRtrPimNgAFGenCBSRAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCBSRAdminState.setStatus("current")
_VRtrPimNgAFGenCBSROperState_Type = TmnxOperState
_VRtrPimNgAFGenCBSROperState_Object = MibTableColumn
vRtrPimNgAFGenCBSROperState = _VRtrPimNgAFGenCBSROperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 8),
    _VRtrPimNgAFGenCBSROperState_Type()
)
vRtrPimNgAFGenCBSROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCBSROperState.setStatus("current")
_VRtrPimNgAFGenBSRAddressType_Type = InetAddressType
_VRtrPimNgAFGenBSRAddressType_Object = MibTableColumn
vRtrPimNgAFGenBSRAddressType = _VRtrPimNgAFGenBSRAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 9),
    _VRtrPimNgAFGenBSRAddressType_Type()
)
vRtrPimNgAFGenBSRAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRAddressType.setStatus("current")


class _VRtrPimNgAFGenBSRAddress_Type(InetAddress):
    """Custom type vRtrPimNgAFGenBSRAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFGenBSRAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAFGenBSRAddress_Object = MibTableColumn
vRtrPimNgAFGenBSRAddress = _VRtrPimNgAFGenBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 10),
    _VRtrPimNgAFGenBSRAddress_Type()
)
vRtrPimNgAFGenBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRAddress.setStatus("current")


class _VRtrPimNgAFGenBSRPriority_Type(Integer32):
    """Custom type vRtrPimNgAFGenBSRPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimNgAFGenBSRPriority_Type.__name__ = "Integer32"
_VRtrPimNgAFGenBSRPriority_Object = MibTableColumn
vRtrPimNgAFGenBSRPriority = _VRtrPimNgAFGenBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 11),
    _VRtrPimNgAFGenBSRPriority_Type()
)
vRtrPimNgAFGenBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRPriority.setStatus("current")
_VRtrPimNgAFGenBSRExpiryTime_Type = Unsigned32
_VRtrPimNgAFGenBSRExpiryTime_Object = MibTableColumn
vRtrPimNgAFGenBSRExpiryTime = _VRtrPimNgAFGenBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 12),
    _VRtrPimNgAFGenBSRExpiryTime_Type()
)
vRtrPimNgAFGenBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRExpiryTime.setUnits("seconds")


class _VRtrPimNgAFGenBSRState_Type(Integer32):
    """Custom type vRtrPimNgAFGenBSRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("candidateBSR", 1),
          ("pendingBSR", 2),
          ("electedBSR", 3),
          ("acceptAny", 4),
          ("acceptPreferred", 5))
    )


_VRtrPimNgAFGenBSRState_Type.__name__ = "Integer32"
_VRtrPimNgAFGenBSRState_Object = MibTableColumn
vRtrPimNgAFGenBSRState = _VRtrPimNgAFGenBSRState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 13),
    _VRtrPimNgAFGenBSRState_Type()
)
vRtrPimNgAFGenBSRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRState.setStatus("current")
_VRtrPimNgAFGenBSRUpTime_Type = Unsigned32
_VRtrPimNgAFGenBSRUpTime_Object = MibTableColumn
vRtrPimNgAFGenBSRUpTime = _VRtrPimNgAFGenBSRUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 14),
    _VRtrPimNgAFGenBSRUpTime_Type()
)
vRtrPimNgAFGenBSRUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRUpTime.setUnits("seconds")
_VRtrPimNgAFGenCRPAddressType_Type = InetAddressType
_VRtrPimNgAFGenCRPAddressType_Object = MibTableColumn
vRtrPimNgAFGenCRPAddressType = _VRtrPimNgAFGenCRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 15),
    _VRtrPimNgAFGenCRPAddressType_Type()
)
vRtrPimNgAFGenCRPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCRPAddressType.setStatus("current")


class _VRtrPimNgAFGenCRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgAFGenCRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFGenCRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAFGenCRPAddress_Object = MibTableColumn
vRtrPimNgAFGenCRPAddress = _VRtrPimNgAFGenCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 16),
    _VRtrPimNgAFGenCRPAddress_Type()
)
vRtrPimNgAFGenCRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCRPAddress.setStatus("current")


class _VRtrPimNgAFGenCRPAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgAFGenCRPAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrPimNgAFGenCRPAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgAFGenCRPAdminState_Object = MibTableColumn
vRtrPimNgAFGenCRPAdminState = _VRtrPimNgAFGenCRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 17),
    _VRtrPimNgAFGenCRPAdminState_Type()
)
vRtrPimNgAFGenCRPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCRPAdminState.setStatus("current")
_VRtrPimNgAFGenCRPOperState_Type = TmnxOperState
_VRtrPimNgAFGenCRPOperState_Object = MibTableColumn
vRtrPimNgAFGenCRPOperState = _VRtrPimNgAFGenCRPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 18),
    _VRtrPimNgAFGenCRPOperState_Type()
)
vRtrPimNgAFGenCRPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCRPOperState.setStatus("current")


class _VRtrPimNgAFGenCRPHoldtime_Type(Integer32):
    """Custom type vRtrPimNgAFGenCRPHoldtime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_VRtrPimNgAFGenCRPHoldtime_Type.__name__ = "Integer32"
_VRtrPimNgAFGenCRPHoldtime_Object = MibTableColumn
vRtrPimNgAFGenCRPHoldtime = _VRtrPimNgAFGenCRPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 19),
    _VRtrPimNgAFGenCRPHoldtime_Type()
)
vRtrPimNgAFGenCRPHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCRPHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCRPHoldtime.setUnits("seconds")


class _VRtrPimNgAFGenCRPPriority_Type(Integer32):
    """Custom type vRtrPimNgAFGenCRPPriority based on Integer32"""
    defaultValue = 192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimNgAFGenCRPPriority_Type.__name__ = "Integer32"
_VRtrPimNgAFGenCRPPriority_Object = MibTableColumn
vRtrPimNgAFGenCRPPriority = _VRtrPimNgAFGenCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 20),
    _VRtrPimNgAFGenCRPPriority_Type()
)
vRtrPimNgAFGenCRPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCRPPriority.setStatus("current")
_VRtrPimNgAFGenMdtDefGrpAddrType_Type = InetAddressType
_VRtrPimNgAFGenMdtDefGrpAddrType_Object = MibTableColumn
vRtrPimNgAFGenMdtDefGrpAddrType = _VRtrPimNgAFGenMdtDefGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 21),
    _VRtrPimNgAFGenMdtDefGrpAddrType_Type()
)
vRtrPimNgAFGenMdtDefGrpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDefGrpAddrType.setStatus("current")


class _VRtrPimNgAFGenMdtDefGrpAddress_Type(InetAddress):
    """Custom type vRtrPimNgAFGenMdtDefGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFGenMdtDefGrpAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAFGenMdtDefGrpAddress_Object = MibTableColumn
vRtrPimNgAFGenMdtDefGrpAddress = _VRtrPimNgAFGenMdtDefGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 22),
    _VRtrPimNgAFGenMdtDefGrpAddress_Type()
)
vRtrPimNgAFGenMdtDefGrpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDefGrpAddress.setStatus("current")
_VRtrPimNgAFGenMTIfIndex_Type = InterfaceIndexOrZero
_VRtrPimNgAFGenMTIfIndex_Object = MibTableColumn
vRtrPimNgAFGenMTIfIndex = _VRtrPimNgAFGenMTIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 23),
    _VRtrPimNgAFGenMTIfIndex_Type()
)
vRtrPimNgAFGenMTIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMTIfIndex.setStatus("current")


class _VRtrPimNgAFGenCBSRHashMaskLen_Type(Integer32):
    """Custom type vRtrPimNgAFGenCBSRHashMaskLen based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrPimNgAFGenCBSRHashMaskLen_Type.__name__ = "Integer32"
_VRtrPimNgAFGenCBSRHashMaskLen_Object = MibTableColumn
vRtrPimNgAFGenCBSRHashMaskLen = _VRtrPimNgAFGenCBSRHashMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 24),
    _VRtrPimNgAFGenCBSRHashMaskLen_Type()
)
vRtrPimNgAFGenCBSRHashMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenCBSRHashMaskLen.setStatus("current")
_VRtrPimNgAFGenBSRHashMaskLen_Type = Integer32
_VRtrPimNgAFGenBSRHashMaskLen_Object = MibTableColumn
vRtrPimNgAFGenBSRHashMaskLen = _VRtrPimNgAFGenBSRHashMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 25),
    _VRtrPimNgAFGenBSRHashMaskLen_Type()
)
vRtrPimNgAFGenBSRHashMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRHashMaskLen.setStatus("current")
_VRtrPimNgAFGenBSRRpfIfIndex_Type = InterfaceIndexOrZero
_VRtrPimNgAFGenBSRRpfIfIndex_Object = MibTableColumn
vRtrPimNgAFGenBSRRpfIfIndex = _VRtrPimNgAFGenBSRRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 26),
    _VRtrPimNgAFGenBSRRpfIfIndex_Type()
)
vRtrPimNgAFGenBSRRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenBSRRpfIfIndex.setStatus("current")


class _VRtrPimNgAFGenRpfLookupSequence_Type(Integer32):
    """Custom type vRtrPimNgAFGenRpfLookupSequence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mucastRouteTable", 0),
          ("ucastRouteTable", 1),
          ("both", 2))
    )


_VRtrPimNgAFGenRpfLookupSequence_Type.__name__ = "Integer32"
_VRtrPimNgAFGenRpfLookupSequence_Object = MibTableColumn
vRtrPimNgAFGenRpfLookupSequence = _VRtrPimNgAFGenRpfLookupSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 27),
    _VRtrPimNgAFGenRpfLookupSequence_Type()
)
vRtrPimNgAFGenRpfLookupSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenRpfLookupSequence.setStatus("current")


class _VRtrPimNgAFGenMdtDataPrefixType_Type(InetAddressType):
    """Custom type vRtrPimNgAFGenMdtDataPrefixType based on InetAddressType"""
    defaultValue = 0


_VRtrPimNgAFGenMdtDataPrefixType_Type.__name__ = "InetAddressType"
_VRtrPimNgAFGenMdtDataPrefixType_Object = MibTableColumn
vRtrPimNgAFGenMdtDataPrefixType = _VRtrPimNgAFGenMdtDataPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 28),
    _VRtrPimNgAFGenMdtDataPrefixType_Type()
)
vRtrPimNgAFGenMdtDataPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDataPrefixType.setStatus("current")


class _VRtrPimNgAFGenMdtDataPrefix_Type(InetAddress):
    """Custom type vRtrPimNgAFGenMdtDataPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFGenMdtDataPrefix_Type.__name__ = "InetAddress"
_VRtrPimNgAFGenMdtDataPrefix_Object = MibTableColumn
vRtrPimNgAFGenMdtDataPrefix = _VRtrPimNgAFGenMdtDataPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 29),
    _VRtrPimNgAFGenMdtDataPrefix_Type()
)
vRtrPimNgAFGenMdtDataPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDataPrefix.setStatus("current")


class _VRtrPimNgAFGenMdtDataPrefixMask_Type(InetAddressPrefixLength):
    """Custom type vRtrPimNgAFGenMdtDataPrefixMask based on InetAddressPrefixLength"""
    defaultValue = 0


_VRtrPimNgAFGenMdtDataPrefixMask_Type.__name__ = "InetAddressPrefixLength"
_VRtrPimNgAFGenMdtDataPrefixMask_Object = MibTableColumn
vRtrPimNgAFGenMdtDataPrefixMask = _VRtrPimNgAFGenMdtDataPrefixMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 30),
    _VRtrPimNgAFGenMdtDataPrefixMask_Type()
)
vRtrPimNgAFGenMdtDataPrefixMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDataPrefixMask.setStatus("current")


class _VRtrPimNgAFGenMdtDataDlayIntrvl_Type(Unsigned32):
    """Custom type vRtrPimNgAFGenMdtDataDlayIntrvl based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 180),
    )


_VRtrPimNgAFGenMdtDataDlayIntrvl_Type.__name__ = "Unsigned32"
_VRtrPimNgAFGenMdtDataDlayIntrvl_Object = MibTableColumn
vRtrPimNgAFGenMdtDataDlayIntrvl = _VRtrPimNgAFGenMdtDataDlayIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 31),
    _VRtrPimNgAFGenMdtDataDlayIntrvl_Type()
)
vRtrPimNgAFGenMdtDataDlayIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDataDlayIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDataDlayIntrvl.setUnits("seconds")


class _VRtrPimNgAFGenMdtDataJoinTlvPck_Type(TruthValue):
    """Custom type vRtrPimNgAFGenMdtDataJoinTlvPck based on TruthValue"""
    defaultValue = 1


_VRtrPimNgAFGenMdtDataJoinTlvPck_Type.__name__ = "TruthValue"
_VRtrPimNgAFGenMdtDataJoinTlvPck_Object = MibTableColumn
vRtrPimNgAFGenMdtDataJoinTlvPck = _VRtrPimNgAFGenMdtDataJoinTlvPck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 32),
    _VRtrPimNgAFGenMdtDataJoinTlvPck_Type()
)
vRtrPimNgAFGenMdtDataJoinTlvPck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDataJoinTlvPck.setStatus("current")
_VRtrPimNgAFGenRowLastChanged_Type = TimeStamp
_VRtrPimNgAFGenRowLastChanged_Object = MibTableColumn
vRtrPimNgAFGenRowLastChanged = _VRtrPimNgAFGenRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 33),
    _VRtrPimNgAFGenRowLastChanged_Type()
)
vRtrPimNgAFGenRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenRowLastChanged.setStatus("current")


class _VRtrPimNgAFGenERP_Type(TruthValue):
    """Custom type vRtrPimNgAFGenERP based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAFGenERP_Type.__name__ = "TruthValue"
_VRtrPimNgAFGenERP_Object = MibTableColumn
vRtrPimNgAFGenERP = _VRtrPimNgAFGenERP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 34),
    _VRtrPimNgAFGenERP_Type()
)
vRtrPimNgAFGenERP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenERP.setStatus("current")


class _VRtrPimNgAFGenERPAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgAFGenERPAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrPimNgAFGenERPAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgAFGenERPAdminState_Object = MibTableColumn
vRtrPimNgAFGenERPAdminState = _VRtrPimNgAFGenERPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 35),
    _VRtrPimNgAFGenERPAdminState_Type()
)
vRtrPimNgAFGenERPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenERPAdminState.setStatus("current")


class _VRtrPimNgAFGenMvpnAutoDiscovery_Type(TruthValue):
    """Custom type vRtrPimNgAFGenMvpnAutoDiscovery based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAFGenMvpnAutoDiscovery_Type.__name__ = "TruthValue"
_VRtrPimNgAFGenMvpnAutoDiscovery_Object = MibTableColumn
vRtrPimNgAFGenMvpnAutoDiscovery = _VRtrPimNgAFGenMvpnAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 36),
    _VRtrPimNgAFGenMvpnAutoDiscovery_Type()
)
vRtrPimNgAFGenMvpnAutoDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMvpnAutoDiscovery.setStatus("obsolete")


class _VRtrPimNgAFGenMvpnCMcastSignal_Type(Integer32):
    """Custom type vRtrPimNgAFGenMvpnCMcastSignal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 0),
          ("pim", 1))
    )


_VRtrPimNgAFGenMvpnCMcastSignal_Type.__name__ = "Integer32"
_VRtrPimNgAFGenMvpnCMcastSignal_Object = MibTableColumn
vRtrPimNgAFGenMvpnCMcastSignal = _VRtrPimNgAFGenMvpnCMcastSignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 37),
    _VRtrPimNgAFGenMvpnCMcastSignal_Type()
)
vRtrPimNgAFGenMvpnCMcastSignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMvpnCMcastSignal.setStatus("current")


class _VRtrPimNgAFGenMvpnGrpAddrMode_Type(Integer32):
    """Custom type vRtrPimNgAFGenMvpnGrpAddrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("asm", 1),
          ("ssm", 2))
    )


_VRtrPimNgAFGenMvpnGrpAddrMode_Type.__name__ = "Integer32"
_VRtrPimNgAFGenMvpnGrpAddrMode_Object = MibTableColumn
vRtrPimNgAFGenMvpnGrpAddrMode = _VRtrPimNgAFGenMvpnGrpAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 38),
    _VRtrPimNgAFGenMvpnGrpAddrMode_Type()
)
vRtrPimNgAFGenMvpnGrpAddrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMvpnGrpAddrMode.setStatus("current")


class _VRtrPimNgAFGenMvpnSpmsiAutoDisc_Type(TruthValue):
    """Custom type vRtrPimNgAFGenMvpnSpmsiAutoDisc based on TruthValue"""
    defaultValue = 1


_VRtrPimNgAFGenMvpnSpmsiAutoDisc_Type.__name__ = "TruthValue"
_VRtrPimNgAFGenMvpnSpmsiAutoDisc_Object = MibTableColumn
vRtrPimNgAFGenMvpnSpmsiAutoDisc = _VRtrPimNgAFGenMvpnSpmsiAutoDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 39),
    _VRtrPimNgAFGenMvpnSpmsiAutoDisc_Type()
)
vRtrPimNgAFGenMvpnSpmsiAutoDisc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMvpnSpmsiAutoDisc.setStatus("current")


class _VRtrPimNgAFGenMvpnUMHSelection_Type(Integer32):
    """Custom type vRtrPimNgAFGenMvpnUMHSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highestip", 0),
          ("hashbased", 1),
          ("tunnelstatus", 2),
          ("unicastRtPref", 3))
    )


_VRtrPimNgAFGenMvpnUMHSelection_Type.__name__ = "Integer32"
_VRtrPimNgAFGenMvpnUMHSelection_Object = MibTableColumn
vRtrPimNgAFGenMvpnUMHSelection = _VRtrPimNgAFGenMvpnUMHSelection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 40),
    _VRtrPimNgAFGenMvpnUMHSelection_Type()
)
vRtrPimNgAFGenMvpnUMHSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMvpnUMHSelection.setStatus("current")


class _VRtrPimNgAFGenMvpnIntersiteShrd_Type(TmnxEnabledDisabled):
    """Custom type vRtrPimNgAFGenMvpnIntersiteShrd based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrPimNgAFGenMvpnIntersiteShrd_Type.__name__ = "TmnxEnabledDisabled"
_VRtrPimNgAFGenMvpnIntersiteShrd_Object = MibTableColumn
vRtrPimNgAFGenMvpnIntersiteShrd = _VRtrPimNgAFGenMvpnIntersiteShrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 41),
    _VRtrPimNgAFGenMvpnIntersiteShrd_Type()
)
vRtrPimNgAFGenMvpnIntersiteShrd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMvpnIntersiteShrd.setStatus("current")


class _VRtrPimNgAFGenSSMDefRangeDisabl_Type(TruthValue):
    """Custom type vRtrPimNgAFGenSSMDefRangeDisabl based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAFGenSSMDefRangeDisabl_Type.__name__ = "TruthValue"
_VRtrPimNgAFGenSSMDefRangeDisabl_Object = MibTableColumn
vRtrPimNgAFGenSSMDefRangeDisabl = _VRtrPimNgAFGenSSMDefRangeDisabl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 42),
    _VRtrPimNgAFGenSSMDefRangeDisabl_Type()
)
vRtrPimNgAFGenSSMDefRangeDisabl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenSSMDefRangeDisabl.setStatus("current")


class _VRtrPimNgAFGenMvpnAD_Type(Integer32):
    """Custom type vRtrPimNgAFGenMvpnAD based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("default", 1),
          ("mdtSafi", 2))
    )


_VRtrPimNgAFGenMvpnAD_Type.__name__ = "Integer32"
_VRtrPimNgAFGenMvpnAD_Object = MibTableColumn
vRtrPimNgAFGenMvpnAD = _VRtrPimNgAFGenMvpnAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 43),
    _VRtrPimNgAFGenMvpnAD_Type()
)
vRtrPimNgAFGenMvpnAD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMvpnAD.setStatus("current")


class _VRtrPimNgAFGenMdtDataGrpAddrMode_Type(Integer32):
    """Custom type vRtrPimNgAFGenMdtDataGrpAddrMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("asm", 1),
          ("ssm", 2))
    )


_VRtrPimNgAFGenMdtDataGrpAddrMode_Type.__name__ = "Integer32"
_VRtrPimNgAFGenMdtDataGrpAddrMode_Object = MibTableColumn
vRtrPimNgAFGenMdtDataGrpAddrMode = _VRtrPimNgAFGenMdtDataGrpAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 44),
    _VRtrPimNgAFGenMdtDataGrpAddrMode_Type()
)
vRtrPimNgAFGenMdtDataGrpAddrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenMdtDataGrpAddrMode.setStatus("current")


class _VRtrPimNgAFGenEnableAsmDataMdt_Type(TruthValue):
    """Custom type vRtrPimNgAFGenEnableAsmDataMdt based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAFGenEnableAsmDataMdt_Type.__name__ = "TruthValue"
_VRtrPimNgAFGenEnableAsmDataMdt_Object = MibTableColumn
vRtrPimNgAFGenEnableAsmDataMdt = _VRtrPimNgAFGenEnableAsmDataMdt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 45),
    _VRtrPimNgAFGenEnableAsmDataMdt_Type()
)
vRtrPimNgAFGenEnableAsmDataMdt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenEnableAsmDataMdt.setStatus("current")


class _VRtrPimNgAfGenAutoRPDiscovery_Type(TruthValue):
    """Custom type vRtrPimNgAfGenAutoRPDiscovery based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAfGenAutoRPDiscovery_Type.__name__ = "TruthValue"
_VRtrPimNgAfGenAutoRPDiscovery_Object = MibTableColumn
vRtrPimNgAfGenAutoRPDiscovery = _VRtrPimNgAfGenAutoRPDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 46),
    _VRtrPimNgAfGenAutoRPDiscovery_Type()
)
vRtrPimNgAfGenAutoRPDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAfGenAutoRPDiscovery.setStatus("current")


class _VRtrPimNgAfGenSSMAsrtCompMode_Type(TruthValue):
    """Custom type vRtrPimNgAfGenSSMAsrtCompMode based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAfGenSSMAsrtCompMode_Type.__name__ = "TruthValue"
_VRtrPimNgAfGenSSMAsrtCompMode_Object = MibTableColumn
vRtrPimNgAfGenSSMAsrtCompMode = _VRtrPimNgAfGenSSMAsrtCompMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 47),
    _VRtrPimNgAfGenSSMAsrtCompMode_Type()
)
vRtrPimNgAfGenSSMAsrtCompMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAfGenSSMAsrtCompMode.setStatus("current")


class _VRtrPimNgAfGenMdtType_Type(Integer32):
    """Custom type vRtrPimNgAfGenMdtType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("senderOnly", 0),
          ("receiverOnly", 1),
          ("senderReceiver", 2))
    )


_VRtrPimNgAfGenMdtType_Type.__name__ = "Integer32"
_VRtrPimNgAfGenMdtType_Object = MibTableColumn
vRtrPimNgAfGenMdtType = _VRtrPimNgAfGenMdtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 48),
    _VRtrPimNgAfGenMdtType_Type()
)
vRtrPimNgAfGenMdtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAfGenMdtType.setStatus("current")


class _VRtrPimNgAfGenMcastFastFailover_Type(TruthValue):
    """Custom type vRtrPimNgAfGenMcastFastFailover based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAfGenMcastFastFailover_Type.__name__ = "TruthValue"
_VRtrPimNgAfGenMcastFastFailover_Object = MibTableColumn
vRtrPimNgAfGenMcastFastFailover = _VRtrPimNgAfGenMcastFastFailover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 49),
    _VRtrPimNgAfGenMcastFastFailover_Type()
)
vRtrPimNgAfGenMcastFastFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAfGenMcastFastFailover.setStatus("current")


class _VRtrPimNgAFGenSourceAddressType_Type(InetAddressType):
    """Custom type vRtrPimNgAFGenSourceAddressType based on InetAddressType"""
    defaultValue = 0


_VRtrPimNgAFGenSourceAddressType_Type.__name__ = "InetAddressType"
_VRtrPimNgAFGenSourceAddressType_Object = MibTableColumn
vRtrPimNgAFGenSourceAddressType = _VRtrPimNgAFGenSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 50),
    _VRtrPimNgAFGenSourceAddressType_Type()
)
vRtrPimNgAFGenSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenSourceAddressType.setStatus("current")


class _VRtrPimNgAFGenSourceAddress_Type(InetAddress):
    """Custom type vRtrPimNgAFGenSourceAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFGenSourceAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAFGenSourceAddress_Object = MibTableColumn
vRtrPimNgAFGenSourceAddress = _VRtrPimNgAFGenSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 51),
    _VRtrPimNgAFGenSourceAddress_Type()
)
vRtrPimNgAFGenSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenSourceAddress.setStatus("current")


class _VRtrPimNgAFGenGrpPrefixAny_Type(TruthValue):
    """Custom type vRtrPimNgAFGenGrpPrefixAny based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAFGenGrpPrefixAny_Type.__name__ = "TruthValue"
_VRtrPimNgAFGenGrpPrefixAny_Object = MibTableColumn
vRtrPimNgAFGenGrpPrefixAny = _VRtrPimNgAFGenGrpPrefixAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 52),
    _VRtrPimNgAFGenGrpPrefixAny_Type()
)
vRtrPimNgAFGenGrpPrefixAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFGenGrpPrefixAny.setStatus("current")


class _VRtrPimNgAfGenMvpnPersistSA_Type(TruthValue):
    """Custom type vRtrPimNgAfGenMvpnPersistSA based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAfGenMvpnPersistSA_Type.__name__ = "TruthValue"
_VRtrPimNgAfGenMvpnPersistSA_Object = MibTableColumn
vRtrPimNgAfGenMvpnPersistSA = _VRtrPimNgAfGenMvpnPersistSA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 53),
    _VRtrPimNgAfGenMvpnPersistSA_Type()
)
vRtrPimNgAfGenMvpnPersistSA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAfGenMvpnPersistSA.setStatus("current")


class _VRtrPimNgAfGenUnicastRtRemoval_Type(TruthValue):
    """Custom type vRtrPimNgAfGenUnicastRtRemoval based on TruthValue"""
    defaultValue = 2


_VRtrPimNgAfGenUnicastRtRemoval_Type.__name__ = "TruthValue"
_VRtrPimNgAfGenUnicastRtRemoval_Object = MibTableColumn
vRtrPimNgAfGenUnicastRtRemoval = _VRtrPimNgAfGenUnicastRtRemoval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 4, 1, 54),
    _VRtrPimNgAfGenUnicastRtRemoval_Type()
)
vRtrPimNgAfGenUnicastRtRemoval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAfGenUnicastRtRemoval.setStatus("current")
_VRtrPimNgStaticRPTableLstChnged_Type = TimeStamp
_VRtrPimNgStaticRPTableLstChnged_Object = MibScalar
vRtrPimNgStaticRPTableLstChnged = _VRtrPimNgStaticRPTableLstChnged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 5),
    _VRtrPimNgStaticRPTableLstChnged_Type()
)
vRtrPimNgStaticRPTableLstChnged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPTableLstChnged.setStatus("current")
_VRtrPimNgStaticRPTable_Object = MibTable
vRtrPimNgStaticRPTable = _VRtrPimNgStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 6)
)
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPTable.setStatus("current")
_VRtrPimNgStaticRPEntry_Object = MibTableRow
vRtrPimNgStaticRPEntry = _VRtrPimNgStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 6, 1)
)
vRtrPimNgStaticRPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRPAddressType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRPAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPEntry.setStatus("current")
_VRtrPimNgStaticRPRPAddressType_Type = InetAddressType
_VRtrPimNgStaticRPRPAddressType_Object = MibTableColumn
vRtrPimNgStaticRPRPAddressType = _VRtrPimNgStaticRPRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 6, 1, 1),
    _VRtrPimNgStaticRPRPAddressType_Type()
)
vRtrPimNgStaticRPRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPRPAddressType.setStatus("current")


class _VRtrPimNgStaticRPRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgStaticRPRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgStaticRPRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgStaticRPRPAddress_Object = MibTableColumn
vRtrPimNgStaticRPRPAddress = _VRtrPimNgStaticRPRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 6, 1, 2),
    _VRtrPimNgStaticRPRPAddress_Type()
)
vRtrPimNgStaticRPRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPRPAddress.setStatus("current")
_VRtrPimNgStaticRPRowStatus_Type = RowStatus
_VRtrPimNgStaticRPRowStatus_Object = MibTableColumn
vRtrPimNgStaticRPRowStatus = _VRtrPimNgStaticRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 6, 1, 3),
    _VRtrPimNgStaticRPRowStatus_Type()
)
vRtrPimNgStaticRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPRowStatus.setStatus("current")
_VRtrPimNgStaticRPRowLastChanged_Type = TimeStamp
_VRtrPimNgStaticRPRowLastChanged_Object = MibTableColumn
vRtrPimNgStaticRPRowLastChanged = _VRtrPimNgStaticRPRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 6, 1, 4),
    _VRtrPimNgStaticRPRowLastChanged_Type()
)
vRtrPimNgStaticRPRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPRowLastChanged.setStatus("current")


class _VRtrPimNgStaticRPOverride_Type(TruthValue):
    """Custom type vRtrPimNgStaticRPOverride based on TruthValue"""
    defaultValue = 2


_VRtrPimNgStaticRPOverride_Type.__name__ = "TruthValue"
_VRtrPimNgStaticRPOverride_Object = MibTableColumn
vRtrPimNgStaticRPOverride = _VRtrPimNgStaticRPOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 6, 1, 5),
    _VRtrPimNgStaticRPOverride_Type()
)
vRtrPimNgStaticRPOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgStaticRPOverride.setStatus("current")
_VRtrPimNgStGrptoRPTableLstChngd_Type = TimeStamp
_VRtrPimNgStGrptoRPTableLstChngd_Object = MibScalar
vRtrPimNgStGrptoRPTableLstChngd = _VRtrPimNgStGrptoRPTableLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 7),
    _VRtrPimNgStGrptoRPTableLstChngd_Type()
)
vRtrPimNgStGrptoRPTableLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgStGrptoRPTableLstChngd.setStatus("current")
_VRtrPimNgStGrptoRPTable_Object = MibTable
vRtrPimNgStGrptoRPTable = _VRtrPimNgStGrptoRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8)
)
if mibBuilder.loadTexts:
    vRtrPimNgStGrptoRPTable.setStatus("current")
_VRtrPimNgStGrpToRPEntry_Object = MibTableRow
vRtrPimNgStGrpToRPEntry = _VRtrPimNgStGrpToRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1)
)
vRtrPimNgStGrpToRPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrptoRPRPAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrptoRPRPAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticGroupAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticGroupAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticGroupMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgStGrpToRPEntry.setStatus("current")
_VRtrPimNgStGrptoRPRPAddrType_Type = InetAddressType
_VRtrPimNgStGrptoRPRPAddrType_Object = MibTableColumn
vRtrPimNgStGrptoRPRPAddrType = _VRtrPimNgStGrptoRPRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1, 1),
    _VRtrPimNgStGrptoRPRPAddrType_Type()
)
vRtrPimNgStGrptoRPRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgStGrptoRPRPAddrType.setStatus("current")


class _VRtrPimNgStGrptoRPRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgStGrptoRPRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgStGrptoRPRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgStGrptoRPRPAddress_Object = MibTableColumn
vRtrPimNgStGrptoRPRPAddress = _VRtrPimNgStGrptoRPRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1, 2),
    _VRtrPimNgStGrptoRPRPAddress_Type()
)
vRtrPimNgStGrptoRPRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgStGrptoRPRPAddress.setStatus("current")
_VRtrPimNgStaticGroupAddrType_Type = InetAddressType
_VRtrPimNgStaticGroupAddrType_Object = MibTableColumn
vRtrPimNgStaticGroupAddrType = _VRtrPimNgStaticGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1, 3),
    _VRtrPimNgStaticGroupAddrType_Type()
)
vRtrPimNgStaticGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgStaticGroupAddrType.setStatus("current")


class _VRtrPimNgStaticGroupAddr_Type(InetAddress):
    """Custom type vRtrPimNgStaticGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgStaticGroupAddr_Type.__name__ = "InetAddress"
_VRtrPimNgStaticGroupAddr_Object = MibTableColumn
vRtrPimNgStaticGroupAddr = _VRtrPimNgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1, 4),
    _VRtrPimNgStaticGroupAddr_Type()
)
vRtrPimNgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgStaticGroupAddr.setStatus("current")
_VRtrPimNgStaticGroupMask_Type = InetAddressPrefixLength
_VRtrPimNgStaticGroupMask_Object = MibTableColumn
vRtrPimNgStaticGroupMask = _VRtrPimNgStaticGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1, 5),
    _VRtrPimNgStaticGroupMask_Type()
)
vRtrPimNgStaticGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgStaticGroupMask.setStatus("current")
_VRtrPimNgStGrpToRPRowStatus_Type = RowStatus
_VRtrPimNgStGrpToRPRowStatus_Object = MibTableColumn
vRtrPimNgStGrpToRPRowStatus = _VRtrPimNgStGrpToRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1, 6),
    _VRtrPimNgStGrpToRPRowStatus_Type()
)
vRtrPimNgStGrpToRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgStGrpToRPRowStatus.setStatus("current")
_VRtrPimNgStGrpToRPRowLstChanged_Type = TimeStamp
_VRtrPimNgStGrpToRPRowLstChanged_Object = MibTableColumn
vRtrPimNgStGrpToRPRowLstChanged = _VRtrPimNgStGrpToRPRowLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 8, 1, 7),
    _VRtrPimNgStGrpToRPRowLstChanged_Type()
)
vRtrPimNgStGrpToRPRowLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgStGrpToRPRowLstChanged.setStatus("current")
_VRtrPimNgGrpSrcTable_Object = MibTable
vRtrPimNgGrpSrcTable = _VRtrPimNgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9)
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcTable.setStatus("current")
_VRtrPimNgGrpSrcEntry_Object = MibTableRow
vRtrPimNgGrpSrcEntry = _VRtrPimNgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1)
)
vRtrPimNgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcEntry.setStatus("current")
_VRtrPimNgGrpSrcGrpAddrType_Type = InetAddressType
_VRtrPimNgGrpSrcGrpAddrType_Object = MibTableColumn
vRtrPimNgGrpSrcGrpAddrType = _VRtrPimNgGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 1),
    _VRtrPimNgGrpSrcGrpAddrType_Type()
)
vRtrPimNgGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpAddrType.setStatus("current")


class _VRtrPimNgGrpSrcGroupAddress_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcGroupAddress_Object = MibTableColumn
vRtrPimNgGrpSrcGroupAddress = _VRtrPimNgGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 2),
    _VRtrPimNgGrpSrcGroupAddress_Type()
)
vRtrPimNgGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGroupAddress.setStatus("current")
_VRtrPimNgGrpSrcSrcAddrType_Type = InetAddressType
_VRtrPimNgGrpSrcSrcAddrType_Object = MibTableColumn
vRtrPimNgGrpSrcSrcAddrType = _VRtrPimNgGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 3),
    _VRtrPimNgGrpSrcSrcAddrType_Type()
)
vRtrPimNgGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcSrcAddrType.setStatus("current")


class _VRtrPimNgGrpSrcSourceAddress_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcSourceAddress_Object = MibTableColumn
vRtrPimNgGrpSrcSourceAddress = _VRtrPimNgGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 4),
    _VRtrPimNgGrpSrcSourceAddress_Type()
)
vRtrPimNgGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcSourceAddress.setStatus("current")


class _VRtrPimNgGrpSrcType_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starStarRP", 0),
          ("starG", 1),
          ("sg", 2))
    )


_VRtrPimNgGrpSrcType_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcType_Object = MibTableColumn
vRtrPimNgGrpSrcType = _VRtrPimNgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 5),
    _VRtrPimNgGrpSrcType_Type()
)
vRtrPimNgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcType.setStatus("current")
_VRtrPimNgGrpSrcRPAddrType_Type = InetAddressType
_VRtrPimNgGrpSrcRPAddrType_Object = MibTableColumn
vRtrPimNgGrpSrcRPAddrType = _VRtrPimNgGrpSrcRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 6),
    _VRtrPimNgGrpSrcRPAddrType_Type()
)
vRtrPimNgGrpSrcRPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRPAddrType.setStatus("current")


class _VRtrPimNgGrpSrcRPAddr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcRPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcRPAddr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcRPAddr_Object = MibTableColumn
vRtrPimNgGrpSrcRPAddr = _VRtrPimNgGrpSrcRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 7),
    _VRtrPimNgGrpSrcRPAddr_Type()
)
vRtrPimNgGrpSrcRPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRPAddr.setStatus("current")
_VRtrPimNgGrpSrcRpfNbrAddrType_Type = InetAddressType
_VRtrPimNgGrpSrcRpfNbrAddrType_Object = MibTableColumn
vRtrPimNgGrpSrcRpfNbrAddrType = _VRtrPimNgGrpSrcRpfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 8),
    _VRtrPimNgGrpSrcRpfNbrAddrType_Type()
)
vRtrPimNgGrpSrcRpfNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRpfNbrAddrType.setStatus("current")


class _VRtrPimNgGrpSrcRpfNbrAddr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcRpfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcRpfNbrAddr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcRpfNbrAddr_Object = MibTableColumn
vRtrPimNgGrpSrcRpfNbrAddr = _VRtrPimNgGrpSrcRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 9),
    _VRtrPimNgGrpSrcRpfNbrAddr_Type()
)
vRtrPimNgGrpSrcRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRpfNbrAddr.setStatus("current")
_VRtrPimNgGrpSrcRpfIfIndex_Type = InterfaceIndexOrZero
_VRtrPimNgGrpSrcRpfIfIndex_Object = MibTableColumn
vRtrPimNgGrpSrcRpfIfIndex = _VRtrPimNgGrpSrcRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 10),
    _VRtrPimNgGrpSrcRpfIfIndex_Type()
)
vRtrPimNgGrpSrcRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRpfIfIndex.setStatus("current")
_VRtrPimNgGrpSrcRptRpfNbrAdrType_Type = InetAddressType
_VRtrPimNgGrpSrcRptRpfNbrAdrType_Object = MibTableColumn
vRtrPimNgGrpSrcRptRpfNbrAdrType = _VRtrPimNgGrpSrcRptRpfNbrAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 11),
    _VRtrPimNgGrpSrcRptRpfNbrAdrType_Type()
)
vRtrPimNgGrpSrcRptRpfNbrAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRptRpfNbrAdrType.setStatus("current")


class _VRtrPimNgGrpSrcRptRpfNbrAddr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcRptRpfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcRptRpfNbrAddr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcRptRpfNbrAddr_Object = MibTableColumn
vRtrPimNgGrpSrcRptRpfNbrAddr = _VRtrPimNgGrpSrcRptRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 12),
    _VRtrPimNgGrpSrcRptRpfNbrAddr_Type()
)
vRtrPimNgGrpSrcRptRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRptRpfNbrAddr.setStatus("current")
_VRtrPimNgGrpSrcMRIBNHopAddrType_Type = InetAddressType
_VRtrPimNgGrpSrcMRIBNHopAddrType_Object = MibTableColumn
vRtrPimNgGrpSrcMRIBNHopAddrType = _VRtrPimNgGrpSrcMRIBNHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 13),
    _VRtrPimNgGrpSrcMRIBNHopAddrType_Type()
)
vRtrPimNgGrpSrcMRIBNHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcMRIBNHopAddrType.setStatus("current")


class _VRtrPimNgGrpSrcMRIBNextHopAddr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcMRIBNextHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrPimNgGrpSrcMRIBNextHopAddr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcMRIBNextHopAddr_Object = MibTableColumn
vRtrPimNgGrpSrcMRIBNextHopAddr = _VRtrPimNgGrpSrcMRIBNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 14),
    _VRtrPimNgGrpSrcMRIBNextHopAddr_Type()
)
vRtrPimNgGrpSrcMRIBNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcMRIBNextHopAddr.setStatus("current")


class _VRtrPimNgGrpSrcMRIBSrcFlags_Type(Bits):
    """Custom type vRtrPimNgGrpSrcMRIBSrcFlags based on Bits"""
    namedValues = NamedValues(
        *(("self", 0),
          ("direct", 1),
          ("remote", 2))
    )

_VRtrPimNgGrpSrcMRIBSrcFlags_Type.__name__ = "Bits"
_VRtrPimNgGrpSrcMRIBSrcFlags_Object = MibTableColumn
vRtrPimNgGrpSrcMRIBSrcFlags = _VRtrPimNgGrpSrcMRIBSrcFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 15),
    _VRtrPimNgGrpSrcMRIBSrcFlags_Type()
)
vRtrPimNgGrpSrcMRIBSrcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcMRIBSrcFlags.setStatus("current")


class _VRtrPimNgGrpSrcFlags_Type(Bits):
    """Custom type vRtrPimNgGrpSrcFlags based on Bits"""
    namedValues = NamedValues(
        *(("sptBit", 0),
          ("rptPruneDesired", 1))
    )

_VRtrPimNgGrpSrcFlags_Type.__name__ = "Bits"
_VRtrPimNgGrpSrcFlags_Object = MibTableColumn
vRtrPimNgGrpSrcFlags = _VRtrPimNgGrpSrcFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 16),
    _VRtrPimNgGrpSrcFlags_Type()
)
vRtrPimNgGrpSrcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcFlags.setStatus("current")


class _VRtrPimNgGrpSrcUpstreamJpState_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcUpstreamJpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notJoined", 0),
          ("joined", 1))
    )


_VRtrPimNgGrpSrcUpstreamJpState_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcUpstreamJpState_Object = MibTableColumn
vRtrPimNgGrpSrcUpstreamJpState = _VRtrPimNgGrpSrcUpstreamJpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 17),
    _VRtrPimNgGrpSrcUpstreamJpState_Type()
)
vRtrPimNgGrpSrcUpstreamJpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUpstreamJpState.setStatus("current")
_VRtrPimNgGrpSrcUpstreamJpTimer_Type = Unsigned32
_VRtrPimNgGrpSrcUpstreamJpTimer_Object = MibTableColumn
vRtrPimNgGrpSrcUpstreamJpTimer = _VRtrPimNgGrpSrcUpstreamJpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 18),
    _VRtrPimNgGrpSrcUpstreamJpTimer_Type()
)
vRtrPimNgGrpSrcUpstreamJpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUpstreamJpTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUpstreamJpTimer.setUnits("seconds")


class _VRtrPimNgGrpSrcUstrmRptJpState_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcUstrmRptJpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notJoinedStarG", 0),
          ("notPruned", 1),
          ("pruned", 2))
    )


_VRtrPimNgGrpSrcUstrmRptJpState_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcUstrmRptJpState_Object = MibTableColumn
vRtrPimNgGrpSrcUstrmRptJpState = _VRtrPimNgGrpSrcUstrmRptJpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 19),
    _VRtrPimNgGrpSrcUstrmRptJpState_Type()
)
vRtrPimNgGrpSrcUstrmRptJpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUstrmRptJpState.setStatus("current")
_VRtrPimNgGrpSrcUstrmRptOvrdeTmr_Type = Unsigned32
_VRtrPimNgGrpSrcUstrmRptOvrdeTmr_Object = MibTableColumn
vRtrPimNgGrpSrcUstrmRptOvrdeTmr = _VRtrPimNgGrpSrcUstrmRptOvrdeTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 20),
    _VRtrPimNgGrpSrcUstrmRptOvrdeTmr_Type()
)
vRtrPimNgGrpSrcUstrmRptOvrdeTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUstrmRptOvrdeTmr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUstrmRptOvrdeTmr.setUnits("seconds")


class _VRtrPimNgGrpSrcRegisterState_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcRegisterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("joinPending", 2),
          ("prune", 3),
          ("nullJoin", 4))
    )


_VRtrPimNgGrpSrcRegisterState_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcRegisterState_Object = MibTableColumn
vRtrPimNgGrpSrcRegisterState = _VRtrPimNgGrpSrcRegisterState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 21),
    _VRtrPimNgGrpSrcRegisterState_Type()
)
vRtrPimNgGrpSrcRegisterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRegisterState.setStatus("current")
_VRtrPimNgGrpSrcRegisterStopTmr_Type = Unsigned32
_VRtrPimNgGrpSrcRegisterStopTmr_Object = MibTableColumn
vRtrPimNgGrpSrcRegisterStopTmr = _VRtrPimNgGrpSrcRegisterStopTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 22),
    _VRtrPimNgGrpSrcRegisterStopTmr_Type()
)
vRtrPimNgGrpSrcRegisterStopTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRegisterStopTmr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRegisterStopTmr.setUnits("seconds")
_VRtrPimNgGrpSrcKeepaliveTimer_Type = Unsigned32
_VRtrPimNgGrpSrcKeepaliveTimer_Object = MibTableColumn
vRtrPimNgGrpSrcKeepaliveTimer = _VRtrPimNgGrpSrcKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 23),
    _VRtrPimNgGrpSrcKeepaliveTimer_Type()
)
vRtrPimNgGrpSrcKeepaliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcKeepaliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcKeepaliveTimer.setUnits("seconds")
_VRtrPimNgGrpSrcNumImmediateOif_Type = Gauge32
_VRtrPimNgGrpSrcNumImmediateOif_Object = MibTableColumn
vRtrPimNgGrpSrcNumImmediateOif = _VRtrPimNgGrpSrcNumImmediateOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 24),
    _VRtrPimNgGrpSrcNumImmediateOif_Type()
)
vRtrPimNgGrpSrcNumImmediateOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumImmediateOif.setStatus("current")
_VRtrPimNgGrpSrcNumInheritedOif_Type = Gauge32
_VRtrPimNgGrpSrcNumInheritedOif_Object = MibTableColumn
vRtrPimNgGrpSrcNumInheritedOif = _VRtrPimNgGrpSrcNumInheritedOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 25),
    _VRtrPimNgGrpSrcNumInheritedOif_Type()
)
vRtrPimNgGrpSrcNumInheritedOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumInheritedOif.setStatus("current")
_VRtrPimNgGrpSrcNumInherRptOif_Type = Gauge32
_VRtrPimNgGrpSrcNumInherRptOif_Object = MibTableColumn
vRtrPimNgGrpSrcNumInherRptOif = _VRtrPimNgGrpSrcNumInherRptOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 26),
    _VRtrPimNgGrpSrcNumInherRptOif_Type()
)
vRtrPimNgGrpSrcNumInherRptOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumInherRptOif.setStatus("current")
_VRtrPimNgGrpSrcNumLclRxInclIf_Type = Gauge32
_VRtrPimNgGrpSrcNumLclRxInclIf_Object = MibTableColumn
vRtrPimNgGrpSrcNumLclRxInclIf = _VRtrPimNgGrpSrcNumLclRxInclIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 27),
    _VRtrPimNgGrpSrcNumLclRxInclIf_Type()
)
vRtrPimNgGrpSrcNumLclRxInclIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumLclRxInclIf.setStatus("current")
_VRtrPimNgGrpSrcNumLclRxExclIf_Type = Gauge32
_VRtrPimNgGrpSrcNumLclRxExclIf_Object = MibTableColumn
vRtrPimNgGrpSrcNumLclRxExclIf = _VRtrPimNgGrpSrcNumLclRxExclIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 28),
    _VRtrPimNgGrpSrcNumLclRxExclIf_Type()
)
vRtrPimNgGrpSrcNumLclRxExclIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumLclRxExclIf.setStatus("current")
_VRtrPimNgGrpSrcNumJoinPruneIf_Type = Gauge32
_VRtrPimNgGrpSrcNumJoinPruneIf_Object = MibTableColumn
vRtrPimNgGrpSrcNumJoinPruneIf = _VRtrPimNgGrpSrcNumJoinPruneIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 29),
    _VRtrPimNgGrpSrcNumJoinPruneIf_Type()
)
vRtrPimNgGrpSrcNumJoinPruneIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumJoinPruneIf.setStatus("current")
_VRtrPimNgGrpSrcNumLostAssertIf_Type = Gauge32
_VRtrPimNgGrpSrcNumLostAssertIf_Object = MibTableColumn
vRtrPimNgGrpSrcNumLostAssertIf = _VRtrPimNgGrpSrcNumLostAssertIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 30),
    _VRtrPimNgGrpSrcNumLostAssertIf_Type()
)
vRtrPimNgGrpSrcNumLostAssertIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumLostAssertIf.setStatus("current")
_VRtrPimNgGrpSrcUpTime_Type = Unsigned32
_VRtrPimNgGrpSrcUpTime_Object = MibTableColumn
vRtrPimNgGrpSrcUpTime = _VRtrPimNgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 31),
    _VRtrPimNgGrpSrcUpTime_Type()
)
vRtrPimNgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUpTime.setUnits("seconds")
_VRtrPimNgGrpSrcNumSGRptPruneOif_Type = Gauge32
_VRtrPimNgGrpSrcNumSGRptPruneOif_Object = MibTableColumn
vRtrPimNgGrpSrcNumSGRptPruneOif = _VRtrPimNgGrpSrcNumSGRptPruneOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 32),
    _VRtrPimNgGrpSrcNumSGRptPruneOif_Type()
)
vRtrPimNgGrpSrcNumSGRptPruneOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcNumSGRptPruneOif.setStatus("current")
_VRtrPimNgGrpSrcRxRegFrmAnycstRP_Type = TruthValue
_VRtrPimNgGrpSrcRxRegFrmAnycstRP_Object = MibTableColumn
vRtrPimNgGrpSrcRxRegFrmAnycstRP = _VRtrPimNgGrpSrcRxRegFrmAnycstRP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 33),
    _VRtrPimNgGrpSrcRxRegFrmAnycstRP_Type()
)
vRtrPimNgGrpSrcRxRegFrmAnycstRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRxRegFrmAnycstRP.setStatus("current")


class _VRtrPimNgGrpSrcRslvdByRtTblType_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcRslvdByRtTblType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mucastRouteTable", 1),
          ("ucastRouteTable", 2))
    )


_VRtrPimNgGrpSrcRslvdByRtTblType_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcRslvdByRtTblType_Object = MibTableColumn
vRtrPimNgGrpSrcRslvdByRtTblType = _VRtrPimNgGrpSrcRslvdByRtTblType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 34),
    _VRtrPimNgGrpSrcRslvdByRtTblType_Type()
)
vRtrPimNgGrpSrcRslvdByRtTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRslvdByRtTblType.setStatus("current")
_VRtrPimNgGrpSrcCurrFwdingRate_Type = Counter32
_VRtrPimNgGrpSrcCurrFwdingRate_Object = MibTableColumn
vRtrPimNgGrpSrcCurrFwdingRate = _VRtrPimNgGrpSrcCurrFwdingRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 35),
    _VRtrPimNgGrpSrcCurrFwdingRate_Type()
)
vRtrPimNgGrpSrcCurrFwdingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcCurrFwdingRate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcCurrFwdingRate.setUnits("bps")
_VRtrPimNgGrpSrcCurrFwdingOFRate_Type = Counter32
_VRtrPimNgGrpSrcCurrFwdingOFRate_Object = MibTableColumn
vRtrPimNgGrpSrcCurrFwdingOFRate = _VRtrPimNgGrpSrcCurrFwdingOFRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 36),
    _VRtrPimNgGrpSrcCurrFwdingOFRate_Type()
)
vRtrPimNgGrpSrcCurrFwdingOFRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcCurrFwdingOFRate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcCurrFwdingOFRate.setUnits("bps")
_VRtrPimNgGrpSrcCurrFwdingHCRate_Type = Counter64
_VRtrPimNgGrpSrcCurrFwdingHCRate_Object = MibTableColumn
vRtrPimNgGrpSrcCurrFwdingHCRate = _VRtrPimNgGrpSrcCurrFwdingHCRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 37),
    _VRtrPimNgGrpSrcCurrFwdingHCRate_Type()
)
vRtrPimNgGrpSrcCurrFwdingHCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcCurrFwdingHCRate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcCurrFwdingHCRate.setUnits("bps")
_VRtrPimNgGrpSrcGrpSptThreshold_Type = Unsigned32
_VRtrPimNgGrpSrcGrpSptThreshold_Object = MibTableColumn
vRtrPimNgGrpSrcGrpSptThreshold = _VRtrPimNgGrpSrcGrpSptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 38),
    _VRtrPimNgGrpSrcGrpSptThreshold_Type()
)
vRtrPimNgGrpSrcGrpSptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpSptThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpSptThreshold.setUnits("kbps")


class _VRtrPimNgGrpSrcGrpAdminBw_Type(Gauge32):
    """Custom type vRtrPimNgGrpSrcGrpAdminBw based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_VRtrPimNgGrpSrcGrpAdminBw_Type.__name__ = "Gauge32"
_VRtrPimNgGrpSrcGrpAdminBw_Object = MibTableColumn
vRtrPimNgGrpSrcGrpAdminBw = _VRtrPimNgGrpSrcGrpAdminBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 39),
    _VRtrPimNgGrpSrcGrpAdminBw_Type()
)
vRtrPimNgGrpSrcGrpAdminBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpAdminBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpAdminBw.setUnits("kbps")


class _VRtrPimNgGrpSrcGrpEcmpOptThresh_Type(Unsigned32):
    """Custom type vRtrPimNgGrpSrcGrpEcmpOptThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrPimNgGrpSrcGrpEcmpOptThresh_Type.__name__ = "Unsigned32"
_VRtrPimNgGrpSrcGrpEcmpOptThresh_Object = MibTableColumn
vRtrPimNgGrpSrcGrpEcmpOptThresh = _VRtrPimNgGrpSrcGrpEcmpOptThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 40),
    _VRtrPimNgGrpSrcGrpEcmpOptThresh_Type()
)
vRtrPimNgGrpSrcGrpEcmpOptThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpEcmpOptThresh.setStatus("current")
_VRtrPimNgGrpSrcSpmsiRpfIfIndex_Type = InterfaceIndexOrZero
_VRtrPimNgGrpSrcSpmsiRpfIfIndex_Object = MibTableColumn
vRtrPimNgGrpSrcSpmsiRpfIfIndex = _VRtrPimNgGrpSrcSpmsiRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 41),
    _VRtrPimNgGrpSrcSpmsiRpfIfIndex_Type()
)
vRtrPimNgGrpSrcSpmsiRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcSpmsiRpfIfIndex.setStatus("current")
_VRtrPimNgGrpSrcRpfSecNbrAddrTyp_Type = InetAddressType
_VRtrPimNgGrpSrcRpfSecNbrAddrTyp_Object = MibTableColumn
vRtrPimNgGrpSrcRpfSecNbrAddrTyp = _VRtrPimNgGrpSrcRpfSecNbrAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 42),
    _VRtrPimNgGrpSrcRpfSecNbrAddrTyp_Type()
)
vRtrPimNgGrpSrcRpfSecNbrAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRpfSecNbrAddrTyp.setStatus("current")


class _VRtrPimNgGrpSrcRpfSecNbrAddr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcRpfSecNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcRpfSecNbrAddr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcRpfSecNbrAddr_Object = MibTableColumn
vRtrPimNgGrpSrcRpfSecNbrAddr = _VRtrPimNgGrpSrcRpfSecNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 43),
    _VRtrPimNgGrpSrcRpfSecNbrAddr_Type()
)
vRtrPimNgGrpSrcRpfSecNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRpfSecNbrAddr.setStatus("current")
_VRtrPimNgGrpSrcRpfSecIfIndex_Type = InterfaceIndexOrZero
_VRtrPimNgGrpSrcRpfSecIfIndex_Object = MibTableColumn
vRtrPimNgGrpSrcRpfSecIfIndex = _VRtrPimNgGrpSrcRpfSecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 44),
    _VRtrPimNgGrpSrcRpfSecIfIndex_Type()
)
vRtrPimNgGrpSrcRpfSecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRpfSecIfIndex.setStatus("current")
_VRtrPimNgGrpSrcAdvtAddrType_Type = InetAddressType
_VRtrPimNgGrpSrcAdvtAddrType_Object = MibTableColumn
vRtrPimNgGrpSrcAdvtAddrType = _VRtrPimNgGrpSrcAdvtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 45),
    _VRtrPimNgGrpSrcAdvtAddrType_Type()
)
vRtrPimNgGrpSrcAdvtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcAdvtAddrType.setStatus("current")


class _VRtrPimNgGrpSrcAdvtAddr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcAdvtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcAdvtAddr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcAdvtAddr_Object = MibTableColumn
vRtrPimNgGrpSrcAdvtAddr = _VRtrPimNgGrpSrcAdvtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 46),
    _VRtrPimNgGrpSrcAdvtAddr_Type()
)
vRtrPimNgGrpSrcAdvtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcAdvtAddr.setStatus("current")


class _VRtrPimNgGrpSrcStdbyMRIBSrcFlags_Type(Bits):
    """Custom type vRtrPimNgGrpSrcStdbyMRIBSrcFlags based on Bits"""
    namedValues = NamedValues(
        *(("self", 0),
          ("direct", 1),
          ("remote", 2))
    )

_VRtrPimNgGrpSrcStdbyMRIBSrcFlags_Type.__name__ = "Bits"
_VRtrPimNgGrpSrcStdbyMRIBSrcFlags_Object = MibTableColumn
vRtrPimNgGrpSrcStdbyMRIBSrcFlags = _VRtrPimNgGrpSrcStdbyMRIBSrcFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 47),
    _VRtrPimNgGrpSrcStdbyMRIBSrcFlags_Type()
)
vRtrPimNgGrpSrcStdbyMRIBSrcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStdbyMRIBSrcFlags.setStatus("current")


class _VRtrPimNgGrpSrcStdbyUpJpState_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcStdbyUpJpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notJoined", 0),
          ("joined", 1))
    )


_VRtrPimNgGrpSrcStdbyUpJpState_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcStdbyUpJpState_Object = MibTableColumn
vRtrPimNgGrpSrcStdbyUpJpState = _VRtrPimNgGrpSrcStdbyUpJpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 48),
    _VRtrPimNgGrpSrcStdbyUpJpState_Type()
)
vRtrPimNgGrpSrcStdbyUpJpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStdbyUpJpState.setStatus("current")
_VRtrPimNgGrpSrcStdbyUpJpTimer_Type = Unsigned32
_VRtrPimNgGrpSrcStdbyUpJpTimer_Object = MibTableColumn
vRtrPimNgGrpSrcStdbyUpJpTimer = _VRtrPimNgGrpSrcStdbyUpJpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 49),
    _VRtrPimNgGrpSrcStdbyUpJpTimer_Type()
)
vRtrPimNgGrpSrcStdbyUpJpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStdbyUpJpTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStdbyUpJpTimer.setUnits("seconds")
_VRtrPimNgGrpSrcDSRpfvNbrType_Type = InetAddressType
_VRtrPimNgGrpSrcDSRpfvNbrType_Object = MibTableColumn
vRtrPimNgGrpSrcDSRpfvNbrType = _VRtrPimNgGrpSrcDSRpfvNbrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 50),
    _VRtrPimNgGrpSrcDSRpfvNbrType_Type()
)
vRtrPimNgGrpSrcDSRpfvNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcDSRpfvNbrType.setStatus("current")


class _VRtrPimNgGrpSrcDSRpfvNbr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcDSRpfvNbr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcDSRpfvNbr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcDSRpfvNbr_Object = MibTableColumn
vRtrPimNgGrpSrcDSRpfvNbr = _VRtrPimNgGrpSrcDSRpfvNbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 51),
    _VRtrPimNgGrpSrcDSRpfvNbr_Type()
)
vRtrPimNgGrpSrcDSRpfvNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcDSRpfvNbr.setStatus("current")
_VRtrPimNgGrpSrcDSRpfvProxyType_Type = InetAddressType
_VRtrPimNgGrpSrcDSRpfvProxyType_Object = MibTableColumn
vRtrPimNgGrpSrcDSRpfvProxyType = _VRtrPimNgGrpSrcDSRpfvProxyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 52),
    _VRtrPimNgGrpSrcDSRpfvProxyType_Type()
)
vRtrPimNgGrpSrcDSRpfvProxyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcDSRpfvProxyType.setStatus("current")


class _VRtrPimNgGrpSrcDSRpfvProxy_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcDSRpfvProxy based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcDSRpfvProxy_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcDSRpfvProxy_Object = MibTableColumn
vRtrPimNgGrpSrcDSRpfvProxy = _VRtrPimNgGrpSrcDSRpfvProxy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 53),
    _VRtrPimNgGrpSrcDSRpfvProxy_Type()
)
vRtrPimNgGrpSrcDSRpfvProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcDSRpfvProxy.setStatus("current")
_VRtrPimNgGrpSrcDSRpfvRD_Type = TmnxVPNRouteDistinguisher
_VRtrPimNgGrpSrcDSRpfvRD_Object = MibTableColumn
vRtrPimNgGrpSrcDSRpfvRD = _VRtrPimNgGrpSrcDSRpfvRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 54),
    _VRtrPimNgGrpSrcDSRpfvRD_Type()
)
vRtrPimNgGrpSrcDSRpfvRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcDSRpfvRD.setStatus("current")


class _VRtrPimNgGrpSrcDSRpfvType_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcDSRpfvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mvpn", 1),
          ("core", 2))
    )


_VRtrPimNgGrpSrcDSRpfvType_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcDSRpfvType_Object = MibTableColumn
vRtrPimNgGrpSrcDSRpfvType = _VRtrPimNgGrpSrcDSRpfvType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 55),
    _VRtrPimNgGrpSrcDSRpfvType_Type()
)
vRtrPimNgGrpSrcDSRpfvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcDSRpfvType.setStatus("current")
_VRtrPimNgGrpSrcUPRpfvNbrType_Type = InetAddressType
_VRtrPimNgGrpSrcUPRpfvNbrType_Object = MibTableColumn
vRtrPimNgGrpSrcUPRpfvNbrType = _VRtrPimNgGrpSrcUPRpfvNbrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 56),
    _VRtrPimNgGrpSrcUPRpfvNbrType_Type()
)
vRtrPimNgGrpSrcUPRpfvNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUPRpfvNbrType.setStatus("current")


class _VRtrPimNgGrpSrcUPRpfvNbr_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcUPRpfvNbr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcUPRpfvNbr_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcUPRpfvNbr_Object = MibTableColumn
vRtrPimNgGrpSrcUPRpfvNbr = _VRtrPimNgGrpSrcUPRpfvNbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 57),
    _VRtrPimNgGrpSrcUPRpfvNbr_Type()
)
vRtrPimNgGrpSrcUPRpfvNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUPRpfvNbr.setStatus("current")
_VRtrPimNgGrpSrcUPRpfvProxyType_Type = InetAddressType
_VRtrPimNgGrpSrcUPRpfvProxyType_Object = MibTableColumn
vRtrPimNgGrpSrcUPRpfvProxyType = _VRtrPimNgGrpSrcUPRpfvProxyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 58),
    _VRtrPimNgGrpSrcUPRpfvProxyType_Type()
)
vRtrPimNgGrpSrcUPRpfvProxyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUPRpfvProxyType.setStatus("current")


class _VRtrPimNgGrpSrcUPRpfvProxy_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcUPRpfvProxy based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcUPRpfvProxy_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcUPRpfvProxy_Object = MibTableColumn
vRtrPimNgGrpSrcUPRpfvProxy = _VRtrPimNgGrpSrcUPRpfvProxy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 59),
    _VRtrPimNgGrpSrcUPRpfvProxy_Type()
)
vRtrPimNgGrpSrcUPRpfvProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUPRpfvProxy.setStatus("current")
_VRtrPimNgGrpSrcUPRpfvRD_Type = TmnxVPNRouteDistinguisher
_VRtrPimNgGrpSrcUPRpfvRD_Object = MibTableColumn
vRtrPimNgGrpSrcUPRpfvRD = _VRtrPimNgGrpSrcUPRpfvRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 60),
    _VRtrPimNgGrpSrcUPRpfvRD_Type()
)
vRtrPimNgGrpSrcUPRpfvRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUPRpfvRD.setStatus("current")


class _VRtrPimNgGrpSrcUPRpfvType_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcUPRpfvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mvpn", 1),
          ("core", 2))
    )


_VRtrPimNgGrpSrcUPRpfvType_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcUPRpfvType_Object = MibTableColumn
vRtrPimNgGrpSrcUPRpfvType = _VRtrPimNgGrpSrcUPRpfvType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 61),
    _VRtrPimNgGrpSrcUPRpfvType_Type()
)
vRtrPimNgGrpSrcUPRpfvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcUPRpfvType.setStatus("current")


class _VRtrPimNgGrpSrcRpfvFlags_Type(Bits):
    """Custom type vRtrPimNgGrpSrcRpfvFlags based on Bits"""
    namedValues = NamedValues(
        ("upNbrNoJa", 0)
    )

_VRtrPimNgGrpSrcRpfvFlags_Type.__name__ = "Bits"
_VRtrPimNgGrpSrcRpfvFlags_Object = MibTableColumn
vRtrPimNgGrpSrcRpfvFlags = _VRtrPimNgGrpSrcRpfvFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 62),
    _VRtrPimNgGrpSrcRpfvFlags_Type()
)
vRtrPimNgGrpSrcRpfvFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcRpfvFlags.setStatus("current")


class _VRtrPimNgGrpSrcState_Type(Integer32):
    """Custom type vRtrPimNgGrpSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("active", 1),
          ("standby", 2))
    )


_VRtrPimNgGrpSrcState_Type.__name__ = "Integer32"
_VRtrPimNgGrpSrcState_Object = MibTableColumn
vRtrPimNgGrpSrcState = _VRtrPimNgGrpSrcState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 9, 1, 63),
    _VRtrPimNgGrpSrcState_Type()
)
vRtrPimNgGrpSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcState.setStatus("current")
_VRtrPimNgGrpSrcIfTable_Object = MibTable
vRtrPimNgGrpSrcIfTable = _VRtrPimNgGrpSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 10)
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcIfTable.setStatus("current")
_VRtrPimNgGrpSrcIfEntry_Object = MibTableRow
vRtrPimNgGrpSrcIfEntry = _VRtrPimNgGrpSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 10, 1)
)
vRtrPimNgGrpSrcIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSourceAddress"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcIfEntry.setStatus("current")


class _VRtrPimNgGrpSrcIfFlags_Type(Bits):
    """Custom type vRtrPimNgGrpSrcIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("localRxInclude", 3),
          ("localRxExclude", 4),
          ("joinPruneList", 5),
          ("lostAssertList", 6),
          ("sgRptPruneOifList", 7))
    )

_VRtrPimNgGrpSrcIfFlags_Type.__name__ = "Bits"
_VRtrPimNgGrpSrcIfFlags_Object = MibTableColumn
vRtrPimNgGrpSrcIfFlags = _VRtrPimNgGrpSrcIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 10, 1, 1),
    _VRtrPimNgGrpSrcIfFlags_Type()
)
vRtrPimNgGrpSrcIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcIfFlags.setStatus("current")
_VRtrPimNgGrpSrcSpmsiIfIndex_Type = InterfaceIndexOrZero
_VRtrPimNgGrpSrcSpmsiIfIndex_Object = MibTableColumn
vRtrPimNgGrpSrcSpmsiIfIndex = _VRtrPimNgGrpSrcSpmsiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 10, 1, 2),
    _VRtrPimNgGrpSrcSpmsiIfIndex_Type()
)
vRtrPimNgGrpSrcSpmsiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcSpmsiIfIndex.setStatus("current")
_VRtrPimNgCRPGrpPrfxTblLstChnged_Type = TimeStamp
_VRtrPimNgCRPGrpPrfxTblLstChnged_Object = MibScalar
vRtrPimNgCRPGrpPrfxTblLstChnged = _VRtrPimNgCRPGrpPrfxTblLstChnged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 11),
    _VRtrPimNgCRPGrpPrfxTblLstChnged_Type()
)
vRtrPimNgCRPGrpPrfxTblLstChnged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrfxTblLstChnged.setStatus("obsolete")
_VRtrPimNgCRPGrpPrefixTable_Object = MibTable
vRtrPimNgCRPGrpPrefixTable = _VRtrPimNgCRPGrpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 12)
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixTable.setStatus("obsolete")
_VRtrPimNgCRPGrpPrefixEntry_Object = MibTableRow
vRtrPimNgCRPGrpPrefixEntry = _VRtrPimNgCRPGrpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 12, 1)
)
vRtrPimNgCRPGrpPrefixEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrfixGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrefixGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrefixGrpMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixEntry.setStatus("obsolete")
_VRtrPimNgCRPGrpPrfixGrpAddrType_Type = InetAddressType
_VRtrPimNgCRPGrpPrfixGrpAddrType_Object = MibTableColumn
vRtrPimNgCRPGrpPrfixGrpAddrType = _VRtrPimNgCRPGrpPrfixGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 12, 1, 1),
    _VRtrPimNgCRPGrpPrfixGrpAddrType_Type()
)
vRtrPimNgCRPGrpPrfixGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrfixGrpAddrType.setStatus("obsolete")


class _VRtrPimNgCRPGrpPrefixGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgCRPGrpPrefixGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgCRPGrpPrefixGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgCRPGrpPrefixGrpAddr_Object = MibTableColumn
vRtrPimNgCRPGrpPrefixGrpAddr = _VRtrPimNgCRPGrpPrefixGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 12, 1, 2),
    _VRtrPimNgCRPGrpPrefixGrpAddr_Type()
)
vRtrPimNgCRPGrpPrefixGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixGrpAddr.setStatus("obsolete")
_VRtrPimNgCRPGrpPrefixGrpMask_Type = IpAddressPrefixLength
_VRtrPimNgCRPGrpPrefixGrpMask_Object = MibTableColumn
vRtrPimNgCRPGrpPrefixGrpMask = _VRtrPimNgCRPGrpPrefixGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 12, 1, 3),
    _VRtrPimNgCRPGrpPrefixGrpMask_Type()
)
vRtrPimNgCRPGrpPrefixGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixGrpMask.setStatus("obsolete")
_VRtrPimNgCRPGrpPrefixRowStatus_Type = RowStatus
_VRtrPimNgCRPGrpPrefixRowStatus_Object = MibTableColumn
vRtrPimNgCRPGrpPrefixRowStatus = _VRtrPimNgCRPGrpPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 12, 1, 4),
    _VRtrPimNgCRPGrpPrefixRowStatus_Type()
)
vRtrPimNgCRPGrpPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixRowStatus.setStatus("obsolete")
_VRtrPimNgCRPGrpPrfixRowLstChngd_Type = TimeStamp
_VRtrPimNgCRPGrpPrfixRowLstChngd_Object = MibTableColumn
vRtrPimNgCRPGrpPrfixRowLstChngd = _VRtrPimNgCRPGrpPrfixRowLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 12, 1, 5),
    _VRtrPimNgCRPGrpPrfixRowLstChngd_Type()
)
vRtrPimNgCRPGrpPrfixRowLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrfixRowLstChngd.setStatus("obsolete")
_VRtrPimNgCRPTable_Object = MibTable
vRtrPimNgCRPTable = _VRtrPimNgCRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13)
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPTable.setStatus("obsolete")
_VRtrPimNgCRPEntry_Object = MibTableRow
vRtrPimNgCRPEntry = _VRtrPimNgCRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1)
)
vRtrPimNgCRPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPAddressType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPEntry.setStatus("obsolete")
_VRtrPimNgCRPAddressType_Type = InetAddressType
_VRtrPimNgCRPAddressType_Object = MibTableColumn
vRtrPimNgCRPAddressType = _VRtrPimNgCRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 1),
    _VRtrPimNgCRPAddressType_Type()
)
vRtrPimNgCRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPAddressType.setStatus("obsolete")


class _VRtrPimNgCRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgCRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgCRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgCRPAddress_Object = MibTableColumn
vRtrPimNgCRPAddress = _VRtrPimNgCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 2),
    _VRtrPimNgCRPAddress_Type()
)
vRtrPimNgCRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPAddress.setStatus("obsolete")
_VRtrPimNgCRPGrpAddrType_Type = InetAddressType
_VRtrPimNgCRPGrpAddrType_Object = MibTableColumn
vRtrPimNgCRPGrpAddrType = _VRtrPimNgCRPGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 3),
    _VRtrPimNgCRPGrpAddrType_Type()
)
vRtrPimNgCRPGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpAddrType.setStatus("obsolete")


class _VRtrPimNgCRPGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgCRPGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgCRPGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgCRPGrpAddr_Object = MibTableColumn
vRtrPimNgCRPGrpAddr = _VRtrPimNgCRPGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 4),
    _VRtrPimNgCRPGrpAddr_Type()
)
vRtrPimNgCRPGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpAddr.setStatus("obsolete")
_VRtrPimNgCRPGrpMask_Type = IpAddressPrefixLength
_VRtrPimNgCRPGrpMask_Object = MibTableColumn
vRtrPimNgCRPGrpMask = _VRtrPimNgCRPGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 5),
    _VRtrPimNgCRPGrpMask_Type()
)
vRtrPimNgCRPGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpMask.setStatus("obsolete")
_VRtrPimNgCRPHoldtime_Type = Integer32
_VRtrPimNgCRPHoldtime_Object = MibTableColumn
vRtrPimNgCRPHoldtime = _VRtrPimNgCRPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 6),
    _VRtrPimNgCRPHoldtime_Type()
)
vRtrPimNgCRPHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPHoldtime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrPimNgCRPHoldtime.setUnits("seconds")
_VRtrPimNgCRPPriority_Type = Integer32
_VRtrPimNgCRPPriority_Object = MibTableColumn
vRtrPimNgCRPPriority = _VRtrPimNgCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 7),
    _VRtrPimNgCRPPriority_Type()
)
vRtrPimNgCRPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPPriority.setStatus("obsolete")
_VRtrPimNgCRPExpiryTime_Type = Integer32
_VRtrPimNgCRPExpiryTime_Object = MibTableColumn
vRtrPimNgCRPExpiryTime = _VRtrPimNgCRPExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 13, 1, 8),
    _VRtrPimNgCRPExpiryTime_Type()
)
vRtrPimNgCRPExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPExpiryTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrPimNgCRPExpiryTime.setUnits("seconds")
_VRtrPimNgRPSetTable_Object = MibTable
vRtrPimNgRPSetTable = _VRtrPimNgRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14)
)
if mibBuilder.loadTexts:
    vRtrPimNgRPSetTable.setStatus("obsolete")
_VRtrPimNgRPSetEntry_Object = MibTableRow
vRtrPimNgRPSetEntry = _VRtrPimNgRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1)
)
vRtrPimNgRPSetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetGrpMask"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetCRPAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetCRPAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgRPSetEntry.setStatus("obsolete")


class _VRtrPimNgRPSetType_Type(Integer32):
    """Custom type vRtrPimNgRPSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2),
          ("auto-rp", 3))
    )


_VRtrPimNgRPSetType_Type.__name__ = "Integer32"
_VRtrPimNgRPSetType_Object = MibTableColumn
vRtrPimNgRPSetType = _VRtrPimNgRPSetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 1),
    _VRtrPimNgRPSetType_Type()
)
vRtrPimNgRPSetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetType.setStatus("obsolete")
_VRtrPimNgRPSetGrpAddrType_Type = InetAddressType
_VRtrPimNgRPSetGrpAddrType_Object = MibTableColumn
vRtrPimNgRPSetGrpAddrType = _VRtrPimNgRPSetGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 2),
    _VRtrPimNgRPSetGrpAddrType_Type()
)
vRtrPimNgRPSetGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetGrpAddrType.setStatus("obsolete")


class _VRtrPimNgRPSetGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgRPSetGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgRPSetGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgRPSetGrpAddr_Object = MibTableColumn
vRtrPimNgRPSetGrpAddr = _VRtrPimNgRPSetGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 3),
    _VRtrPimNgRPSetGrpAddr_Type()
)
vRtrPimNgRPSetGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetGrpAddr.setStatus("obsolete")
_VRtrPimNgRPSetGrpMask_Type = IpAddressPrefixLength
_VRtrPimNgRPSetGrpMask_Object = MibTableColumn
vRtrPimNgRPSetGrpMask = _VRtrPimNgRPSetGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 4),
    _VRtrPimNgRPSetGrpMask_Type()
)
vRtrPimNgRPSetGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetGrpMask.setStatus("obsolete")
_VRtrPimNgRPSetCRPAddrType_Type = InetAddressType
_VRtrPimNgRPSetCRPAddrType_Object = MibTableColumn
vRtrPimNgRPSetCRPAddrType = _VRtrPimNgRPSetCRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 5),
    _VRtrPimNgRPSetCRPAddrType_Type()
)
vRtrPimNgRPSetCRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetCRPAddrType.setStatus("obsolete")


class _VRtrPimNgRPSetCRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgRPSetCRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgRPSetCRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgRPSetCRPAddress_Object = MibTableColumn
vRtrPimNgRPSetCRPAddress = _VRtrPimNgRPSetCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 6),
    _VRtrPimNgRPSetCRPAddress_Type()
)
vRtrPimNgRPSetCRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetCRPAddress.setStatus("obsolete")
_VRtrPimNgRPSetHoldtime_Type = Integer32
_VRtrPimNgRPSetHoldtime_Object = MibTableColumn
vRtrPimNgRPSetHoldtime = _VRtrPimNgRPSetHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 7),
    _VRtrPimNgRPSetHoldtime_Type()
)
vRtrPimNgRPSetHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetHoldtime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetHoldtime.setUnits("seconds")
_VRtrPimNgRPSetPriority_Type = Integer32
_VRtrPimNgRPSetPriority_Object = MibTableColumn
vRtrPimNgRPSetPriority = _VRtrPimNgRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 8),
    _VRtrPimNgRPSetPriority_Type()
)
vRtrPimNgRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetPriority.setStatus("obsolete")
_VRtrPimNgRPSetExpiryTime_Type = Unsigned32
_VRtrPimNgRPSetExpiryTime_Object = MibTableColumn
vRtrPimNgRPSetExpiryTime = _VRtrPimNgRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 14, 1, 9),
    _VRtrPimNgRPSetExpiryTime_Type()
)
vRtrPimNgRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetExpiryTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetExpiryTime.setUnits("seconds")
_VRtrPimNgGenStatTable_Object = MibTable
vRtrPimNgGenStatTable = _VRtrPimNgGenStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15)
)
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTable.setStatus("current")
_VRtrPimNgGenStatEntry_Object = MibTableRow
vRtrPimNgGenStatEntry = _VRtrPimNgGenStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1)
)
if mibBuilder.loadTexts:
    vRtrPimNgGenStatEntry.setStatus("current")
_VRtrPimNgGenStatTxCrpaPdus_Type = Counter32
_VRtrPimNgGenStatTxCrpaPdus_Object = MibTableColumn
vRtrPimNgGenStatTxCrpaPdus = _VRtrPimNgGenStatTxCrpaPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 1),
    _VRtrPimNgGenStatTxCrpaPdus_Type()
)
vRtrPimNgGenStatTxCrpaPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxCrpaPdus.setStatus("current")
_VRtrPimNgGenStatTxCrpaPduErrs_Type = Counter32
_VRtrPimNgGenStatTxCrpaPduErrs_Object = MibTableColumn
vRtrPimNgGenStatTxCrpaPduErrs = _VRtrPimNgGenStatTxCrpaPduErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 2),
    _VRtrPimNgGenStatTxCrpaPduErrs_Type()
)
vRtrPimNgGenStatTxCrpaPduErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxCrpaPduErrs.setStatus("current")
_VRtrPimNgGenStatRxCrpaPdus_Type = Counter32
_VRtrPimNgGenStatRxCrpaPdus_Object = MibTableColumn
vRtrPimNgGenStatRxCrpaPdus = _VRtrPimNgGenStatRxCrpaPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 3),
    _VRtrPimNgGenStatRxCrpaPdus_Type()
)
vRtrPimNgGenStatRxCrpaPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatRxCrpaPdus.setStatus("current")
_VRtrPimNgGenStatRxCrpaPduDrops_Type = Counter32
_VRtrPimNgGenStatRxCrpaPduDrops_Object = MibTableColumn
vRtrPimNgGenStatRxCrpaPduDrops = _VRtrPimNgGenStatRxCrpaPduDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 4),
    _VRtrPimNgGenStatRxCrpaPduDrops_Type()
)
vRtrPimNgGenStatRxCrpaPduDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatRxCrpaPduDrops.setStatus("current")
_VRtrPimNgGenStatStarStarRPTypes_Type = Gauge32
_VRtrPimNgGenStatStarStarRPTypes_Object = MibTableColumn
vRtrPimNgGenStatStarStarRPTypes = _VRtrPimNgGenStatStarStarRPTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 5),
    _VRtrPimNgGenStatStarStarRPTypes_Type()
)
vRtrPimNgGenStatStarStarRPTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatStarStarRPTypes.setStatus("current")
_VRtrPimNgGenStatStarGTypes_Type = Gauge32
_VRtrPimNgGenStatStarGTypes_Object = MibTableColumn
vRtrPimNgGenStatStarGTypes = _VRtrPimNgGenStatStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 6),
    _VRtrPimNgGenStatStarGTypes_Type()
)
vRtrPimNgGenStatStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatStarGTypes.setStatus("current")
_VRtrPimNgGenStatSGTypes_Type = Gauge32
_VRtrPimNgGenStatSGTypes_Object = MibTableColumn
vRtrPimNgGenStatSGTypes = _VRtrPimNgGenStatSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 7),
    _VRtrPimNgGenStatSGTypes_Type()
)
vRtrPimNgGenStatSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatSGTypes.setStatus("current")
_VRtrPimNgGenStatTxRegisters_Type = Counter32
_VRtrPimNgGenStatTxRegisters_Object = MibTableColumn
vRtrPimNgGenStatTxRegisters = _VRtrPimNgGenStatTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 8),
    _VRtrPimNgGenStatTxRegisters_Type()
)
vRtrPimNgGenStatTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxRegisters.setStatus("current")
_VRtrPimNgGenStatTxRegisterErrs_Type = Counter32
_VRtrPimNgGenStatTxRegisterErrs_Object = MibTableColumn
vRtrPimNgGenStatTxRegisterErrs = _VRtrPimNgGenStatTxRegisterErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 9),
    _VRtrPimNgGenStatTxRegisterErrs_Type()
)
vRtrPimNgGenStatTxRegisterErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxRegisterErrs.setStatus("current")
_VRtrPimNgGenStatTxNullRegisters_Type = Counter32
_VRtrPimNgGenStatTxNullRegisters_Object = MibTableColumn
vRtrPimNgGenStatTxNullRegisters = _VRtrPimNgGenStatTxNullRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 10),
    _VRtrPimNgGenStatTxNullRegisters_Type()
)
vRtrPimNgGenStatTxNullRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxNullRegisters.setStatus("current")
_VRtrPimNgGenStatTxRegTTLDrops_Type = Counter32
_VRtrPimNgGenStatTxRegTTLDrops_Object = MibTableColumn
vRtrPimNgGenStatTxRegTTLDrops = _VRtrPimNgGenStatTxRegTTLDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 11),
    _VRtrPimNgGenStatTxRegTTLDrops_Type()
)
vRtrPimNgGenStatTxRegTTLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxRegTTLDrops.setStatus("current")
_VRtrPimNgGenStatForwardCrpaPdus_Type = Counter32
_VRtrPimNgGenStatForwardCrpaPdus_Object = MibTableColumn
vRtrPimNgGenStatForwardCrpaPdus = _VRtrPimNgGenStatForwardCrpaPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 12),
    _VRtrPimNgGenStatForwardCrpaPdus_Type()
)
vRtrPimNgGenStatForwardCrpaPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatForwardCrpaPdus.setStatus("current")
_VRtrPimNgGenStatFwdCrpaDrops_Type = Counter32
_VRtrPimNgGenStatFwdCrpaDrops_Object = MibTableColumn
vRtrPimNgGenStatFwdCrpaDrops = _VRtrPimNgGenStatFwdCrpaDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 13),
    _VRtrPimNgGenStatFwdCrpaDrops_Type()
)
vRtrPimNgGenStatFwdCrpaDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatFwdCrpaDrops.setStatus("current")
_VRtrPimNgGenStatTxMdtJoinTlvs_Type = Counter32
_VRtrPimNgGenStatTxMdtJoinTlvs_Object = MibTableColumn
vRtrPimNgGenStatTxMdtJoinTlvs = _VRtrPimNgGenStatTxMdtJoinTlvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 14),
    _VRtrPimNgGenStatTxMdtJoinTlvs_Type()
)
vRtrPimNgGenStatTxMdtJoinTlvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxMdtJoinTlvs.setStatus("current")
_VRtrPimNgGenStatRxMdtJoinTlvs_Type = Counter32
_VRtrPimNgGenStatRxMdtJoinTlvs_Object = MibTableColumn
vRtrPimNgGenStatRxMdtJoinTlvs = _VRtrPimNgGenStatRxMdtJoinTlvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 15),
    _VRtrPimNgGenStatRxMdtJoinTlvs_Type()
)
vRtrPimNgGenStatRxMdtJoinTlvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatRxMdtJoinTlvs.setStatus("current")
_VRtrPimNgGenStatTxMdtJnTlvErrs_Type = Counter32
_VRtrPimNgGenStatTxMdtJnTlvErrs_Object = MibTableColumn
vRtrPimNgGenStatTxMdtJnTlvErrs = _VRtrPimNgGenStatTxMdtJnTlvErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 16),
    _VRtrPimNgGenStatTxMdtJnTlvErrs_Type()
)
vRtrPimNgGenStatTxMdtJnTlvErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxMdtJnTlvErrs.setStatus("current")
_VRtrPimNgGenStatRxMdtJnTlvErrs_Type = Counter32
_VRtrPimNgGenStatRxMdtJnTlvErrs_Object = MibTableColumn
vRtrPimNgGenStatRxMdtJnTlvErrs = _VRtrPimNgGenStatRxMdtJnTlvErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 17),
    _VRtrPimNgGenStatRxMdtJnTlvErrs_Type()
)
vRtrPimNgGenStatRxMdtJnTlvErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatRxMdtJnTlvErrs.setStatus("current")
_VRtrPimNgGenStatTxActiveMdts_Type = Gauge32
_VRtrPimNgGenStatTxActiveMdts_Object = MibTableColumn
vRtrPimNgGenStatTxActiveMdts = _VRtrPimNgGenStatTxActiveMdts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 18),
    _VRtrPimNgGenStatTxActiveMdts_Type()
)
vRtrPimNgGenStatTxActiveMdts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxActiveMdts.setStatus("current")
_VRtrPimNgGenStatRxActiveMdts_Type = Gauge32
_VRtrPimNgGenStatRxActiveMdts_Object = MibTableColumn
vRtrPimNgGenStatRxActiveMdts = _VRtrPimNgGenStatRxActiveMdts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 19),
    _VRtrPimNgGenStatRxActiveMdts_Type()
)
vRtrPimNgGenStatRxActiveMdts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatRxActiveMdts.setStatus("current")
_VRtrPimNgGenStatTxSpmsiLimitHits_Type = Counter32
_VRtrPimNgGenStatTxSpmsiLimitHits_Object = MibTableColumn
vRtrPimNgGenStatTxSpmsiLimitHits = _VRtrPimNgGenStatTxSpmsiLimitHits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 20),
    _VRtrPimNgGenStatTxSpmsiLimitHits_Type()
)
vRtrPimNgGenStatTxSpmsiLimitHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxSpmsiLimitHits.setStatus("current")
_VRtrPimNgGenStatRxCtrlPduIfDrops_Type = Counter32
_VRtrPimNgGenStatRxCtrlPduIfDrops_Object = MibTableColumn
vRtrPimNgGenStatRxCtrlPduIfDrops = _VRtrPimNgGenStatRxCtrlPduIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 21),
    _VRtrPimNgGenStatRxCtrlPduIfDrops_Type()
)
vRtrPimNgGenStatRxCtrlPduIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatRxCtrlPduIfDrops.setStatus("current")
_VRtrPimNgGenStatP2mpPmsiReqFails_Type = Counter32
_VRtrPimNgGenStatP2mpPmsiReqFails_Object = MibTableColumn
vRtrPimNgGenStatP2mpPmsiReqFails = _VRtrPimNgGenStatP2mpPmsiReqFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 22),
    _VRtrPimNgGenStatP2mpPmsiReqFails_Type()
)
vRtrPimNgGenStatP2mpPmsiReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatP2mpPmsiReqFails.setStatus("current")
_VRtrPimNgGenStatP2mpPmsiCrtFails_Type = Counter32
_VRtrPimNgGenStatP2mpPmsiCrtFails_Object = MibTableColumn
vRtrPimNgGenStatP2mpPmsiCrtFails = _VRtrPimNgGenStatP2mpPmsiCrtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 23),
    _VRtrPimNgGenStatP2mpPmsiCrtFails_Type()
)
vRtrPimNgGenStatP2mpPmsiCrtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatP2mpPmsiCrtFails.setStatus("current")
_VRtrPimNgGenStatTxMdts_Type = Counter32
_VRtrPimNgGenStatTxMdts_Object = MibTableColumn
vRtrPimNgGenStatTxMdts = _VRtrPimNgGenStatTxMdts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 24),
    _VRtrPimNgGenStatTxMdts_Type()
)
vRtrPimNgGenStatTxMdts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatTxMdts.setStatus("current")
_VRtrPimNgGenStatRxMdts_Type = Counter32
_VRtrPimNgGenStatRxMdts_Object = MibTableColumn
vRtrPimNgGenStatRxMdts = _VRtrPimNgGenStatRxMdts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 15, 1, 25),
    _VRtrPimNgGenStatRxMdts_Type()
)
vRtrPimNgGenStatRxMdts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGenStatRxMdts.setStatus("current")
_VRtrPimNgGrpSrcStatTable_Object = MibTable
vRtrPimNgGrpSrcStatTable = _VRtrPimNgGrpSrcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16)
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatTable.setStatus("current")
_VRtrPimNgGrpSrcStatEntry_Object = MibTableRow
vRtrPimNgGrpSrcStatEntry = _VRtrPimNgGrpSrcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1)
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatEntry.setStatus("current")
_VRtrPimNgGrpSrcStatFrwdedPkts_Type = Counter32
_VRtrPimNgGrpSrcStatFrwdedPkts_Object = MibTableColumn
vRtrPimNgGrpSrcStatFrwdedPkts = _VRtrPimNgGrpSrcStatFrwdedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 1),
    _VRtrPimNgGrpSrcStatFrwdedPkts_Type()
)
vRtrPimNgGrpSrcStatFrwdedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatFrwdedPkts.setStatus("current")
_VRtrPimNgGrpSrcStatOFFrwdedPkts_Type = Counter32
_VRtrPimNgGrpSrcStatOFFrwdedPkts_Object = MibTableColumn
vRtrPimNgGrpSrcStatOFFrwdedPkts = _VRtrPimNgGrpSrcStatOFFrwdedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 2),
    _VRtrPimNgGrpSrcStatOFFrwdedPkts_Type()
)
vRtrPimNgGrpSrcStatOFFrwdedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatOFFrwdedPkts.setStatus("current")
_VRtrPimNgGrpSrcStatHCFrwdedPkts_Type = Counter64
_VRtrPimNgGrpSrcStatHCFrwdedPkts_Object = MibTableColumn
vRtrPimNgGrpSrcStatHCFrwdedPkts = _VRtrPimNgGrpSrcStatHCFrwdedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 3),
    _VRtrPimNgGrpSrcStatHCFrwdedPkts_Type()
)
vRtrPimNgGrpSrcStatHCFrwdedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatHCFrwdedPkts.setStatus("current")
_VRtrPimNgGrpSrcStatDscrdPkts_Type = Counter32
_VRtrPimNgGrpSrcStatDscrdPkts_Object = MibTableColumn
vRtrPimNgGrpSrcStatDscrdPkts = _VRtrPimNgGrpSrcStatDscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 4),
    _VRtrPimNgGrpSrcStatDscrdPkts_Type()
)
vRtrPimNgGrpSrcStatDscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatDscrdPkts.setStatus("current")
_VRtrPimNgGrpSrcStatOFDscrdPkts_Type = Counter32
_VRtrPimNgGrpSrcStatOFDscrdPkts_Object = MibTableColumn
vRtrPimNgGrpSrcStatOFDscrdPkts = _VRtrPimNgGrpSrcStatOFDscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 5),
    _VRtrPimNgGrpSrcStatOFDscrdPkts_Type()
)
vRtrPimNgGrpSrcStatOFDscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatOFDscrdPkts.setStatus("current")
_VRtrPimNgGrpSrcStatHCDscrdPkts_Type = Counter64
_VRtrPimNgGrpSrcStatHCDscrdPkts_Object = MibTableColumn
vRtrPimNgGrpSrcStatHCDscrdPkts = _VRtrPimNgGrpSrcStatHCDscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 6),
    _VRtrPimNgGrpSrcStatHCDscrdPkts_Type()
)
vRtrPimNgGrpSrcStatHCDscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatHCDscrdPkts.setStatus("current")
_VRtrPimNgGrpSrcStatRPFMsmtch_Type = Counter32
_VRtrPimNgGrpSrcStatRPFMsmtch_Object = MibTableColumn
vRtrPimNgGrpSrcStatRPFMsmtch = _VRtrPimNgGrpSrcStatRPFMsmtch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 7),
    _VRtrPimNgGrpSrcStatRPFMsmtch_Type()
)
vRtrPimNgGrpSrcStatRPFMsmtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatRPFMsmtch.setStatus("current")
_VRtrPimNgGrpSrcStatOFRPFMsmtch_Type = Counter32
_VRtrPimNgGrpSrcStatOFRPFMsmtch_Object = MibTableColumn
vRtrPimNgGrpSrcStatOFRPFMsmtch = _VRtrPimNgGrpSrcStatOFRPFMsmtch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 8),
    _VRtrPimNgGrpSrcStatOFRPFMsmtch_Type()
)
vRtrPimNgGrpSrcStatOFRPFMsmtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatOFRPFMsmtch.setStatus("current")
_VRtrPimNgGrpSrcStatHCRPFMsmtch_Type = Counter64
_VRtrPimNgGrpSrcStatHCRPFMsmtch_Object = MibTableColumn
vRtrPimNgGrpSrcStatHCRPFMsmtch = _VRtrPimNgGrpSrcStatHCRPFMsmtch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 9),
    _VRtrPimNgGrpSrcStatHCRPFMsmtch_Type()
)
vRtrPimNgGrpSrcStatHCRPFMsmtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatHCRPFMsmtch.setStatus("current")
_VRtrPimNgGrpSrcStatFrdedOct_Type = Counter32
_VRtrPimNgGrpSrcStatFrdedOct_Object = MibTableColumn
vRtrPimNgGrpSrcStatFrdedOct = _VRtrPimNgGrpSrcStatFrdedOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 10),
    _VRtrPimNgGrpSrcStatFrdedOct_Type()
)
vRtrPimNgGrpSrcStatFrdedOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatFrdedOct.setStatus("current")
_VRtrPimNgGrpSrcStatOFFrdedOct_Type = Counter32
_VRtrPimNgGrpSrcStatOFFrdedOct_Object = MibTableColumn
vRtrPimNgGrpSrcStatOFFrdedOct = _VRtrPimNgGrpSrcStatOFFrdedOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 11),
    _VRtrPimNgGrpSrcStatOFFrdedOct_Type()
)
vRtrPimNgGrpSrcStatOFFrdedOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatOFFrdedOct.setStatus("current")
_VRtrPimNgGrpSrcStatHCFrdedOct_Type = Counter64
_VRtrPimNgGrpSrcStatHCFrdedOct_Object = MibTableColumn
vRtrPimNgGrpSrcStatHCFrdedOct = _VRtrPimNgGrpSrcStatHCFrdedOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 16, 1, 12),
    _VRtrPimNgGrpSrcStatHCFrdedOct_Type()
)
vRtrPimNgGrpSrcStatHCFrdedOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcStatHCFrdedOct.setStatus("current")
_VRtrPimNgGenPolicyTable_Object = MibTable
vRtrPimNgGenPolicyTable = _VRtrPimNgGenPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17)
)
if mibBuilder.loadTexts:
    vRtrPimNgGenPolicyTable.setStatus("current")
_VRtrPimNgGenPolicyEntry_Object = MibTableRow
vRtrPimNgGenPolicyEntry = _VRtrPimNgGenPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1)
)
if mibBuilder.loadTexts:
    vRtrPimNgGenPolicyEntry.setStatus("current")


class _VRtrPimNgImportJoinPrunePolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportJoinPrunePolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportJoinPrunePolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportJoinPrunePolicy1_Object = MibTableColumn
vRtrPimNgImportJoinPrunePolicy1 = _VRtrPimNgImportJoinPrunePolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 1),
    _VRtrPimNgImportJoinPrunePolicy1_Type()
)
vRtrPimNgImportJoinPrunePolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportJoinPrunePolicy1.setStatus("current")


class _VRtrPimNgImportJoinPrunePolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportJoinPrunePolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportJoinPrunePolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportJoinPrunePolicy2_Object = MibTableColumn
vRtrPimNgImportJoinPrunePolicy2 = _VRtrPimNgImportJoinPrunePolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 2),
    _VRtrPimNgImportJoinPrunePolicy2_Type()
)
vRtrPimNgImportJoinPrunePolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportJoinPrunePolicy2.setStatus("current")


class _VRtrPimNgImportJoinPrunePolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportJoinPrunePolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportJoinPrunePolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportJoinPrunePolicy3_Object = MibTableColumn
vRtrPimNgImportJoinPrunePolicy3 = _VRtrPimNgImportJoinPrunePolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 3),
    _VRtrPimNgImportJoinPrunePolicy3_Type()
)
vRtrPimNgImportJoinPrunePolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportJoinPrunePolicy3.setStatus("current")


class _VRtrPimNgImportJoinPrunePolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportJoinPrunePolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportJoinPrunePolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportJoinPrunePolicy4_Object = MibTableColumn
vRtrPimNgImportJoinPrunePolicy4 = _VRtrPimNgImportJoinPrunePolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 4),
    _VRtrPimNgImportJoinPrunePolicy4_Type()
)
vRtrPimNgImportJoinPrunePolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportJoinPrunePolicy4.setStatus("current")


class _VRtrPimNgImportJoinPrunePolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportJoinPrunePolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportJoinPrunePolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportJoinPrunePolicy5_Object = MibTableColumn
vRtrPimNgImportJoinPrunePolicy5 = _VRtrPimNgImportJoinPrunePolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 5),
    _VRtrPimNgImportJoinPrunePolicy5_Type()
)
vRtrPimNgImportJoinPrunePolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportJoinPrunePolicy5.setStatus("current")


class _VRtrPimNgImportRegisterPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportRegisterPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportRegisterPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportRegisterPolicy1_Object = MibTableColumn
vRtrPimNgImportRegisterPolicy1 = _VRtrPimNgImportRegisterPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 6),
    _VRtrPimNgImportRegisterPolicy1_Type()
)
vRtrPimNgImportRegisterPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportRegisterPolicy1.setStatus("current")


class _VRtrPimNgImportRegisterPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportRegisterPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportRegisterPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportRegisterPolicy2_Object = MibTableColumn
vRtrPimNgImportRegisterPolicy2 = _VRtrPimNgImportRegisterPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 7),
    _VRtrPimNgImportRegisterPolicy2_Type()
)
vRtrPimNgImportRegisterPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportRegisterPolicy2.setStatus("current")


class _VRtrPimNgImportRegisterPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportRegisterPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportRegisterPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportRegisterPolicy3_Object = MibTableColumn
vRtrPimNgImportRegisterPolicy3 = _VRtrPimNgImportRegisterPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 8),
    _VRtrPimNgImportRegisterPolicy3_Type()
)
vRtrPimNgImportRegisterPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportRegisterPolicy3.setStatus("current")


class _VRtrPimNgImportRegisterPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportRegisterPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportRegisterPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportRegisterPolicy4_Object = MibTableColumn
vRtrPimNgImportRegisterPolicy4 = _VRtrPimNgImportRegisterPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 9),
    _VRtrPimNgImportRegisterPolicy4_Type()
)
vRtrPimNgImportRegisterPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportRegisterPolicy4.setStatus("current")


class _VRtrPimNgImportRegisterPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportRegisterPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportRegisterPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportRegisterPolicy5_Object = MibTableColumn
vRtrPimNgImportRegisterPolicy5 = _VRtrPimNgImportRegisterPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 10),
    _VRtrPimNgImportRegisterPolicy5_Type()
)
vRtrPimNgImportRegisterPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportRegisterPolicy5.setStatus("current")


class _VRtrPimNgImportBootstrapPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportBootstrapPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportBootstrapPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportBootstrapPolicy1_Object = MibTableColumn
vRtrPimNgImportBootstrapPolicy1 = _VRtrPimNgImportBootstrapPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 11),
    _VRtrPimNgImportBootstrapPolicy1_Type()
)
vRtrPimNgImportBootstrapPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportBootstrapPolicy1.setStatus("current")


class _VRtrPimNgImportBootstrapPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportBootstrapPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportBootstrapPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportBootstrapPolicy2_Object = MibTableColumn
vRtrPimNgImportBootstrapPolicy2 = _VRtrPimNgImportBootstrapPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 12),
    _VRtrPimNgImportBootstrapPolicy2_Type()
)
vRtrPimNgImportBootstrapPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportBootstrapPolicy2.setStatus("current")


class _VRtrPimNgImportBootstrapPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportBootstrapPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportBootstrapPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportBootstrapPolicy3_Object = MibTableColumn
vRtrPimNgImportBootstrapPolicy3 = _VRtrPimNgImportBootstrapPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 13),
    _VRtrPimNgImportBootstrapPolicy3_Type()
)
vRtrPimNgImportBootstrapPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportBootstrapPolicy3.setStatus("current")


class _VRtrPimNgImportBootstrapPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportBootstrapPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportBootstrapPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportBootstrapPolicy4_Object = MibTableColumn
vRtrPimNgImportBootstrapPolicy4 = _VRtrPimNgImportBootstrapPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 14),
    _VRtrPimNgImportBootstrapPolicy4_Type()
)
vRtrPimNgImportBootstrapPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportBootstrapPolicy4.setStatus("current")


class _VRtrPimNgImportBootstrapPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgImportBootstrapPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgImportBootstrapPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgImportBootstrapPolicy5_Object = MibTableColumn
vRtrPimNgImportBootstrapPolicy5 = _VRtrPimNgImportBootstrapPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 15),
    _VRtrPimNgImportBootstrapPolicy5_Type()
)
vRtrPimNgImportBootstrapPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgImportBootstrapPolicy5.setStatus("current")


class _VRtrPimNgExportBootstrapPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgExportBootstrapPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgExportBootstrapPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgExportBootstrapPolicy1_Object = MibTableColumn
vRtrPimNgExportBootstrapPolicy1 = _VRtrPimNgExportBootstrapPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 16),
    _VRtrPimNgExportBootstrapPolicy1_Type()
)
vRtrPimNgExportBootstrapPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgExportBootstrapPolicy1.setStatus("current")


class _VRtrPimNgExportBootstrapPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgExportBootstrapPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgExportBootstrapPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgExportBootstrapPolicy2_Object = MibTableColumn
vRtrPimNgExportBootstrapPolicy2 = _VRtrPimNgExportBootstrapPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 17),
    _VRtrPimNgExportBootstrapPolicy2_Type()
)
vRtrPimNgExportBootstrapPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgExportBootstrapPolicy2.setStatus("current")


class _VRtrPimNgExportBootstrapPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgExportBootstrapPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgExportBootstrapPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgExportBootstrapPolicy3_Object = MibTableColumn
vRtrPimNgExportBootstrapPolicy3 = _VRtrPimNgExportBootstrapPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 18),
    _VRtrPimNgExportBootstrapPolicy3_Type()
)
vRtrPimNgExportBootstrapPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgExportBootstrapPolicy3.setStatus("current")


class _VRtrPimNgExportBootstrapPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgExportBootstrapPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgExportBootstrapPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgExportBootstrapPolicy4_Object = MibTableColumn
vRtrPimNgExportBootstrapPolicy4 = _VRtrPimNgExportBootstrapPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 19),
    _VRtrPimNgExportBootstrapPolicy4_Type()
)
vRtrPimNgExportBootstrapPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgExportBootstrapPolicy4.setStatus("current")


class _VRtrPimNgExportBootstrapPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimNgExportBootstrapPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimNgExportBootstrapPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimNgExportBootstrapPolicy5_Object = MibTableColumn
vRtrPimNgExportBootstrapPolicy5 = _VRtrPimNgExportBootstrapPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 17, 1, 20),
    _VRtrPimNgExportBootstrapPolicy5_Type()
)
vRtrPimNgExportBootstrapPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgExportBootstrapPolicy5.setStatus("current")
_VRtrPimNgSSMGroupTableLstChngd_Type = TimeStamp
_VRtrPimNgSSMGroupTableLstChngd_Object = MibScalar
vRtrPimNgSSMGroupTableLstChngd = _VRtrPimNgSSMGroupTableLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 18),
    _VRtrPimNgSSMGroupTableLstChngd_Type()
)
vRtrPimNgSSMGroupTableLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupTableLstChngd.setStatus("current")
_VRtrPimNgSSMGroupTable_Object = MibTable
vRtrPimNgSSMGroupTable = _VRtrPimNgSSMGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 19)
)
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupTable.setStatus("current")
_VRtrPimNgSSMGroupEntry_Object = MibTableRow
vRtrPimNgSSMGroupEntry = _VRtrPimNgSSMGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 19, 1)
)
vRtrPimNgSSMGroupEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupAddressType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupEntry.setStatus("current")
_VRtrPimNgSSMGroupAddressType_Type = InetAddressType
_VRtrPimNgSSMGroupAddressType_Object = MibTableColumn
vRtrPimNgSSMGroupAddressType = _VRtrPimNgSSMGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 19, 1, 1),
    _VRtrPimNgSSMGroupAddressType_Type()
)
vRtrPimNgSSMGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupAddressType.setStatus("current")


class _VRtrPimNgSSMGroupAddress_Type(InetAddress):
    """Custom type vRtrPimNgSSMGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgSSMGroupAddress_Type.__name__ = "InetAddress"
_VRtrPimNgSSMGroupAddress_Object = MibTableColumn
vRtrPimNgSSMGroupAddress = _VRtrPimNgSSMGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 19, 1, 2),
    _VRtrPimNgSSMGroupAddress_Type()
)
vRtrPimNgSSMGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupAddress.setStatus("current")
_VRtrPimNgSSMGroupMask_Type = InetAddressPrefixLength
_VRtrPimNgSSMGroupMask_Object = MibTableColumn
vRtrPimNgSSMGroupMask = _VRtrPimNgSSMGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 19, 1, 3),
    _VRtrPimNgSSMGroupMask_Type()
)
vRtrPimNgSSMGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupMask.setStatus("current")
_VRtrPimNgSSMGroupRowStatus_Type = RowStatus
_VRtrPimNgSSMGroupRowStatus_Object = MibTableColumn
vRtrPimNgSSMGroupRowStatus = _VRtrPimNgSSMGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 19, 1, 4),
    _VRtrPimNgSSMGroupRowStatus_Type()
)
vRtrPimNgSSMGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupRowStatus.setStatus("current")
_VRtrPimNgSSMGroupRowLastChanged_Type = TimeStamp
_VRtrPimNgSSMGroupRowLastChanged_Object = MibTableColumn
vRtrPimNgSSMGroupRowLastChanged = _VRtrPimNgSSMGroupRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 19, 1, 5),
    _VRtrPimNgSSMGroupRowLastChanged_Type()
)
vRtrPimNgSSMGroupRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgSSMGroupRowLastChanged.setStatus("current")
_VRtrPimNgAnycastRPTableLstChngd_Type = TimeStamp
_VRtrPimNgAnycastRPTableLstChngd_Object = MibScalar
vRtrPimNgAnycastRPTableLstChngd = _VRtrPimNgAnycastRPTableLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 20),
    _VRtrPimNgAnycastRPTableLstChngd_Type()
)
vRtrPimNgAnycastRPTableLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPTableLstChngd.setStatus("current")
_VRtrPimNgAnycastRPTable_Object = MibTable
vRtrPimNgAnycastRPTable = _VRtrPimNgAnycastRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21)
)
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPTable.setStatus("current")
_VRtrPimNgAnycastRPEntry_Object = MibTableRow
vRtrPimNgAnycastRPEntry = _VRtrPimNgAnycastRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21, 1)
)
vRtrPimNgAnycastRPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPAddressType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPPeerAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPEntry.setStatus("current")
_VRtrPimNgAnycastRPAddressType_Type = InetAddressType
_VRtrPimNgAnycastRPAddressType_Object = MibTableColumn
vRtrPimNgAnycastRPAddressType = _VRtrPimNgAnycastRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21, 1, 1),
    _VRtrPimNgAnycastRPAddressType_Type()
)
vRtrPimNgAnycastRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPAddressType.setStatus("current")


class _VRtrPimNgAnycastRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgAnycastRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAnycastRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAnycastRPAddress_Object = MibTableColumn
vRtrPimNgAnycastRPAddress = _VRtrPimNgAnycastRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21, 1, 2),
    _VRtrPimNgAnycastRPAddress_Type()
)
vRtrPimNgAnycastRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPAddress.setStatus("current")
_VRtrPimNgAnycastRPPeerAddrType_Type = InetAddressType
_VRtrPimNgAnycastRPPeerAddrType_Object = MibTableColumn
vRtrPimNgAnycastRPPeerAddrType = _VRtrPimNgAnycastRPPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21, 1, 3),
    _VRtrPimNgAnycastRPPeerAddrType_Type()
)
vRtrPimNgAnycastRPPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPPeerAddrType.setStatus("current")


class _VRtrPimNgAnycastRPPeerAddress_Type(InetAddress):
    """Custom type vRtrPimNgAnycastRPPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAnycastRPPeerAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAnycastRPPeerAddress_Object = MibTableColumn
vRtrPimNgAnycastRPPeerAddress = _VRtrPimNgAnycastRPPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21, 1, 4),
    _VRtrPimNgAnycastRPPeerAddress_Type()
)
vRtrPimNgAnycastRPPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPPeerAddress.setStatus("current")
_VRtrPimNgAnycastRPRowStatus_Type = RowStatus
_VRtrPimNgAnycastRPRowStatus_Object = MibTableColumn
vRtrPimNgAnycastRPRowStatus = _VRtrPimNgAnycastRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21, 1, 5),
    _VRtrPimNgAnycastRPRowStatus_Type()
)
vRtrPimNgAnycastRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPRowStatus.setStatus("current")
_VRtrPimNgAnycastRPRowLstChanged_Type = TimeStamp
_VRtrPimNgAnycastRPRowLstChanged_Object = MibTableColumn
vRtrPimNgAnycastRPRowLstChanged = _VRtrPimNgAnycastRPRowLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 21, 1, 6),
    _VRtrPimNgAnycastRPRowLstChanged_Type()
)
vRtrPimNgAnycastRPRowLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAnycastRPRowLstChanged.setStatus("current")
_VRtrPimNgSptSwOvrThdTabLstChngd_Type = TimeStamp
_VRtrPimNgSptSwOvrThdTabLstChngd_Object = MibScalar
vRtrPimNgSptSwOvrThdTabLstChngd = _VRtrPimNgSptSwOvrThdTabLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 22),
    _VRtrPimNgSptSwOvrThdTabLstChngd_Type()
)
vRtrPimNgSptSwOvrThdTabLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwOvrThdTabLstChngd.setStatus("current")
_VRtrPimNgSptSwitchoverThdTable_Object = MibTable
vRtrPimNgSptSwitchoverThdTable = _VRtrPimNgSptSwitchoverThdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23)
)
if mibBuilder.loadTexts:
    vRtrPimNgSptSwitchoverThdTable.setStatus("current")
_VRtrPimNgSptSwitchoverThdEntry_Object = MibTableRow
vRtrPimNgSptSwitchoverThdEntry = _VRtrPimNgSptSwitchoverThdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23, 1)
)
vRtrPimNgSptSwitchoverThdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwOvrThdTblGpAdType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwOvrThdTblGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwOvrThdTblGpAdMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgSptSwitchoverThdEntry.setStatus("current")
_VRtrPimNgSptSwOvrThdTblGpAdType_Type = InetAddressType
_VRtrPimNgSptSwOvrThdTblGpAdType_Object = MibTableColumn
vRtrPimNgSptSwOvrThdTblGpAdType = _VRtrPimNgSptSwOvrThdTblGpAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23, 1, 1),
    _VRtrPimNgSptSwOvrThdTblGpAdType_Type()
)
vRtrPimNgSptSwOvrThdTblGpAdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwOvrThdTblGpAdType.setStatus("current")


class _VRtrPimNgSptSwOvrThdTblGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgSptSwOvrThdTblGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgSptSwOvrThdTblGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgSptSwOvrThdTblGrpAddr_Object = MibTableColumn
vRtrPimNgSptSwOvrThdTblGrpAddr = _VRtrPimNgSptSwOvrThdTblGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23, 1, 2),
    _VRtrPimNgSptSwOvrThdTblGrpAddr_Type()
)
vRtrPimNgSptSwOvrThdTblGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwOvrThdTblGrpAddr.setStatus("current")
_VRtrPimNgSptSwOvrThdTblGpAdMask_Type = InetAddressPrefixLength
_VRtrPimNgSptSwOvrThdTblGpAdMask_Object = MibTableColumn
vRtrPimNgSptSwOvrThdTblGpAdMask = _VRtrPimNgSptSwOvrThdTblGpAdMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23, 1, 3),
    _VRtrPimNgSptSwOvrThdTblGpAdMask_Type()
)
vRtrPimNgSptSwOvrThdTblGpAdMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwOvrThdTblGpAdMask.setStatus("current")
_VRtrPimNgSptSwovrThdRowStatus_Type = RowStatus
_VRtrPimNgSptSwovrThdRowStatus_Object = MibTableColumn
vRtrPimNgSptSwovrThdRowStatus = _VRtrPimNgSptSwovrThdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23, 1, 4),
    _VRtrPimNgSptSwovrThdRowStatus_Type()
)
vRtrPimNgSptSwovrThdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwovrThdRowStatus.setStatus("current")
_VRtrPimNgSptSwovrThdRowLstChngd_Type = TimeStamp
_VRtrPimNgSptSwovrThdRowLstChngd_Object = MibTableColumn
vRtrPimNgSptSwovrThdRowLstChngd = _VRtrPimNgSptSwovrThdRowLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23, 1, 5),
    _VRtrPimNgSptSwovrThdRowLstChngd_Type()
)
vRtrPimNgSptSwovrThdRowLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwovrThdRowLstChngd.setStatus("current")


class _VRtrPimNgSptSwitchoverThd_Type(Unsigned32):
    """Custom type vRtrPimNgSptSwitchoverThd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrPimNgSptSwitchoverThd_Type.__name__ = "Unsigned32"
_VRtrPimNgSptSwitchoverThd_Object = MibTableColumn
vRtrPimNgSptSwitchoverThd = _VRtrPimNgSptSwitchoverThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 23, 1, 6),
    _VRtrPimNgSptSwitchoverThd_Type()
)
vRtrPimNgSptSwitchoverThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwitchoverThd.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgSptSwitchoverThd.setUnits("kbps")
_VRtrPimNgDataMtThdTableLstChngd_Type = TimeStamp
_VRtrPimNgDataMtThdTableLstChngd_Object = MibScalar
vRtrPimNgDataMtThdTableLstChngd = _VRtrPimNgDataMtThdTableLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 24),
    _VRtrPimNgDataMtThdTableLstChngd_Type()
)
vRtrPimNgDataMtThdTableLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdTableLstChngd.setStatus("current")
_VRtrPimNgDataMtThdTable_Object = MibTable
vRtrPimNgDataMtThdTable = _VRtrPimNgDataMtThdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25)
)
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdTable.setStatus("current")
_VRtrPimNgDataMtThdEntry_Object = MibTableRow
vRtrPimNgDataMtThdEntry = _VRtrPimNgDataMtThdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25, 1)
)
vRtrPimNgDataMtThdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdTblGrpAdrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdTblGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdTblGrpAdrMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdEntry.setStatus("current")
_VRtrPimNgDataMtThdTblGrpAdrType_Type = InetAddressType
_VRtrPimNgDataMtThdTblGrpAdrType_Object = MibTableColumn
vRtrPimNgDataMtThdTblGrpAdrType = _VRtrPimNgDataMtThdTblGrpAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25, 1, 1),
    _VRtrPimNgDataMtThdTblGrpAdrType_Type()
)
vRtrPimNgDataMtThdTblGrpAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdTblGrpAdrType.setStatus("current")


class _VRtrPimNgDataMtThdTblGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgDataMtThdTblGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgDataMtThdTblGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgDataMtThdTblGrpAddr_Object = MibTableColumn
vRtrPimNgDataMtThdTblGrpAddr = _VRtrPimNgDataMtThdTblGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25, 1, 2),
    _VRtrPimNgDataMtThdTblGrpAddr_Type()
)
vRtrPimNgDataMtThdTblGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdTblGrpAddr.setStatus("current")
_VRtrPimNgDataMtThdTblGrpAdrMask_Type = InetAddressPrefixLength
_VRtrPimNgDataMtThdTblGrpAdrMask_Object = MibTableColumn
vRtrPimNgDataMtThdTblGrpAdrMask = _VRtrPimNgDataMtThdTblGrpAdrMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25, 1, 3),
    _VRtrPimNgDataMtThdTblGrpAdrMask_Type()
)
vRtrPimNgDataMtThdTblGrpAdrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdTblGrpAdrMask.setStatus("current")
_VRtrPimNgDataMtThdRowStatus_Type = RowStatus
_VRtrPimNgDataMtThdRowStatus_Object = MibTableColumn
vRtrPimNgDataMtThdRowStatus = _VRtrPimNgDataMtThdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25, 1, 4),
    _VRtrPimNgDataMtThdRowStatus_Type()
)
vRtrPimNgDataMtThdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdRowStatus.setStatus("current")
_VRtrPimNgDataMtThdRowLstChngd_Type = TimeStamp
_VRtrPimNgDataMtThdRowLstChngd_Object = MibTableColumn
vRtrPimNgDataMtThdRowLstChngd = _VRtrPimNgDataMtThdRowLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25, 1, 5),
    _VRtrPimNgDataMtThdRowLstChngd_Type()
)
vRtrPimNgDataMtThdRowLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThdRowLstChngd.setStatus("current")


class _VRtrPimNgDataMtThd_Type(Unsigned32):
    """Custom type vRtrPimNgDataMtThd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_VRtrPimNgDataMtThd_Type.__name__ = "Unsigned32"
_VRtrPimNgDataMtThd_Object = MibTableColumn
vRtrPimNgDataMtThd = _VRtrPimNgDataMtThd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 25, 1, 6),
    _VRtrPimNgDataMtThd_Type()
)
vRtrPimNgDataMtThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThd.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtThd.setUnits("kbps")
_VRtrPimNgIfMcacLevelTblLstChngd_Type = TimeStamp
_VRtrPimNgIfMcacLevelTblLstChngd_Object = MibScalar
vRtrPimNgIfMcacLevelTblLstChngd = _VRtrPimNgIfMcacLevelTblLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 26),
    _VRtrPimNgIfMcacLevelTblLstChngd_Type()
)
vRtrPimNgIfMcacLevelTblLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLevelTblLstChngd.setStatus("current")
_VRtrPimNgIfMcacLevelTable_Object = MibTable
vRtrPimNgIfMcacLevelTable = _VRtrPimNgIfMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 27)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLevelTable.setStatus("current")
_VRtrPimNgIfMcacLevelEntry_Object = MibTableRow
vRtrPimNgIfMcacLevelEntry = _VRtrPimNgIfMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 27, 1)
)
vRtrPimNgIfMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLevelEntry.setStatus("current")
_VRtrPimNgIfMcacLevelRowStatus_Type = RowStatus
_VRtrPimNgIfMcacLevelRowStatus_Object = MibTableColumn
vRtrPimNgIfMcacLevelRowStatus = _VRtrPimNgIfMcacLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 27, 1, 1),
    _VRtrPimNgIfMcacLevelRowStatus_Type()
)
vRtrPimNgIfMcacLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLevelRowStatus.setStatus("current")
_VRtrPimNgIfMcacLvlRowLstChngd_Type = TimeStamp
_VRtrPimNgIfMcacLvlRowLstChngd_Object = MibTableColumn
vRtrPimNgIfMcacLvlRowLstChngd = _VRtrPimNgIfMcacLvlRowLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 27, 1, 2),
    _VRtrPimNgIfMcacLvlRowLstChngd_Type()
)
vRtrPimNgIfMcacLvlRowLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLvlRowLstChngd.setStatus("current")


class _VRtrPimNgIfMcacLevelBW_Type(Unsigned32):
    """Custom type vRtrPimNgIfMcacLevelBW based on Unsigned32"""
    defaultValue = 1


_VRtrPimNgIfMcacLevelBW_Type.__name__ = "Unsigned32"
_VRtrPimNgIfMcacLevelBW_Object = MibTableColumn
vRtrPimNgIfMcacLevelBW = _VRtrPimNgIfMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 27, 1, 3),
    _VRtrPimNgIfMcacLevelBW_Type()
)
vRtrPimNgIfMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLevelBW.setUnits("kbps")
_VRtrPimNgIfMcacLagTableLstChngd_Type = TimeStamp
_VRtrPimNgIfMcacLagTableLstChngd_Object = MibScalar
vRtrPimNgIfMcacLagTableLstChngd = _VRtrPimNgIfMcacLagTableLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 28),
    _VRtrPimNgIfMcacLagTableLstChngd_Type()
)
vRtrPimNgIfMcacLagTableLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLagTableLstChngd.setStatus("current")
_VRtrPimNgIfMcacLagTable_Object = MibTable
vRtrPimNgIfMcacLagTable = _VRtrPimNgIfMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 29)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLagTable.setStatus("current")
_VRtrPimNgIfMcacLagEntry_Object = MibTableRow
vRtrPimNgIfMcacLagEntry = _VRtrPimNgIfMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 29, 1)
)
vRtrPimNgIfMcacLagEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLagEntry.setStatus("current")
_VRtrPimNgIfMcacLagRowStatus_Type = RowStatus
_VRtrPimNgIfMcacLagRowStatus_Object = MibTableColumn
vRtrPimNgIfMcacLagRowStatus = _VRtrPimNgIfMcacLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 29, 1, 1),
    _VRtrPimNgIfMcacLagRowStatus_Type()
)
vRtrPimNgIfMcacLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLagRowStatus.setStatus("current")
_VRtrPimNgIfMcacLagRowLstChngd_Type = TimeStamp
_VRtrPimNgIfMcacLagRowLstChngd_Object = MibTableColumn
vRtrPimNgIfMcacLagRowLstChngd = _VRtrPimNgIfMcacLagRowLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 29, 1, 2),
    _VRtrPimNgIfMcacLagRowLstChngd_Type()
)
vRtrPimNgIfMcacLagRowLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLagRowLstChngd.setStatus("current")


class _VRtrPimNgIfMcacLagLevel_Type(Unsigned32):
    """Custom type vRtrPimNgIfMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VRtrPimNgIfMcacLagLevel_Type.__name__ = "Unsigned32"
_VRtrPimNgIfMcacLagLevel_Object = MibTableColumn
vRtrPimNgIfMcacLagLevel = _VRtrPimNgIfMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 29, 1, 3),
    _VRtrPimNgIfMcacLagLevel_Type()
)
vRtrPimNgIfMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacLagLevel.setStatus("current")
_VRtrPimNgERPGrpPrfxTblLstChnged_Type = TimeStamp
_VRtrPimNgERPGrpPrfxTblLstChnged_Object = MibScalar
vRtrPimNgERPGrpPrfxTblLstChnged = _VRtrPimNgERPGrpPrfxTblLstChnged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 30),
    _VRtrPimNgERPGrpPrfxTblLstChnged_Type()
)
vRtrPimNgERPGrpPrfxTblLstChnged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgERPGrpPrfxTblLstChnged.setStatus("current")
_VRtrPimNgERPGrpPrefixTable_Object = MibTable
vRtrPimNgERPGrpPrefixTable = _VRtrPimNgERPGrpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 31)
)
if mibBuilder.loadTexts:
    vRtrPimNgERPGrpPrefixTable.setStatus("current")
_VRtrPimNgERPGrpPrefixEntry_Object = MibTableRow
vRtrPimNgERPGrpPrefixEntry = _VRtrPimNgERPGrpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 31, 1)
)
vRtrPimNgERPGrpPrefixEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgERPGrpPrfixGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgERPGrpPrefixGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgERPGrpPrefixGrpMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgERPGrpPrefixEntry.setStatus("current")
_VRtrPimNgERPGrpPrfixGrpAddrType_Type = InetAddressType
_VRtrPimNgERPGrpPrfixGrpAddrType_Object = MibTableColumn
vRtrPimNgERPGrpPrfixGrpAddrType = _VRtrPimNgERPGrpPrfixGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 31, 1, 1),
    _VRtrPimNgERPGrpPrfixGrpAddrType_Type()
)
vRtrPimNgERPGrpPrfixGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgERPGrpPrfixGrpAddrType.setStatus("current")


class _VRtrPimNgERPGrpPrefixGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgERPGrpPrefixGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VRtrPimNgERPGrpPrefixGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgERPGrpPrefixGrpAddr_Object = MibTableColumn
vRtrPimNgERPGrpPrefixGrpAddr = _VRtrPimNgERPGrpPrefixGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 31, 1, 2),
    _VRtrPimNgERPGrpPrefixGrpAddr_Type()
)
vRtrPimNgERPGrpPrefixGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgERPGrpPrefixGrpAddr.setStatus("current")
_VRtrPimNgERPGrpPrefixGrpMask_Type = InetAddressPrefixLength
_VRtrPimNgERPGrpPrefixGrpMask_Object = MibTableColumn
vRtrPimNgERPGrpPrefixGrpMask = _VRtrPimNgERPGrpPrefixGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 31, 1, 3),
    _VRtrPimNgERPGrpPrefixGrpMask_Type()
)
vRtrPimNgERPGrpPrefixGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgERPGrpPrefixGrpMask.setStatus("current")
_VRtrPimNgERPGrpPrefixRowStatus_Type = RowStatus
_VRtrPimNgERPGrpPrefixRowStatus_Object = MibTableColumn
vRtrPimNgERPGrpPrefixRowStatus = _VRtrPimNgERPGrpPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 31, 1, 4),
    _VRtrPimNgERPGrpPrefixRowStatus_Type()
)
vRtrPimNgERPGrpPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgERPGrpPrefixRowStatus.setStatus("current")
_VRtrPimNgRsvpIfTable_Object = MibTable
vRtrPimNgRsvpIfTable = _VRtrPimNgRsvpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32)
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfTable.setStatus("current")
_VRtrPimNgRsvpIfEntry_Object = MibTableRow
vRtrPimNgRsvpIfEntry = _VRtrPimNgRsvpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32, 1)
)
vRtrPimNgRsvpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIfLspName"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIfSenderAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIfSenderAddr"),
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfEntry.setStatus("current")
_VRtrPimNgRsvpIfLspName_Type = TNamedItem
_VRtrPimNgRsvpIfLspName_Object = MibTableColumn
vRtrPimNgRsvpIfLspName = _VRtrPimNgRsvpIfLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32, 1, 1),
    _VRtrPimNgRsvpIfLspName_Type()
)
vRtrPimNgRsvpIfLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfLspName.setStatus("current")
_VRtrPimNgRsvpIfSenderAddrType_Type = InetAddressType
_VRtrPimNgRsvpIfSenderAddrType_Object = MibTableColumn
vRtrPimNgRsvpIfSenderAddrType = _VRtrPimNgRsvpIfSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32, 1, 2),
    _VRtrPimNgRsvpIfSenderAddrType_Type()
)
vRtrPimNgRsvpIfSenderAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfSenderAddrType.setStatus("current")


class _VRtrPimNgRsvpIfSenderAddr_Type(InetAddress):
    """Custom type vRtrPimNgRsvpIfSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgRsvpIfSenderAddr_Type.__name__ = "InetAddress"
_VRtrPimNgRsvpIfSenderAddr_Object = MibTableColumn
vRtrPimNgRsvpIfSenderAddr = _VRtrPimNgRsvpIfSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32, 1, 3),
    _VRtrPimNgRsvpIfSenderAddr_Type()
)
vRtrPimNgRsvpIfSenderAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfSenderAddr.setStatus("current")
_VRtrPimNgRsvpIfRowStatus_Type = RowStatus
_VRtrPimNgRsvpIfRowStatus_Object = MibTableColumn
vRtrPimNgRsvpIfRowStatus = _VRtrPimNgRsvpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32, 1, 4),
    _VRtrPimNgRsvpIfRowStatus_Type()
)
vRtrPimNgRsvpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfRowStatus.setStatus("current")
_VRtrPimNgRsvpIfOperState_Type = TmnxOperState
_VRtrPimNgRsvpIfOperState_Object = MibTableColumn
vRtrPimNgRsvpIfOperState = _VRtrPimNgRsvpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32, 1, 5),
    _VRtrPimNgRsvpIfOperState_Type()
)
vRtrPimNgRsvpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfOperState.setStatus("current")
_VRtrPimNgRsvpIfIndex_Type = InterfaceIndex
_VRtrPimNgRsvpIfIndex_Object = MibTableColumn
vRtrPimNgRsvpIfIndex = _VRtrPimNgRsvpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 32, 1, 6),
    _VRtrPimNgRsvpIfIndex_Type()
)
vRtrPimNgRsvpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIfIndex.setStatus("current")
_VRtrPimNgCRPGpPfxInetTblLstChngd_Type = TimeStamp
_VRtrPimNgCRPGpPfxInetTblLstChngd_Object = MibScalar
vRtrPimNgCRPGpPfxInetTblLstChngd = _VRtrPimNgCRPGpPfxInetTblLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 33),
    _VRtrPimNgCRPGpPfxInetTblLstChngd_Type()
)
vRtrPimNgCRPGpPfxInetTblLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGpPfxInetTblLstChngd.setStatus("current")
_VRtrPimNgCRPGrpPrefixInetTable_Object = MibTable
vRtrPimNgCRPGrpPrefixInetTable = _VRtrPimNgCRPGrpPrefixInetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 34)
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixInetTable.setStatus("current")
_VRtrPimNgCRPGrpPrefixInetEntry_Object = MibTableRow
vRtrPimNgCRPGrpPrefixInetEntry = _VRtrPimNgCRPGrpPrefixInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 34, 1)
)
vRtrPimNgCRPGrpPrefixInetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPfxInetGrpAdrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrefixInetGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrefixInetGrpMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixInetEntry.setStatus("current")
_VRtrPimNgCRPGrpPfxInetGrpAdrType_Type = InetAddressType
_VRtrPimNgCRPGrpPfxInetGrpAdrType_Object = MibTableColumn
vRtrPimNgCRPGrpPfxInetGrpAdrType = _VRtrPimNgCRPGrpPfxInetGrpAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 34, 1, 1),
    _VRtrPimNgCRPGrpPfxInetGrpAdrType_Type()
)
vRtrPimNgCRPGrpPfxInetGrpAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPfxInetGrpAdrType.setStatus("current")


class _VRtrPimNgCRPGrpPrefixInetGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgCRPGrpPrefixInetGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgCRPGrpPrefixInetGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgCRPGrpPrefixInetGrpAddr_Object = MibTableColumn
vRtrPimNgCRPGrpPrefixInetGrpAddr = _VRtrPimNgCRPGrpPrefixInetGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 34, 1, 2),
    _VRtrPimNgCRPGrpPrefixInetGrpAddr_Type()
)
vRtrPimNgCRPGrpPrefixInetGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixInetGrpAddr.setStatus("current")
_VRtrPimNgCRPGrpPrefixInetGrpMask_Type = InetAddressPrefixLength
_VRtrPimNgCRPGrpPrefixInetGrpMask_Object = MibTableColumn
vRtrPimNgCRPGrpPrefixInetGrpMask = _VRtrPimNgCRPGrpPrefixInetGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 34, 1, 3),
    _VRtrPimNgCRPGrpPrefixInetGrpMask_Type()
)
vRtrPimNgCRPGrpPrefixInetGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrefixInetGrpMask.setStatus("current")
_VRtrPimNgCRPGrpPrfxInetRowStatus_Type = RowStatus
_VRtrPimNgCRPGrpPrfxInetRowStatus_Object = MibTableColumn
vRtrPimNgCRPGrpPrfxInetRowStatus = _VRtrPimNgCRPGrpPrfxInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 34, 1, 4),
    _VRtrPimNgCRPGrpPrfxInetRowStatus_Type()
)
vRtrPimNgCRPGrpPrfxInetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPrfxInetRowStatus.setStatus("current")
_VRtrPimNgCRPGrpPfxInetRowLstChgd_Type = TimeStamp
_VRtrPimNgCRPGrpPfxInetRowLstChgd_Object = MibTableColumn
vRtrPimNgCRPGrpPfxInetRowLstChgd = _VRtrPimNgCRPGrpPfxInetRowLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 34, 1, 5),
    _VRtrPimNgCRPGrpPfxInetRowLstChgd_Type()
)
vRtrPimNgCRPGrpPfxInetRowLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPGrpPfxInetRowLstChgd.setStatus("current")
_VRtrPimNgCRPInetTable_Object = MibTable
vRtrPimNgCRPInetTable = _VRtrPimNgCRPInetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35)
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetTable.setStatus("current")
_VRtrPimNgCRPInetEntry_Object = MibTableRow
vRtrPimNgCRPInetEntry = _VRtrPimNgCRPInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1)
)
vRtrPimNgCRPInetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetAddressType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetGrpMask"),
)
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetEntry.setStatus("current")
_VRtrPimNgCRPInetAddressType_Type = InetAddressType
_VRtrPimNgCRPInetAddressType_Object = MibTableColumn
vRtrPimNgCRPInetAddressType = _VRtrPimNgCRPInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 1),
    _VRtrPimNgCRPInetAddressType_Type()
)
vRtrPimNgCRPInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetAddressType.setStatus("current")


class _VRtrPimNgCRPInetAddress_Type(InetAddress):
    """Custom type vRtrPimNgCRPInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgCRPInetAddress_Type.__name__ = "InetAddress"
_VRtrPimNgCRPInetAddress_Object = MibTableColumn
vRtrPimNgCRPInetAddress = _VRtrPimNgCRPInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 2),
    _VRtrPimNgCRPInetAddress_Type()
)
vRtrPimNgCRPInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetAddress.setStatus("current")
_VRtrPimNgCRPInetGrpAddrType_Type = InetAddressType
_VRtrPimNgCRPInetGrpAddrType_Object = MibTableColumn
vRtrPimNgCRPInetGrpAddrType = _VRtrPimNgCRPInetGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 3),
    _VRtrPimNgCRPInetGrpAddrType_Type()
)
vRtrPimNgCRPInetGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetGrpAddrType.setStatus("current")


class _VRtrPimNgCRPInetGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgCRPInetGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgCRPInetGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgCRPInetGrpAddr_Object = MibTableColumn
vRtrPimNgCRPInetGrpAddr = _VRtrPimNgCRPInetGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 4),
    _VRtrPimNgCRPInetGrpAddr_Type()
)
vRtrPimNgCRPInetGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetGrpAddr.setStatus("current")
_VRtrPimNgCRPInetGrpMask_Type = InetAddressPrefixLength
_VRtrPimNgCRPInetGrpMask_Object = MibTableColumn
vRtrPimNgCRPInetGrpMask = _VRtrPimNgCRPInetGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 5),
    _VRtrPimNgCRPInetGrpMask_Type()
)
vRtrPimNgCRPInetGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetGrpMask.setStatus("current")
_VRtrPimNgCRPInetHoldtime_Type = Integer32
_VRtrPimNgCRPInetHoldtime_Object = MibTableColumn
vRtrPimNgCRPInetHoldtime = _VRtrPimNgCRPInetHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 6),
    _VRtrPimNgCRPInetHoldtime_Type()
)
vRtrPimNgCRPInetHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetHoldtime.setUnits("seconds")
_VRtrPimNgCRPInetPriority_Type = Integer32
_VRtrPimNgCRPInetPriority_Object = MibTableColumn
vRtrPimNgCRPInetPriority = _VRtrPimNgCRPInetPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 7),
    _VRtrPimNgCRPInetPriority_Type()
)
vRtrPimNgCRPInetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetPriority.setStatus("current")
_VRtrPimNgCRPInetExpiryTime_Type = Integer32
_VRtrPimNgCRPInetExpiryTime_Object = MibTableColumn
vRtrPimNgCRPInetExpiryTime = _VRtrPimNgCRPInetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 35, 1, 8),
    _VRtrPimNgCRPInetExpiryTime_Type()
)
vRtrPimNgCRPInetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgCRPInetExpiryTime.setUnits("seconds")
_VRtrPimNgRPSetInetTable_Object = MibTable
vRtrPimNgRPSetInetTable = _VRtrPimNgRPSetInetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36)
)
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetTable.setStatus("current")
_VRtrPimNgRPSetInetEntry_Object = MibTableRow
vRtrPimNgRPSetInetEntry = _VRtrPimNgRPSetInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1)
)
vRtrPimNgRPSetInetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetGrpMask"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetCRPAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetCRPAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetEntry.setStatus("current")


class _VRtrPimNgRPSetInetType_Type(Integer32):
    """Custom type vRtrPimNgRPSetInetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2),
          ("auto-rp", 3))
    )


_VRtrPimNgRPSetInetType_Type.__name__ = "Integer32"
_VRtrPimNgRPSetInetType_Object = MibTableColumn
vRtrPimNgRPSetInetType = _VRtrPimNgRPSetInetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 1),
    _VRtrPimNgRPSetInetType_Type()
)
vRtrPimNgRPSetInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetType.setStatus("current")
_VRtrPimNgRPSetInetGrpAddrType_Type = InetAddressType
_VRtrPimNgRPSetInetGrpAddrType_Object = MibTableColumn
vRtrPimNgRPSetInetGrpAddrType = _VRtrPimNgRPSetInetGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 2),
    _VRtrPimNgRPSetInetGrpAddrType_Type()
)
vRtrPimNgRPSetInetGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetGrpAddrType.setStatus("current")


class _VRtrPimNgRPSetInetGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgRPSetInetGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgRPSetInetGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgRPSetInetGrpAddr_Object = MibTableColumn
vRtrPimNgRPSetInetGrpAddr = _VRtrPimNgRPSetInetGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 3),
    _VRtrPimNgRPSetInetGrpAddr_Type()
)
vRtrPimNgRPSetInetGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetGrpAddr.setStatus("current")
_VRtrPimNgRPSetInetGrpMask_Type = InetAddressPrefixLength
_VRtrPimNgRPSetInetGrpMask_Object = MibTableColumn
vRtrPimNgRPSetInetGrpMask = _VRtrPimNgRPSetInetGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 4),
    _VRtrPimNgRPSetInetGrpMask_Type()
)
vRtrPimNgRPSetInetGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetGrpMask.setStatus("current")
_VRtrPimNgRPSetInetCRPAddrType_Type = InetAddressType
_VRtrPimNgRPSetInetCRPAddrType_Object = MibTableColumn
vRtrPimNgRPSetInetCRPAddrType = _VRtrPimNgRPSetInetCRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 5),
    _VRtrPimNgRPSetInetCRPAddrType_Type()
)
vRtrPimNgRPSetInetCRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetCRPAddrType.setStatus("current")


class _VRtrPimNgRPSetInetCRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgRPSetInetCRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgRPSetInetCRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgRPSetInetCRPAddress_Object = MibTableColumn
vRtrPimNgRPSetInetCRPAddress = _VRtrPimNgRPSetInetCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 6),
    _VRtrPimNgRPSetInetCRPAddress_Type()
)
vRtrPimNgRPSetInetCRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetCRPAddress.setStatus("current")
_VRtrPimNgRPSetInetHoldtime_Type = Integer32
_VRtrPimNgRPSetInetHoldtime_Object = MibTableColumn
vRtrPimNgRPSetInetHoldtime = _VRtrPimNgRPSetInetHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 7),
    _VRtrPimNgRPSetInetHoldtime_Type()
)
vRtrPimNgRPSetInetHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetHoldtime.setUnits("seconds")
_VRtrPimNgRPSetInetPriority_Type = Integer32
_VRtrPimNgRPSetInetPriority_Object = MibTableColumn
vRtrPimNgRPSetInetPriority = _VRtrPimNgRPSetInetPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 8),
    _VRtrPimNgRPSetInetPriority_Type()
)
vRtrPimNgRPSetInetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetPriority.setStatus("current")
_VRtrPimNgRPSetInetExpiryTime_Type = Unsigned32
_VRtrPimNgRPSetInetExpiryTime_Object = MibTableColumn
vRtrPimNgRPSetInetExpiryTime = _VRtrPimNgRPSetInetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 36, 1, 9),
    _VRtrPimNgRPSetInetExpiryTime_Type()
)
vRtrPimNgRPSetInetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgRPSetInetExpiryTime.setUnits("seconds")
_VRtrPimNgGrpSrcHostTable_Object = MibTable
vRtrPimNgGrpSrcHostTable = _VRtrPimNgGrpSrcHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 37)
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcHostTable.setStatus("current")
_VRtrPimNgGrpSrcHostEntry_Object = MibTableRow
vRtrPimNgGrpSrcHostEntry = _VRtrPimNgGrpSrcHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 37, 1)
)
vRtrPimNgGrpSrcHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSourceAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcHostAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcHostAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcHostEntry.setStatus("current")
_VRtrPimNgGrpSrcHostAddrType_Type = InetAddressType
_VRtrPimNgGrpSrcHostAddrType_Object = MibTableColumn
vRtrPimNgGrpSrcHostAddrType = _VRtrPimNgGrpSrcHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 37, 1, 1),
    _VRtrPimNgGrpSrcHostAddrType_Type()
)
vRtrPimNgGrpSrcHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcHostAddrType.setStatus("current")


class _VRtrPimNgGrpSrcHostAddress_Type(InetAddress):
    """Custom type vRtrPimNgGrpSrcHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgGrpSrcHostAddress_Type.__name__ = "InetAddress"
_VRtrPimNgGrpSrcHostAddress_Object = MibTableColumn
vRtrPimNgGrpSrcHostAddress = _VRtrPimNgGrpSrcHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 37, 1, 2),
    _VRtrPimNgGrpSrcHostAddress_Type()
)
vRtrPimNgGrpSrcHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcHostAddress.setStatus("current")


class _VRtrPimNgGrpSrcHostFlags_Type(Bits):
    """Custom type vRtrPimNgGrpSrcHostFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("localRxInclude", 3),
          ("localRxExclude", 4),
          ("joinPruneList", 5),
          ("lostAssertList", 6),
          ("sgRptPruneOifList", 7))
    )

_VRtrPimNgGrpSrcHostFlags_Type.__name__ = "Bits"
_VRtrPimNgGrpSrcHostFlags_Object = MibTableColumn
vRtrPimNgGrpSrcHostFlags = _VRtrPimNgGrpSrcHostFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 37, 1, 3),
    _VRtrPimNgGrpSrcHostFlags_Type()
)
vRtrPimNgGrpSrcHostFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcHostFlags.setStatus("current")
_VRtrPimNgGrpSrcGrpIfTable_Object = MibTable
vRtrPimNgGrpSrcGrpIfTable = _VRtrPimNgGrpSrcGrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 38)
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpIfTable.setStatus("current")
_VRtrPimNgGrpSrcGrpIfEntry_Object = MibTableRow
vRtrPimNgGrpSrcGrpIfEntry = _VRtrPimNgGrpSrcGrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 38, 1)
)
vRtrPimNgGrpSrcGrpIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSourceAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpIfFwdSvcId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpIfIndex"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpIfEntry.setStatus("current")


class _VRtrPimNgGrpSrcGrpIfFwdSvcId_Type(TmnxServId):
    """Custom type vRtrPimNgGrpSrcGrpIfFwdSvcId based on TmnxServId"""
    defaultValue = 0


_VRtrPimNgGrpSrcGrpIfFwdSvcId_Type.__name__ = "TmnxServId"
_VRtrPimNgGrpSrcGrpIfFwdSvcId_Object = MibTableColumn
vRtrPimNgGrpSrcGrpIfFwdSvcId = _VRtrPimNgGrpSrcGrpIfFwdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 38, 1, 1),
    _VRtrPimNgGrpSrcGrpIfFwdSvcId_Type()
)
vRtrPimNgGrpSrcGrpIfFwdSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpIfFwdSvcId.setStatus("current")
_VRtrPimNgGrpSrcGrpIfIndex_Type = InterfaceIndex
_VRtrPimNgGrpSrcGrpIfIndex_Object = MibTableColumn
vRtrPimNgGrpSrcGrpIfIndex = _VRtrPimNgGrpSrcGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 38, 1, 2),
    _VRtrPimNgGrpSrcGrpIfIndex_Type()
)
vRtrPimNgGrpSrcGrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpIfIndex.setStatus("current")


class _VRtrPimNgGrpSrcGrpIfFlags_Type(Bits):
    """Custom type vRtrPimNgGrpSrcGrpIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("localRxInclude", 3),
          ("localRxExclude", 4),
          ("joinPruneList", 5),
          ("lostAssertList", 6),
          ("sgRptPruneOifList", 7))
    )

_VRtrPimNgGrpSrcGrpIfFlags_Type.__name__ = "Bits"
_VRtrPimNgGrpSrcGrpIfFlags_Object = MibTableColumn
vRtrPimNgGrpSrcGrpIfFlags = _VRtrPimNgGrpSrcGrpIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 38, 1, 3),
    _VRtrPimNgGrpSrcGrpIfFlags_Type()
)
vRtrPimNgGrpSrcGrpIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgGrpSrcGrpIfFlags.setStatus("current")
_VRtrPimNgMvpnUMHPETblLastChg_Type = TimeStamp
_VRtrPimNgMvpnUMHPETblLastChg_Object = MibScalar
vRtrPimNgMvpnUMHPETblLastChg = _VRtrPimNgMvpnUMHPETblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 39),
    _VRtrPimNgMvpnUMHPETblLastChg_Type()
)
vRtrPimNgMvpnUMHPETblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPETblLastChg.setStatus("current")
_VRtrPimNgMvpnUMHPETable_Object = MibTable
vRtrPimNgMvpnUMHPETable = _VRtrPimNgMvpnUMHPETable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40)
)
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPETable.setStatus("current")
_VRtrPimNgMvpnUMHPEEntry_Object = MibTableRow
vRtrPimNgMvpnUMHPEEntry = _VRtrPimNgMvpnUMHPEEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40, 1)
)
vRtrPimNgMvpnUMHPEEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEAddr"),
)
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPEEntry.setStatus("current")
_VRtrPimNgMvpnUMHPEAddrType_Type = InetAddressType
_VRtrPimNgMvpnUMHPEAddrType_Object = MibTableColumn
vRtrPimNgMvpnUMHPEAddrType = _VRtrPimNgMvpnUMHPEAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40, 1, 1),
    _VRtrPimNgMvpnUMHPEAddrType_Type()
)
vRtrPimNgMvpnUMHPEAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPEAddrType.setStatus("current")


class _VRtrPimNgMvpnUMHPEAddr_Type(InetAddress):
    """Custom type vRtrPimNgMvpnUMHPEAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgMvpnUMHPEAddr_Type.__name__ = "InetAddress"
_VRtrPimNgMvpnUMHPEAddr_Object = MibTableColumn
vRtrPimNgMvpnUMHPEAddr = _VRtrPimNgMvpnUMHPEAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40, 1, 2),
    _VRtrPimNgMvpnUMHPEAddr_Type()
)
vRtrPimNgMvpnUMHPEAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPEAddr.setStatus("current")
_VRtrPimNgMvpnUMHPERowStatus_Type = RowStatus
_VRtrPimNgMvpnUMHPERowStatus_Object = MibTableColumn
vRtrPimNgMvpnUMHPERowStatus = _VRtrPimNgMvpnUMHPERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40, 1, 3),
    _VRtrPimNgMvpnUMHPERowStatus_Type()
)
vRtrPimNgMvpnUMHPERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPERowStatus.setStatus("current")
_VRtrPimNgMvpnUMHPELastChanged_Type = TimeStamp
_VRtrPimNgMvpnUMHPELastChanged_Object = MibTableColumn
vRtrPimNgMvpnUMHPELastChanged = _VRtrPimNgMvpnUMHPELastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40, 1, 4),
    _VRtrPimNgMvpnUMHPELastChanged_Type()
)
vRtrPimNgMvpnUMHPELastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPELastChanged.setStatus("current")


class _VRtrPimNgMvpnUMHPEStandbyAdrTyp_Type(InetAddressType):
    """Custom type vRtrPimNgMvpnUMHPEStandbyAdrTyp based on InetAddressType"""
    defaultValue = 0


_VRtrPimNgMvpnUMHPEStandbyAdrTyp_Type.__name__ = "InetAddressType"
_VRtrPimNgMvpnUMHPEStandbyAdrTyp_Object = MibTableColumn
vRtrPimNgMvpnUMHPEStandbyAdrTyp = _VRtrPimNgMvpnUMHPEStandbyAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40, 1, 5),
    _VRtrPimNgMvpnUMHPEStandbyAdrTyp_Type()
)
vRtrPimNgMvpnUMHPEStandbyAdrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPEStandbyAdrTyp.setStatus("current")


class _VRtrPimNgMvpnUMHPEStandbyAddr_Type(InetAddress):
    """Custom type vRtrPimNgMvpnUMHPEStandbyAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgMvpnUMHPEStandbyAddr_Type.__name__ = "InetAddress"
_VRtrPimNgMvpnUMHPEStandbyAddr_Object = MibTableColumn
vRtrPimNgMvpnUMHPEStandbyAddr = _VRtrPimNgMvpnUMHPEStandbyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 40, 1, 6),
    _VRtrPimNgMvpnUMHPEStandbyAddr_Type()
)
vRtrPimNgMvpnUMHPEStandbyAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnUMHPEStandbyAddr.setStatus("current")
_VRtrPimNgMvpnSrcPrefixTblLstChg_Type = TimeStamp
_VRtrPimNgMvpnSrcPrefixTblLstChg_Object = MibScalar
vRtrPimNgMvpnSrcPrefixTblLstChg = _VRtrPimNgMvpnSrcPrefixTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 41),
    _VRtrPimNgMvpnSrcPrefixTblLstChg_Type()
)
vRtrPimNgMvpnSrcPrefixTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixTblLstChg.setStatus("current")
_VRtrPimNgMvpnSrcPrefixTable_Object = MibTable
vRtrPimNgMvpnSrcPrefixTable = _VRtrPimNgMvpnSrcPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 42)
)
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixTable.setStatus("current")
_VRtrPimNgMvpnSrcPrefixEntry_Object = MibTableRow
vRtrPimNgMvpnSrcPrefixEntry = _VRtrPimNgMvpnSrcPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 42, 1)
)
vRtrPimNgMvpnSrcPrefixEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnSrcPrefixType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnSrcPrefixAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnSrcPrefixLen"),
)
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixEntry.setStatus("current")
_VRtrPimNgMvpnSrcPrefixType_Type = InetAddressType
_VRtrPimNgMvpnSrcPrefixType_Object = MibTableColumn
vRtrPimNgMvpnSrcPrefixType = _VRtrPimNgMvpnSrcPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 42, 1, 1),
    _VRtrPimNgMvpnSrcPrefixType_Type()
)
vRtrPimNgMvpnSrcPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixType.setStatus("current")


class _VRtrPimNgMvpnSrcPrefixAddr_Type(InetAddress):
    """Custom type vRtrPimNgMvpnSrcPrefixAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgMvpnSrcPrefixAddr_Type.__name__ = "InetAddress"
_VRtrPimNgMvpnSrcPrefixAddr_Object = MibTableColumn
vRtrPimNgMvpnSrcPrefixAddr = _VRtrPimNgMvpnSrcPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 42, 1, 2),
    _VRtrPimNgMvpnSrcPrefixAddr_Type()
)
vRtrPimNgMvpnSrcPrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixAddr.setStatus("current")
_VRtrPimNgMvpnSrcPrefixLen_Type = InetAddressPrefixLength
_VRtrPimNgMvpnSrcPrefixLen_Object = MibTableColumn
vRtrPimNgMvpnSrcPrefixLen = _VRtrPimNgMvpnSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 42, 1, 3),
    _VRtrPimNgMvpnSrcPrefixLen_Type()
)
vRtrPimNgMvpnSrcPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixLen.setStatus("current")
_VRtrPimNgMvpnSrcPrefixRowStatus_Type = RowStatus
_VRtrPimNgMvpnSrcPrefixRowStatus_Object = MibTableColumn
vRtrPimNgMvpnSrcPrefixRowStatus = _VRtrPimNgMvpnSrcPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 42, 1, 4),
    _VRtrPimNgMvpnSrcPrefixRowStatus_Type()
)
vRtrPimNgMvpnSrcPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixRowStatus.setStatus("current")
_VRtrPimNgMvpnSrcPrefixRowLastChg_Type = TimeStamp
_VRtrPimNgMvpnSrcPrefixRowLastChg_Object = MibTableColumn
vRtrPimNgMvpnSrcPrefixRowLastChg = _VRtrPimNgMvpnSrcPrefixRowLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 42, 1, 5),
    _VRtrPimNgMvpnSrcPrefixRowLastChg_Type()
)
vRtrPimNgMvpnSrcPrefixRowLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnSrcPrefixRowLastChg.setStatus("current")
_VRtrPimNgExtranetCDTblLstChg_Type = TimeStamp
_VRtrPimNgExtranetCDTblLstChg_Object = MibScalar
vRtrPimNgExtranetCDTblLstChg = _VRtrPimNgExtranetCDTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 43),
    _VRtrPimNgExtranetCDTblLstChg_Type()
)
vRtrPimNgExtranetCDTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDTblLstChg.setStatus("current")
_VRtrPimNgExtranetCDTable_Object = MibTable
vRtrPimNgExtranetCDTable = _VRtrPimNgExtranetCDTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44)
)
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDTable.setStatus("current")
_VRtrPimNgExtranetCDEntry_Object = MibTableRow
vRtrPimNgExtranetCDEntry = _VRtrPimNgExtranetCDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44, 1)
)
vRtrPimNgExtranetCDEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgExtranetCDGrpPfxType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgExtranetCDGrpPfxAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgExtranetCDGrpPfxLen"),
)
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDEntry.setStatus("current")
_VRtrPimNgExtranetCDGrpPfxType_Type = InetAddressType
_VRtrPimNgExtranetCDGrpPfxType_Object = MibTableColumn
vRtrPimNgExtranetCDGrpPfxType = _VRtrPimNgExtranetCDGrpPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44, 1, 1),
    _VRtrPimNgExtranetCDGrpPfxType_Type()
)
vRtrPimNgExtranetCDGrpPfxType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDGrpPfxType.setStatus("current")


class _VRtrPimNgExtranetCDGrpPfxAddr_Type(InetAddress):
    """Custom type vRtrPimNgExtranetCDGrpPfxAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgExtranetCDGrpPfxAddr_Type.__name__ = "InetAddress"
_VRtrPimNgExtranetCDGrpPfxAddr_Object = MibTableColumn
vRtrPimNgExtranetCDGrpPfxAddr = _VRtrPimNgExtranetCDGrpPfxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44, 1, 2),
    _VRtrPimNgExtranetCDGrpPfxAddr_Type()
)
vRtrPimNgExtranetCDGrpPfxAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDGrpPfxAddr.setStatus("current")
_VRtrPimNgExtranetCDGrpPfxLen_Type = InetAddressPrefixLength
_VRtrPimNgExtranetCDGrpPfxLen_Object = MibTableColumn
vRtrPimNgExtranetCDGrpPfxLen = _VRtrPimNgExtranetCDGrpPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44, 1, 3),
    _VRtrPimNgExtranetCDGrpPfxLen_Type()
)
vRtrPimNgExtranetCDGrpPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDGrpPfxLen.setStatus("current")
_VRtrPimNgExtranetCDMvpnId_Type = Unsigned32
_VRtrPimNgExtranetCDMvpnId_Object = MibTableColumn
vRtrPimNgExtranetCDMvpnId = _VRtrPimNgExtranetCDMvpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44, 1, 4),
    _VRtrPimNgExtranetCDMvpnId_Type()
)
vRtrPimNgExtranetCDMvpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDMvpnId.setStatus("current")
_VRtrPimNgExtranetCDRowStatus_Type = RowStatus
_VRtrPimNgExtranetCDRowStatus_Object = MibTableColumn
vRtrPimNgExtranetCDRowStatus = _VRtrPimNgExtranetCDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44, 1, 5),
    _VRtrPimNgExtranetCDRowStatus_Type()
)
vRtrPimNgExtranetCDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDRowStatus.setStatus("current")
_VRtrPimNgExtranetCDRowLstChg_Type = TimeStamp
_VRtrPimNgExtranetCDRowLstChg_Object = MibTableColumn
vRtrPimNgExtranetCDRowLstChg = _VRtrPimNgExtranetCDRowLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 1, 44, 1, 6),
    _VRtrPimNgExtranetCDRowLstChg_Type()
)
vRtrPimNgExtranetCDRowLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgExtranetCDRowLstChg.setStatus("current")
_VRtrPimNgIfObjs_ObjectIdentity = ObjectIdentity
vRtrPimNgIfObjs = _VRtrPimNgIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2)
)
_VRtrPimNgIfTableLastChanged_Type = TimeStamp
_VRtrPimNgIfTableLastChanged_Object = MibScalar
vRtrPimNgIfTableLastChanged = _VRtrPimNgIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 1),
    _VRtrPimNgIfTableLastChanged_Type()
)
vRtrPimNgIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTableLastChanged.setStatus("current")
_VRtrPimNgIfTable_Object = MibTable
vRtrPimNgIfTable = _VRtrPimNgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfTable.setStatus("current")
_VRtrPimNgIfEntry_Object = MibTableRow
vRtrPimNgIfEntry = _VRtrPimNgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1)
)
vRtrPimNgIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrPimNgIfEntry.setStatus("current")
_VRtrPimNgIfRowStatus_Type = RowStatus
_VRtrPimNgIfRowStatus_Object = MibTableColumn
vRtrPimNgIfRowStatus = _VRtrPimNgIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 1),
    _VRtrPimNgIfRowStatus_Type()
)
vRtrPimNgIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfRowStatus.setStatus("current")
_VRtrPimNgIfLastChangeTime_Type = TimeStamp
_VRtrPimNgIfLastChangeTime_Object = MibTableColumn
vRtrPimNgIfLastChangeTime = _VRtrPimNgIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 2),
    _VRtrPimNgIfLastChangeTime_Type()
)
vRtrPimNgIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfLastChangeTime.setStatus("current")


class _VRtrPimNgIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrPimNgIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgIfAdminState_Object = MibTableColumn
vRtrPimNgIfAdminState = _VRtrPimNgIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 3),
    _VRtrPimNgIfAdminState_Type()
)
vRtrPimNgIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfAdminState.setStatus("current")
_VRtrPimNgIfOperState_Type = TmnxOperState
_VRtrPimNgIfOperState_Object = MibTableColumn
vRtrPimNgIfOperState = _VRtrPimNgIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 4),
    _VRtrPimNgIfOperState_Type()
)
vRtrPimNgIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfOperState.setStatus("current")


class _VRtrPimNgIfHelloInterval_Type(Integer32):
    """Custom type vRtrPimNgIfHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimNgIfHelloInterval_Type.__name__ = "Integer32"
_VRtrPimNgIfHelloInterval_Object = MibTableColumn
vRtrPimNgIfHelloInterval = _VRtrPimNgIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 5),
    _VRtrPimNgIfHelloInterval_Type()
)
vRtrPimNgIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfHelloInterval.setUnits("seconds")


class _VRtrPimNgIfTrackingSupport_Type(TruthValue):
    """Custom type vRtrPimNgIfTrackingSupport based on TruthValue"""
    defaultValue = 2


_VRtrPimNgIfTrackingSupport_Type.__name__ = "TruthValue"
_VRtrPimNgIfTrackingSupport_Object = MibTableColumn
vRtrPimNgIfTrackingSupport = _VRtrPimNgIfTrackingSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 6),
    _VRtrPimNgIfTrackingSupport_Type()
)
vRtrPimNgIfTrackingSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfTrackingSupport.setStatus("current")


class _VRtrPimNgIfMulticastSenders_Type(Integer32):
    """Custom type vRtrPimNgIfMulticastSenders based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("always", 1),
          ("never", 2))
    )


_VRtrPimNgIfMulticastSenders_Type.__name__ = "Integer32"
_VRtrPimNgIfMulticastSenders_Object = MibTableColumn
vRtrPimNgIfMulticastSenders = _VRtrPimNgIfMulticastSenders_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 7),
    _VRtrPimNgIfMulticastSenders_Type()
)
vRtrPimNgIfMulticastSenders.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMulticastSenders.setStatus("current")
_VRtrPimNgIfAutoCreated_Type = TruthValue
_VRtrPimNgIfAutoCreated_Object = MibTableColumn
vRtrPimNgIfAutoCreated = _VRtrPimNgIfAutoCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 8),
    _VRtrPimNgIfAutoCreated_Type()
)
vRtrPimNgIfAutoCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfAutoCreated.setStatus("current")


class _VRtrPimNgIfBSMCheckRouterAlert_Type(TruthValue):
    """Custom type vRtrPimNgIfBSMCheckRouterAlert based on TruthValue"""
    defaultValue = 2


_VRtrPimNgIfBSMCheckRouterAlert_Type.__name__ = "TruthValue"
_VRtrPimNgIfBSMCheckRouterAlert_Object = MibTableColumn
vRtrPimNgIfBSMCheckRouterAlert = _VRtrPimNgIfBSMCheckRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 9),
    _VRtrPimNgIfBSMCheckRouterAlert_Type()
)
vRtrPimNgIfBSMCheckRouterAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfBSMCheckRouterAlert.setStatus("current")


class _VRtrPimNgIfHelloMultiplier_Type(Unsigned32):
    """Custom type vRtrPimNgIfHelloMultiplier based on Unsigned32"""
    defaultValue = 35

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_VRtrPimNgIfHelloMultiplier_Type.__name__ = "Unsigned32"
_VRtrPimNgIfHelloMultiplier_Object = MibTableColumn
vRtrPimNgIfHelloMultiplier = _VRtrPimNgIfHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 10),
    _VRtrPimNgIfHelloMultiplier_Type()
)
vRtrPimNgIfHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfHelloMultiplier.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfHelloMultiplier.setUnits("deci-units")


class _VRtrPimNgIfImprovedAssert_Type(TruthValue):
    """Custom type vRtrPimNgIfImprovedAssert based on TruthValue"""
    defaultValue = 1


_VRtrPimNgIfImprovedAssert_Type.__name__ = "TruthValue"
_VRtrPimNgIfImprovedAssert_Object = MibTableColumn
vRtrPimNgIfImprovedAssert = _VRtrPimNgIfImprovedAssert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 11),
    _VRtrPimNgIfImprovedAssert_Type()
)
vRtrPimNgIfImprovedAssert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfImprovedAssert.setStatus("current")


class _VRtrPimNgIfStickyDR_Type(TruthValue):
    """Custom type vRtrPimNgIfStickyDR based on TruthValue"""
    defaultValue = 2


_VRtrPimNgIfStickyDR_Type.__name__ = "TruthValue"
_VRtrPimNgIfStickyDR_Object = MibTableColumn
vRtrPimNgIfStickyDR = _VRtrPimNgIfStickyDR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 12),
    _VRtrPimNgIfStickyDR_Type()
)
vRtrPimNgIfStickyDR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfStickyDR.setStatus("current")


class _VRtrPimNgIfStickyDRPriority_Type(Unsigned32):
    """Custom type vRtrPimNgIfStickyDRPriority based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrPimNgIfStickyDRPriority_Type.__name__ = "Unsigned32"
_VRtrPimNgIfStickyDRPriority_Object = MibTableColumn
vRtrPimNgIfStickyDRPriority = _VRtrPimNgIfStickyDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 13),
    _VRtrPimNgIfStickyDRPriority_Type()
)
vRtrPimNgIfStickyDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfStickyDRPriority.setStatus("current")


class _VRtrPimNgIfMaxGroups_Type(Unsigned32):
    """Custom type vRtrPimNgIfMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_VRtrPimNgIfMaxGroups_Type.__name__ = "Unsigned32"
_VRtrPimNgIfMaxGroups_Object = MibTableColumn
vRtrPimNgIfMaxGroups = _VRtrPimNgIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 14),
    _VRtrPimNgIfMaxGroups_Type()
)
vRtrPimNgIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMaxGroups.setStatus("current")


class _VRtrPimNgIfEnableBfd_Type(TruthValue):
    """Custom type vRtrPimNgIfEnableBfd based on TruthValue"""
    defaultValue = 2


_VRtrPimNgIfEnableBfd_Type.__name__ = "TruthValue"
_VRtrPimNgIfEnableBfd_Object = MibTableColumn
vRtrPimNgIfEnableBfd = _VRtrPimNgIfEnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 15),
    _VRtrPimNgIfEnableBfd_Type()
)
vRtrPimNgIfEnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfEnableBfd.setStatus("current")


class _VRtrPimNgIfThreeWayHello_Type(Integer32):
    """Custom type vRtrPimNgIfThreeWayHello based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VRtrPimNgIfThreeWayHello_Type.__name__ = "Integer32"
_VRtrPimNgIfThreeWayHello_Object = MibTableColumn
vRtrPimNgIfThreeWayHello = _VRtrPimNgIfThreeWayHello_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 16),
    _VRtrPimNgIfThreeWayHello_Type()
)
vRtrPimNgIfThreeWayHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfThreeWayHello.setStatus("current")


class _VRtrPimNgIfMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrPimNgIfMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_VRtrPimNgIfMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrPimNgIfMcacPolicyName_Object = MibTableColumn
vRtrPimNgIfMcacPolicyName = _VRtrPimNgIfMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 17),
    _VRtrPimNgIfMcacPolicyName_Type()
)
vRtrPimNgIfMcacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacPolicyName.setStatus("current")


class _VRtrPimNgIfMcacUnconstrainedBW_Type(Integer32):
    """Custom type vRtrPimNgIfMcacUnconstrainedBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrPimNgIfMcacUnconstrainedBW_Type.__name__ = "Integer32"
_VRtrPimNgIfMcacUnconstrainedBW_Object = MibTableColumn
vRtrPimNgIfMcacUnconstrainedBW = _VRtrPimNgIfMcacUnconstrainedBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 18),
    _VRtrPimNgIfMcacUnconstrainedBW_Type()
)
vRtrPimNgIfMcacUnconstrainedBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacUnconstrainedBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacUnconstrainedBW.setUnits("kbps")


class _VRtrPimNgIfMcacConstAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgIfMcacConstAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrPimNgIfMcacConstAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgIfMcacConstAdminState_Object = MibTableColumn
vRtrPimNgIfMcacConstAdminState = _VRtrPimNgIfMcacConstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 19),
    _VRtrPimNgIfMcacConstAdminState_Type()
)
vRtrPimNgIfMcacConstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacConstAdminState.setStatus("current")


class _VRtrPimNgIfMcacPreRsvdMandBW_Type(Integer32):
    """Custom type vRtrPimNgIfMcacPreRsvdMandBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrPimNgIfMcacPreRsvdMandBW_Type.__name__ = "Integer32"
_VRtrPimNgIfMcacPreRsvdMandBW_Object = MibTableColumn
vRtrPimNgIfMcacPreRsvdMandBW = _VRtrPimNgIfMcacPreRsvdMandBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 20),
    _VRtrPimNgIfMcacPreRsvdMandBW_Type()
)
vRtrPimNgIfMcacPreRsvdMandBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacPreRsvdMandBW.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacPreRsvdMandBW.setUnits("kbps")
_VRtrPimNgIfMcacinUseMandBw_Type = Unsigned32
_VRtrPimNgIfMcacinUseMandBw_Object = MibTableColumn
vRtrPimNgIfMcacinUseMandBw = _VRtrPimNgIfMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 21),
    _VRtrPimNgIfMcacinUseMandBw_Type()
)
vRtrPimNgIfMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacinUseMandBw.setUnits("kbps")
_VRtrPimNgIfMcacinUseOpnlBw_Type = Unsigned32
_VRtrPimNgIfMcacinUseOpnlBw_Object = MibTableColumn
vRtrPimNgIfMcacinUseOpnlBw = _VRtrPimNgIfMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 22),
    _VRtrPimNgIfMcacinUseOpnlBw_Type()
)
vRtrPimNgIfMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacinUseOpnlBw.setUnits("kbps")
_VRtrPimNgIfMcacAvailMandBw_Type = Unsigned32
_VRtrPimNgIfMcacAvailMandBw_Object = MibTableColumn
vRtrPimNgIfMcacAvailMandBw = _VRtrPimNgIfMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 23),
    _VRtrPimNgIfMcacAvailMandBw_Type()
)
vRtrPimNgIfMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacAvailMandBw.setUnits("kbps")
_VRtrPimNgIfMcacAvailOpnlBw_Type = Unsigned32
_VRtrPimNgIfMcacAvailOpnlBw_Object = MibTableColumn
vRtrPimNgIfMcacAvailOpnlBw = _VRtrPimNgIfMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 24),
    _VRtrPimNgIfMcacAvailOpnlBw_Type()
)
vRtrPimNgIfMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacAvailOpnlBw.setUnits("kbps")
_VRtrPimNgIfMcacValuesInTransit_Type = TruthValue
_VRtrPimNgIfMcacValuesInTransit_Object = MibTableColumn
vRtrPimNgIfMcacValuesInTransit = _VRtrPimNgIfMcacValuesInTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 25),
    _VRtrPimNgIfMcacValuesInTransit_Type()
)
vRtrPimNgIfMcacValuesInTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacValuesInTransit.setStatus("current")


class _VRtrPimNgIfDRPriority_Type(Unsigned32):
    """Custom type vRtrPimNgIfDRPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrPimNgIfDRPriority_Type.__name__ = "Unsigned32"
_VRtrPimNgIfDRPriority_Object = MibTableColumn
vRtrPimNgIfDRPriority = _VRtrPimNgIfDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 26),
    _VRtrPimNgIfDRPriority_Type()
)
vRtrPimNgIfDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfDRPriority.setStatus("current")


class _VRtrPimNgIfAssertPeriod_Type(Integer32):
    """Custom type vRtrPimNgIfAssertPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_VRtrPimNgIfAssertPeriod_Type.__name__ = "Integer32"
_VRtrPimNgIfAssertPeriod_Object = MibTableColumn
vRtrPimNgIfAssertPeriod = _VRtrPimNgIfAssertPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 27),
    _VRtrPimNgIfAssertPeriod_Type()
)
vRtrPimNgIfAssertPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfAssertPeriod.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfAssertPeriod.setUnits("seconds")


class _VRtrPimNgIfInstantPruneEcho_Type(TmnxEnabledDisabled):
    """Custom type vRtrPimNgIfInstantPruneEcho based on TmnxEnabledDisabled"""
    defaultValue = 2


_VRtrPimNgIfInstantPruneEcho_Type.__name__ = "TmnxEnabledDisabled"
_VRtrPimNgIfInstantPruneEcho_Object = MibTableColumn
vRtrPimNgIfInstantPruneEcho = _VRtrPimNgIfInstantPruneEcho_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 28),
    _VRtrPimNgIfInstantPruneEcho_Type()
)
vRtrPimNgIfInstantPruneEcho.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfInstantPruneEcho.setStatus("current")


class _VRtrPimNgIfIpv6EnableBfd_Type(TruthValue):
    """Custom type vRtrPimNgIfIpv6EnableBfd based on TruthValue"""
    defaultValue = 2


_VRtrPimNgIfIpv6EnableBfd_Type.__name__ = "TruthValue"
_VRtrPimNgIfIpv6EnableBfd_Object = MibTableColumn
vRtrPimNgIfIpv6EnableBfd = _VRtrPimNgIfIpv6EnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 29),
    _VRtrPimNgIfIpv6EnableBfd_Type()
)
vRtrPimNgIfIpv6EnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfIpv6EnableBfd.setStatus("current")


class _VRtrPimNgIfP2mpLdpTreeJoin_Type(TruthValue):
    """Custom type vRtrPimNgIfP2mpLdpTreeJoin based on TruthValue"""
    defaultValue = 2


_VRtrPimNgIfP2mpLdpTreeJoin_Type.__name__ = "TruthValue"
_VRtrPimNgIfP2mpLdpTreeJoin_Object = MibTableColumn
vRtrPimNgIfP2mpLdpTreeJoin = _VRtrPimNgIfP2mpLdpTreeJoin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 30),
    _VRtrPimNgIfP2mpLdpTreeJoin_Type()
)
vRtrPimNgIfP2mpLdpTreeJoin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfP2mpLdpTreeJoin.setStatus("current")


class _VRtrPimNgIfExtranetType_Type(Integer32):
    """Custom type vRtrPimNgIfExtranetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rx", 0),
          ("tx", 1),
          ("none", 3))
    )


_VRtrPimNgIfExtranetType_Type.__name__ = "Integer32"
_VRtrPimNgIfExtranetType_Object = MibTableColumn
vRtrPimNgIfExtranetType = _VRtrPimNgIfExtranetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 31),
    _VRtrPimNgIfExtranetType_Type()
)
vRtrPimNgIfExtranetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfExtranetType.setStatus("current")


class _VRtrPimNgIfExtranetMvpnId_Type(Unsigned32):
    """Custom type vRtrPimNgIfExtranetMvpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240),
    )


_VRtrPimNgIfExtranetMvpnId_Type.__name__ = "Unsigned32"
_VRtrPimNgIfExtranetMvpnId_Object = MibTableColumn
vRtrPimNgIfExtranetMvpnId = _VRtrPimNgIfExtranetMvpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 32),
    _VRtrPimNgIfExtranetMvpnId_Type()
)
vRtrPimNgIfExtranetMvpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfExtranetMvpnId.setStatus("current")


class _VRtrPimNgIfMcacUseLagPortWeight_Type(TruthValue):
    """Custom type vRtrPimNgIfMcacUseLagPortWeight based on TruthValue"""
    defaultValue = 2


_VRtrPimNgIfMcacUseLagPortWeight_Type.__name__ = "TruthValue"
_VRtrPimNgIfMcacUseLagPortWeight_Object = MibTableColumn
vRtrPimNgIfMcacUseLagPortWeight = _VRtrPimNgIfMcacUseLagPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 2, 1, 33),
    _VRtrPimNgIfMcacUseLagPortWeight_Type()
)
vRtrPimNgIfMcacUseLagPortWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacUseLagPortWeight.setStatus("current")
_VRtrPimNgAFIfTable_Object = MibTable
vRtrPimNgAFIfTable = _VRtrPimNgAFIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3)
)
if mibBuilder.loadTexts:
    vRtrPimNgAFIfTable.setStatus("current")
_VRtrPimNgAFIfEntry_Object = MibTableRow
vRtrPimNgAFIfEntry = _VRtrPimNgAFIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1)
)
vRtrPimNgAFIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfAFType"),
)
if mibBuilder.loadTexts:
    vRtrPimNgAFIfEntry.setStatus("current")
_VRtrPimNgAFIfAFType_Type = TmnxMulticastAddrFamily
_VRtrPimNgAFIfAFType_Object = MibTableColumn
vRtrPimNgAFIfAFType = _VRtrPimNgAFIfAFType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 1),
    _VRtrPimNgAFIfAFType_Type()
)
vRtrPimNgAFIfAFType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfAFType.setStatus("current")


class _VRtrPimNgAFIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimNgAFIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrPimNgAFIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimNgAFIfAdminState_Object = MibTableColumn
vRtrPimNgAFIfAdminState = _VRtrPimNgAFIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 2),
    _VRtrPimNgAFIfAdminState_Type()
)
vRtrPimNgAFIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfAdminState.setStatus("current")
_VRtrPimNgAFIfOperState_Type = TmnxOperState
_VRtrPimNgAFIfOperState_Object = MibTableColumn
vRtrPimNgAFIfOperState = _VRtrPimNgAFIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 3),
    _VRtrPimNgAFIfOperState_Type()
)
vRtrPimNgAFIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfOperState.setStatus("current")
_VRtrPimNgAFIfMdtDefGrpAddrType_Type = InetAddressType
_VRtrPimNgAFIfMdtDefGrpAddrType_Object = MibTableColumn
vRtrPimNgAFIfMdtDefGrpAddrType = _VRtrPimNgAFIfMdtDefGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 4),
    _VRtrPimNgAFIfMdtDefGrpAddrType_Type()
)
vRtrPimNgAFIfMdtDefGrpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfMdtDefGrpAddrType.setStatus("current")


class _VRtrPimNgAFIfMdtDefGrpAddress_Type(InetAddress):
    """Custom type vRtrPimNgAFIfMdtDefGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFIfMdtDefGrpAddress_Type.__name__ = "InetAddress"
_VRtrPimNgAFIfMdtDefGrpAddress_Object = MibTableColumn
vRtrPimNgAFIfMdtDefGrpAddress = _VRtrPimNgAFIfMdtDefGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 5),
    _VRtrPimNgAFIfMdtDefGrpAddress_Type()
)
vRtrPimNgAFIfMdtDefGrpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfMdtDefGrpAddress.setStatus("current")


class _VRtrPimNgAFIfNextHelloTime_Type(Unsigned32):
    """Custom type vRtrPimNgAFIfNextHelloTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimNgAFIfNextHelloTime_Type.__name__ = "Unsigned32"
_VRtrPimNgAFIfNextHelloTime_Object = MibTableColumn
vRtrPimNgAFIfNextHelloTime = _VRtrPimNgAFIfNextHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 6),
    _VRtrPimNgAFIfNextHelloTime_Type()
)
vRtrPimNgAFIfNextHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfNextHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfNextHelloTime.setUnits("seconds")
_VRtrPimNgAFIfOperDRPriority_Type = Unsigned32
_VRtrPimNgAFIfOperDRPriority_Object = MibTableColumn
vRtrPimNgAFIfOperDRPriority = _VRtrPimNgAFIfOperDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 7),
    _VRtrPimNgAFIfOperDRPriority_Type()
)
vRtrPimNgAFIfOperDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfOperDRPriority.setStatus("current")
_VRtrPimNgAFIfCurrentGroups_Type = Gauge32
_VRtrPimNgAFIfCurrentGroups_Object = MibTableColumn
vRtrPimNgAFIfCurrentGroups = _VRtrPimNgAFIfCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 8),
    _VRtrPimNgAFIfCurrentGroups_Type()
)
vRtrPimNgAFIfCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfCurrentGroups.setStatus("current")
_VRtrPimNgAFIfMaxGroupsTillNow_Type = Counter32
_VRtrPimNgAFIfMaxGroupsTillNow_Object = MibTableColumn
vRtrPimNgAFIfMaxGroupsTillNow = _VRtrPimNgAFIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 9),
    _VRtrPimNgAFIfMaxGroupsTillNow_Type()
)
vRtrPimNgAFIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfMaxGroupsTillNow.setStatus("current")
_VRtrPimNgAFIfDRType_Type = InetAddressType
_VRtrPimNgAFIfDRType_Object = MibTableColumn
vRtrPimNgAFIfDRType = _VRtrPimNgAFIfDRType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 10),
    _VRtrPimNgAFIfDRType_Type()
)
vRtrPimNgAFIfDRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfDRType.setStatus("current")


class _VRtrPimNgAFIfDR_Type(InetAddress):
    """Custom type vRtrPimNgAFIfDR based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgAFIfDR_Type.__name__ = "InetAddress"
_VRtrPimNgAFIfDR_Object = MibTableColumn
vRtrPimNgAFIfDR = _VRtrPimNgAFIfDR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 11),
    _VRtrPimNgAFIfDR_Type()
)
vRtrPimNgAFIfDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfDR.setStatus("current")
_VRtrPimNgAFIfTrackSprtOperState_Type = TruthValue
_VRtrPimNgAFIfTrackSprtOperState_Object = MibTableColumn
vRtrPimNgAFIfTrackSprtOperState = _VRtrPimNgAFIfTrackSprtOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 3, 1, 12),
    _VRtrPimNgAFIfTrackSprtOperState_Type()
)
vRtrPimNgAFIfTrackSprtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgAFIfTrackSprtOperState.setStatus("current")
_VRtrPimNgIfNeighborTable_Object = MibTable
vRtrPimNgIfNeighborTable = _VRtrPimNgIfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborTable.setStatus("current")
_VRtrPimNgIfNeighborEntry_Object = MibTableRow
vRtrPimNgIfNeighborEntry = _VRtrPimNgIfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1)
)
vRtrPimNgIfNeighborEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborAddressType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborEntry.setStatus("current")
_VRtrPimNgIfNeighborAddressType_Type = InetAddressType
_VRtrPimNgIfNeighborAddressType_Object = MibTableColumn
vRtrPimNgIfNeighborAddressType = _VRtrPimNgIfNeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 1),
    _VRtrPimNgIfNeighborAddressType_Type()
)
vRtrPimNgIfNeighborAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborAddressType.setStatus("current")


class _VRtrPimNgIfNeighborAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfNeighborAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfNeighborAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfNeighborAddress_Object = MibTableColumn
vRtrPimNgIfNeighborAddress = _VRtrPimNgIfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 2),
    _VRtrPimNgIfNeighborAddress_Type()
)
vRtrPimNgIfNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborAddress.setStatus("current")
_VRtrPimNgIfNeighborUpTime_Type = Unsigned32
_VRtrPimNgIfNeighborUpTime_Object = MibTableColumn
vRtrPimNgIfNeighborUpTime = _VRtrPimNgIfNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 3),
    _VRtrPimNgIfNeighborUpTime_Type()
)
vRtrPimNgIfNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborUpTime.setUnits("seconds")
_VRtrPimNgIfNeighborExpiryTime_Type = Unsigned32
_VRtrPimNgIfNeighborExpiryTime_Object = MibTableColumn
vRtrPimNgIfNeighborExpiryTime = _VRtrPimNgIfNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 4),
    _VRtrPimNgIfNeighborExpiryTime_Type()
)
vRtrPimNgIfNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborExpiryTime.setUnits("seconds")
_VRtrPimNgIfNeighborGenId_Type = Unsigned32
_VRtrPimNgIfNeighborGenId_Object = MibTableColumn
vRtrPimNgIfNeighborGenId = _VRtrPimNgIfNeighborGenId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 5),
    _VRtrPimNgIfNeighborGenId_Type()
)
vRtrPimNgIfNeighborGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborGenId.setStatus("current")
_VRtrPimNgIfNeighborDrPriority_Type = Unsigned32
_VRtrPimNgIfNeighborDrPriority_Object = MibTableColumn
vRtrPimNgIfNeighborDrPriority = _VRtrPimNgIfNeighborDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 6),
    _VRtrPimNgIfNeighborDrPriority_Type()
)
vRtrPimNgIfNeighborDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborDrPriority.setStatus("current")
_VRtrPimNgIfNeighborDrPriorPrsnt_Type = TruthValue
_VRtrPimNgIfNeighborDrPriorPrsnt_Object = MibTableColumn
vRtrPimNgIfNeighborDrPriorPrsnt = _VRtrPimNgIfNeighborDrPriorPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 7),
    _VRtrPimNgIfNeighborDrPriorPrsnt_Type()
)
vRtrPimNgIfNeighborDrPriorPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborDrPriorPrsnt.setStatus("current")
_VRtrPimNgIfNeighborLanDelay_Type = Unsigned32
_VRtrPimNgIfNeighborLanDelay_Object = MibTableColumn
vRtrPimNgIfNeighborLanDelay = _VRtrPimNgIfNeighborLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 8),
    _VRtrPimNgIfNeighborLanDelay_Type()
)
vRtrPimNgIfNeighborLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborLanDelay.setUnits("milliseconds")
_VRtrPimNgIfNeighborLanDlayPrsnt_Type = TruthValue
_VRtrPimNgIfNeighborLanDlayPrsnt_Object = MibTableColumn
vRtrPimNgIfNeighborLanDlayPrsnt = _VRtrPimNgIfNeighborLanDlayPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 9),
    _VRtrPimNgIfNeighborLanDlayPrsnt_Type()
)
vRtrPimNgIfNeighborLanDlayPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborLanDlayPrsnt.setStatus("current")
_VRtrPimNgIfNeighborTrckngSpprt_Type = TruthValue
_VRtrPimNgIfNeighborTrckngSpprt_Object = MibTableColumn
vRtrPimNgIfNeighborTrckngSpprt = _VRtrPimNgIfNeighborTrckngSpprt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 10),
    _VRtrPimNgIfNeighborTrckngSpprt_Type()
)
vRtrPimNgIfNeighborTrckngSpprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborTrckngSpprt.setStatus("current")
_VRtrPimNgIfNeighborHoldTime_Type = Unsigned32
_VRtrPimNgIfNeighborHoldTime_Object = MibTableColumn
vRtrPimNgIfNeighborHoldTime = _VRtrPimNgIfNeighborHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 11),
    _VRtrPimNgIfNeighborHoldTime_Type()
)
vRtrPimNgIfNeighborHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborHoldTime.setUnits("seconds")
_VRtrPimNgIfNeighborOvrdeIntrvl_Type = Unsigned32
_VRtrPimNgIfNeighborOvrdeIntrvl_Object = MibTableColumn
vRtrPimNgIfNeighborOvrdeIntrvl = _VRtrPimNgIfNeighborOvrdeIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 12),
    _VRtrPimNgIfNeighborOvrdeIntrvl_Type()
)
vRtrPimNgIfNeighborOvrdeIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborOvrdeIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborOvrdeIntrvl.setUnits("milliseconds")
_VRtrPimNgIfNeighborJASupport_Type = TruthValue
_VRtrPimNgIfNeighborJASupport_Object = MibTableColumn
vRtrPimNgIfNeighborJASupport = _VRtrPimNgIfNeighborJASupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 4, 1, 13),
    _VRtrPimNgIfNeighborJASupport_Type()
)
vRtrPimNgIfNeighborJASupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborJASupport.setStatus("current")
_VRtrPimNgIfGrpSrcTable_Object = MibTable
vRtrPimNgIfGrpSrcTable = _VRtrPimNgIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcTable.setStatus("current")
_VRtrPimNgIfGrpSrcEntry_Object = MibTableRow
vRtrPimNgIfGrpSrcEntry = _VRtrPimNgIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1)
)
vRtrPimNgIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcGroupAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcSourceAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcEntry.setStatus("current")


class _VRtrPimNgIfGrpSrcType_Type(Integer32):
    """Custom type vRtrPimNgIfGrpSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starStarRP", 0),
          ("starG", 1),
          ("sg", 2))
    )


_VRtrPimNgIfGrpSrcType_Type.__name__ = "Integer32"
_VRtrPimNgIfGrpSrcType_Object = MibTableColumn
vRtrPimNgIfGrpSrcType = _VRtrPimNgIfGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 1),
    _VRtrPimNgIfGrpSrcType_Type()
)
vRtrPimNgIfGrpSrcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcType.setStatus("current")
_VRtrPimNgIfGrpSrcGroupAddrType_Type = InetAddressType
_VRtrPimNgIfGrpSrcGroupAddrType_Object = MibTableColumn
vRtrPimNgIfGrpSrcGroupAddrType = _VRtrPimNgIfGrpSrcGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 2),
    _VRtrPimNgIfGrpSrcGroupAddrType_Type()
)
vRtrPimNgIfGrpSrcGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcGroupAddrType.setStatus("current")


class _VRtrPimNgIfGrpSrcGroupAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcGroupAddress_Object = MibTableColumn
vRtrPimNgIfGrpSrcGroupAddress = _VRtrPimNgIfGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 3),
    _VRtrPimNgIfGrpSrcGroupAddress_Type()
)
vRtrPimNgIfGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcGroupAddress.setStatus("current")
_VRtrPimNgIfGrpSrcSourceAddrType_Type = InetAddressType
_VRtrPimNgIfGrpSrcSourceAddrType_Object = MibTableColumn
vRtrPimNgIfGrpSrcSourceAddrType = _VRtrPimNgIfGrpSrcSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 4),
    _VRtrPimNgIfGrpSrcSourceAddrType_Type()
)
vRtrPimNgIfGrpSrcSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcSourceAddrType.setStatus("current")


class _VRtrPimNgIfGrpSrcSourceAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcSourceAddress_Object = MibTableColumn
vRtrPimNgIfGrpSrcSourceAddress = _VRtrPimNgIfGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 5),
    _VRtrPimNgIfGrpSrcSourceAddress_Type()
)
vRtrPimNgIfGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcSourceAddress.setStatus("current")
_VRtrPimNgIfGrpSrcRPAddrType_Type = InetAddressType
_VRtrPimNgIfGrpSrcRPAddrType_Object = MibTableColumn
vRtrPimNgIfGrpSrcRPAddrType = _VRtrPimNgIfGrpSrcRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 6),
    _VRtrPimNgIfGrpSrcRPAddrType_Type()
)
vRtrPimNgIfGrpSrcRPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRPAddrType.setStatus("current")


class _VRtrPimNgIfGrpSrcRPAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcRPAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcRPAddress_Object = MibTableColumn
vRtrPimNgIfGrpSrcRPAddress = _VRtrPimNgIfGrpSrcRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 7),
    _VRtrPimNgIfGrpSrcRPAddress_Type()
)
vRtrPimNgIfGrpSrcRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRPAddress.setStatus("current")


class _VRtrPimNgIfGrpSrcJPState_Type(Integer32):
    """Custom type vRtrPimNgIfGrpSrcJPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_VRtrPimNgIfGrpSrcJPState_Type.__name__ = "Integer32"
_VRtrPimNgIfGrpSrcJPState_Object = MibTableColumn
vRtrPimNgIfGrpSrcJPState = _VRtrPimNgIfGrpSrcJPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 8),
    _VRtrPimNgIfGrpSrcJPState_Type()
)
vRtrPimNgIfGrpSrcJPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcJPState.setStatus("current")
_VRtrPimNgIfGrpSrcPrunePendTimer_Type = Unsigned32
_VRtrPimNgIfGrpSrcPrunePendTimer_Object = MibTableColumn
vRtrPimNgIfGrpSrcPrunePendTimer = _VRtrPimNgIfGrpSrcPrunePendTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 9),
    _VRtrPimNgIfGrpSrcPrunePendTimer_Type()
)
vRtrPimNgIfGrpSrcPrunePendTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcPrunePendTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcPrunePendTimer.setUnits("seconds")
_VRtrPimNgIfGrpSrcJoinPruneTimer_Type = Unsigned32
_VRtrPimNgIfGrpSrcJoinPruneTimer_Object = MibTableColumn
vRtrPimNgIfGrpSrcJoinPruneTimer = _VRtrPimNgIfGrpSrcJoinPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 10),
    _VRtrPimNgIfGrpSrcJoinPruneTimer_Type()
)
vRtrPimNgIfGrpSrcJoinPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcJoinPruneTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcJoinPruneTimer.setUnits("seconds")


class _VRtrPimNgIfGrpSrcJPRptState_Type(Integer32):
    """Custom type vRtrPimNgIfGrpSrcJPRptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_VRtrPimNgIfGrpSrcJPRptState_Type.__name__ = "Integer32"
_VRtrPimNgIfGrpSrcJPRptState_Object = MibTableColumn
vRtrPimNgIfGrpSrcJPRptState = _VRtrPimNgIfGrpSrcJPRptState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 11),
    _VRtrPimNgIfGrpSrcJPRptState_Type()
)
vRtrPimNgIfGrpSrcJPRptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcJPRptState.setStatus("current")
_VRtrPimNgIfGrpSrcRptPrnePendTmr_Type = Unsigned32
_VRtrPimNgIfGrpSrcRptPrnePendTmr_Object = MibTableColumn
vRtrPimNgIfGrpSrcRptPrnePendTmr = _VRtrPimNgIfGrpSrcRptPrnePendTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 12),
    _VRtrPimNgIfGrpSrcRptPrnePendTmr_Type()
)
vRtrPimNgIfGrpSrcRptPrnePendTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRptPrnePendTmr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRptPrnePendTmr.setUnits("seconds")
_VRtrPimNgIfGrpSrcRptJoinPrneTmr_Type = Unsigned32
_VRtrPimNgIfGrpSrcRptJoinPrneTmr_Object = MibTableColumn
vRtrPimNgIfGrpSrcRptJoinPrneTmr = _VRtrPimNgIfGrpSrcRptJoinPrneTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 13),
    _VRtrPimNgIfGrpSrcRptJoinPrneTmr_Type()
)
vRtrPimNgIfGrpSrcRptJoinPrneTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRptJoinPrneTmr.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRptJoinPrneTmr.setUnits("seconds")


class _VRtrPimNgIfGrpSrcAssertState_Type(Integer32):
    """Custom type vRtrPimNgIfGrpSrcAssertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("lostAssert", 1),
          ("wonAssert", 2))
    )


_VRtrPimNgIfGrpSrcAssertState_Type.__name__ = "Integer32"
_VRtrPimNgIfGrpSrcAssertState_Object = MibTableColumn
vRtrPimNgIfGrpSrcAssertState = _VRtrPimNgIfGrpSrcAssertState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 14),
    _VRtrPimNgIfGrpSrcAssertState_Type()
)
vRtrPimNgIfGrpSrcAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAssertState.setStatus("current")
_VRtrPimNgIfGrpSrcAssertTimer_Type = Unsigned32
_VRtrPimNgIfGrpSrcAssertTimer_Object = MibTableColumn
vRtrPimNgIfGrpSrcAssertTimer = _VRtrPimNgIfGrpSrcAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 15),
    _VRtrPimNgIfGrpSrcAssertTimer_Type()
)
vRtrPimNgIfGrpSrcAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAssertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAssertTimer.setUnits("seconds")
_VRtrPimNgIfGrpSrcAssertMetric_Type = Unsigned32
_VRtrPimNgIfGrpSrcAssertMetric_Object = MibTableColumn
vRtrPimNgIfGrpSrcAssertMetric = _VRtrPimNgIfGrpSrcAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 16),
    _VRtrPimNgIfGrpSrcAssertMetric_Type()
)
vRtrPimNgIfGrpSrcAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAssertMetric.setStatus("current")
_VRtrPimNgIfGrpSrcAsrtMetricPref_Type = Unsigned32
_VRtrPimNgIfGrpSrcAsrtMetricPref_Object = MibTableColumn
vRtrPimNgIfGrpSrcAsrtMetricPref = _VRtrPimNgIfGrpSrcAsrtMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 17),
    _VRtrPimNgIfGrpSrcAsrtMetricPref_Type()
)
vRtrPimNgIfGrpSrcAsrtMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAsrtMetricPref.setStatus("current")
_VRtrPimNgIfGrpSrcAssertRPTBit_Type = TruthValue
_VRtrPimNgIfGrpSrcAssertRPTBit_Object = MibTableColumn
vRtrPimNgIfGrpSrcAssertRPTBit = _VRtrPimNgIfGrpSrcAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 18),
    _VRtrPimNgIfGrpSrcAssertRPTBit_Type()
)
vRtrPimNgIfGrpSrcAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAssertRPTBit.setStatus("current")
_VRtrPimNgIfGrpSrcAsrtWinnerMtrc_Type = Unsigned32
_VRtrPimNgIfGrpSrcAsrtWinnerMtrc_Object = MibTableColumn
vRtrPimNgIfGrpSrcAsrtWinnerMtrc = _VRtrPimNgIfGrpSrcAsrtWinnerMtrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 19),
    _VRtrPimNgIfGrpSrcAsrtWinnerMtrc_Type()
)
vRtrPimNgIfGrpSrcAsrtWinnerMtrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAsrtWinnerMtrc.setStatus("current")
_VRtrPimNgIfGrpSrcAsrtWnrMtrcPrf_Type = Unsigned32
_VRtrPimNgIfGrpSrcAsrtWnrMtrcPrf_Object = MibTableColumn
vRtrPimNgIfGrpSrcAsrtWnrMtrcPrf = _VRtrPimNgIfGrpSrcAsrtWnrMtrcPrf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 20),
    _VRtrPimNgIfGrpSrcAsrtWnrMtrcPrf_Type()
)
vRtrPimNgIfGrpSrcAsrtWnrMtrcPrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAsrtWnrMtrcPrf.setStatus("current")
_VRtrPimNgIfGrpSrcAsrtWnrRPTBit_Type = TruthValue
_VRtrPimNgIfGrpSrcAsrtWnrRPTBit_Object = MibTableColumn
vRtrPimNgIfGrpSrcAsrtWnrRPTBit = _VRtrPimNgIfGrpSrcAsrtWnrRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 21),
    _VRtrPimNgIfGrpSrcAsrtWnrRPTBit_Type()
)
vRtrPimNgIfGrpSrcAsrtWnrRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAsrtWnrRPTBit.setStatus("current")
_VRtrPimNgIfGrpSrcAsrtWnrAddrTyp_Type = InetAddressType
_VRtrPimNgIfGrpSrcAsrtWnrAddrTyp_Object = MibTableColumn
vRtrPimNgIfGrpSrcAsrtWnrAddrTyp = _VRtrPimNgIfGrpSrcAsrtWnrAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 22),
    _VRtrPimNgIfGrpSrcAsrtWnrAddrTyp_Type()
)
vRtrPimNgIfGrpSrcAsrtWnrAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAsrtWnrAddrTyp.setStatus("current")


class _VRtrPimNgIfGrpSrcAsrtWinnerAddr_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcAsrtWinnerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcAsrtWinnerAddr_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcAsrtWinnerAddr_Object = MibTableColumn
vRtrPimNgIfGrpSrcAsrtWinnerAddr = _VRtrPimNgIfGrpSrcAsrtWinnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 23),
    _VRtrPimNgIfGrpSrcAsrtWinnerAddr_Type()
)
vRtrPimNgIfGrpSrcAsrtWinnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcAsrtWinnerAddr.setStatus("current")
_VRtrPimNgIfGrpSrcUpTime_Type = Unsigned32
_VRtrPimNgIfGrpSrcUpTime_Object = MibTableColumn
vRtrPimNgIfGrpSrcUpTime = _VRtrPimNgIfGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 24),
    _VRtrPimNgIfGrpSrcUpTime_Type()
)
vRtrPimNgIfGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcUpTime.setUnits("seconds")
_VRtrPimNgIfGrpSrcDataMtIfIndex_Type = InterfaceIndexOrZero
_VRtrPimNgIfGrpSrcDataMtIfIndex_Object = MibTableColumn
vRtrPimNgIfGrpSrcDataMtIfIndex = _VRtrPimNgIfGrpSrcDataMtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 5, 1, 25),
    _VRtrPimNgIfGrpSrcDataMtIfIndex_Type()
)
vRtrPimNgIfGrpSrcDataMtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcDataMtIfIndex.setStatus("current")
_VRtrPimNgIfStatsTable_Object = MibTable
vRtrPimNgIfStatsTable = _VRtrPimNgIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfStatsTable.setStatus("current")
_VRtrPimNgIfStatsEntry_Object = MibTableRow
vRtrPimNgIfStatsEntry = _VRtrPimNgIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfStatsEntry.setStatus("current")
_VRtrPimNgIfTxPkts_Type = Counter32
_VRtrPimNgIfTxPkts_Object = MibTableColumn
vRtrPimNgIfTxPkts = _VRtrPimNgIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 1),
    _VRtrPimNgIfTxPkts_Type()
)
vRtrPimNgIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxPkts.setStatus("current")
_VRtrPimNgIfTxHellos_Type = Counter32
_VRtrPimNgIfTxHellos_Object = MibTableColumn
vRtrPimNgIfTxHellos = _VRtrPimNgIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 2),
    _VRtrPimNgIfTxHellos_Type()
)
vRtrPimNgIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxHellos.setStatus("current")
_VRtrPimNgIfTxAsserts_Type = Counter32
_VRtrPimNgIfTxAsserts_Object = MibTableColumn
vRtrPimNgIfTxAsserts = _VRtrPimNgIfTxAsserts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 3),
    _VRtrPimNgIfTxAsserts_Type()
)
vRtrPimNgIfTxAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxAsserts.setStatus("current")
_VRtrPimNgIfTxRegisterStops_Type = Counter32
_VRtrPimNgIfTxRegisterStops_Object = MibTableColumn
vRtrPimNgIfTxRegisterStops = _VRtrPimNgIfTxRegisterStops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 4),
    _VRtrPimNgIfTxRegisterStops_Type()
)
vRtrPimNgIfTxRegisterStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxRegisterStops.setStatus("current")
_VRtrPimNgIfTxRegisterStopErrs_Type = Counter32
_VRtrPimNgIfTxRegisterStopErrs_Object = MibTableColumn
vRtrPimNgIfTxRegisterStopErrs = _VRtrPimNgIfTxRegisterStopErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 5),
    _VRtrPimNgIfTxRegisterStopErrs_Type()
)
vRtrPimNgIfTxRegisterStopErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxRegisterStopErrs.setStatus("current")
_VRtrPimNgIfTxBsmPdus_Type = Counter32
_VRtrPimNgIfTxBsmPdus_Object = MibTableColumn
vRtrPimNgIfTxBsmPdus = _VRtrPimNgIfTxBsmPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 6),
    _VRtrPimNgIfTxBsmPdus_Type()
)
vRtrPimNgIfTxBsmPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxBsmPdus.setStatus("current")
_VRtrPimNgIfTxBsmErrs_Type = Counter32
_VRtrPimNgIfTxBsmErrs_Object = MibTableColumn
vRtrPimNgIfTxBsmErrs = _VRtrPimNgIfTxBsmErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 7),
    _VRtrPimNgIfTxBsmErrs_Type()
)
vRtrPimNgIfTxBsmErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxBsmErrs.setStatus("current")
_VRtrPimNgIfRxPkts_Type = Counter32
_VRtrPimNgIfRxPkts_Object = MibTableColumn
vRtrPimNgIfRxPkts = _VRtrPimNgIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 8),
    _VRtrPimNgIfRxPkts_Type()
)
vRtrPimNgIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxPkts.setStatus("current")
_VRtrPimNgIfRxHellos_Type = Counter32
_VRtrPimNgIfRxHellos_Object = MibTableColumn
vRtrPimNgIfRxHellos = _VRtrPimNgIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 9),
    _VRtrPimNgIfRxHellos_Type()
)
vRtrPimNgIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxHellos.setStatus("current")
_VRtrPimNgIfRxHellosDropped_Type = Counter32
_VRtrPimNgIfRxHellosDropped_Object = MibTableColumn
vRtrPimNgIfRxHellosDropped = _VRtrPimNgIfRxHellosDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 10),
    _VRtrPimNgIfRxHellosDropped_Type()
)
vRtrPimNgIfRxHellosDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxHellosDropped.setStatus("current")
_VRtrPimNgIfRxNbrUnknown_Type = Counter32
_VRtrPimNgIfRxNbrUnknown_Object = MibTableColumn
vRtrPimNgIfRxNbrUnknown = _VRtrPimNgIfRxNbrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 11),
    _VRtrPimNgIfRxNbrUnknown_Type()
)
vRtrPimNgIfRxNbrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxNbrUnknown.setStatus("current")
_VRtrPimNgIfRxBadChecksumDiscard_Type = Counter32
_VRtrPimNgIfRxBadChecksumDiscard_Object = MibTableColumn
vRtrPimNgIfRxBadChecksumDiscard = _VRtrPimNgIfRxBadChecksumDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 12),
    _VRtrPimNgIfRxBadChecksumDiscard_Type()
)
vRtrPimNgIfRxBadChecksumDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBadChecksumDiscard.setStatus("current")
_VRtrPimNgIfRxBadVersionDiscard_Type = Counter32
_VRtrPimNgIfRxBadVersionDiscard_Object = MibTableColumn
vRtrPimNgIfRxBadVersionDiscard = _VRtrPimNgIfRxBadVersionDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 13),
    _VRtrPimNgIfRxBadVersionDiscard_Type()
)
vRtrPimNgIfRxBadVersionDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBadVersionDiscard.setStatus("current")
_VRtrPimNgIfRxBadEncodings_Type = Counter32
_VRtrPimNgIfRxBadEncodings_Object = MibTableColumn
vRtrPimNgIfRxBadEncodings = _VRtrPimNgIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 14),
    _VRtrPimNgIfRxBadEncodings_Type()
)
vRtrPimNgIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBadEncodings.setStatus("current")
_VRtrPimNgIfRxAsserts_Type = Counter32
_VRtrPimNgIfRxAsserts_Object = MibTableColumn
vRtrPimNgIfRxAsserts = _VRtrPimNgIfRxAsserts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 15),
    _VRtrPimNgIfRxAsserts_Type()
)
vRtrPimNgIfRxAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxAsserts.setStatus("current")
_VRtrPimNgIfRxAssertErrs_Type = Counter32
_VRtrPimNgIfRxAssertErrs_Object = MibTableColumn
vRtrPimNgIfRxAssertErrs = _VRtrPimNgIfRxAssertErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 16),
    _VRtrPimNgIfRxAssertErrs_Type()
)
vRtrPimNgIfRxAssertErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxAssertErrs.setStatus("current")
_VRtrPimNgIfRxRegisters_Type = Counter32
_VRtrPimNgIfRxRegisters_Object = MibTableColumn
vRtrPimNgIfRxRegisters = _VRtrPimNgIfRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 17),
    _VRtrPimNgIfRxRegisters_Type()
)
vRtrPimNgIfRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxRegisters.setStatus("current")
_VRtrPimNgIfRxRegisterErrs_Type = Counter32
_VRtrPimNgIfRxRegisterErrs_Object = MibTableColumn
vRtrPimNgIfRxRegisterErrs = _VRtrPimNgIfRxRegisterErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 18),
    _VRtrPimNgIfRxRegisterErrs_Type()
)
vRtrPimNgIfRxRegisterErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxRegisterErrs.setStatus("current")
_VRtrPimNgIfRxNullRegisters_Type = Counter32
_VRtrPimNgIfRxNullRegisters_Object = MibTableColumn
vRtrPimNgIfRxNullRegisters = _VRtrPimNgIfRxNullRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 19),
    _VRtrPimNgIfRxNullRegisters_Type()
)
vRtrPimNgIfRxNullRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxNullRegisters.setStatus("current")
_VRtrPimNgIfRxRegisterStops_Type = Counter32
_VRtrPimNgIfRxRegisterStops_Object = MibTableColumn
vRtrPimNgIfRxRegisterStops = _VRtrPimNgIfRxRegisterStops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 20),
    _VRtrPimNgIfRxRegisterStops_Type()
)
vRtrPimNgIfRxRegisterStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxRegisterStops.setStatus("current")
_VRtrPimNgIfRxRegisterStopErrs_Type = Counter32
_VRtrPimNgIfRxRegisterStopErrs_Object = MibTableColumn
vRtrPimNgIfRxRegisterStopErrs = _VRtrPimNgIfRxRegisterStopErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 21),
    _VRtrPimNgIfRxRegisterStopErrs_Type()
)
vRtrPimNgIfRxRegisterStopErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxRegisterStopErrs.setStatus("current")
_VRtrPimNgIfRxCRPAdvNoRtrAlert_Type = Counter32
_VRtrPimNgIfRxCRPAdvNoRtrAlert_Object = MibTableColumn
vRtrPimNgIfRxCRPAdvNoRtrAlert = _VRtrPimNgIfRxCRPAdvNoRtrAlert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 22),
    _VRtrPimNgIfRxCRPAdvNoRtrAlert_Type()
)
vRtrPimNgIfRxCRPAdvNoRtrAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxCRPAdvNoRtrAlert.setStatus("current")
_VRtrPimNgIfRxBsmPdus_Type = Counter32
_VRtrPimNgIfRxBsmPdus_Object = MibTableColumn
vRtrPimNgIfRxBsmPdus = _VRtrPimNgIfRxBsmPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 23),
    _VRtrPimNgIfRxBsmPdus_Type()
)
vRtrPimNgIfRxBsmPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBsmPdus.setStatus("current")
_VRtrPimNgIfRxBsmPduDrops_Type = Counter32
_VRtrPimNgIfRxBsmPduDrops_Object = MibTableColumn
vRtrPimNgIfRxBsmPduDrops = _VRtrPimNgIfRxBsmPduDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 24),
    _VRtrPimNgIfRxBsmPduDrops_Type()
)
vRtrPimNgIfRxBsmPduDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBsmPduDrops.setStatus("current")
_VRtrPimNgIfStarStarRPTypes_Type = Gauge32
_VRtrPimNgIfStarStarRPTypes_Object = MibTableColumn
vRtrPimNgIfStarStarRPTypes = _VRtrPimNgIfStarStarRPTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 25),
    _VRtrPimNgIfStarStarRPTypes_Type()
)
vRtrPimNgIfStarStarRPTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfStarStarRPTypes.setStatus("current")
_VRtrPimNgIfStarGTypes_Type = Gauge32
_VRtrPimNgIfStarGTypes_Object = MibTableColumn
vRtrPimNgIfStarGTypes = _VRtrPimNgIfStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 26),
    _VRtrPimNgIfStarGTypes_Type()
)
vRtrPimNgIfStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfStarGTypes.setStatus("current")
_VRtrPimNgIfSGTypes_Type = Gauge32
_VRtrPimNgIfSGTypes_Object = MibTableColumn
vRtrPimNgIfSGTypes = _VRtrPimNgIfSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 27),
    _VRtrPimNgIfSGTypes_Type()
)
vRtrPimNgIfSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfSGTypes.setStatus("current")
_VRtrPimNgIfJoinPolicyDrops_Type = Counter32
_VRtrPimNgIfJoinPolicyDrops_Object = MibTableColumn
vRtrPimNgIfJoinPolicyDrops = _VRtrPimNgIfJoinPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 28),
    _VRtrPimNgIfJoinPolicyDrops_Type()
)
vRtrPimNgIfJoinPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfJoinPolicyDrops.setStatus("current")
_VRtrPimNgIfRegisterPolicyDrops_Type = Counter32
_VRtrPimNgIfRegisterPolicyDrops_Object = MibTableColumn
vRtrPimNgIfRegisterPolicyDrops = _VRtrPimNgIfRegisterPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 29),
    _VRtrPimNgIfRegisterPolicyDrops_Type()
)
vRtrPimNgIfRegisterPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRegisterPolicyDrops.setStatus("current")
_VRtrPimNgIfBtrImpPolicyDrops_Type = Counter32
_VRtrPimNgIfBtrImpPolicyDrops_Object = MibTableColumn
vRtrPimNgIfBtrImpPolicyDrops = _VRtrPimNgIfBtrImpPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 30),
    _VRtrPimNgIfBtrImpPolicyDrops_Type()
)
vRtrPimNgIfBtrImpPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfBtrImpPolicyDrops.setStatus("current")
_VRtrPimNgIfBtrExpPolicyDrops_Type = Counter32
_VRtrPimNgIfBtrExpPolicyDrops_Object = MibTableColumn
vRtrPimNgIfBtrExpPolicyDrops = _VRtrPimNgIfBtrExpPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 31),
    _VRtrPimNgIfBtrExpPolicyDrops_Type()
)
vRtrPimNgIfBtrExpPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfBtrExpPolicyDrops.setStatus("current")
_VRtrPimNgIfTxJoinPrunes_Type = Counter32
_VRtrPimNgIfTxJoinPrunes_Object = MibTableColumn
vRtrPimNgIfTxJoinPrunes = _VRtrPimNgIfTxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 32),
    _VRtrPimNgIfTxJoinPrunes_Type()
)
vRtrPimNgIfTxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxJoinPrunes.setStatus("current")
_VRtrPimNgIfRxJoinPrunes_Type = Counter32
_VRtrPimNgIfRxJoinPrunes_Object = MibTableColumn
vRtrPimNgIfRxJoinPrunes = _VRtrPimNgIfRxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 33),
    _VRtrPimNgIfRxJoinPrunes_Type()
)
vRtrPimNgIfRxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxJoinPrunes.setStatus("current")
_VRtrPimNgIfRxInvalidJoinPrunes_Type = Counter32
_VRtrPimNgIfRxInvalidJoinPrunes_Object = MibTableColumn
vRtrPimNgIfRxInvalidJoinPrunes = _VRtrPimNgIfRxInvalidJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 34),
    _VRtrPimNgIfRxInvalidJoinPrunes_Type()
)
vRtrPimNgIfRxInvalidJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxInvalidJoinPrunes.setStatus("current")
_VRtrPimNgIfRxInvalidRegisters_Type = Counter32
_VRtrPimNgIfRxInvalidRegisters_Object = MibTableColumn
vRtrPimNgIfRxInvalidRegisters = _VRtrPimNgIfRxInvalidRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 35),
    _VRtrPimNgIfRxInvalidRegisters_Type()
)
vRtrPimNgIfRxInvalidRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxInvalidRegisters.setStatus("current")
_VRtrPimNgIfRxUnknownPdus_Type = Counter32
_VRtrPimNgIfRxUnknownPdus_Object = MibTableColumn
vRtrPimNgIfRxUnknownPdus = _VRtrPimNgIfRxUnknownPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 36),
    _VRtrPimNgIfRxUnknownPdus_Type()
)
vRtrPimNgIfRxUnknownPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxUnknownPdus.setStatus("current")
_VRtrPimNgIfRxJoinPruneErrs_Type = Counter32
_VRtrPimNgIfRxJoinPruneErrs_Object = MibTableColumn
vRtrPimNgIfRxJoinPruneErrs = _VRtrPimNgIfRxJoinPruneErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 37),
    _VRtrPimNgIfRxJoinPruneErrs_Type()
)
vRtrPimNgIfRxJoinPruneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxJoinPruneErrs.setStatus("current")
_VRtrPimNgIfRxBSMNoRouterAlertDrops_Type = Counter32
_VRtrPimNgIfRxBSMNoRouterAlertDrops_Object = MibTableColumn
vRtrPimNgIfRxBSMNoRouterAlertDrops = _VRtrPimNgIfRxBSMNoRouterAlertDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 38),
    _VRtrPimNgIfRxBSMNoRouterAlertDrops_Type()
)
vRtrPimNgIfRxBSMNoRouterAlertDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBSMNoRouterAlertDrops.setStatus("current")
_VRtrPimNgIfRxBSMWrongIfDrops_Type = Counter32
_VRtrPimNgIfRxBSMWrongIfDrops_Object = MibTableColumn
vRtrPimNgIfRxBSMWrongIfDrops = _VRtrPimNgIfRxBSMWrongIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 39),
    _VRtrPimNgIfRxBSMWrongIfDrops_Type()
)
vRtrPimNgIfRxBSMWrongIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBSMWrongIfDrops.setStatus("current")
_VRtrPimNgIfMcacPolicyDrops_Type = Counter32
_VRtrPimNgIfMcacPolicyDrops_Object = MibTableColumn
vRtrPimNgIfMcacPolicyDrops = _VRtrPimNgIfMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 40),
    _VRtrPimNgIfMcacPolicyDrops_Type()
)
vRtrPimNgIfMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfMcacPolicyDrops.setStatus("current")
_VRtrPimNgIfTxIntraASAD_Type = Counter32
_VRtrPimNgIfTxIntraASAD_Object = MibTableColumn
vRtrPimNgIfTxIntraASAD = _VRtrPimNgIfTxIntraASAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 41),
    _VRtrPimNgIfTxIntraASAD_Type()
)
vRtrPimNgIfTxIntraASAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxIntraASAD.setStatus("current")
_VRtrPimNgIfRxIntraASAD_Type = Counter32
_VRtrPimNgIfRxIntraASAD_Object = MibTableColumn
vRtrPimNgIfRxIntraASAD = _VRtrPimNgIfRxIntraASAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 42),
    _VRtrPimNgIfRxIntraASAD_Type()
)
vRtrPimNgIfRxIntraASAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxIntraASAD.setStatus("current")
_VRtrPimNgIfRxIntraASADErrs_Type = Counter32
_VRtrPimNgIfRxIntraASADErrs_Object = MibTableColumn
vRtrPimNgIfRxIntraASADErrs = _VRtrPimNgIfRxIntraASADErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 43),
    _VRtrPimNgIfRxIntraASADErrs_Type()
)
vRtrPimNgIfRxIntraASADErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxIntraASADErrs.setStatus("current")
_VRtrPimNgIfTxInterASAD_Type = Counter32
_VRtrPimNgIfTxInterASAD_Object = MibTableColumn
vRtrPimNgIfTxInterASAD = _VRtrPimNgIfTxInterASAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 44),
    _VRtrPimNgIfTxInterASAD_Type()
)
vRtrPimNgIfTxInterASAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxInterASAD.setStatus("current")
_VRtrPimNgIfRxInterASAD_Type = Counter32
_VRtrPimNgIfRxInterASAD_Object = MibTableColumn
vRtrPimNgIfRxInterASAD = _VRtrPimNgIfRxInterASAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 45),
    _VRtrPimNgIfRxInterASAD_Type()
)
vRtrPimNgIfRxInterASAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxInterASAD.setStatus("current")
_VRtrPimNgIfRxInterASADErrs_Type = Counter32
_VRtrPimNgIfRxInterASADErrs_Object = MibTableColumn
vRtrPimNgIfRxInterASADErrs = _VRtrPimNgIfRxInterASADErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 46),
    _VRtrPimNgIfRxInterASADErrs_Type()
)
vRtrPimNgIfRxInterASADErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxInterASADErrs.setStatus("current")
_VRtrPimNgIfTxSpmsiAD_Type = Counter32
_VRtrPimNgIfTxSpmsiAD_Object = MibTableColumn
vRtrPimNgIfTxSpmsiAD = _VRtrPimNgIfTxSpmsiAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 47),
    _VRtrPimNgIfTxSpmsiAD_Type()
)
vRtrPimNgIfTxSpmsiAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxSpmsiAD.setStatus("current")
_VRtrPimNgIfRxSpmsiAD_Type = Counter32
_VRtrPimNgIfRxSpmsiAD_Object = MibTableColumn
vRtrPimNgIfRxSpmsiAD = _VRtrPimNgIfRxSpmsiAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 48),
    _VRtrPimNgIfRxSpmsiAD_Type()
)
vRtrPimNgIfRxSpmsiAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxSpmsiAD.setStatus("current")
_VRtrPimNgIfRxSpmsiADErrs_Type = Counter32
_VRtrPimNgIfRxSpmsiADErrs_Object = MibTableColumn
vRtrPimNgIfRxSpmsiADErrs = _VRtrPimNgIfRxSpmsiADErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 49),
    _VRtrPimNgIfRxSpmsiADErrs_Type()
)
vRtrPimNgIfRxSpmsiADErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxSpmsiADErrs.setStatus("current")
_VRtrPimNgIfTxLeafAD_Type = Counter32
_VRtrPimNgIfTxLeafAD_Object = MibTableColumn
vRtrPimNgIfTxLeafAD = _VRtrPimNgIfTxLeafAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 50),
    _VRtrPimNgIfTxLeafAD_Type()
)
vRtrPimNgIfTxLeafAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxLeafAD.setStatus("current")
_VRtrPimNgIfRxLeafAD_Type = Counter32
_VRtrPimNgIfRxLeafAD_Object = MibTableColumn
vRtrPimNgIfRxLeafAD = _VRtrPimNgIfRxLeafAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 51),
    _VRtrPimNgIfRxLeafAD_Type()
)
vRtrPimNgIfRxLeafAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxLeafAD.setStatus("current")
_VRtrPimNgIfRxLeafADErrs_Type = Counter32
_VRtrPimNgIfRxLeafADErrs_Object = MibTableColumn
vRtrPimNgIfRxLeafADErrs = _VRtrPimNgIfRxLeafADErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 52),
    _VRtrPimNgIfRxLeafADErrs_Type()
)
vRtrPimNgIfRxLeafADErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxLeafADErrs.setStatus("current")
_VRtrPimNgIfTxSrcActAD_Type = Counter32
_VRtrPimNgIfTxSrcActAD_Object = MibTableColumn
vRtrPimNgIfTxSrcActAD = _VRtrPimNgIfTxSrcActAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 53),
    _VRtrPimNgIfTxSrcActAD_Type()
)
vRtrPimNgIfTxSrcActAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxSrcActAD.setStatus("current")
_VRtrPimNgIfRxSrcActAD_Type = Counter32
_VRtrPimNgIfRxSrcActAD_Object = MibTableColumn
vRtrPimNgIfRxSrcActAD = _VRtrPimNgIfRxSrcActAD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 54),
    _VRtrPimNgIfRxSrcActAD_Type()
)
vRtrPimNgIfRxSrcActAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxSrcActAD.setStatus("current")
_VRtrPimNgIfTxSrcActADErrs_Type = Counter32
_VRtrPimNgIfTxSrcActADErrs_Object = MibTableColumn
vRtrPimNgIfTxSrcActADErrs = _VRtrPimNgIfTxSrcActADErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 55),
    _VRtrPimNgIfTxSrcActADErrs_Type()
)
vRtrPimNgIfTxSrcActADErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxSrcActADErrs.setStatus("current")
_VRtrPimNgIfTxSharedTreeJoin_Type = Counter32
_VRtrPimNgIfTxSharedTreeJoin_Object = MibTableColumn
vRtrPimNgIfTxSharedTreeJoin = _VRtrPimNgIfTxSharedTreeJoin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 56),
    _VRtrPimNgIfTxSharedTreeJoin_Type()
)
vRtrPimNgIfTxSharedTreeJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxSharedTreeJoin.setStatus("current")
_VRtrPimNgIfRxSharedTreeJoin_Type = Counter32
_VRtrPimNgIfRxSharedTreeJoin_Object = MibTableColumn
vRtrPimNgIfRxSharedTreeJoin = _VRtrPimNgIfRxSharedTreeJoin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 57),
    _VRtrPimNgIfRxSharedTreeJoin_Type()
)
vRtrPimNgIfRxSharedTreeJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxSharedTreeJoin.setStatus("current")
_VRtrPimNgIfRxSharedTreeJoinErrs_Type = Counter32
_VRtrPimNgIfRxSharedTreeJoinErrs_Object = MibTableColumn
vRtrPimNgIfRxSharedTreeJoinErrs = _VRtrPimNgIfRxSharedTreeJoinErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 58),
    _VRtrPimNgIfRxSharedTreeJoinErrs_Type()
)
vRtrPimNgIfRxSharedTreeJoinErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxSharedTreeJoinErrs.setStatus("current")
_VRtrPimNgIfTxSrcTreeJoin_Type = Counter32
_VRtrPimNgIfTxSrcTreeJoin_Object = MibTableColumn
vRtrPimNgIfTxSrcTreeJoin = _VRtrPimNgIfTxSrcTreeJoin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 59),
    _VRtrPimNgIfTxSrcTreeJoin_Type()
)
vRtrPimNgIfTxSrcTreeJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxSrcTreeJoin.setStatus("current")
_VRtrPimNgIfRxSrcTreeJoin_Type = Counter32
_VRtrPimNgIfRxSrcTreeJoin_Object = MibTableColumn
vRtrPimNgIfRxSrcTreeJoin = _VRtrPimNgIfRxSrcTreeJoin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 60),
    _VRtrPimNgIfRxSrcTreeJoin_Type()
)
vRtrPimNgIfRxSrcTreeJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxSrcTreeJoin.setStatus("current")
_VRtrPimNgIfRxSrcTreeJoinErrs_Type = Counter32
_VRtrPimNgIfRxSrcTreeJoinErrs_Object = MibTableColumn
vRtrPimNgIfRxSrcTreeJoinErrs = _VRtrPimNgIfRxSrcTreeJoinErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 61),
    _VRtrPimNgIfRxSrcTreeJoinErrs_Type()
)
vRtrPimNgIfRxSrcTreeJoinErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxSrcTreeJoinErrs.setStatus("current")
_VRtrPimNgIfTxBgpPkts_Type = Counter32
_VRtrPimNgIfTxBgpPkts_Object = MibTableColumn
vRtrPimNgIfTxBgpPkts = _VRtrPimNgIfTxBgpPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 62),
    _VRtrPimNgIfTxBgpPkts_Type()
)
vRtrPimNgIfTxBgpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxBgpPkts.setStatus("current")
_VRtrPimNgIfRxBgpPkts_Type = Counter32
_VRtrPimNgIfRxBgpPkts_Object = MibTableColumn
vRtrPimNgIfRxBgpPkts = _VRtrPimNgIfRxBgpPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 63),
    _VRtrPimNgIfRxBgpPkts_Type()
)
vRtrPimNgIfRxBgpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxBgpPkts.setStatus("current")
_VRtrPimNgIfTxMdtSafi_Type = Counter32
_VRtrPimNgIfTxMdtSafi_Object = MibTableColumn
vRtrPimNgIfTxMdtSafi = _VRtrPimNgIfTxMdtSafi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 64),
    _VRtrPimNgIfTxMdtSafi_Type()
)
vRtrPimNgIfTxMdtSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxMdtSafi.setStatus("current")
_VRtrPimNgIfRxMdtSafi_Type = Counter32
_VRtrPimNgIfRxMdtSafi_Object = MibTableColumn
vRtrPimNgIfRxMdtSafi = _VRtrPimNgIfRxMdtSafi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 65),
    _VRtrPimNgIfRxMdtSafi_Type()
)
vRtrPimNgIfRxMdtSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxMdtSafi.setStatus("current")
_VRtrPimNgIfRxMdtSafiErrs_Type = Counter32
_VRtrPimNgIfRxMdtSafiErrs_Object = MibTableColumn
vRtrPimNgIfRxMdtSafiErrs = _VRtrPimNgIfRxMdtSafiErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 66),
    _VRtrPimNgIfRxMdtSafiErrs_Type()
)
vRtrPimNgIfRxMdtSafiErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxMdtSafiErrs.setStatus("current")
_VRtrPimNgIfRxAutoRpGenErrs_Type = Counter32
_VRtrPimNgIfRxAutoRpGenErrs_Object = MibTableColumn
vRtrPimNgIfRxAutoRpGenErrs = _VRtrPimNgIfRxAutoRpGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 67),
    _VRtrPimNgIfRxAutoRpGenErrs_Type()
)
vRtrPimNgIfRxAutoRpGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxAutoRpGenErrs.setStatus("current")
_VRtrPimNgIfRxAutoRpAnnounce_Type = Counter32
_VRtrPimNgIfRxAutoRpAnnounce_Object = MibTableColumn
vRtrPimNgIfRxAutoRpAnnounce = _VRtrPimNgIfRxAutoRpAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 68),
    _VRtrPimNgIfRxAutoRpAnnounce_Type()
)
vRtrPimNgIfRxAutoRpAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxAutoRpAnnounce.setStatus("current")
_VRtrPimNgIfTxAutoRpAnnounce_Type = Counter32
_VRtrPimNgIfTxAutoRpAnnounce_Object = MibTableColumn
vRtrPimNgIfTxAutoRpAnnounce = _VRtrPimNgIfTxAutoRpAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 69),
    _VRtrPimNgIfTxAutoRpAnnounce_Type()
)
vRtrPimNgIfTxAutoRpAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxAutoRpAnnounce.setStatus("current")
_VRtrPimNgIfRxAutoRpAnnounceErrs_Type = Counter32
_VRtrPimNgIfRxAutoRpAnnounceErrs_Object = MibTableColumn
vRtrPimNgIfRxAutoRpAnnounceErrs = _VRtrPimNgIfRxAutoRpAnnounceErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 70),
    _VRtrPimNgIfRxAutoRpAnnounceErrs_Type()
)
vRtrPimNgIfRxAutoRpAnnounceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxAutoRpAnnounceErrs.setStatus("current")
_VRtrPimNgIfTxAutoRpAnnounceErrs_Type = Counter32
_VRtrPimNgIfTxAutoRpAnnounceErrs_Object = MibTableColumn
vRtrPimNgIfTxAutoRpAnnounceErrs = _VRtrPimNgIfTxAutoRpAnnounceErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 71),
    _VRtrPimNgIfTxAutoRpAnnounceErrs_Type()
)
vRtrPimNgIfTxAutoRpAnnounceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxAutoRpAnnounceErrs.setStatus("current")
_VRtrPimNgIfRxAutoRpMapping_Type = Counter32
_VRtrPimNgIfRxAutoRpMapping_Object = MibTableColumn
vRtrPimNgIfRxAutoRpMapping = _VRtrPimNgIfRxAutoRpMapping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 72),
    _VRtrPimNgIfRxAutoRpMapping_Type()
)
vRtrPimNgIfRxAutoRpMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxAutoRpMapping.setStatus("current")
_VRtrPimNgIfTxAutoRpMapping_Type = Counter32
_VRtrPimNgIfTxAutoRpMapping_Object = MibTableColumn
vRtrPimNgIfTxAutoRpMapping = _VRtrPimNgIfTxAutoRpMapping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 73),
    _VRtrPimNgIfTxAutoRpMapping_Type()
)
vRtrPimNgIfTxAutoRpMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxAutoRpMapping.setStatus("current")
_VRtrPimNgIfRxAutoRpMappingErrs_Type = Counter32
_VRtrPimNgIfRxAutoRpMappingErrs_Object = MibTableColumn
vRtrPimNgIfRxAutoRpMappingErrs = _VRtrPimNgIfRxAutoRpMappingErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 74),
    _VRtrPimNgIfRxAutoRpMappingErrs_Type()
)
vRtrPimNgIfRxAutoRpMappingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxAutoRpMappingErrs.setStatus("current")
_VRtrPimNgIfTxAutoRpMappingErrs_Type = Counter32
_VRtrPimNgIfTxAutoRpMappingErrs_Object = MibTableColumn
vRtrPimNgIfTxAutoRpMappingErrs = _VRtrPimNgIfTxAutoRpMappingErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 75),
    _VRtrPimNgIfTxAutoRpMappingErrs_Type()
)
vRtrPimNgIfTxAutoRpMappingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxAutoRpMappingErrs.setStatus("current")
_VRtrPimNgIfRxJoinPrunesMvpnRpfv_Type = Counter32
_VRtrPimNgIfRxJoinPrunesMvpnRpfv_Object = MibTableColumn
vRtrPimNgIfRxJoinPrunesMvpnRpfv = _VRtrPimNgIfRxJoinPrunesMvpnRpfv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 76),
    _VRtrPimNgIfRxJoinPrunesMvpnRpfv_Type()
)
vRtrPimNgIfRxJoinPrunesMvpnRpfv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxJoinPrunesMvpnRpfv.setStatus("current")
_VRtrPimNgIfTxJoinPrunesMvpnRpfv_Type = Counter32
_VRtrPimNgIfTxJoinPrunesMvpnRpfv_Object = MibTableColumn
vRtrPimNgIfTxJoinPrunesMvpnRpfv = _VRtrPimNgIfTxJoinPrunesMvpnRpfv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 77),
    _VRtrPimNgIfTxJoinPrunesMvpnRpfv_Type()
)
vRtrPimNgIfTxJoinPrunesMvpnRpfv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfTxJoinPrunesMvpnRpfv.setStatus("current")
_VRtrPimNgIfRxInvalidJPMvpnRpfv_Type = Counter32
_VRtrPimNgIfRxInvalidJPMvpnRpfv_Object = MibTableColumn
vRtrPimNgIfRxInvalidJPMvpnRpfv = _VRtrPimNgIfRxInvalidJPMvpnRpfv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 6, 1, 78),
    _VRtrPimNgIfRxInvalidJPMvpnRpfv_Type()
)
vRtrPimNgIfRxInvalidJPMvpnRpfv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfRxInvalidJPMvpnRpfv.setStatus("current")
_VRtrPimNgDataMtTable_Object = MibTable
vRtrPimNgDataMtTable = _VRtrPimNgDataMtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7)
)
if mibBuilder.loadTexts:
    vRtrPimNgDataMtTable.setStatus("current")
_VRtrPimNgDataMtEntry_Object = MibTableRow
vRtrPimNgDataMtEntry = _VRtrPimNgDataMtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1)
)
vRtrPimNgDataMtEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdSourceAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdSourceAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdGroupAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdGroupAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgDataMtEntry.setStatus("current")
_VRtrPimNgDataMtMdSourceAddrType_Type = InetAddressType
_VRtrPimNgDataMtMdSourceAddrType_Object = MibTableColumn
vRtrPimNgDataMtMdSourceAddrType = _VRtrPimNgDataMtMdSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1, 1),
    _VRtrPimNgDataMtMdSourceAddrType_Type()
)
vRtrPimNgDataMtMdSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtMdSourceAddrType.setStatus("current")


class _VRtrPimNgDataMtMdSourceAddress_Type(InetAddress):
    """Custom type vRtrPimNgDataMtMdSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgDataMtMdSourceAddress_Type.__name__ = "InetAddress"
_VRtrPimNgDataMtMdSourceAddress_Object = MibTableColumn
vRtrPimNgDataMtMdSourceAddress = _VRtrPimNgDataMtMdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1, 2),
    _VRtrPimNgDataMtMdSourceAddress_Type()
)
vRtrPimNgDataMtMdSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtMdSourceAddress.setStatus("current")
_VRtrPimNgDataMtMdGroupAddrType_Type = InetAddressType
_VRtrPimNgDataMtMdGroupAddrType_Object = MibTableColumn
vRtrPimNgDataMtMdGroupAddrType = _VRtrPimNgDataMtMdGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1, 3),
    _VRtrPimNgDataMtMdGroupAddrType_Type()
)
vRtrPimNgDataMtMdGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtMdGroupAddrType.setStatus("current")


class _VRtrPimNgDataMtMdGroupAddress_Type(InetAddress):
    """Custom type vRtrPimNgDataMtMdGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgDataMtMdGroupAddress_Type.__name__ = "InetAddress"
_VRtrPimNgDataMtMdGroupAddress_Object = MibTableColumn
vRtrPimNgDataMtMdGroupAddress = _VRtrPimNgDataMtMdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1, 4),
    _VRtrPimNgDataMtMdGroupAddress_Type()
)
vRtrPimNgDataMtMdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtMdGroupAddress.setStatus("current")
_VRtrPimNgDataMtIfIndex_Type = InterfaceIndex
_VRtrPimNgDataMtIfIndex_Object = MibTableColumn
vRtrPimNgDataMtIfIndex = _VRtrPimNgDataMtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1, 5),
    _VRtrPimNgDataMtIfIndex_Type()
)
vRtrPimNgDataMtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtIfIndex.setStatus("current")
_VRtrPimNgDataMtUptime_Type = Unsigned32
_VRtrPimNgDataMtUptime_Object = MibTableColumn
vRtrPimNgDataMtUptime = _VRtrPimNgDataMtUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1, 6),
    _VRtrPimNgDataMtUptime_Type()
)
vRtrPimNgDataMtUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtUptime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtUptime.setUnits("seconds")
_VRtrPimNgDataMtNumVpnSGs_Type = Unsigned32
_VRtrPimNgDataMtNumVpnSGs_Object = MibTableColumn
vRtrPimNgDataMtNumVpnSGs = _VRtrPimNgDataMtNumVpnSGs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 7, 1, 7),
    _VRtrPimNgDataMtNumVpnSGs_Type()
)
vRtrPimNgDataMtNumVpnSGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtNumVpnSGs.setStatus("current")
_VRtrPimNgDataMtCGrpSrcTable_Object = MibTable
vRtrPimNgDataMtCGrpSrcTable = _VRtrPimNgDataMtCGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8)
)
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcTable.setStatus("current")
_VRtrPimNgDataMtCGrpSrcEntry_Object = MibTableRow
vRtrPimNgDataMtCGrpSrcEntry = _VRtrPimNgDataMtCGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1)
)
vRtrPimNgDataMtCGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdSourceAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdSourceAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdGroupAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtMdGroupAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcGrpAdType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcGroupAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcSrcAdType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcSrcAddr"),
)
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcEntry.setStatus("current")
_VRtrPimNgDataMtCGrpSrcGrpAdType_Type = InetAddressType
_VRtrPimNgDataMtCGrpSrcGrpAdType_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcGrpAdType = _VRtrPimNgDataMtCGrpSrcGrpAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 1),
    _VRtrPimNgDataMtCGrpSrcGrpAdType_Type()
)
vRtrPimNgDataMtCGrpSrcGrpAdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcGrpAdType.setStatus("current")


class _VRtrPimNgDataMtCGrpSrcGroupAddr_Type(InetAddress):
    """Custom type vRtrPimNgDataMtCGrpSrcGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgDataMtCGrpSrcGroupAddr_Type.__name__ = "InetAddress"
_VRtrPimNgDataMtCGrpSrcGroupAddr_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcGroupAddr = _VRtrPimNgDataMtCGrpSrcGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 2),
    _VRtrPimNgDataMtCGrpSrcGroupAddr_Type()
)
vRtrPimNgDataMtCGrpSrcGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcGroupAddr.setStatus("current")
_VRtrPimNgDataMtCGrpSrcSrcAdType_Type = InetAddressType
_VRtrPimNgDataMtCGrpSrcSrcAdType_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcSrcAdType = _VRtrPimNgDataMtCGrpSrcSrcAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 3),
    _VRtrPimNgDataMtCGrpSrcSrcAdType_Type()
)
vRtrPimNgDataMtCGrpSrcSrcAdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcSrcAdType.setStatus("current")


class _VRtrPimNgDataMtCGrpSrcSrcAddr_Type(InetAddress):
    """Custom type vRtrPimNgDataMtCGrpSrcSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgDataMtCGrpSrcSrcAddr_Type.__name__ = "InetAddress"
_VRtrPimNgDataMtCGrpSrcSrcAddr_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcSrcAddr = _VRtrPimNgDataMtCGrpSrcSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 4),
    _VRtrPimNgDataMtCGrpSrcSrcAddr_Type()
)
vRtrPimNgDataMtCGrpSrcSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcSrcAddr.setStatus("current")


class _VRtrPimNgDataMtCGrpSrcState_Type(Integer32):
    """Custom type vRtrPimNgDataMtCGrpSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txJoinPending", 0),
          ("txJoined", 1),
          ("rxNotJoined", 2),
          ("rxJoined", 3))
    )


_VRtrPimNgDataMtCGrpSrcState_Type.__name__ = "Integer32"
_VRtrPimNgDataMtCGrpSrcState_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcState = _VRtrPimNgDataMtCGrpSrcState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 5),
    _VRtrPimNgDataMtCGrpSrcState_Type()
)
vRtrPimNgDataMtCGrpSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcState.setStatus("current")
_VRtrPimNgDataMtCGrpSrcJoinTimer_Type = Unsigned32
_VRtrPimNgDataMtCGrpSrcJoinTimer_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcJoinTimer = _VRtrPimNgDataMtCGrpSrcJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 6),
    _VRtrPimNgDataMtCGrpSrcJoinTimer_Type()
)
vRtrPimNgDataMtCGrpSrcJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcJoinTimer.setUnits("seconds")
_VRtrPimNgDataMtCGrpSrcHolddownTimer_Type = Unsigned32
_VRtrPimNgDataMtCGrpSrcHolddownTimer_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcHolddownTimer = _VRtrPimNgDataMtCGrpSrcHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 7),
    _VRtrPimNgDataMtCGrpSrcHolddownTimer_Type()
)
vRtrPimNgDataMtCGrpSrcHolddownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcHolddownTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcHolddownTimer.setUnits("seconds")
_VRtrPimNgDataMtCGrpSrcExpiryTimer_Type = Unsigned32
_VRtrPimNgDataMtCGrpSrcExpiryTimer_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcExpiryTimer = _VRtrPimNgDataMtCGrpSrcExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 8),
    _VRtrPimNgDataMtCGrpSrcExpiryTimer_Type()
)
vRtrPimNgDataMtCGrpSrcExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcExpiryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcExpiryTimer.setUnits("seconds")
_VRtrPimNgDataMtCGrpSrcUptime_Type = Unsigned32
_VRtrPimNgDataMtCGrpSrcUptime_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcUptime = _VRtrPimNgDataMtCGrpSrcUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 9),
    _VRtrPimNgDataMtCGrpSrcUptime_Type()
)
vRtrPimNgDataMtCGrpSrcUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcUptime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcUptime.setUnits("seconds")
_VRtrPimNgDataMtCGrpSrcDataMtThreshold_Type = Unsigned32
_VRtrPimNgDataMtCGrpSrcDataMtThreshold_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcDataMtThreshold = _VRtrPimNgDataMtCGrpSrcDataMtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 10),
    _VRtrPimNgDataMtCGrpSrcDataMtThreshold_Type()
)
vRtrPimNgDataMtCGrpSrcDataMtThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcDataMtThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcDataMtThreshold.setUnits("kbps")
_VRtrPimNgDataMtCGrpSrcIfIndex_Type = InterfaceIndex
_VRtrPimNgDataMtCGrpSrcIfIndex_Object = MibTableColumn
vRtrPimNgDataMtCGrpSrcIfIndex = _VRtrPimNgDataMtCGrpSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 8, 1, 11),
    _VRtrPimNgDataMtCGrpSrcIfIndex_Type()
)
vRtrPimNgDataMtCGrpSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgDataMtCGrpSrcIfIndex.setStatus("current")
_VRtrPimNgIfSecNbrTblLstChanged_Type = TimeStamp
_VRtrPimNgIfSecNbrTblLstChanged_Object = MibScalar
vRtrPimNgIfSecNbrTblLstChanged = _VRtrPimNgIfSecNbrTblLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 9),
    _VRtrPimNgIfSecNbrTblLstChanged_Type()
)
vRtrPimNgIfSecNbrTblLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfSecNbrTblLstChanged.setStatus("current")
_VRtrPimNgIfSecNbrTable_Object = MibTable
vRtrPimNgIfSecNbrTable = _VRtrPimNgIfSecNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 10)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfSecNbrTable.setStatus("current")
_VRtrPimNgIfSecNbrEntry_Object = MibTableRow
vRtrPimNgIfSecNbrEntry = _VRtrPimNgIfSecNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 10, 1)
)
vRtrPimNgIfSecNbrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborAddressType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfSecNbrAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfSecNbrAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgIfSecNbrEntry.setStatus("current")
_VRtrPimNgIfSecNbrAddrType_Type = InetAddressType
_VRtrPimNgIfSecNbrAddrType_Object = MibTableColumn
vRtrPimNgIfSecNbrAddrType = _VRtrPimNgIfSecNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 10, 1, 1),
    _VRtrPimNgIfSecNbrAddrType_Type()
)
vRtrPimNgIfSecNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfSecNbrAddrType.setStatus("current")


class _VRtrPimNgIfSecNbrAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfSecNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfSecNbrAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfSecNbrAddress_Object = MibTableColumn
vRtrPimNgIfSecNbrAddress = _VRtrPimNgIfSecNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 10, 1, 2),
    _VRtrPimNgIfSecNbrAddress_Type()
)
vRtrPimNgIfSecNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfSecNbrAddress.setStatus("current")
_VRtrPimNgRsvpPmsiTable_Object = MibTable
vRtrPimNgRsvpPmsiTable = _VRtrPimNgRsvpPmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11)
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiTable.setStatus("current")
_VRtrPimNgRsvpPmsiEntry_Object = MibTableRow
vRtrPimNgRsvpPmsiEntry = _VRtrPimNgRsvpPmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1)
)
vRtrPimNgRsvpPmsiEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiExtTunlAdrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiExtTunnelAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiTunnelId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiP2MPId"),
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiEntry.setStatus("current")
_VRtrPimNgRsvpPmsiExtTunlAdrType_Type = InetAddressType
_VRtrPimNgRsvpPmsiExtTunlAdrType_Object = MibTableColumn
vRtrPimNgRsvpPmsiExtTunlAdrType = _VRtrPimNgRsvpPmsiExtTunlAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 1),
    _VRtrPimNgRsvpPmsiExtTunlAdrType_Type()
)
vRtrPimNgRsvpPmsiExtTunlAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiExtTunlAdrType.setStatus("current")


class _VRtrPimNgRsvpPmsiExtTunnelAddr_Type(InetAddress):
    """Custom type vRtrPimNgRsvpPmsiExtTunnelAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgRsvpPmsiExtTunnelAddr_Type.__name__ = "InetAddress"
_VRtrPimNgRsvpPmsiExtTunnelAddr_Object = MibTableColumn
vRtrPimNgRsvpPmsiExtTunnelAddr = _VRtrPimNgRsvpPmsiExtTunnelAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 2),
    _VRtrPimNgRsvpPmsiExtTunnelAddr_Type()
)
vRtrPimNgRsvpPmsiExtTunnelAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiExtTunnelAddr.setStatus("current")
_VRtrPimNgRsvpPmsiTunnelId_Type = Unsigned32
_VRtrPimNgRsvpPmsiTunnelId_Object = MibTableColumn
vRtrPimNgRsvpPmsiTunnelId = _VRtrPimNgRsvpPmsiTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 3),
    _VRtrPimNgRsvpPmsiTunnelId_Type()
)
vRtrPimNgRsvpPmsiTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiTunnelId.setStatus("current")
_VRtrPimNgRsvpPmsiP2MPId_Type = Unsigned32
_VRtrPimNgRsvpPmsiP2MPId_Object = MibTableColumn
vRtrPimNgRsvpPmsiP2MPId = _VRtrPimNgRsvpPmsiP2MPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 4),
    _VRtrPimNgRsvpPmsiP2MPId_Type()
)
vRtrPimNgRsvpPmsiP2MPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiP2MPId.setStatus("current")
_VRtrPimNgRsvpPmsiIfIndex_Type = InterfaceIndex
_VRtrPimNgRsvpPmsiIfIndex_Object = MibTableColumn
vRtrPimNgRsvpPmsiIfIndex = _VRtrPimNgRsvpPmsiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 5),
    _VRtrPimNgRsvpPmsiIfIndex_Type()
)
vRtrPimNgRsvpPmsiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiIfIndex.setStatus("current")
_VRtrPimNgRsvpPmsiUptime_Type = Unsigned32
_VRtrPimNgRsvpPmsiUptime_Object = MibTableColumn
vRtrPimNgRsvpPmsiUptime = _VRtrPimNgRsvpPmsiUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 6),
    _VRtrPimNgRsvpPmsiUptime_Type()
)
vRtrPimNgRsvpPmsiUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiUptime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiUptime.setUnits("seconds")
_VRtrPimNgRsvpPmsiNumVpnSGs_Type = Unsigned32
_VRtrPimNgRsvpPmsiNumVpnSGs_Object = MibTableColumn
vRtrPimNgRsvpPmsiNumVpnSGs = _VRtrPimNgRsvpPmsiNumVpnSGs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 7),
    _VRtrPimNgRsvpPmsiNumVpnSGs_Type()
)
vRtrPimNgRsvpPmsiNumVpnSGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiNumVpnSGs.setStatus("current")


class _VRtrPimNgRsvpPmsiIfType_Type(Integer32):
    """Custom type vRtrPimNgRsvpPmsiIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rx", 0),
          ("tx", 1))
    )


_VRtrPimNgRsvpPmsiIfType_Type.__name__ = "Integer32"
_VRtrPimNgRsvpPmsiIfType_Object = MibTableColumn
vRtrPimNgRsvpPmsiIfType = _VRtrPimNgRsvpPmsiIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 11, 1, 8),
    _VRtrPimNgRsvpPmsiIfType_Type()
)
vRtrPimNgRsvpPmsiIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiIfType.setStatus("current")
_VRtrPimNgRsvpPmsiCGrpSrcTable_Object = MibTable
vRtrPimNgRsvpPmsiCGrpSrcTable = _VRtrPimNgRsvpPmsiCGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12)
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiCGrpSrcTable.setStatus("current")
_VRtrPimNgRsvpPmsiCGrpSrcEntry_Object = MibTableRow
vRtrPimNgRsvpPmsiCGrpSrcEntry = _VRtrPimNgRsvpPmsiCGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1)
)
vRtrPimNgRsvpPmsiCGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiExtTunlAdrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiExtTunnelAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiTunnelId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiP2MPId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcGrpAdType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcSrcAdType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcSrcAddr"),
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpPmsiCGrpSrcEntry.setStatus("current")
_VRtrPimRsvpPmsiCGrpSrcGrpAdType_Type = InetAddressType
_VRtrPimRsvpPmsiCGrpSrcGrpAdType_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcGrpAdType = _VRtrPimRsvpPmsiCGrpSrcGrpAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 1),
    _VRtrPimRsvpPmsiCGrpSrcGrpAdType_Type()
)
vRtrPimRsvpPmsiCGrpSrcGrpAdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcGrpAdType.setStatus("current")


class _VRtrPimRsvpPmsiCGrpSrcGrpAddr_Type(InetAddress):
    """Custom type vRtrPimRsvpPmsiCGrpSrcGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimRsvpPmsiCGrpSrcGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimRsvpPmsiCGrpSrcGrpAddr_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcGrpAddr = _VRtrPimRsvpPmsiCGrpSrcGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 2),
    _VRtrPimRsvpPmsiCGrpSrcGrpAddr_Type()
)
vRtrPimRsvpPmsiCGrpSrcGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcGrpAddr.setStatus("current")
_VRtrPimRsvpPmsiCGrpSrcSrcAdType_Type = InetAddressType
_VRtrPimRsvpPmsiCGrpSrcSrcAdType_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcSrcAdType = _VRtrPimRsvpPmsiCGrpSrcSrcAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 3),
    _VRtrPimRsvpPmsiCGrpSrcSrcAdType_Type()
)
vRtrPimRsvpPmsiCGrpSrcSrcAdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcSrcAdType.setStatus("current")


class _VRtrPimRsvpPmsiCGrpSrcSrcAddr_Type(InetAddress):
    """Custom type vRtrPimRsvpPmsiCGrpSrcSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimRsvpPmsiCGrpSrcSrcAddr_Type.__name__ = "InetAddress"
_VRtrPimRsvpPmsiCGrpSrcSrcAddr_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcSrcAddr = _VRtrPimRsvpPmsiCGrpSrcSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 4),
    _VRtrPimRsvpPmsiCGrpSrcSrcAddr_Type()
)
vRtrPimRsvpPmsiCGrpSrcSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcSrcAddr.setStatus("current")


class _VRtrPimRsvpPmsiCGrpSrcState_Type(Integer32):
    """Custom type vRtrPimRsvpPmsiCGrpSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txJoinPending", 0),
          ("txJoined", 1),
          ("rxNotJoined", 2),
          ("rxJoined", 3))
    )


_VRtrPimRsvpPmsiCGrpSrcState_Type.__name__ = "Integer32"
_VRtrPimRsvpPmsiCGrpSrcState_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcState = _VRtrPimRsvpPmsiCGrpSrcState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 5),
    _VRtrPimRsvpPmsiCGrpSrcState_Type()
)
vRtrPimRsvpPmsiCGrpSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcState.setStatus("current")
_VRtrPimRsvpPmsiCGrpSrcJoinTimer_Type = Unsigned32
_VRtrPimRsvpPmsiCGrpSrcJoinTimer_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcJoinTimer = _VRtrPimRsvpPmsiCGrpSrcJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 6),
    _VRtrPimRsvpPmsiCGrpSrcJoinTimer_Type()
)
vRtrPimRsvpPmsiCGrpSrcJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcJoinTimer.setUnits("seconds")
_VRtrPimRsvpPmsiCGrpSrcHldDnTimer_Type = Unsigned32
_VRtrPimRsvpPmsiCGrpSrcHldDnTimer_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcHldDnTimer = _VRtrPimRsvpPmsiCGrpSrcHldDnTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 7),
    _VRtrPimRsvpPmsiCGrpSrcHldDnTimer_Type()
)
vRtrPimRsvpPmsiCGrpSrcHldDnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcHldDnTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcHldDnTimer.setUnits("seconds")
_VRtrPimRsvpPmsiCGrpSrcExpTimer_Type = Unsigned32
_VRtrPimRsvpPmsiCGrpSrcExpTimer_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcExpTimer = _VRtrPimRsvpPmsiCGrpSrcExpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 8),
    _VRtrPimRsvpPmsiCGrpSrcExpTimer_Type()
)
vRtrPimRsvpPmsiCGrpSrcExpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcExpTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcExpTimer.setUnits("seconds")
_VRtrPimRsvpPmsiCGrpSrcUptime_Type = Unsigned32
_VRtrPimRsvpPmsiCGrpSrcUptime_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcUptime = _VRtrPimRsvpPmsiCGrpSrcUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 9),
    _VRtrPimRsvpPmsiCGrpSrcUptime_Type()
)
vRtrPimRsvpPmsiCGrpSrcUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcUptime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcUptime.setUnits("seconds")
_VRtrPimDataMtCGrpSrcDataThresh_Type = Unsigned32
_VRtrPimDataMtCGrpSrcDataThresh_Object = MibTableColumn
vRtrPimDataMtCGrpSrcDataThresh = _VRtrPimDataMtCGrpSrcDataThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 10),
    _VRtrPimDataMtCGrpSrcDataThresh_Type()
)
vRtrPimDataMtCGrpSrcDataThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimDataMtCGrpSrcDataThresh.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimDataMtCGrpSrcDataThresh.setUnits("kbps")
_VRtrPimRsvpPmsiCGrpSrcIfIndex_Type = InterfaceIndex
_VRtrPimRsvpPmsiCGrpSrcIfIndex_Object = MibTableColumn
vRtrPimRsvpPmsiCGrpSrcIfIndex = _VRtrPimRsvpPmsiCGrpSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 12, 1, 11),
    _VRtrPimRsvpPmsiCGrpSrcIfIndex_Type()
)
vRtrPimRsvpPmsiCGrpSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRsvpPmsiCGrpSrcIfIndex.setStatus("current")
_VRtrPimNgLdpPmsiTable_Object = MibTable
vRtrPimNgLdpPmsiTable = _VRtrPimNgLdpPmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13)
)
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiTable.setStatus("current")
_VRtrPimNgLdpPmsiEntry_Object = MibTableRow
vRtrPimNgLdpPmsiEntry = _VRtrPimNgLdpPmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1)
)
vRtrPimNgLdpPmsiEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiRootAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiRootAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiLspId"),
)
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiEntry.setStatus("current")
_VRtrPimNgLdpPmsiRootAddrType_Type = InetAddressType
_VRtrPimNgLdpPmsiRootAddrType_Object = MibTableColumn
vRtrPimNgLdpPmsiRootAddrType = _VRtrPimNgLdpPmsiRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1, 1),
    _VRtrPimNgLdpPmsiRootAddrType_Type()
)
vRtrPimNgLdpPmsiRootAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiRootAddrType.setStatus("current")


class _VRtrPimNgLdpPmsiRootAddr_Type(InetAddress):
    """Custom type vRtrPimNgLdpPmsiRootAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgLdpPmsiRootAddr_Type.__name__ = "InetAddress"
_VRtrPimNgLdpPmsiRootAddr_Object = MibTableColumn
vRtrPimNgLdpPmsiRootAddr = _VRtrPimNgLdpPmsiRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1, 2),
    _VRtrPimNgLdpPmsiRootAddr_Type()
)
vRtrPimNgLdpPmsiRootAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiRootAddr.setStatus("current")
_VRtrPimNgLdpPmsiLspId_Type = Unsigned32
_VRtrPimNgLdpPmsiLspId_Object = MibTableColumn
vRtrPimNgLdpPmsiLspId = _VRtrPimNgLdpPmsiLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1, 3),
    _VRtrPimNgLdpPmsiLspId_Type()
)
vRtrPimNgLdpPmsiLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiLspId.setStatus("current")
_VRtrPimNgLdpPmsiIfIndex_Type = InterfaceIndex
_VRtrPimNgLdpPmsiIfIndex_Object = MibTableColumn
vRtrPimNgLdpPmsiIfIndex = _VRtrPimNgLdpPmsiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1, 4),
    _VRtrPimNgLdpPmsiIfIndex_Type()
)
vRtrPimNgLdpPmsiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiIfIndex.setStatus("current")
_VRtrPimNgLdpPmsiUptime_Type = Unsigned32
_VRtrPimNgLdpPmsiUptime_Object = MibTableColumn
vRtrPimNgLdpPmsiUptime = _VRtrPimNgLdpPmsiUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1, 5),
    _VRtrPimNgLdpPmsiUptime_Type()
)
vRtrPimNgLdpPmsiUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiUptime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiUptime.setUnits("seconds")
_VRtrPimNgLdpPmsiNumVpnSGs_Type = Unsigned32
_VRtrPimNgLdpPmsiNumVpnSGs_Object = MibTableColumn
vRtrPimNgLdpPmsiNumVpnSGs = _VRtrPimNgLdpPmsiNumVpnSGs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1, 6),
    _VRtrPimNgLdpPmsiNumVpnSGs_Type()
)
vRtrPimNgLdpPmsiNumVpnSGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiNumVpnSGs.setStatus("current")


class _VRtrPimNgLdpPmsiIfType_Type(Integer32):
    """Custom type vRtrPimNgLdpPmsiIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rx", 0),
          ("tx", 1))
    )


_VRtrPimNgLdpPmsiIfType_Type.__name__ = "Integer32"
_VRtrPimNgLdpPmsiIfType_Object = MibTableColumn
vRtrPimNgLdpPmsiIfType = _VRtrPimNgLdpPmsiIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 13, 1, 7),
    _VRtrPimNgLdpPmsiIfType_Type()
)
vRtrPimNgLdpPmsiIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiIfType.setStatus("current")
_VRtrPimNgLdpPmsiCGrpSrcTable_Object = MibTable
vRtrPimNgLdpPmsiCGrpSrcTable = _VRtrPimNgLdpPmsiCGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14)
)
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiCGrpSrcTable.setStatus("current")
_VRtrPimNgLdpPmsiCGrpSrcEntry_Object = MibTableRow
vRtrPimNgLdpPmsiCGrpSrcEntry = _VRtrPimNgLdpPmsiCGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1)
)
vRtrPimNgLdpPmsiCGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiRootAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiRootAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiLspId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcGrpAdType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcGrpAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcSrcAdType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcSrcAddr"),
)
if mibBuilder.loadTexts:
    vRtrPimNgLdpPmsiCGrpSrcEntry.setStatus("current")
_VRtrPimLdpPmsiCGrpSrcGrpAdType_Type = InetAddressType
_VRtrPimLdpPmsiCGrpSrcGrpAdType_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcGrpAdType = _VRtrPimLdpPmsiCGrpSrcGrpAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 1),
    _VRtrPimLdpPmsiCGrpSrcGrpAdType_Type()
)
vRtrPimLdpPmsiCGrpSrcGrpAdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcGrpAdType.setStatus("current")


class _VRtrPimLdpPmsiCGrpSrcGrpAddr_Type(InetAddress):
    """Custom type vRtrPimLdpPmsiCGrpSrcGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimLdpPmsiCGrpSrcGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimLdpPmsiCGrpSrcGrpAddr_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcGrpAddr = _VRtrPimLdpPmsiCGrpSrcGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 2),
    _VRtrPimLdpPmsiCGrpSrcGrpAddr_Type()
)
vRtrPimLdpPmsiCGrpSrcGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcGrpAddr.setStatus("current")
_VRtrPimLdpPmsiCGrpSrcSrcAdType_Type = InetAddressType
_VRtrPimLdpPmsiCGrpSrcSrcAdType_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcSrcAdType = _VRtrPimLdpPmsiCGrpSrcSrcAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 3),
    _VRtrPimLdpPmsiCGrpSrcSrcAdType_Type()
)
vRtrPimLdpPmsiCGrpSrcSrcAdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcSrcAdType.setStatus("current")


class _VRtrPimLdpPmsiCGrpSrcSrcAddr_Type(InetAddress):
    """Custom type vRtrPimLdpPmsiCGrpSrcSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimLdpPmsiCGrpSrcSrcAddr_Type.__name__ = "InetAddress"
_VRtrPimLdpPmsiCGrpSrcSrcAddr_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcSrcAddr = _VRtrPimLdpPmsiCGrpSrcSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 4),
    _VRtrPimLdpPmsiCGrpSrcSrcAddr_Type()
)
vRtrPimLdpPmsiCGrpSrcSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcSrcAddr.setStatus("current")


class _VRtrPimLdpPmsiCGrpSrcState_Type(Integer32):
    """Custom type vRtrPimLdpPmsiCGrpSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txJoinPending", 0),
          ("txJoined", 1),
          ("rxNotJoined", 2),
          ("rxJoined", 3))
    )


_VRtrPimLdpPmsiCGrpSrcState_Type.__name__ = "Integer32"
_VRtrPimLdpPmsiCGrpSrcState_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcState = _VRtrPimLdpPmsiCGrpSrcState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 5),
    _VRtrPimLdpPmsiCGrpSrcState_Type()
)
vRtrPimLdpPmsiCGrpSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcState.setStatus("current")
_VRtrPimLdpPmsiCGrpSrcJoinTimer_Type = Unsigned32
_VRtrPimLdpPmsiCGrpSrcJoinTimer_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcJoinTimer = _VRtrPimLdpPmsiCGrpSrcJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 6),
    _VRtrPimLdpPmsiCGrpSrcJoinTimer_Type()
)
vRtrPimLdpPmsiCGrpSrcJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcJoinTimer.setUnits("seconds")
_VRtrPimLdpPmsiCGrpSrcHldDnTimer_Type = Unsigned32
_VRtrPimLdpPmsiCGrpSrcHldDnTimer_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcHldDnTimer = _VRtrPimLdpPmsiCGrpSrcHldDnTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 7),
    _VRtrPimLdpPmsiCGrpSrcHldDnTimer_Type()
)
vRtrPimLdpPmsiCGrpSrcHldDnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcHldDnTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcHldDnTimer.setUnits("seconds")
_VRtrPimLdpPmsiCGrpSrcExpTimer_Type = Unsigned32
_VRtrPimLdpPmsiCGrpSrcExpTimer_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcExpTimer = _VRtrPimLdpPmsiCGrpSrcExpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 8),
    _VRtrPimLdpPmsiCGrpSrcExpTimer_Type()
)
vRtrPimLdpPmsiCGrpSrcExpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcExpTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcExpTimer.setUnits("seconds")
_VRtrPimLdpPmsiCGrpSrcUptime_Type = Unsigned32
_VRtrPimLdpPmsiCGrpSrcUptime_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcUptime = _VRtrPimLdpPmsiCGrpSrcUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 9),
    _VRtrPimLdpPmsiCGrpSrcUptime_Type()
)
vRtrPimLdpPmsiCGrpSrcUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcUptime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcUptime.setUnits("seconds")
_VRtrPimLdpDataMtCGrpSrcDataThres_Type = Unsigned32
_VRtrPimLdpDataMtCGrpSrcDataThres_Object = MibTableColumn
vRtrPimLdpDataMtCGrpSrcDataThres = _VRtrPimLdpDataMtCGrpSrcDataThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 10),
    _VRtrPimLdpDataMtCGrpSrcDataThres_Type()
)
vRtrPimLdpDataMtCGrpSrcDataThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimLdpDataMtCGrpSrcDataThres.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimLdpDataMtCGrpSrcDataThres.setUnits("kbps")
_VRtrPimLdpPmsiCGrpSrcIfIndex_Type = InterfaceIndex
_VRtrPimLdpPmsiCGrpSrcIfIndex_Object = MibTableColumn
vRtrPimLdpPmsiCGrpSrcIfIndex = _VRtrPimLdpPmsiCGrpSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 14, 1, 11),
    _VRtrPimLdpPmsiCGrpSrcIfIndex_Type()
)
vRtrPimLdpPmsiCGrpSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimLdpPmsiCGrpSrcIfIndex.setStatus("current")
_VRtrPimNgRsvpIPmsiTable_Object = MibTable
vRtrPimNgRsvpIPmsiTable = _VRtrPimNgRsvpIPmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 15)
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIPmsiTable.setStatus("current")
_VRtrPimNgRsvpIPmsiEntry_Object = MibTableRow
vRtrPimNgRsvpIPmsiEntry = _VRtrPimNgRsvpIPmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 15, 1)
)
vRtrPimNgRsvpIPmsiEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIPmsiEntry.setStatus("current")
_VRtrPimNgRsvpIPmsiExtTunlAdrType_Type = InetAddressType
_VRtrPimNgRsvpIPmsiExtTunlAdrType_Object = MibTableColumn
vRtrPimNgRsvpIPmsiExtTunlAdrType = _VRtrPimNgRsvpIPmsiExtTunlAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 15, 1, 1),
    _VRtrPimNgRsvpIPmsiExtTunlAdrType_Type()
)
vRtrPimNgRsvpIPmsiExtTunlAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIPmsiExtTunlAdrType.setStatus("current")


class _VRtrPimNgRsvpIPmsiExtTunnelAddr_Type(InetAddress):
    """Custom type vRtrPimNgRsvpIPmsiExtTunnelAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgRsvpIPmsiExtTunnelAddr_Type.__name__ = "InetAddress"
_VRtrPimNgRsvpIPmsiExtTunnelAddr_Object = MibTableColumn
vRtrPimNgRsvpIPmsiExtTunnelAddr = _VRtrPimNgRsvpIPmsiExtTunnelAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 15, 1, 2),
    _VRtrPimNgRsvpIPmsiExtTunnelAddr_Type()
)
vRtrPimNgRsvpIPmsiExtTunnelAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIPmsiExtTunnelAddr.setStatus("current")
_VRtrPimNgRsvpIPmsiLspName_Type = TNamedItem
_VRtrPimNgRsvpIPmsiLspName_Object = MibTableColumn
vRtrPimNgRsvpIPmsiLspName = _VRtrPimNgRsvpIPmsiLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 15, 1, 3),
    _VRtrPimNgRsvpIPmsiLspName_Type()
)
vRtrPimNgRsvpIPmsiLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIPmsiLspName.setStatus("current")
_VRtrPimNgRsvpIPmsiP2MPId_Type = Unsigned32
_VRtrPimNgRsvpIPmsiP2MPId_Object = MibTableColumn
vRtrPimNgRsvpIPmsiP2MPId = _VRtrPimNgRsvpIPmsiP2MPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 15, 1, 4),
    _VRtrPimNgRsvpIPmsiP2MPId_Type()
)
vRtrPimNgRsvpIPmsiP2MPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIPmsiP2MPId.setStatus("current")
_VRtrPimNgRsvpIPmsiTunnelId_Type = Unsigned32
_VRtrPimNgRsvpIPmsiTunnelId_Object = MibTableColumn
vRtrPimNgRsvpIPmsiTunnelId = _VRtrPimNgRsvpIPmsiTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 15, 1, 5),
    _VRtrPimNgRsvpIPmsiTunnelId_Type()
)
vRtrPimNgRsvpIPmsiTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgRsvpIPmsiTunnelId.setStatus("current")
_VRtrPimNgLdpIPmsiTable_Object = MibTable
vRtrPimNgLdpIPmsiTable = _VRtrPimNgLdpIPmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 16)
)
if mibBuilder.loadTexts:
    vRtrPimNgLdpIPmsiTable.setStatus("current")
_VRtrPimNgLdpIPmsiEntry_Object = MibTableRow
vRtrPimNgLdpIPmsiEntry = _VRtrPimNgLdpIPmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 16, 1)
)
vRtrPimNgLdpIPmsiEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrPimNgLdpIPmsiEntry.setStatus("current")
_VRtrPimNgLdpIPmsiRootAddrType_Type = InetAddressType
_VRtrPimNgLdpIPmsiRootAddrType_Object = MibTableColumn
vRtrPimNgLdpIPmsiRootAddrType = _VRtrPimNgLdpIPmsiRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 16, 1, 1),
    _VRtrPimNgLdpIPmsiRootAddrType_Type()
)
vRtrPimNgLdpIPmsiRootAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpIPmsiRootAddrType.setStatus("current")


class _VRtrPimNgLdpIPmsiRootAddr_Type(InetAddress):
    """Custom type vRtrPimNgLdpIPmsiRootAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgLdpIPmsiRootAddr_Type.__name__ = "InetAddress"
_VRtrPimNgLdpIPmsiRootAddr_Object = MibTableColumn
vRtrPimNgLdpIPmsiRootAddr = _VRtrPimNgLdpIPmsiRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 16, 1, 2),
    _VRtrPimNgLdpIPmsiRootAddr_Type()
)
vRtrPimNgLdpIPmsiRootAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpIPmsiRootAddr.setStatus("current")
_VRtrPimNgLdpIPmsiLspId_Type = Unsigned32
_VRtrPimNgLdpIPmsiLspId_Object = MibTableColumn
vRtrPimNgLdpIPmsiLspId = _VRtrPimNgLdpIPmsiLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 16, 1, 3),
    _VRtrPimNgLdpIPmsiLspId_Type()
)
vRtrPimNgLdpIPmsiLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpIPmsiLspId.setStatus("current")
_VRtrPimNgLdpIPmsiLspName_Type = TNamedItem
_VRtrPimNgLdpIPmsiLspName_Object = MibTableColumn
vRtrPimNgLdpIPmsiLspName = _VRtrPimNgLdpIPmsiLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 16, 1, 4),
    _VRtrPimNgLdpIPmsiLspName_Type()
)
vRtrPimNgLdpIPmsiLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgLdpIPmsiLspName.setStatus("current")
_VRtrPimNgMvpnExtranetTable_Object = MibTable
vRtrPimNgMvpnExtranetTable = _VRtrPimNgMvpnExtranetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17)
)
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetTable.setStatus("current")
_VRtrPimNgMvpnExtranetEntry_Object = MibTableRow
vRtrPimNgMvpnExtranetEntry = _VRtrPimNgMvpnExtranetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17, 1)
)
vRtrPimNgMvpnExtranetEntry.setIndexNames(
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnExtranetNHAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnExtranetNHAddr"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnExtranetRD"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnExtranetSrcMvpn"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnExtranetRecvMvpn"),
)
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetEntry.setStatus("current")
_VRtrPimNgMvpnExtranetNHAddrType_Type = InetAddressType
_VRtrPimNgMvpnExtranetNHAddrType_Object = MibTableColumn
vRtrPimNgMvpnExtranetNHAddrType = _VRtrPimNgMvpnExtranetNHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17, 1, 1),
    _VRtrPimNgMvpnExtranetNHAddrType_Type()
)
vRtrPimNgMvpnExtranetNHAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetNHAddrType.setStatus("current")


class _VRtrPimNgMvpnExtranetNHAddr_Type(InetAddress):
    """Custom type vRtrPimNgMvpnExtranetNHAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgMvpnExtranetNHAddr_Type.__name__ = "InetAddress"
_VRtrPimNgMvpnExtranetNHAddr_Object = MibTableColumn
vRtrPimNgMvpnExtranetNHAddr = _VRtrPimNgMvpnExtranetNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17, 1, 2),
    _VRtrPimNgMvpnExtranetNHAddr_Type()
)
vRtrPimNgMvpnExtranetNHAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetNHAddr.setStatus("current")
_VRtrPimNgMvpnExtranetRD_Type = TmnxVPNRouteDistinguisher
_VRtrPimNgMvpnExtranetRD_Object = MibTableColumn
vRtrPimNgMvpnExtranetRD = _VRtrPimNgMvpnExtranetRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17, 1, 3),
    _VRtrPimNgMvpnExtranetRD_Type()
)
vRtrPimNgMvpnExtranetRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetRD.setStatus("current")
_VRtrPimNgMvpnExtranetSrcMvpn_Type = Unsigned32
_VRtrPimNgMvpnExtranetSrcMvpn_Object = MibTableColumn
vRtrPimNgMvpnExtranetSrcMvpn = _VRtrPimNgMvpnExtranetSrcMvpn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17, 1, 4),
    _VRtrPimNgMvpnExtranetSrcMvpn_Type()
)
vRtrPimNgMvpnExtranetSrcMvpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetSrcMvpn.setStatus("current")
_VRtrPimNgMvpnExtranetRecvMvpn_Type = Unsigned32
_VRtrPimNgMvpnExtranetRecvMvpn_Object = MibTableColumn
vRtrPimNgMvpnExtranetRecvMvpn = _VRtrPimNgMvpnExtranetRecvMvpn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17, 1, 5),
    _VRtrPimNgMvpnExtranetRecvMvpn_Type()
)
vRtrPimNgMvpnExtranetRecvMvpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetRecvMvpn.setStatus("current")
_VRtrPimNgMvpnExtranetRecvRefCnt_Type = Unsigned32
_VRtrPimNgMvpnExtranetRecvRefCnt_Object = MibTableColumn
vRtrPimNgMvpnExtranetRecvRefCnt = _VRtrPimNgMvpnExtranetRecvRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 17, 1, 6),
    _VRtrPimNgMvpnExtranetRecvRefCnt_Type()
)
vRtrPimNgMvpnExtranetRecvRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgMvpnExtranetRecvRefCnt.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvTable_Object = MibTable
vRtrPimNgIfGrpSrcRpfvTable = _VRtrPimNgIfGrpSrcRpfvTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18)
)
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvTable.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvEntry_Object = MibTableRow
vRtrPimNgIfGrpSrcRpfvEntry = _VRtrPimNgIfGrpSrcRpfvEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1)
)
vRtrPimNgIfGrpSrcRpfvEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvSGType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvGrpAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvGrpAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvSrcAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvSrcAddress"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvNbrAddrType"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvNbrAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvEntry.setStatus("current")


class _VRtrPimNgIfGrpSrcRpfvSGType_Type(Integer32):
    """Custom type vRtrPimNgIfGrpSrcRpfvSGType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starStarRP", 0),
          ("starG", 1),
          ("sg", 2))
    )


_VRtrPimNgIfGrpSrcRpfvSGType_Type.__name__ = "Integer32"
_VRtrPimNgIfGrpSrcRpfvSGType_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvSGType = _VRtrPimNgIfGrpSrcRpfvSGType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 1),
    _VRtrPimNgIfGrpSrcRpfvSGType_Type()
)
vRtrPimNgIfGrpSrcRpfvSGType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvSGType.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvGrpAddrType_Type = InetAddressType
_VRtrPimNgIfGrpSrcRpfvGrpAddrType_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvGrpAddrType = _VRtrPimNgIfGrpSrcRpfvGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 2),
    _VRtrPimNgIfGrpSrcRpfvGrpAddrType_Type()
)
vRtrPimNgIfGrpSrcRpfvGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvGrpAddrType.setStatus("current")


class _VRtrPimNgIfGrpSrcRpfvGrpAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcRpfvGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcRpfvGrpAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcRpfvGrpAddress_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvGrpAddress = _VRtrPimNgIfGrpSrcRpfvGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 3),
    _VRtrPimNgIfGrpSrcRpfvGrpAddress_Type()
)
vRtrPimNgIfGrpSrcRpfvGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvGrpAddress.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvSrcAddrType_Type = InetAddressType
_VRtrPimNgIfGrpSrcRpfvSrcAddrType_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvSrcAddrType = _VRtrPimNgIfGrpSrcRpfvSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 4),
    _VRtrPimNgIfGrpSrcRpfvSrcAddrType_Type()
)
vRtrPimNgIfGrpSrcRpfvSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvSrcAddrType.setStatus("current")


class _VRtrPimNgIfGrpSrcRpfvSrcAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcRpfvSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcRpfvSrcAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcRpfvSrcAddress_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvSrcAddress = _VRtrPimNgIfGrpSrcRpfvSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 5),
    _VRtrPimNgIfGrpSrcRpfvSrcAddress_Type()
)
vRtrPimNgIfGrpSrcRpfvSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvSrcAddress.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvNbrAddrType_Type = InetAddressType
_VRtrPimNgIfGrpSrcRpfvNbrAddrType_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvNbrAddrType = _VRtrPimNgIfGrpSrcRpfvNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 6),
    _VRtrPimNgIfGrpSrcRpfvNbrAddrType_Type()
)
vRtrPimNgIfGrpSrcRpfvNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvNbrAddrType.setStatus("current")


class _VRtrPimNgIfGrpSrcRpfvNbrAddress_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcRpfvNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcRpfvNbrAddress_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcRpfvNbrAddress_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvNbrAddress = _VRtrPimNgIfGrpSrcRpfvNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 7),
    _VRtrPimNgIfGrpSrcRpfvNbrAddress_Type()
)
vRtrPimNgIfGrpSrcRpfvNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvNbrAddress.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvPrxyAddrTyp_Type = InetAddressType
_VRtrPimNgIfGrpSrcRpfvPrxyAddrTyp_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvPrxyAddrTyp = _VRtrPimNgIfGrpSrcRpfvPrxyAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 8),
    _VRtrPimNgIfGrpSrcRpfvPrxyAddrTyp_Type()
)
vRtrPimNgIfGrpSrcRpfvPrxyAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvPrxyAddrTyp.setStatus("current")


class _VRtrPimNgIfGrpSrcRpfvProxyAddr_Type(InetAddress):
    """Custom type vRtrPimNgIfGrpSrcRpfvProxyAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgIfGrpSrcRpfvProxyAddr_Type.__name__ = "InetAddress"
_VRtrPimNgIfGrpSrcRpfvProxyAddr_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvProxyAddr = _VRtrPimNgIfGrpSrcRpfvProxyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 9),
    _VRtrPimNgIfGrpSrcRpfvProxyAddr_Type()
)
vRtrPimNgIfGrpSrcRpfvProxyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvProxyAddr.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvRD_Type = TmnxVPNRouteDistinguisher
_VRtrPimNgIfGrpSrcRpfvRD_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvRD = _VRtrPimNgIfGrpSrcRpfvRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 10),
    _VRtrPimNgIfGrpSrcRpfvRD_Type()
)
vRtrPimNgIfGrpSrcRpfvRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvRD.setStatus("current")


class _VRtrPimNgIfGrpSrcRpfvType_Type(Integer32):
    """Custom type vRtrPimNgIfGrpSrcRpfvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mvpn", 1),
          ("core", 2))
    )


_VRtrPimNgIfGrpSrcRpfvType_Type.__name__ = "Integer32"
_VRtrPimNgIfGrpSrcRpfvType_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvType = _VRtrPimNgIfGrpSrcRpfvType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 11),
    _VRtrPimNgIfGrpSrcRpfvType_Type()
)
vRtrPimNgIfGrpSrcRpfvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvType.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvIfWinner_Type = TruthValue
_VRtrPimNgIfGrpSrcRpfvIfWinner_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvIfWinner = _VRtrPimNgIfGrpSrcRpfvIfWinner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 12),
    _VRtrPimNgIfGrpSrcRpfvIfWinner_Type()
)
vRtrPimNgIfGrpSrcRpfvIfWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvIfWinner.setStatus("current")
_VRtrPimNgIfGrpSrcRpfvNbrWinner_Type = TruthValue
_VRtrPimNgIfGrpSrcRpfvNbrWinner_Object = MibTableColumn
vRtrPimNgIfGrpSrcRpfvNbrWinner = _VRtrPimNgIfGrpSrcRpfvNbrWinner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 2, 18, 1, 13),
    _VRtrPimNgIfGrpSrcRpfvNbrWinner_Type()
)
vRtrPimNgIfGrpSrcRpfvNbrWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimNgIfGrpSrcRpfvNbrWinner.setStatus("current")
_VRtrPimNgNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrPimNgNotificationObjs = _VRtrPimNgNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3)
)
_VRtrPimNgNotifySourceIpType_Type = InetAddressType
_VRtrPimNgNotifySourceIpType_Object = MibScalar
vRtrPimNgNotifySourceIpType = _VRtrPimNgNotifySourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 1),
    _VRtrPimNgNotifySourceIpType_Type()
)
vRtrPimNgNotifySourceIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifySourceIpType.setStatus("current")


class _VRtrPimNgNotifySourceIp_Type(InetAddress):
    """Custom type vRtrPimNgNotifySourceIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgNotifySourceIp_Type.__name__ = "InetAddress"
_VRtrPimNgNotifySourceIp_Object = MibScalar
vRtrPimNgNotifySourceIp = _VRtrPimNgNotifySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 2),
    _VRtrPimNgNotifySourceIp_Type()
)
vRtrPimNgNotifySourceIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifySourceIp.setStatus("current")
_VRtrPimNgNotifyGroupAddrType_Type = InetAddressType
_VRtrPimNgNotifyGroupAddrType_Object = MibScalar
vRtrPimNgNotifyGroupAddrType = _VRtrPimNgNotifyGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 3),
    _VRtrPimNgNotifyGroupAddrType_Type()
)
vRtrPimNgNotifyGroupAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyGroupAddrType.setStatus("current")


class _VRtrPimNgNotifyGroupAddr_Type(InetAddress):
    """Custom type vRtrPimNgNotifyGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgNotifyGroupAddr_Type.__name__ = "InetAddress"
_VRtrPimNgNotifyGroupAddr_Object = MibScalar
vRtrPimNgNotifyGroupAddr = _VRtrPimNgNotifyGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 4),
    _VRtrPimNgNotifyGroupAddr_Type()
)
vRtrPimNgNotifyGroupAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyGroupAddr.setStatus("current")
_VRtrPimNgNotifyRPAddrType_Type = InetAddressType
_VRtrPimNgNotifyRPAddrType_Object = MibScalar
vRtrPimNgNotifyRPAddrType = _VRtrPimNgNotifyRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 5),
    _VRtrPimNgNotifyRPAddrType_Type()
)
vRtrPimNgNotifyRPAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyRPAddrType.setStatus("current")


class _VRtrPimNgNotifyRPAddr_Type(InetAddress):
    """Custom type vRtrPimNgNotifyRPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgNotifyRPAddr_Type.__name__ = "InetAddress"
_VRtrPimNgNotifyRPAddr_Object = MibScalar
vRtrPimNgNotifyRPAddr = _VRtrPimNgNotifyRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 6),
    _VRtrPimNgNotifyRPAddr_Type()
)
vRtrPimNgNotifyRPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyRPAddr.setStatus("current")
_VRtrPimNgNotifyWrongRPAddrType_Type = InetAddressType
_VRtrPimNgNotifyWrongRPAddrType_Object = MibScalar
vRtrPimNgNotifyWrongRPAddrType = _VRtrPimNgNotifyWrongRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 7),
    _VRtrPimNgNotifyWrongRPAddrType_Type()
)
vRtrPimNgNotifyWrongRPAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyWrongRPAddrType.setStatus("current")


class _VRtrPimNgNotifyWrongRPAddr_Type(InetAddress):
    """Custom type vRtrPimNgNotifyWrongRPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgNotifyWrongRPAddr_Type.__name__ = "InetAddress"
_VRtrPimNgNotifyWrongRPAddr_Object = MibScalar
vRtrPimNgNotifyWrongRPAddr = _VRtrPimNgNotifyWrongRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 8),
    _VRtrPimNgNotifyWrongRPAddr_Type()
)
vRtrPimNgNotifyWrongRPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyWrongRPAddr.setStatus("current")


class _VRtrPimNgNotifyMsgType_Type(Integer32):
    """Custom type vRtrPimNgNotifyMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("hello", 0),
          ("register", 1),
          ("registerStop", 2),
          ("joinPrune", 3),
          ("bootstrap", 4),
          ("assert", 5),
          ("graft", 6),
          ("graftAck", 7),
          ("crpAdv", 8),
          ("igmpLocalMembership", 9))
    )


_VRtrPimNgNotifyMsgType_Type.__name__ = "Integer32"
_VRtrPimNgNotifyMsgType_Object = MibScalar
vRtrPimNgNotifyMsgType = _VRtrPimNgNotifyMsgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 9),
    _VRtrPimNgNotifyMsgType_Type()
)
vRtrPimNgNotifyMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyMsgType.setStatus("current")
_VRtrPimNgWrongMdtDefGrpAddrType_Type = InetAddressType
_VRtrPimNgWrongMdtDefGrpAddrType_Object = MibScalar
vRtrPimNgWrongMdtDefGrpAddrType = _VRtrPimNgWrongMdtDefGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 10),
    _VRtrPimNgWrongMdtDefGrpAddrType_Type()
)
vRtrPimNgWrongMdtDefGrpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongMdtDefGrpAddrType.setStatus("current")


class _VRtrPimNgWrongMdtDefGrpAddr_Type(InetAddress):
    """Custom type vRtrPimNgWrongMdtDefGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgWrongMdtDefGrpAddr_Type.__name__ = "InetAddress"
_VRtrPimNgWrongMdtDefGrpAddr_Object = MibScalar
vRtrPimNgWrongMdtDefGrpAddr = _VRtrPimNgWrongMdtDefGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 11),
    _VRtrPimNgWrongMdtDefGrpAddr_Type()
)
vRtrPimNgWrongMdtDefGrpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongMdtDefGrpAddr.setStatus("current")


class _VRtrPimNgWrongPmsiType_Type(Integer32):
    """Custom type vRtrPimNgWrongPmsiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pimSsm", 0),
          ("pimSm", 1),
          ("rsvp", 2),
          ("ldp", 3))
    )


_VRtrPimNgWrongPmsiType_Type.__name__ = "Integer32"
_VRtrPimNgWrongPmsiType_Object = MibScalar
vRtrPimNgWrongPmsiType = _VRtrPimNgWrongPmsiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 12),
    _VRtrPimNgWrongPmsiType_Type()
)
vRtrPimNgWrongPmsiType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiType.setStatus("current")
_VRtrPimNgWrongPmsiP2mpId_Type = Unsigned32
_VRtrPimNgWrongPmsiP2mpId_Object = MibScalar
vRtrPimNgWrongPmsiP2mpId = _VRtrPimNgWrongPmsiP2mpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 13),
    _VRtrPimNgWrongPmsiP2mpId_Type()
)
vRtrPimNgWrongPmsiP2mpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiP2mpId.setStatus("current")
_VRtrPimNgWrongPmsiTunnelId_Type = Unsigned32
_VRtrPimNgWrongPmsiTunnelId_Object = MibScalar
vRtrPimNgWrongPmsiTunnelId = _VRtrPimNgWrongPmsiTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 14),
    _VRtrPimNgWrongPmsiTunnelId_Type()
)
vRtrPimNgWrongPmsiTunnelId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiTunnelId.setStatus("current")
_VRtrPimNgWrongPmsiExtTunlAdrTyp_Type = InetAddressType
_VRtrPimNgWrongPmsiExtTunlAdrTyp_Object = MibScalar
vRtrPimNgWrongPmsiExtTunlAdrTyp = _VRtrPimNgWrongPmsiExtTunlAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 15),
    _VRtrPimNgWrongPmsiExtTunlAdrTyp_Type()
)
vRtrPimNgWrongPmsiExtTunlAdrTyp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiExtTunlAdrTyp.setStatus("current")


class _VRtrPimNgWrongPmsiExtTunlAddr_Type(InetAddress):
    """Custom type vRtrPimNgWrongPmsiExtTunlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgWrongPmsiExtTunlAddr_Type.__name__ = "InetAddress"
_VRtrPimNgWrongPmsiExtTunlAddr_Object = MibScalar
vRtrPimNgWrongPmsiExtTunlAddr = _VRtrPimNgWrongPmsiExtTunlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 16),
    _VRtrPimNgWrongPmsiExtTunlAddr_Type()
)
vRtrPimNgWrongPmsiExtTunlAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiExtTunlAddr.setStatus("current")
_VRtrPimNgWrongVprnId_Type = TmnxVRtrID
_VRtrPimNgWrongVprnId_Object = MibScalar
vRtrPimNgWrongVprnId = _VRtrPimNgWrongVprnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 17),
    _VRtrPimNgWrongVprnId_Type()
)
vRtrPimNgWrongVprnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongVprnId.setStatus("current")
_VRtrPimNgWrongPmsiLdpLspId_Type = Unsigned32
_VRtrPimNgWrongPmsiLdpLspId_Object = MibScalar
vRtrPimNgWrongPmsiLdpLspId = _VRtrPimNgWrongPmsiLdpLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 18),
    _VRtrPimNgWrongPmsiLdpLspId_Type()
)
vRtrPimNgWrongPmsiLdpLspId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiLdpLspId.setStatus("current")
_VRtrPimNgWrongPmsiSenderAdrTyp_Type = InetAddressType
_VRtrPimNgWrongPmsiSenderAdrTyp_Object = MibScalar
vRtrPimNgWrongPmsiSenderAdrTyp = _VRtrPimNgWrongPmsiSenderAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 19),
    _VRtrPimNgWrongPmsiSenderAdrTyp_Type()
)
vRtrPimNgWrongPmsiSenderAdrTyp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiSenderAdrTyp.setStatus("current")


class _VRtrPimNgWrongPmsiSenderAddr_Type(InetAddress):
    """Custom type vRtrPimNgWrongPmsiSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrPimNgWrongPmsiSenderAddr_Type.__name__ = "InetAddress"
_VRtrPimNgWrongPmsiSenderAddr_Object = MibScalar
vRtrPimNgWrongPmsiSenderAddr = _VRtrPimNgWrongPmsiSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 20),
    _VRtrPimNgWrongPmsiSenderAddr_Type()
)
vRtrPimNgWrongPmsiSenderAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgWrongPmsiSenderAddr.setStatus("current")
_VRtrPimNgNotifySourceAddrType_Type = InetAddressType
_VRtrPimNgNotifySourceAddrType_Object = MibScalar
vRtrPimNgNotifySourceAddrType = _VRtrPimNgNotifySourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 21),
    _VRtrPimNgNotifySourceAddrType_Type()
)
vRtrPimNgNotifySourceAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifySourceAddrType.setStatus("current")
_VRtrPimNgNotifySourceAddr_Type = InetAddress
_VRtrPimNgNotifySourceAddr_Object = MibScalar
vRtrPimNgNotifySourceAddr = _VRtrPimNgNotifySourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 22),
    _VRtrPimNgNotifySourceAddr_Type()
)
vRtrPimNgNotifySourceAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifySourceAddr.setStatus("current")
_VRtrPimNgNotifyDescription_Type = DisplayString
_VRtrPimNgNotifyDescription_Object = MibScalar
vRtrPimNgNotifyDescription = _VRtrPimNgNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 50, 3, 23),
    _VRtrPimNgNotifyDescription_Type()
)
vRtrPimNgNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrPimNgNotifyDescription.setStatus("current")
_VRtrPimNgNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrPimNgNotifyPrefix = _VRtrPimNgNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50)
)
_VRtrPimNgNotifications_ObjectIdentity = ObjectIdentity
vRtrPimNgNotifications = _VRtrPimNgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0)
)
vRtrPimNgAFGenEntry.registerAugmentions(
    ("TIMETRA-PIM-NG-MIB",
     "vRtrPimNgGenStatEntry")
)
vRtrPimNgGenStatEntry.setIndexNames(*vRtrPimNgAFGenEntry.getIndexNames())
vRtrPimNgGrpSrcEntry.registerAugmentions(
    ("TIMETRA-PIM-NG-MIB",
     "vRtrPimNgGrpSrcStatEntry")
)
vRtrPimNgGrpSrcStatEntry.setIndexNames(*vRtrPimNgGrpSrcEntry.getIndexNames())
vRtrPimNgGeneralEntry.registerAugmentions(
    ("TIMETRA-PIM-NG-MIB",
     "vRtrPimNgGenPolicyEntry")
)
vRtrPimNgGenPolicyEntry.setIndexNames(*vRtrPimNgGeneralEntry.getIndexNames())
vRtrPimNgAFIfEntry.registerAugmentions(
    ("TIMETRA-PIM-NG-MIB",
     "vRtrPimNgIfStatsEntry")
)
vRtrPimNgIfStatsEntry.setIndexNames(*vRtrPimNgAFIfEntry.getIndexNames())

# Managed Objects groups

tmnxPimNgGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 1)
)
tmnxPimNgGlobalGroup.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgGeneralTableLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenCreateInterfaces"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenMaxMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenNonDrAttractTraffic"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpBalance"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpBalanceHoldTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpReBlncInProg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpLastReBlncTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpRebalanceType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpOptThreshold"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpNextBalanceTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenLagUsageOptimize"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenTableLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSROperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRUpTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMTIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRHashMaskLen"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRHashMaskLen"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRRpfIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenRpfLookupSequence"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefixType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefix"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefixMask"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataDlayIntrvl"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataJoinTlvPck"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPTableLstChnged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPOverride"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrptoRPTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrpToRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrpToRPRowLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrfxTblLstChnged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrefixRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrfixRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxCrpaPduErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxCrpaPduDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatStarStarRPTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatStarGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatSGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegisterErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxNullRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegTTLDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatForwardCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatFwdCrpaDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxMdtJoinTlvs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxMdtJoinTlvs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxMdtJnTlvErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxMdtJnTlvErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxActiveMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxActiveMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPRowLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwOvrThdTabLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwovrThdRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwovrThdRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwitchoverThd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThd"))
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalGroup.setStatus("obsolete")

tmnxPimNgGlobalGrpSrcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 2)
)
tmnxPimNgGlobalGrpSrcGroup.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRPAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfNbrAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfNbrAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRptRpfNbrAdrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRptRpfNbrAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcMRIBNHopAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcMRIBNextHopAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcMRIBSrcFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUpstreamJpState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUpstreamJpTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUstrmRptJpState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUstrmRptOvrdeTmr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRegisterState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRegisterStopTmr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcKeepaliveTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumImmediateOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumInheritedOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumInherRptOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumLclRxInclIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumLclRxExclIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumJoinPruneIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumLostAssertIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUpTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumSGRptPruneOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRxRegFrmAnycstRP"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRslvdByRtTblType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcCurrFwdingRate"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcCurrFwdingOFRate"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcCurrFwdingHCRate"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpSptThreshold"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcIfFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatFrwdedPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFFrwdedPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCFrwdedPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatDscrdPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFDscrdPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCDscrdPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatRPFMsmtch"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFRPFMsmtch"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCRPFMsmtch"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatFrdedOct"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFFrdedOct"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCFrdedOct"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpAdminBw"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpEcmpOptThresh"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcHostFlags"))
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalGrpSrcGroup.setStatus("obsolete")

tmnxPimNgIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 3)
)
tmnxPimNgIfGroup.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTableLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfLastChangeTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfHelloInterval"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTrackingSupport"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMulticastSenders"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfAutoCreated"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfBSMCheckRouterAlert"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfHelloMultiplier"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfImprovedAssert"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfStickyDR"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfStickyDRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMaxGroups"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfEnableBfd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfThreeWayHello"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacPolicyName"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacUnconstrainedBW"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacConstAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacPreRsvdMandBW"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacinUseMandBw"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacinUseOpnlBw"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacAvailMandBw"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacAvailOpnlBw"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacValuesInTransit"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfDRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfAssertPeriod"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfMdtDefGrpAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfMdtDefGrpAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfNextHelloTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfOperDRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfCurrentGroups"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfMaxGroupsTillNow"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfDRType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfDR"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFIfTrackSprtOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborUpTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborGenId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborDrPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborDrPriorPrsnt"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborLanDelay"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborLanDlayPrsnt"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborTrckngSpprt"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborHoldTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborOvrdeIntrvl"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRPAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcJPState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcPrunePendTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcJoinPruneTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcJPRptState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRptPrnePendTmr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRptJoinPrneTmr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAssertState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAssertTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAssertMetric"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAsrtMetricPref"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAssertRPTBit"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAsrtWinnerMtrc"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAsrtWnrMtrcPrf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAsrtWnrRPTBit"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAsrtWnrAddrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcAsrtWinnerAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcUpTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcDataMtIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxHellos"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxAsserts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxRegisterStops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxRegisterStopErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxBsmPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxBsmErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxHellos"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxHellosDropped"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxNbrUnknown"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBadChecksumDiscard"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBadVersionDiscard"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBadEncodings"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxAsserts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxAssertErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxRegisterErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxNullRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxRegisterStops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxRegisterStopErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxCRPAdvNoRtrAlert"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBsmPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBsmPduDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfStarStarRPTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfStarGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfSGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfJoinPolicyDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRegisterPolicyDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfBtrImpPolicyDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfBtrExpPolicyDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxJoinPrunes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxJoinPrunes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxInvalidJoinPrunes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxInvalidRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxUnknownPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxJoinPruneErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBSMNoRouterAlertDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBSMWrongIfDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtUptime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtNumVpnSGs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcJoinTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcHolddownTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcExpiryTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcUptime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcDataMtThreshold"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtCGrpSrcIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacPolicyDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLevelTblLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLevelRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLvlRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLevelBW"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLagTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLagRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLagRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacLagLevel"))
)
if mibBuilder.loadTexts:
    tmnxPimNgIfGroup.setStatus("current")

tmnxPimNgNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 4)
)
tmnxPimNgNotifyObjsGroup.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIpType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyRPAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyWrongRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyWrongRPAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyMsgType"))
)
if mibBuilder.loadTexts:
    tmnxPimNgNotifyObjsGroup.setStatus("current")

tmnxPimNgEmbeddedRPV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 6)
)
tmnxPimNgEmbeddedRPV7v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenERP"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenERPAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgERPGrpPrfxTblLstChnged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgERPGrpPrefixRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxPimNgEmbeddedRPV7v0Group.setStatus("current")

tmnxPimNgMvpnV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 7)
)
tmnxPimNgMvpnV7v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnAutoDiscovery"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnCMcastSignal"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnGrpAddrMode"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnSpmsiAutoDisc"))
)
if mibBuilder.loadTexts:
    tmnxPimNgMvpnV7v0Group.setStatus("obsolete")

tmnxPimNgV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 8)
)
tmnxPimNgV7v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIfRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIfOperState"))
)
if mibBuilder.loadTexts:
    tmnxPimNgV7v0Group.setStatus("current")

tmnxPimNgGlobalGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 9)
)
tmnxPimNgGlobalGroupV7v0.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgGeneralTableLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenCreateInterfaces"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenMaxMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenNonDrAttractTraffic"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpBalance"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpBalanceHoldTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpReBlncInProg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpLastReBlncTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpRebalanceType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpNextBalanceTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenLagUsageOptimize"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenTableLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSROperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRUpTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMTIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRHashMaskLen"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRHashMaskLen"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRRpfIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenRpfLookupSequence"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefixType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefix"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefixMask"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataDlayIntrvl"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataJoinTlvPck"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPTableLstChnged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPOverride"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrptoRPTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrpToRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrpToRPRowLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxCrpaPduErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxCrpaPduDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatStarStarRPTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatStarGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatSGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegisterErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxNullRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegTTLDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatForwardCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatFwdCrpaDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxMdtJoinTlvs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxMdtJoinTlvs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxMdtJnTlvErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxMdtJnTlvErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxActiveMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxActiveMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPRowLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwOvrThdTabLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwovrThdRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwovrThdRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwitchoverThd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGpPfxInetTblLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrfxInetRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPfxInetRowLstChgd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalGroupV7v0.setStatus("obsolete")

tmnxPimNgObsoleteV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 10)
)
tmnxPimNgObsoleteV7v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrfxTblLstChnged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrefixRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrfixRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxPimNgObsoleteV7v0Group.setStatus("current")

tmnxPimIfSecNbrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 11)
)
tmnxPimIfSecNbrV6v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfSecNbrTblLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfSecNbrAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfSecNbrAddress"))
)
if mibBuilder.loadTexts:
    tmnxPimIfSecNbrV6v0Group.setStatus("current")

tmnxPimNgIfStatsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 12)
)
tmnxPimNgIfStatsV7v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxIntraASAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxIntraASAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxIntraASADErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxInterASAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxInterASAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxInterASADErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxSpmsiAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxSpmsiAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxSpmsiADErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxLeafAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxLeafAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxLeafADErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxSrcActAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxSrcActAD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxSrcActADErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxSharedTreeJoin"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxSharedTreeJoin"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxSharedTreeJoinErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxSrcTreeJoin"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxSrcTreeJoin"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxSrcTreeJoinErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxBgpPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxBgpPkts"))
)
if mibBuilder.loadTexts:
    tmnxPimNgIfStatsV7v0Group.setStatus("current")

tmnxPimNgObsoleteV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 13)
)
tmnxPimNgObsoleteV6v0Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpOptThreshold")
)
if mibBuilder.loadTexts:
    tmnxPimNgObsoleteV6v0Group.setStatus("current")

tmnxPimNgNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 15)
)
tmnxPimNgNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongMdtDefGrpAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongMdtDefGrpAddr"))
)
if mibBuilder.loadTexts:
    tmnxPimNgNotifyObjsV7v0Group.setStatus("current")

tmnxPimNgMvpnV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 16)
)
tmnxPimNgMvpnV8v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnUMHSelection"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnIntersiteShrd"))
)
if mibBuilder.loadTexts:
    tmnxPimNgMvpnV8v0Group.setStatus("current")

tmnxPimNgEchoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 17)
)
tmnxPimNgEchoGroup.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfInstantPruneEcho")
)
if mibBuilder.loadTexts:
    tmnxPimNgEchoGroup.setStatus("current")

tmnxPimNgIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 19)
)
tmnxPimNgIfV8v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiUptime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiNumVpnSGs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcJoinTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcHldDnTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcExpTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcUptime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimDataMtCGrpSrcDataThresh"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimRsvpPmsiCGrpSrcIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxPimNgIfV8v0Group.setStatus("current")

tmnxPimNgGlobalSSMV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 20)
)
tmnxPimNgGlobalSSMV6v1Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenSSMDefRangeDisabl")
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalSSMV6v1Group.setStatus("current")

tmnxPimNgGlobalGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 21)
)
tmnxPimNgGlobalGroupV8v0.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgGeneralTableLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenCreateInterfaces"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenMaxMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenNonDrAttractTraffic"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpBalance"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpBalanceHoldTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpReBlncInProg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpLastReBlncTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpRebalanceType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpNextBalanceTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenLagUsageOptimize"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenTableLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSROperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRUpTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPAdminState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPOperState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCRPPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMTIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenCBSRHashMaskLen"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRHashMaskLen"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRRpfIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenRpfLookupSequence"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefixType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefix"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataPrefixMask"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataDlayIntrvl"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataJoinTlvPck"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPTableLstChnged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStaticRPOverride"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrptoRPTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrpToRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgStGrpToRPRowLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxCrpaPduErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxCrpaPduDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatStarStarRPTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatStarGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatSGTypes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegisterErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxNullRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxRegTTLDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatForwardCrpaPdus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatFwdCrpaDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxMdtJoinTlvs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxMdtJoinTlvs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxMdtJnTlvErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxMdtJnTlvErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxActiveMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxActiveMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportJoinPrunePolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportRegisterPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgImportBootstrapPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy1"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy2"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy3"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy4"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExportBootstrapPolicy5"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSSMGroupRowLastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAnycastRPRowLstChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwOvrThdTabLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwovrThdRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwovrThdRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSptSwitchoverThd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdTableLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThdRowLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtThd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGpPfxInetTblLstChngd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPrfxInetRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPGrpPfxInetRowLstChgd"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgCRPInetExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetHoldtime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetPriority"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRPSetInetExpiryTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEcmpHashingEnabled"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenEnableMdtSpt"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxSpmsiLimitHits"))
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalGroupV8v0.setStatus("current")

tmnxPimNgGlobalGrpSrcV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 22)
)
tmnxPimNgGlobalGrpSrcV9v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRPAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfNbrAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfNbrAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRptRpfNbrAdrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRptRpfNbrAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcMRIBNHopAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcMRIBNextHopAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcMRIBSrcFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUpstreamJpState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUpstreamJpTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUstrmRptJpState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUstrmRptOvrdeTmr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRegisterState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRegisterStopTmr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcKeepaliveTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumImmediateOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumInheritedOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumInherRptOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumLclRxInclIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumLclRxExclIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumJoinPruneIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumLostAssertIf"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUpTime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcNumSGRptPruneOif"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRxRegFrmAnycstRP"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRslvdByRtTblType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcCurrFwdingRate"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcCurrFwdingOFRate"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcCurrFwdingHCRate"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpSptThreshold"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcIfFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatFrwdedPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFFrwdedPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCFrwdedPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatDscrdPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFDscrdPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCDscrdPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatRPFMsmtch"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFRPFMsmtch"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCRPFMsmtch"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatFrdedOct"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatOFFrdedOct"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStatHCFrdedOct"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpAdminBw"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpEcmpOptThresh"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcHostFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcGrpIfFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxCtrlPduIfDrops"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatP2mpPmsiReqFails"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatP2mpPmsiCrtFails"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSpmsiRpfIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcSpmsiIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatTxMdts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenStatRxMdts"))
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalGrpSrcV9v0Group.setStatus("current")

tmnxPimNgIfIpv6BfdV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 23)
)
tmnxPimNgIfIpv6BfdV9v0Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfIpv6EnableBfd")
)
if mibBuilder.loadTexts:
    tmnxPimNgIfIpv6BfdV9v0Group.setStatus("current")

tmnxPimNgNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 24)
)
tmnxPimNgNotifyObjsV8v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiP2mpId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiTunnelId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiExtTunlAdrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiExtTunlAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongVprnId"))
)
if mibBuilder.loadTexts:
    tmnxPimNgNotifyObjsV8v0Group.setStatus("current")

tmnxPimNgLdpEntryV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 25)
)
tmnxPimNgLdpEntryV10v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiUptime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiNumVpnSGs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcJoinTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcHldDnTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcExpTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcUptime"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimLdpDataMtCGrpSrcDataThres"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimLdpPmsiCGrpSrcIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpPmsiIfType"))
)
if mibBuilder.loadTexts:
    tmnxPimNgLdpEntryV10v0Group.setStatus("current")

tmnxPimNgNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 26)
)
tmnxPimNgNotifyObjsV9v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiLdpLspId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiSenderAdrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiSenderAddr"))
)
if mibBuilder.loadTexts:
    tmnxPimNgNotifyObjsV9v0Group.setStatus("current")

tmnxPimNgObsoletedV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 27)
)
tmnxPimNgObsoletedV9v0Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnAutoDiscovery")
)
if mibBuilder.loadTexts:
    tmnxPimNgObsoletedV9v0Group.setStatus("current")

tmnxPimNgMvpnV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 28)
)
tmnxPimNgMvpnV9v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnCMcastSignal"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnGrpAddrMode"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnSpmsiAutoDisc"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMvpnAD"))
)
if mibBuilder.loadTexts:
    tmnxPimNgMvpnV9v0Group.setStatus("current")

tmnxPimNgIfStatsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 29)
)
tmnxPimNgIfStatsV9v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxMdtSafi"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxMdtSafi"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxMdtSafiErrs"))
)
if mibBuilder.loadTexts:
    tmnxPimNgIfStatsV9v0Group.setStatus("current")

tmnxPimNgIfV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 30)
)
tmnxPimNgIfV10v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfP2mpLdpTreeJoin"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfExtranetType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfExtranetMvpnId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpPmsiIfType"))
)
if mibBuilder.loadTexts:
    tmnxPimNgIfV10v0Group.setStatus("current")

tmnxPimNgIfIPMSIV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 31)
)
tmnxPimNgIfIPMSIV9v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIPmsiExtTunlAdrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIPmsiExtTunnelAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIPmsiLspName"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIPmsiP2MPId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgRsvpIPmsiTunnelId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpIPmsiRootAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpIPmsiRootAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpIPmsiLspId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgLdpIPmsiLspName"))
)
if mibBuilder.loadTexts:
    tmnxPimNgIfIPMSIV9v0Group.setStatus("current")

tmnxPimNgMvpnV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 32)
)
tmnxPimNgMvpnV9v0R4Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPETblLastChg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPERowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPELastChanged"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEStandbyAdrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnUMHPEStandbyAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfSecNbrAddrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfSecNbrAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfSecIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDataGrpAddrMode"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenEnableAsmDataMdt"))
)
if mibBuilder.loadTexts:
    tmnxPimNgMvpnV9v0R4Group.setStatus("current")

tmnxPimNgGlobalGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 33)
)
tmnxPimNgGlobalGroupV10v0.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAfGenAutoRPDiscovery"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAfGenSSMAsrtCompMode"))
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalGroupV10v0.setStatus("current")

tmnxPimNgIfStatsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 34)
)
tmnxPimNgIfStatsV10v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxAutoRpGenErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxAutoRpAnnounce"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxAutoRpAnnounce"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxAutoRpAnnounceErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxAutoRpAnnounceErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxAutoRpMapping"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxAutoRpMapping"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxAutoRpMappingErrs"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxAutoRpMappingErrs"))
)
if mibBuilder.loadTexts:
    tmnxPimNgIfStatsV10v0Group.setStatus("current")

tmnxPimNgMvpnExtranetGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 35)
)
tmnxPimNgMvpnExtranetGroupV10v0.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnExtranetRecvRefCnt")
)
if mibBuilder.loadTexts:
    tmnxPimNgMvpnExtranetGroupV10v0.setStatus("current")

tmnxPimNgGlobalGrpSrcV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 37)
)
tmnxPimNgGlobalGrpSrcV10v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcAdvtAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcAdvtAddr"))
)
if mibBuilder.loadTexts:
    tmnxPimNgGlobalGrpSrcV10v0Group.setStatus("current")

tmnxPimNgMVPNSndrRecvV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 38)
)
tmnxPimNgMVPNSndrRecvV11v0Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAfGenMdtType")
)
if mibBuilder.loadTexts:
    tmnxPimNgMVPNSndrRecvV11v0Group.setStatus("current")

tmnxPimNgFastFailover11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 39)
)
tmnxPimNgFastFailover11v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAfGenMcastFastFailover"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStdbyMRIBSrcFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStdbyUpJpState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStdbyUpJpTimer"))
)
if mibBuilder.loadTexts:
    tmnxPimNgFastFailover11v0Group.setStatus("current")

tmnxPimNgInterASMvpnV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 40)
)
tmnxPimNgInterASMvpnV11v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenRpfVectorFlags"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborJASupport"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxJoinPrunesMvpnRpfv"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfTxJoinPrunesMvpnRpfv"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxInvalidJPMvpnRpfv"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcStdbyUpJpTimer"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcDSRpfvNbrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcDSRpfvNbr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcDSRpfvProxyType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcDSRpfvProxy"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcDSRpfvRD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcDSRpfvType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUPRpfvNbrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUPRpfvNbr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUPRpfvProxyType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUPRpfvProxy"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUPRpfvRD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcUPRpfvType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvPrxyAddrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvProxyAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvRD"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvIfWinner"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfGrpSrcRpfvNbrWinner"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcRpfvFlags"))
)
if mibBuilder.loadTexts:
    tmnxPimNgInterASMvpnV11v0Group.setStatus("current")

tmnxPimNgCDV12v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 41)
)
tmnxPimNgCDV12v0Grp.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenSourceAddressType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenSourceAddress"))
)
if mibBuilder.loadTexts:
    tmnxPimNgCDV12v0Grp.setStatus("current")

tmnxPimNgMvpnSrcPrefixV12v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 42)
)
tmnxPimNgMvpnSrcPrefixV12v0Grp.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnSrcPrefixRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnSrcPrefixRowLastChg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMvpnSrcPrefixTblLstChg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpSrcState"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAfGenMvpnPersistSA"))
)
if mibBuilder.loadTexts:
    tmnxPimNgMvpnSrcPrefixV12v0Grp.setStatus("current")

tmnxPimNgSgStatcExtrntV12v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 43)
)
tmnxPimNgSgStatcExtrntV12v0Grp.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgExtranetCDRowLstChg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExtranetCDTblLstChg"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExtranetCDMvpnId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgExtranetCDRowStatus"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenGrpPrefixAny"))
)
if mibBuilder.loadTexts:
    tmnxPimNgSgStatcExtrntV12v0Grp.setStatus("current")

tmnxPimNgNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 44)
)
tmnxPimNgNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxPimNgNotifyObjsV12v0Group.setStatus("current")

tmnxPimNgIfV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 45)
)
tmnxPimNgIfV12v0Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacUseLagPortWeight")
)
if mibBuilder.loadTexts:
    tmnxPimNgIfV12v0Group.setStatus("current")

tmnxPimNgUnicastRtRemV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 46)
)
tmnxPimNgUnicastRtRemV12v0Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAfGenUnicastRtRemoval")
)
if mibBuilder.loadTexts:
    tmnxPimNgUnicastRtRemV12v0Group.setStatus("current")


# Notification objects

vRtrPimNgIfNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 1)
)
vRtrPimNgIfNeighborLoss.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborUpTime")
)
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborLoss.setStatus(
        "current"
    )

vRtrPimNgIfNeighborUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 2)
)
vRtrPimNgIfNeighborUp.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborUpTime")
)
if mibBuilder.loadTexts:
    vRtrPimNgIfNeighborUp.setStatus(
        "current"
    )

vRtrPimNgInvalidJoinPrune = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 3)
)
vRtrPimNgInvalidJoinPrune.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxInvalidJoinPrunes"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIpType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyRPAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyWrongRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyWrongRPAddr"))
)
if mibBuilder.loadTexts:
    vRtrPimNgInvalidJoinPrune.setStatus(
        "current"
    )

vRtrPimNgInvalidRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 4)
)
vRtrPimNgInvalidRegister.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxInvalidRegisters"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIpType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyRPAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyWrongRPAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyWrongRPAddr"))
)
if mibBuilder.loadTexts:
    vRtrPimNgInvalidRegister.setStatus(
        "current"
    )

vRtrPimNgGrpInSSMRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 5)
)
vRtrPimNgGrpInSSMRange.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfRxPkts"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIpType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyMsgType"))
)
if mibBuilder.loadTexts:
    vRtrPimNgGrpInSSMRange.setStatus(
        "current"
    )

vRtrPimNgBSRStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 6)
)
vRtrPimNgBSRStateChange.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenBSRState")
)
if mibBuilder.loadTexts:
    vRtrPimNgBSRStateChange.setStatus(
        "current"
    )

vRtrPimNgHelloDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 7)
)
vRtrPimNgHelloDropped.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborUpTime")
)
if mibBuilder.loadTexts:
    vRtrPimNgHelloDropped.setStatus(
        "current"
    )

vRtrPimNgSGLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 8)
)
vRtrPimNgSGLimitExceeded.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCardHwIndex")
)
if mibBuilder.loadTexts:
    vRtrPimNgSGLimitExceeded.setStatus(
        "current"
    )

vRtrPimNgReplicationLmtExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 9)
)
vRtrPimNgReplicationLmtExceeded.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIpType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddr"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardHwIndex"))
)
if mibBuilder.loadTexts:
    vRtrPimNgReplicationLmtExceeded.setStatus(
        "current"
    )

vRtrPimNgMDTLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 10)
)
vRtrPimNgMDTLimitExceeded.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGenMaxMdts"))
)
if mibBuilder.loadTexts:
    vRtrPimNgMDTLimitExceeded.setStatus(
        "current"
    )

vRtrPimNgMaxGrpsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 11)
)
vRtrPimNgMaxGrpsLimitExceeded.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMaxGroups")
)
if mibBuilder.loadTexts:
    vRtrPimNgMaxGrpsLimitExceeded.setStatus(
        "current"
    )

vRtrPimNgDataMtReused = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 12)
)
vRtrPimNgDataMtReused.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtIfIndex"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtNumVpnSGs"))
)
if mibBuilder.loadTexts:
    vRtrPimNgDataMtReused.setStatus(
        "current"
    )

vRtrPimNgMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 13)
)
vRtrPimNgMcacPlcyDropped.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfMcacPolicyName"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyGroupAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifyDescription"))
)
if mibBuilder.loadTexts:
    vRtrPimNgMcacPlcyDropped.setStatus(
        "current"
    )

vRtrPimNgInvalidIPmsiTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 50, 0, 14)
)
vRtrPimNgInvalidIPmsiTunnel.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenMdtDefGrpAddress"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIpType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgNotifySourceIp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongMdtDefGrpAddrType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongMdtDefGrpAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiType"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiP2mpId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiTunnelId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiExtTunlAdrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiExtTunlAddr"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongVprnId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiLdpLspId"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiSenderAdrTyp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgWrongPmsiSenderAddr"))
)
if mibBuilder.loadTexts:
    vRtrPimNgInvalidIPmsiTunnel.setStatus(
        "current"
    )


# Notifications groups

tmnxPimNgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 5)
)
tmnxPimNgNotificationGroup.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborLoss"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgIfNeighborUp"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgInvalidJoinPrune"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgInvalidRegister"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgGrpInSSMRange"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgBSRStateChange"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgHelloDropped"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgSGLimitExceeded"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgReplicationLmtExceeded"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMDTLimitExceeded"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMaxGrpsLimitExceeded"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgDataMtReused"),
        ("TIMETRA-PIM-NG-MIB", "vRtrPimNgMcacPlcyDropped"))
)
if mibBuilder.loadTexts:
    tmnxPimNgNotificationGroup.setStatus(
        "current"
    )

tmnxPimNgNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 2, 14)
)
tmnxPimNgNotificationV7v0Group.setObjects(
    ("TIMETRA-PIM-NG-MIB", "vRtrPimNgInvalidIPmsiTunnel")
)
if mibBuilder.loadTexts:
    tmnxPimNgNotificationV7v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPimNgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1, 1)
)
tmnxPimNgCompliance.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimIfSecNbrV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPimNgCompliance.setStatus(
        "obsolete"
    )

tmnxPimNgV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1, 2)
)
tmnxPimNgV7v0Compliance.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimIfSecNbrV6v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEmbeddedRPV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV7v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotifyObjsV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPimNgV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxPimNgV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1, 3)
)
tmnxPimNgV8v0Compliance.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimIfSecNbrV6v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEmbeddedRPV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotifyObjsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEchoGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalSSMV6v1Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV8v0"))
)
if mibBuilder.loadTexts:
    tmnxPimNgV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxPimNgV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1, 4)
)
tmnxPimNgV9v0Compliance.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimIfSecNbrV6v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEmbeddedRPV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotifyObjsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEchoGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalSSMV6v1Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV8v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIpv6BfdV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIPMSIV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0R4Group"))
)
if mibBuilder.loadTexts:
    tmnxPimNgV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxPimNgV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1, 5)
)
tmnxPimNgV10v0Compliance.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimIfSecNbrV6v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEmbeddedRPV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotifyObjsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEchoGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalSSMV6v1Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV8v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIpv6BfdV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIPMSIV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0R4Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgLdpEntryV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV10v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnExtranetGroupV10v0"))
)
if mibBuilder.loadTexts:
    tmnxPimNgV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxPimNgV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1, 6)
)
tmnxPimNgV11v0Compliance.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimIfSecNbrV6v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEmbeddedRPV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotifyObjsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEchoGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalSSMV6v1Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV8v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIpv6BfdV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIPMSIV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0R4Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgLdpEntryV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV10v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnExtranetGroupV10v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMVPNSndrRecvV11v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgFastFailover11v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgInterASMvpnV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPimNgV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxPimNgV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 50, 1, 7)
)
tmnxPimNgV12v0Compliance.setObjects(
      *(("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimIfSecNbrV6v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEmbeddedRPV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotificationV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotifyObjsV7v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgNotifyObjsV12v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgEchoGroup"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV8v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalSSMV6v1Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV8v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIpv6BfdV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfIPMSIV9v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnV9v0R4Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgLdpEntryV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfV12v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGroupV10v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgIfStatsV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnExtranetGroupV10v0"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgGlobalGrpSrcV10v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMVPNSndrRecvV11v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgFastFailover11v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgInterASMvpnV11v0Group"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgCDV12v0Grp"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgMvpnSrcPrefixV12v0Grp"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgSgStatcExtrntV12v0Grp"),
        ("TIMETRA-PIM-NG-MIB", "tmnxPimNgUnicastRtRemV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPimNgV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PIM-NG-MIB",
    **{"timetraPimNgMIBModule": timetraPimNgMIBModule,
       "tmnxPimNgConformance": tmnxPimNgConformance,
       "tmnxPimNgCompliances": tmnxPimNgCompliances,
       "tmnxPimNgCompliance": tmnxPimNgCompliance,
       "tmnxPimNgV7v0Compliance": tmnxPimNgV7v0Compliance,
       "tmnxPimNgV8v0Compliance": tmnxPimNgV8v0Compliance,
       "tmnxPimNgV9v0Compliance": tmnxPimNgV9v0Compliance,
       "tmnxPimNgV10v0Compliance": tmnxPimNgV10v0Compliance,
       "tmnxPimNgV11v0Compliance": tmnxPimNgV11v0Compliance,
       "tmnxPimNgV12v0Compliance": tmnxPimNgV12v0Compliance,
       "tmnxPimNgGroups": tmnxPimNgGroups,
       "tmnxPimNgGlobalGroup": tmnxPimNgGlobalGroup,
       "tmnxPimNgGlobalGrpSrcGroup": tmnxPimNgGlobalGrpSrcGroup,
       "tmnxPimNgIfGroup": tmnxPimNgIfGroup,
       "tmnxPimNgNotifyObjsGroup": tmnxPimNgNotifyObjsGroup,
       "tmnxPimNgNotificationGroup": tmnxPimNgNotificationGroup,
       "tmnxPimNgEmbeddedRPV7v0Group": tmnxPimNgEmbeddedRPV7v0Group,
       "tmnxPimNgMvpnV7v0Group": tmnxPimNgMvpnV7v0Group,
       "tmnxPimNgV7v0Group": tmnxPimNgV7v0Group,
       "tmnxPimNgGlobalGroupV7v0": tmnxPimNgGlobalGroupV7v0,
       "tmnxPimNgObsoleteV7v0Group": tmnxPimNgObsoleteV7v0Group,
       "tmnxPimIfSecNbrV6v0Group": tmnxPimIfSecNbrV6v0Group,
       "tmnxPimNgIfStatsV7v0Group": tmnxPimNgIfStatsV7v0Group,
       "tmnxPimNgObsoleteV6v0Group": tmnxPimNgObsoleteV6v0Group,
       "tmnxPimNgNotificationV7v0Group": tmnxPimNgNotificationV7v0Group,
       "tmnxPimNgNotifyObjsV7v0Group": tmnxPimNgNotifyObjsV7v0Group,
       "tmnxPimNgMvpnV8v0Group": tmnxPimNgMvpnV8v0Group,
       "tmnxPimNgEchoGroup": tmnxPimNgEchoGroup,
       "tmnxPimNgIfV8v0Group": tmnxPimNgIfV8v0Group,
       "tmnxPimNgGlobalSSMV6v1Group": tmnxPimNgGlobalSSMV6v1Group,
       "tmnxPimNgGlobalGroupV8v0": tmnxPimNgGlobalGroupV8v0,
       "tmnxPimNgGlobalGrpSrcV9v0Group": tmnxPimNgGlobalGrpSrcV9v0Group,
       "tmnxPimNgIfIpv6BfdV9v0Group": tmnxPimNgIfIpv6BfdV9v0Group,
       "tmnxPimNgNotifyObjsV8v0Group": tmnxPimNgNotifyObjsV8v0Group,
       "tmnxPimNgLdpEntryV10v0Group": tmnxPimNgLdpEntryV10v0Group,
       "tmnxPimNgNotifyObjsV9v0Group": tmnxPimNgNotifyObjsV9v0Group,
       "tmnxPimNgObsoletedV9v0Group": tmnxPimNgObsoletedV9v0Group,
       "tmnxPimNgMvpnV9v0Group": tmnxPimNgMvpnV9v0Group,
       "tmnxPimNgIfStatsV9v0Group": tmnxPimNgIfStatsV9v0Group,
       "tmnxPimNgIfV10v0Group": tmnxPimNgIfV10v0Group,
       "tmnxPimNgIfIPMSIV9v0Group": tmnxPimNgIfIPMSIV9v0Group,
       "tmnxPimNgMvpnV9v0R4Group": tmnxPimNgMvpnV9v0R4Group,
       "tmnxPimNgGlobalGroupV10v0": tmnxPimNgGlobalGroupV10v0,
       "tmnxPimNgIfStatsV10v0Group": tmnxPimNgIfStatsV10v0Group,
       "tmnxPimNgMvpnExtranetGroupV10v0": tmnxPimNgMvpnExtranetGroupV10v0,
       "tmnxPimNgGlobalGrpSrcV10v0Group": tmnxPimNgGlobalGrpSrcV10v0Group,
       "tmnxPimNgMVPNSndrRecvV11v0Group": tmnxPimNgMVPNSndrRecvV11v0Group,
       "tmnxPimNgFastFailover11v0Group": tmnxPimNgFastFailover11v0Group,
       "tmnxPimNgInterASMvpnV11v0Group": tmnxPimNgInterASMvpnV11v0Group,
       "tmnxPimNgCDV12v0Grp": tmnxPimNgCDV12v0Grp,
       "tmnxPimNgMvpnSrcPrefixV12v0Grp": tmnxPimNgMvpnSrcPrefixV12v0Grp,
       "tmnxPimNgSgStatcExtrntV12v0Grp": tmnxPimNgSgStatcExtrntV12v0Grp,
       "tmnxPimNgNotifyObjsV12v0Group": tmnxPimNgNotifyObjsV12v0Group,
       "tmnxPimNgIfV12v0Group": tmnxPimNgIfV12v0Group,
       "tmnxPimNgUnicastRtRemV12v0Group": tmnxPimNgUnicastRtRemV12v0Group,
       "tmnxPimNgObjs": tmnxPimNgObjs,
       "vRtrPimNgProtocolObjs": vRtrPimNgProtocolObjs,
       "vRtrPimNgGeneralTableLstChanged": vRtrPimNgGeneralTableLstChanged,
       "vRtrPimNgGeneralTable": vRtrPimNgGeneralTable,
       "vRtrPimNgGeneralEntry": vRtrPimNgGeneralEntry,
       "vRtrPimNgGenRowLastChanged": vRtrPimNgGenRowLastChanged,
       "vRtrPimNgGenAdminState": vRtrPimNgGenAdminState,
       "vRtrPimNgGenOperState": vRtrPimNgGenOperState,
       "vRtrPimNgGenCreateInterfaces": vRtrPimNgGenCreateInterfaces,
       "vRtrPimNgGenMaxMdts": vRtrPimNgGenMaxMdts,
       "vRtrPimNgGenNonDrAttractTraffic": vRtrPimNgGenNonDrAttractTraffic,
       "vRtrPimNgGenEcmpBalance": vRtrPimNgGenEcmpBalance,
       "vRtrPimNgGenEcmpBalanceHoldTime": vRtrPimNgGenEcmpBalanceHoldTime,
       "vRtrPimNgGenEcmpReBlncInProg": vRtrPimNgGenEcmpReBlncInProg,
       "vRtrPimNgGenEcmpLastReBlncTime": vRtrPimNgGenEcmpLastReBlncTime,
       "vRtrPimNgGenEcmpRebalanceType": vRtrPimNgGenEcmpRebalanceType,
       "vRtrPimNgGenEcmpOptThreshold": vRtrPimNgGenEcmpOptThreshold,
       "vRtrPimNgGenEcmpNextBalanceTime": vRtrPimNgGenEcmpNextBalanceTime,
       "vRtrPimNgGenLagUsageOptimize": vRtrPimNgGenLagUsageOptimize,
       "vRtrPimNgGenEcmpHashingEnabled": vRtrPimNgGenEcmpHashingEnabled,
       "vRtrPimNgGenEnableMdtSpt": vRtrPimNgGenEnableMdtSpt,
       "vRtrPimNgGenRpfVectorFlags": vRtrPimNgGenRpfVectorFlags,
       "vRtrPimNgAFGenTableLstChanged": vRtrPimNgAFGenTableLstChanged,
       "vRtrPimNgAFGenTable": vRtrPimNgAFGenTable,
       "vRtrPimNgAFGenEntry": vRtrPimNgAFGenEntry,
       "vRtrPimNgAFGenAFType": vRtrPimNgAFGenAFType,
       "vRtrPimNgAFGenAdminState": vRtrPimNgAFGenAdminState,
       "vRtrPimNgAFGenOperState": vRtrPimNgAFGenOperState,
       "vRtrPimNgAFGenCBSRPriority": vRtrPimNgAFGenCBSRPriority,
       "vRtrPimNgAFGenCBSRAddressType": vRtrPimNgAFGenCBSRAddressType,
       "vRtrPimNgAFGenCBSRAddress": vRtrPimNgAFGenCBSRAddress,
       "vRtrPimNgAFGenCBSRAdminState": vRtrPimNgAFGenCBSRAdminState,
       "vRtrPimNgAFGenCBSROperState": vRtrPimNgAFGenCBSROperState,
       "vRtrPimNgAFGenBSRAddressType": vRtrPimNgAFGenBSRAddressType,
       "vRtrPimNgAFGenBSRAddress": vRtrPimNgAFGenBSRAddress,
       "vRtrPimNgAFGenBSRPriority": vRtrPimNgAFGenBSRPriority,
       "vRtrPimNgAFGenBSRExpiryTime": vRtrPimNgAFGenBSRExpiryTime,
       "vRtrPimNgAFGenBSRState": vRtrPimNgAFGenBSRState,
       "vRtrPimNgAFGenBSRUpTime": vRtrPimNgAFGenBSRUpTime,
       "vRtrPimNgAFGenCRPAddressType": vRtrPimNgAFGenCRPAddressType,
       "vRtrPimNgAFGenCRPAddress": vRtrPimNgAFGenCRPAddress,
       "vRtrPimNgAFGenCRPAdminState": vRtrPimNgAFGenCRPAdminState,
       "vRtrPimNgAFGenCRPOperState": vRtrPimNgAFGenCRPOperState,
       "vRtrPimNgAFGenCRPHoldtime": vRtrPimNgAFGenCRPHoldtime,
       "vRtrPimNgAFGenCRPPriority": vRtrPimNgAFGenCRPPriority,
       "vRtrPimNgAFGenMdtDefGrpAddrType": vRtrPimNgAFGenMdtDefGrpAddrType,
       "vRtrPimNgAFGenMdtDefGrpAddress": vRtrPimNgAFGenMdtDefGrpAddress,
       "vRtrPimNgAFGenMTIfIndex": vRtrPimNgAFGenMTIfIndex,
       "vRtrPimNgAFGenCBSRHashMaskLen": vRtrPimNgAFGenCBSRHashMaskLen,
       "vRtrPimNgAFGenBSRHashMaskLen": vRtrPimNgAFGenBSRHashMaskLen,
       "vRtrPimNgAFGenBSRRpfIfIndex": vRtrPimNgAFGenBSRRpfIfIndex,
       "vRtrPimNgAFGenRpfLookupSequence": vRtrPimNgAFGenRpfLookupSequence,
       "vRtrPimNgAFGenMdtDataPrefixType": vRtrPimNgAFGenMdtDataPrefixType,
       "vRtrPimNgAFGenMdtDataPrefix": vRtrPimNgAFGenMdtDataPrefix,
       "vRtrPimNgAFGenMdtDataPrefixMask": vRtrPimNgAFGenMdtDataPrefixMask,
       "vRtrPimNgAFGenMdtDataDlayIntrvl": vRtrPimNgAFGenMdtDataDlayIntrvl,
       "vRtrPimNgAFGenMdtDataJoinTlvPck": vRtrPimNgAFGenMdtDataJoinTlvPck,
       "vRtrPimNgAFGenRowLastChanged": vRtrPimNgAFGenRowLastChanged,
       "vRtrPimNgAFGenERP": vRtrPimNgAFGenERP,
       "vRtrPimNgAFGenERPAdminState": vRtrPimNgAFGenERPAdminState,
       "vRtrPimNgAFGenMvpnAutoDiscovery": vRtrPimNgAFGenMvpnAutoDiscovery,
       "vRtrPimNgAFGenMvpnCMcastSignal": vRtrPimNgAFGenMvpnCMcastSignal,
       "vRtrPimNgAFGenMvpnGrpAddrMode": vRtrPimNgAFGenMvpnGrpAddrMode,
       "vRtrPimNgAFGenMvpnSpmsiAutoDisc": vRtrPimNgAFGenMvpnSpmsiAutoDisc,
       "vRtrPimNgAFGenMvpnUMHSelection": vRtrPimNgAFGenMvpnUMHSelection,
       "vRtrPimNgAFGenMvpnIntersiteShrd": vRtrPimNgAFGenMvpnIntersiteShrd,
       "vRtrPimNgAFGenSSMDefRangeDisabl": vRtrPimNgAFGenSSMDefRangeDisabl,
       "vRtrPimNgAFGenMvpnAD": vRtrPimNgAFGenMvpnAD,
       "vRtrPimNgAFGenMdtDataGrpAddrMode": vRtrPimNgAFGenMdtDataGrpAddrMode,
       "vRtrPimNgAFGenEnableAsmDataMdt": vRtrPimNgAFGenEnableAsmDataMdt,
       "vRtrPimNgAfGenAutoRPDiscovery": vRtrPimNgAfGenAutoRPDiscovery,
       "vRtrPimNgAfGenSSMAsrtCompMode": vRtrPimNgAfGenSSMAsrtCompMode,
       "vRtrPimNgAfGenMdtType": vRtrPimNgAfGenMdtType,
       "vRtrPimNgAfGenMcastFastFailover": vRtrPimNgAfGenMcastFastFailover,
       "vRtrPimNgAFGenSourceAddressType": vRtrPimNgAFGenSourceAddressType,
       "vRtrPimNgAFGenSourceAddress": vRtrPimNgAFGenSourceAddress,
       "vRtrPimNgAFGenGrpPrefixAny": vRtrPimNgAFGenGrpPrefixAny,
       "vRtrPimNgAfGenMvpnPersistSA": vRtrPimNgAfGenMvpnPersistSA,
       "vRtrPimNgAfGenUnicastRtRemoval": vRtrPimNgAfGenUnicastRtRemoval,
       "vRtrPimNgStaticRPTableLstChnged": vRtrPimNgStaticRPTableLstChnged,
       "vRtrPimNgStaticRPTable": vRtrPimNgStaticRPTable,
       "vRtrPimNgStaticRPEntry": vRtrPimNgStaticRPEntry,
       "vRtrPimNgStaticRPRPAddressType": vRtrPimNgStaticRPRPAddressType,
       "vRtrPimNgStaticRPRPAddress": vRtrPimNgStaticRPRPAddress,
       "vRtrPimNgStaticRPRowStatus": vRtrPimNgStaticRPRowStatus,
       "vRtrPimNgStaticRPRowLastChanged": vRtrPimNgStaticRPRowLastChanged,
       "vRtrPimNgStaticRPOverride": vRtrPimNgStaticRPOverride,
       "vRtrPimNgStGrptoRPTableLstChngd": vRtrPimNgStGrptoRPTableLstChngd,
       "vRtrPimNgStGrptoRPTable": vRtrPimNgStGrptoRPTable,
       "vRtrPimNgStGrpToRPEntry": vRtrPimNgStGrpToRPEntry,
       "vRtrPimNgStGrptoRPRPAddrType": vRtrPimNgStGrptoRPRPAddrType,
       "vRtrPimNgStGrptoRPRPAddress": vRtrPimNgStGrptoRPRPAddress,
       "vRtrPimNgStaticGroupAddrType": vRtrPimNgStaticGroupAddrType,
       "vRtrPimNgStaticGroupAddr": vRtrPimNgStaticGroupAddr,
       "vRtrPimNgStaticGroupMask": vRtrPimNgStaticGroupMask,
       "vRtrPimNgStGrpToRPRowStatus": vRtrPimNgStGrpToRPRowStatus,
       "vRtrPimNgStGrpToRPRowLstChanged": vRtrPimNgStGrpToRPRowLstChanged,
       "vRtrPimNgGrpSrcTable": vRtrPimNgGrpSrcTable,
       "vRtrPimNgGrpSrcEntry": vRtrPimNgGrpSrcEntry,
       "vRtrPimNgGrpSrcGrpAddrType": vRtrPimNgGrpSrcGrpAddrType,
       "vRtrPimNgGrpSrcGroupAddress": vRtrPimNgGrpSrcGroupAddress,
       "vRtrPimNgGrpSrcSrcAddrType": vRtrPimNgGrpSrcSrcAddrType,
       "vRtrPimNgGrpSrcSourceAddress": vRtrPimNgGrpSrcSourceAddress,
       "vRtrPimNgGrpSrcType": vRtrPimNgGrpSrcType,
       "vRtrPimNgGrpSrcRPAddrType": vRtrPimNgGrpSrcRPAddrType,
       "vRtrPimNgGrpSrcRPAddr": vRtrPimNgGrpSrcRPAddr,
       "vRtrPimNgGrpSrcRpfNbrAddrType": vRtrPimNgGrpSrcRpfNbrAddrType,
       "vRtrPimNgGrpSrcRpfNbrAddr": vRtrPimNgGrpSrcRpfNbrAddr,
       "vRtrPimNgGrpSrcRpfIfIndex": vRtrPimNgGrpSrcRpfIfIndex,
       "vRtrPimNgGrpSrcRptRpfNbrAdrType": vRtrPimNgGrpSrcRptRpfNbrAdrType,
       "vRtrPimNgGrpSrcRptRpfNbrAddr": vRtrPimNgGrpSrcRptRpfNbrAddr,
       "vRtrPimNgGrpSrcMRIBNHopAddrType": vRtrPimNgGrpSrcMRIBNHopAddrType,
       "vRtrPimNgGrpSrcMRIBNextHopAddr": vRtrPimNgGrpSrcMRIBNextHopAddr,
       "vRtrPimNgGrpSrcMRIBSrcFlags": vRtrPimNgGrpSrcMRIBSrcFlags,
       "vRtrPimNgGrpSrcFlags": vRtrPimNgGrpSrcFlags,
       "vRtrPimNgGrpSrcUpstreamJpState": vRtrPimNgGrpSrcUpstreamJpState,
       "vRtrPimNgGrpSrcUpstreamJpTimer": vRtrPimNgGrpSrcUpstreamJpTimer,
       "vRtrPimNgGrpSrcUstrmRptJpState": vRtrPimNgGrpSrcUstrmRptJpState,
       "vRtrPimNgGrpSrcUstrmRptOvrdeTmr": vRtrPimNgGrpSrcUstrmRptOvrdeTmr,
       "vRtrPimNgGrpSrcRegisterState": vRtrPimNgGrpSrcRegisterState,
       "vRtrPimNgGrpSrcRegisterStopTmr": vRtrPimNgGrpSrcRegisterStopTmr,
       "vRtrPimNgGrpSrcKeepaliveTimer": vRtrPimNgGrpSrcKeepaliveTimer,
       "vRtrPimNgGrpSrcNumImmediateOif": vRtrPimNgGrpSrcNumImmediateOif,
       "vRtrPimNgGrpSrcNumInheritedOif": vRtrPimNgGrpSrcNumInheritedOif,
       "vRtrPimNgGrpSrcNumInherRptOif": vRtrPimNgGrpSrcNumInherRptOif,
       "vRtrPimNgGrpSrcNumLclRxInclIf": vRtrPimNgGrpSrcNumLclRxInclIf,
       "vRtrPimNgGrpSrcNumLclRxExclIf": vRtrPimNgGrpSrcNumLclRxExclIf,
       "vRtrPimNgGrpSrcNumJoinPruneIf": vRtrPimNgGrpSrcNumJoinPruneIf,
       "vRtrPimNgGrpSrcNumLostAssertIf": vRtrPimNgGrpSrcNumLostAssertIf,
       "vRtrPimNgGrpSrcUpTime": vRtrPimNgGrpSrcUpTime,
       "vRtrPimNgGrpSrcNumSGRptPruneOif": vRtrPimNgGrpSrcNumSGRptPruneOif,
       "vRtrPimNgGrpSrcRxRegFrmAnycstRP": vRtrPimNgGrpSrcRxRegFrmAnycstRP,
       "vRtrPimNgGrpSrcRslvdByRtTblType": vRtrPimNgGrpSrcRslvdByRtTblType,
       "vRtrPimNgGrpSrcCurrFwdingRate": vRtrPimNgGrpSrcCurrFwdingRate,
       "vRtrPimNgGrpSrcCurrFwdingOFRate": vRtrPimNgGrpSrcCurrFwdingOFRate,
       "vRtrPimNgGrpSrcCurrFwdingHCRate": vRtrPimNgGrpSrcCurrFwdingHCRate,
       "vRtrPimNgGrpSrcGrpSptThreshold": vRtrPimNgGrpSrcGrpSptThreshold,
       "vRtrPimNgGrpSrcGrpAdminBw": vRtrPimNgGrpSrcGrpAdminBw,
       "vRtrPimNgGrpSrcGrpEcmpOptThresh": vRtrPimNgGrpSrcGrpEcmpOptThresh,
       "vRtrPimNgGrpSrcSpmsiRpfIfIndex": vRtrPimNgGrpSrcSpmsiRpfIfIndex,
       "vRtrPimNgGrpSrcRpfSecNbrAddrTyp": vRtrPimNgGrpSrcRpfSecNbrAddrTyp,
       "vRtrPimNgGrpSrcRpfSecNbrAddr": vRtrPimNgGrpSrcRpfSecNbrAddr,
       "vRtrPimNgGrpSrcRpfSecIfIndex": vRtrPimNgGrpSrcRpfSecIfIndex,
       "vRtrPimNgGrpSrcAdvtAddrType": vRtrPimNgGrpSrcAdvtAddrType,
       "vRtrPimNgGrpSrcAdvtAddr": vRtrPimNgGrpSrcAdvtAddr,
       "vRtrPimNgGrpSrcStdbyMRIBSrcFlags": vRtrPimNgGrpSrcStdbyMRIBSrcFlags,
       "vRtrPimNgGrpSrcStdbyUpJpState": vRtrPimNgGrpSrcStdbyUpJpState,
       "vRtrPimNgGrpSrcStdbyUpJpTimer": vRtrPimNgGrpSrcStdbyUpJpTimer,
       "vRtrPimNgGrpSrcDSRpfvNbrType": vRtrPimNgGrpSrcDSRpfvNbrType,
       "vRtrPimNgGrpSrcDSRpfvNbr": vRtrPimNgGrpSrcDSRpfvNbr,
       "vRtrPimNgGrpSrcDSRpfvProxyType": vRtrPimNgGrpSrcDSRpfvProxyType,
       "vRtrPimNgGrpSrcDSRpfvProxy": vRtrPimNgGrpSrcDSRpfvProxy,
       "vRtrPimNgGrpSrcDSRpfvRD": vRtrPimNgGrpSrcDSRpfvRD,
       "vRtrPimNgGrpSrcDSRpfvType": vRtrPimNgGrpSrcDSRpfvType,
       "vRtrPimNgGrpSrcUPRpfvNbrType": vRtrPimNgGrpSrcUPRpfvNbrType,
       "vRtrPimNgGrpSrcUPRpfvNbr": vRtrPimNgGrpSrcUPRpfvNbr,
       "vRtrPimNgGrpSrcUPRpfvProxyType": vRtrPimNgGrpSrcUPRpfvProxyType,
       "vRtrPimNgGrpSrcUPRpfvProxy": vRtrPimNgGrpSrcUPRpfvProxy,
       "vRtrPimNgGrpSrcUPRpfvRD": vRtrPimNgGrpSrcUPRpfvRD,
       "vRtrPimNgGrpSrcUPRpfvType": vRtrPimNgGrpSrcUPRpfvType,
       "vRtrPimNgGrpSrcRpfvFlags": vRtrPimNgGrpSrcRpfvFlags,
       "vRtrPimNgGrpSrcState": vRtrPimNgGrpSrcState,
       "vRtrPimNgGrpSrcIfTable": vRtrPimNgGrpSrcIfTable,
       "vRtrPimNgGrpSrcIfEntry": vRtrPimNgGrpSrcIfEntry,
       "vRtrPimNgGrpSrcIfFlags": vRtrPimNgGrpSrcIfFlags,
       "vRtrPimNgGrpSrcSpmsiIfIndex": vRtrPimNgGrpSrcSpmsiIfIndex,
       "vRtrPimNgCRPGrpPrfxTblLstChnged": vRtrPimNgCRPGrpPrfxTblLstChnged,
       "vRtrPimNgCRPGrpPrefixTable": vRtrPimNgCRPGrpPrefixTable,
       "vRtrPimNgCRPGrpPrefixEntry": vRtrPimNgCRPGrpPrefixEntry,
       "vRtrPimNgCRPGrpPrfixGrpAddrType": vRtrPimNgCRPGrpPrfixGrpAddrType,
       "vRtrPimNgCRPGrpPrefixGrpAddr": vRtrPimNgCRPGrpPrefixGrpAddr,
       "vRtrPimNgCRPGrpPrefixGrpMask": vRtrPimNgCRPGrpPrefixGrpMask,
       "vRtrPimNgCRPGrpPrefixRowStatus": vRtrPimNgCRPGrpPrefixRowStatus,
       "vRtrPimNgCRPGrpPrfixRowLstChngd": vRtrPimNgCRPGrpPrfixRowLstChngd,
       "vRtrPimNgCRPTable": vRtrPimNgCRPTable,
       "vRtrPimNgCRPEntry": vRtrPimNgCRPEntry,
       "vRtrPimNgCRPAddressType": vRtrPimNgCRPAddressType,
       "vRtrPimNgCRPAddress": vRtrPimNgCRPAddress,
       "vRtrPimNgCRPGrpAddrType": vRtrPimNgCRPGrpAddrType,
       "vRtrPimNgCRPGrpAddr": vRtrPimNgCRPGrpAddr,
       "vRtrPimNgCRPGrpMask": vRtrPimNgCRPGrpMask,
       "vRtrPimNgCRPHoldtime": vRtrPimNgCRPHoldtime,
       "vRtrPimNgCRPPriority": vRtrPimNgCRPPriority,
       "vRtrPimNgCRPExpiryTime": vRtrPimNgCRPExpiryTime,
       "vRtrPimNgRPSetTable": vRtrPimNgRPSetTable,
       "vRtrPimNgRPSetEntry": vRtrPimNgRPSetEntry,
       "vRtrPimNgRPSetType": vRtrPimNgRPSetType,
       "vRtrPimNgRPSetGrpAddrType": vRtrPimNgRPSetGrpAddrType,
       "vRtrPimNgRPSetGrpAddr": vRtrPimNgRPSetGrpAddr,
       "vRtrPimNgRPSetGrpMask": vRtrPimNgRPSetGrpMask,
       "vRtrPimNgRPSetCRPAddrType": vRtrPimNgRPSetCRPAddrType,
       "vRtrPimNgRPSetCRPAddress": vRtrPimNgRPSetCRPAddress,
       "vRtrPimNgRPSetHoldtime": vRtrPimNgRPSetHoldtime,
       "vRtrPimNgRPSetPriority": vRtrPimNgRPSetPriority,
       "vRtrPimNgRPSetExpiryTime": vRtrPimNgRPSetExpiryTime,
       "vRtrPimNgGenStatTable": vRtrPimNgGenStatTable,
       "vRtrPimNgGenStatEntry": vRtrPimNgGenStatEntry,
       "vRtrPimNgGenStatTxCrpaPdus": vRtrPimNgGenStatTxCrpaPdus,
       "vRtrPimNgGenStatTxCrpaPduErrs": vRtrPimNgGenStatTxCrpaPduErrs,
       "vRtrPimNgGenStatRxCrpaPdus": vRtrPimNgGenStatRxCrpaPdus,
       "vRtrPimNgGenStatRxCrpaPduDrops": vRtrPimNgGenStatRxCrpaPduDrops,
       "vRtrPimNgGenStatStarStarRPTypes": vRtrPimNgGenStatStarStarRPTypes,
       "vRtrPimNgGenStatStarGTypes": vRtrPimNgGenStatStarGTypes,
       "vRtrPimNgGenStatSGTypes": vRtrPimNgGenStatSGTypes,
       "vRtrPimNgGenStatTxRegisters": vRtrPimNgGenStatTxRegisters,
       "vRtrPimNgGenStatTxRegisterErrs": vRtrPimNgGenStatTxRegisterErrs,
       "vRtrPimNgGenStatTxNullRegisters": vRtrPimNgGenStatTxNullRegisters,
       "vRtrPimNgGenStatTxRegTTLDrops": vRtrPimNgGenStatTxRegTTLDrops,
       "vRtrPimNgGenStatForwardCrpaPdus": vRtrPimNgGenStatForwardCrpaPdus,
       "vRtrPimNgGenStatFwdCrpaDrops": vRtrPimNgGenStatFwdCrpaDrops,
       "vRtrPimNgGenStatTxMdtJoinTlvs": vRtrPimNgGenStatTxMdtJoinTlvs,
       "vRtrPimNgGenStatRxMdtJoinTlvs": vRtrPimNgGenStatRxMdtJoinTlvs,
       "vRtrPimNgGenStatTxMdtJnTlvErrs": vRtrPimNgGenStatTxMdtJnTlvErrs,
       "vRtrPimNgGenStatRxMdtJnTlvErrs": vRtrPimNgGenStatRxMdtJnTlvErrs,
       "vRtrPimNgGenStatTxActiveMdts": vRtrPimNgGenStatTxActiveMdts,
       "vRtrPimNgGenStatRxActiveMdts": vRtrPimNgGenStatRxActiveMdts,
       "vRtrPimNgGenStatTxSpmsiLimitHits": vRtrPimNgGenStatTxSpmsiLimitHits,
       "vRtrPimNgGenStatRxCtrlPduIfDrops": vRtrPimNgGenStatRxCtrlPduIfDrops,
       "vRtrPimNgGenStatP2mpPmsiReqFails": vRtrPimNgGenStatP2mpPmsiReqFails,
       "vRtrPimNgGenStatP2mpPmsiCrtFails": vRtrPimNgGenStatP2mpPmsiCrtFails,
       "vRtrPimNgGenStatTxMdts": vRtrPimNgGenStatTxMdts,
       "vRtrPimNgGenStatRxMdts": vRtrPimNgGenStatRxMdts,
       "vRtrPimNgGrpSrcStatTable": vRtrPimNgGrpSrcStatTable,
       "vRtrPimNgGrpSrcStatEntry": vRtrPimNgGrpSrcStatEntry,
       "vRtrPimNgGrpSrcStatFrwdedPkts": vRtrPimNgGrpSrcStatFrwdedPkts,
       "vRtrPimNgGrpSrcStatOFFrwdedPkts": vRtrPimNgGrpSrcStatOFFrwdedPkts,
       "vRtrPimNgGrpSrcStatHCFrwdedPkts": vRtrPimNgGrpSrcStatHCFrwdedPkts,
       "vRtrPimNgGrpSrcStatDscrdPkts": vRtrPimNgGrpSrcStatDscrdPkts,
       "vRtrPimNgGrpSrcStatOFDscrdPkts": vRtrPimNgGrpSrcStatOFDscrdPkts,
       "vRtrPimNgGrpSrcStatHCDscrdPkts": vRtrPimNgGrpSrcStatHCDscrdPkts,
       "vRtrPimNgGrpSrcStatRPFMsmtch": vRtrPimNgGrpSrcStatRPFMsmtch,
       "vRtrPimNgGrpSrcStatOFRPFMsmtch": vRtrPimNgGrpSrcStatOFRPFMsmtch,
       "vRtrPimNgGrpSrcStatHCRPFMsmtch": vRtrPimNgGrpSrcStatHCRPFMsmtch,
       "vRtrPimNgGrpSrcStatFrdedOct": vRtrPimNgGrpSrcStatFrdedOct,
       "vRtrPimNgGrpSrcStatOFFrdedOct": vRtrPimNgGrpSrcStatOFFrdedOct,
       "vRtrPimNgGrpSrcStatHCFrdedOct": vRtrPimNgGrpSrcStatHCFrdedOct,
       "vRtrPimNgGenPolicyTable": vRtrPimNgGenPolicyTable,
       "vRtrPimNgGenPolicyEntry": vRtrPimNgGenPolicyEntry,
       "vRtrPimNgImportJoinPrunePolicy1": vRtrPimNgImportJoinPrunePolicy1,
       "vRtrPimNgImportJoinPrunePolicy2": vRtrPimNgImportJoinPrunePolicy2,
       "vRtrPimNgImportJoinPrunePolicy3": vRtrPimNgImportJoinPrunePolicy3,
       "vRtrPimNgImportJoinPrunePolicy4": vRtrPimNgImportJoinPrunePolicy4,
       "vRtrPimNgImportJoinPrunePolicy5": vRtrPimNgImportJoinPrunePolicy5,
       "vRtrPimNgImportRegisterPolicy1": vRtrPimNgImportRegisterPolicy1,
       "vRtrPimNgImportRegisterPolicy2": vRtrPimNgImportRegisterPolicy2,
       "vRtrPimNgImportRegisterPolicy3": vRtrPimNgImportRegisterPolicy3,
       "vRtrPimNgImportRegisterPolicy4": vRtrPimNgImportRegisterPolicy4,
       "vRtrPimNgImportRegisterPolicy5": vRtrPimNgImportRegisterPolicy5,
       "vRtrPimNgImportBootstrapPolicy1": vRtrPimNgImportBootstrapPolicy1,
       "vRtrPimNgImportBootstrapPolicy2": vRtrPimNgImportBootstrapPolicy2,
       "vRtrPimNgImportBootstrapPolicy3": vRtrPimNgImportBootstrapPolicy3,
       "vRtrPimNgImportBootstrapPolicy4": vRtrPimNgImportBootstrapPolicy4,
       "vRtrPimNgImportBootstrapPolicy5": vRtrPimNgImportBootstrapPolicy5,
       "vRtrPimNgExportBootstrapPolicy1": vRtrPimNgExportBootstrapPolicy1,
       "vRtrPimNgExportBootstrapPolicy2": vRtrPimNgExportBootstrapPolicy2,
       "vRtrPimNgExportBootstrapPolicy3": vRtrPimNgExportBootstrapPolicy3,
       "vRtrPimNgExportBootstrapPolicy4": vRtrPimNgExportBootstrapPolicy4,
       "vRtrPimNgExportBootstrapPolicy5": vRtrPimNgExportBootstrapPolicy5,
       "vRtrPimNgSSMGroupTableLstChngd": vRtrPimNgSSMGroupTableLstChngd,
       "vRtrPimNgSSMGroupTable": vRtrPimNgSSMGroupTable,
       "vRtrPimNgSSMGroupEntry": vRtrPimNgSSMGroupEntry,
       "vRtrPimNgSSMGroupAddressType": vRtrPimNgSSMGroupAddressType,
       "vRtrPimNgSSMGroupAddress": vRtrPimNgSSMGroupAddress,
       "vRtrPimNgSSMGroupMask": vRtrPimNgSSMGroupMask,
       "vRtrPimNgSSMGroupRowStatus": vRtrPimNgSSMGroupRowStatus,
       "vRtrPimNgSSMGroupRowLastChanged": vRtrPimNgSSMGroupRowLastChanged,
       "vRtrPimNgAnycastRPTableLstChngd": vRtrPimNgAnycastRPTableLstChngd,
       "vRtrPimNgAnycastRPTable": vRtrPimNgAnycastRPTable,
       "vRtrPimNgAnycastRPEntry": vRtrPimNgAnycastRPEntry,
       "vRtrPimNgAnycastRPAddressType": vRtrPimNgAnycastRPAddressType,
       "vRtrPimNgAnycastRPAddress": vRtrPimNgAnycastRPAddress,
       "vRtrPimNgAnycastRPPeerAddrType": vRtrPimNgAnycastRPPeerAddrType,
       "vRtrPimNgAnycastRPPeerAddress": vRtrPimNgAnycastRPPeerAddress,
       "vRtrPimNgAnycastRPRowStatus": vRtrPimNgAnycastRPRowStatus,
       "vRtrPimNgAnycastRPRowLstChanged": vRtrPimNgAnycastRPRowLstChanged,
       "vRtrPimNgSptSwOvrThdTabLstChngd": vRtrPimNgSptSwOvrThdTabLstChngd,
       "vRtrPimNgSptSwitchoverThdTable": vRtrPimNgSptSwitchoverThdTable,
       "vRtrPimNgSptSwitchoverThdEntry": vRtrPimNgSptSwitchoverThdEntry,
       "vRtrPimNgSptSwOvrThdTblGpAdType": vRtrPimNgSptSwOvrThdTblGpAdType,
       "vRtrPimNgSptSwOvrThdTblGrpAddr": vRtrPimNgSptSwOvrThdTblGrpAddr,
       "vRtrPimNgSptSwOvrThdTblGpAdMask": vRtrPimNgSptSwOvrThdTblGpAdMask,
       "vRtrPimNgSptSwovrThdRowStatus": vRtrPimNgSptSwovrThdRowStatus,
       "vRtrPimNgSptSwovrThdRowLstChngd": vRtrPimNgSptSwovrThdRowLstChngd,
       "vRtrPimNgSptSwitchoverThd": vRtrPimNgSptSwitchoverThd,
       "vRtrPimNgDataMtThdTableLstChngd": vRtrPimNgDataMtThdTableLstChngd,
       "vRtrPimNgDataMtThdTable": vRtrPimNgDataMtThdTable,
       "vRtrPimNgDataMtThdEntry": vRtrPimNgDataMtThdEntry,
       "vRtrPimNgDataMtThdTblGrpAdrType": vRtrPimNgDataMtThdTblGrpAdrType,
       "vRtrPimNgDataMtThdTblGrpAddr": vRtrPimNgDataMtThdTblGrpAddr,
       "vRtrPimNgDataMtThdTblGrpAdrMask": vRtrPimNgDataMtThdTblGrpAdrMask,
       "vRtrPimNgDataMtThdRowStatus": vRtrPimNgDataMtThdRowStatus,
       "vRtrPimNgDataMtThdRowLstChngd": vRtrPimNgDataMtThdRowLstChngd,
       "vRtrPimNgDataMtThd": vRtrPimNgDataMtThd,
       "vRtrPimNgIfMcacLevelTblLstChngd": vRtrPimNgIfMcacLevelTblLstChngd,
       "vRtrPimNgIfMcacLevelTable": vRtrPimNgIfMcacLevelTable,
       "vRtrPimNgIfMcacLevelEntry": vRtrPimNgIfMcacLevelEntry,
       "vRtrPimNgIfMcacLevelRowStatus": vRtrPimNgIfMcacLevelRowStatus,
       "vRtrPimNgIfMcacLvlRowLstChngd": vRtrPimNgIfMcacLvlRowLstChngd,
       "vRtrPimNgIfMcacLevelBW": vRtrPimNgIfMcacLevelBW,
       "vRtrPimNgIfMcacLagTableLstChngd": vRtrPimNgIfMcacLagTableLstChngd,
       "vRtrPimNgIfMcacLagTable": vRtrPimNgIfMcacLagTable,
       "vRtrPimNgIfMcacLagEntry": vRtrPimNgIfMcacLagEntry,
       "vRtrPimNgIfMcacLagRowStatus": vRtrPimNgIfMcacLagRowStatus,
       "vRtrPimNgIfMcacLagRowLstChngd": vRtrPimNgIfMcacLagRowLstChngd,
       "vRtrPimNgIfMcacLagLevel": vRtrPimNgIfMcacLagLevel,
       "vRtrPimNgERPGrpPrfxTblLstChnged": vRtrPimNgERPGrpPrfxTblLstChnged,
       "vRtrPimNgERPGrpPrefixTable": vRtrPimNgERPGrpPrefixTable,
       "vRtrPimNgERPGrpPrefixEntry": vRtrPimNgERPGrpPrefixEntry,
       "vRtrPimNgERPGrpPrfixGrpAddrType": vRtrPimNgERPGrpPrfixGrpAddrType,
       "vRtrPimNgERPGrpPrefixGrpAddr": vRtrPimNgERPGrpPrefixGrpAddr,
       "vRtrPimNgERPGrpPrefixGrpMask": vRtrPimNgERPGrpPrefixGrpMask,
       "vRtrPimNgERPGrpPrefixRowStatus": vRtrPimNgERPGrpPrefixRowStatus,
       "vRtrPimNgRsvpIfTable": vRtrPimNgRsvpIfTable,
       "vRtrPimNgRsvpIfEntry": vRtrPimNgRsvpIfEntry,
       "vRtrPimNgRsvpIfLspName": vRtrPimNgRsvpIfLspName,
       "vRtrPimNgRsvpIfSenderAddrType": vRtrPimNgRsvpIfSenderAddrType,
       "vRtrPimNgRsvpIfSenderAddr": vRtrPimNgRsvpIfSenderAddr,
       "vRtrPimNgRsvpIfRowStatus": vRtrPimNgRsvpIfRowStatus,
       "vRtrPimNgRsvpIfOperState": vRtrPimNgRsvpIfOperState,
       "vRtrPimNgRsvpIfIndex": vRtrPimNgRsvpIfIndex,
       "vRtrPimNgCRPGpPfxInetTblLstChngd": vRtrPimNgCRPGpPfxInetTblLstChngd,
       "vRtrPimNgCRPGrpPrefixInetTable": vRtrPimNgCRPGrpPrefixInetTable,
       "vRtrPimNgCRPGrpPrefixInetEntry": vRtrPimNgCRPGrpPrefixInetEntry,
       "vRtrPimNgCRPGrpPfxInetGrpAdrType": vRtrPimNgCRPGrpPfxInetGrpAdrType,
       "vRtrPimNgCRPGrpPrefixInetGrpAddr": vRtrPimNgCRPGrpPrefixInetGrpAddr,
       "vRtrPimNgCRPGrpPrefixInetGrpMask": vRtrPimNgCRPGrpPrefixInetGrpMask,
       "vRtrPimNgCRPGrpPrfxInetRowStatus": vRtrPimNgCRPGrpPrfxInetRowStatus,
       "vRtrPimNgCRPGrpPfxInetRowLstChgd": vRtrPimNgCRPGrpPfxInetRowLstChgd,
       "vRtrPimNgCRPInetTable": vRtrPimNgCRPInetTable,
       "vRtrPimNgCRPInetEntry": vRtrPimNgCRPInetEntry,
       "vRtrPimNgCRPInetAddressType": vRtrPimNgCRPInetAddressType,
       "vRtrPimNgCRPInetAddress": vRtrPimNgCRPInetAddress,
       "vRtrPimNgCRPInetGrpAddrType": vRtrPimNgCRPInetGrpAddrType,
       "vRtrPimNgCRPInetGrpAddr": vRtrPimNgCRPInetGrpAddr,
       "vRtrPimNgCRPInetGrpMask": vRtrPimNgCRPInetGrpMask,
       "vRtrPimNgCRPInetHoldtime": vRtrPimNgCRPInetHoldtime,
       "vRtrPimNgCRPInetPriority": vRtrPimNgCRPInetPriority,
       "vRtrPimNgCRPInetExpiryTime": vRtrPimNgCRPInetExpiryTime,
       "vRtrPimNgRPSetInetTable": vRtrPimNgRPSetInetTable,
       "vRtrPimNgRPSetInetEntry": vRtrPimNgRPSetInetEntry,
       "vRtrPimNgRPSetInetType": vRtrPimNgRPSetInetType,
       "vRtrPimNgRPSetInetGrpAddrType": vRtrPimNgRPSetInetGrpAddrType,
       "vRtrPimNgRPSetInetGrpAddr": vRtrPimNgRPSetInetGrpAddr,
       "vRtrPimNgRPSetInetGrpMask": vRtrPimNgRPSetInetGrpMask,
       "vRtrPimNgRPSetInetCRPAddrType": vRtrPimNgRPSetInetCRPAddrType,
       "vRtrPimNgRPSetInetCRPAddress": vRtrPimNgRPSetInetCRPAddress,
       "vRtrPimNgRPSetInetHoldtime": vRtrPimNgRPSetInetHoldtime,
       "vRtrPimNgRPSetInetPriority": vRtrPimNgRPSetInetPriority,
       "vRtrPimNgRPSetInetExpiryTime": vRtrPimNgRPSetInetExpiryTime,
       "vRtrPimNgGrpSrcHostTable": vRtrPimNgGrpSrcHostTable,
       "vRtrPimNgGrpSrcHostEntry": vRtrPimNgGrpSrcHostEntry,
       "vRtrPimNgGrpSrcHostAddrType": vRtrPimNgGrpSrcHostAddrType,
       "vRtrPimNgGrpSrcHostAddress": vRtrPimNgGrpSrcHostAddress,
       "vRtrPimNgGrpSrcHostFlags": vRtrPimNgGrpSrcHostFlags,
       "vRtrPimNgGrpSrcGrpIfTable": vRtrPimNgGrpSrcGrpIfTable,
       "vRtrPimNgGrpSrcGrpIfEntry": vRtrPimNgGrpSrcGrpIfEntry,
       "vRtrPimNgGrpSrcGrpIfFwdSvcId": vRtrPimNgGrpSrcGrpIfFwdSvcId,
       "vRtrPimNgGrpSrcGrpIfIndex": vRtrPimNgGrpSrcGrpIfIndex,
       "vRtrPimNgGrpSrcGrpIfFlags": vRtrPimNgGrpSrcGrpIfFlags,
       "vRtrPimNgMvpnUMHPETblLastChg": vRtrPimNgMvpnUMHPETblLastChg,
       "vRtrPimNgMvpnUMHPETable": vRtrPimNgMvpnUMHPETable,
       "vRtrPimNgMvpnUMHPEEntry": vRtrPimNgMvpnUMHPEEntry,
       "vRtrPimNgMvpnUMHPEAddrType": vRtrPimNgMvpnUMHPEAddrType,
       "vRtrPimNgMvpnUMHPEAddr": vRtrPimNgMvpnUMHPEAddr,
       "vRtrPimNgMvpnUMHPERowStatus": vRtrPimNgMvpnUMHPERowStatus,
       "vRtrPimNgMvpnUMHPELastChanged": vRtrPimNgMvpnUMHPELastChanged,
       "vRtrPimNgMvpnUMHPEStandbyAdrTyp": vRtrPimNgMvpnUMHPEStandbyAdrTyp,
       "vRtrPimNgMvpnUMHPEStandbyAddr": vRtrPimNgMvpnUMHPEStandbyAddr,
       "vRtrPimNgMvpnSrcPrefixTblLstChg": vRtrPimNgMvpnSrcPrefixTblLstChg,
       "vRtrPimNgMvpnSrcPrefixTable": vRtrPimNgMvpnSrcPrefixTable,
       "vRtrPimNgMvpnSrcPrefixEntry": vRtrPimNgMvpnSrcPrefixEntry,
       "vRtrPimNgMvpnSrcPrefixType": vRtrPimNgMvpnSrcPrefixType,
       "vRtrPimNgMvpnSrcPrefixAddr": vRtrPimNgMvpnSrcPrefixAddr,
       "vRtrPimNgMvpnSrcPrefixLen": vRtrPimNgMvpnSrcPrefixLen,
       "vRtrPimNgMvpnSrcPrefixRowStatus": vRtrPimNgMvpnSrcPrefixRowStatus,
       "vRtrPimNgMvpnSrcPrefixRowLastChg": vRtrPimNgMvpnSrcPrefixRowLastChg,
       "vRtrPimNgExtranetCDTblLstChg": vRtrPimNgExtranetCDTblLstChg,
       "vRtrPimNgExtranetCDTable": vRtrPimNgExtranetCDTable,
       "vRtrPimNgExtranetCDEntry": vRtrPimNgExtranetCDEntry,
       "vRtrPimNgExtranetCDGrpPfxType": vRtrPimNgExtranetCDGrpPfxType,
       "vRtrPimNgExtranetCDGrpPfxAddr": vRtrPimNgExtranetCDGrpPfxAddr,
       "vRtrPimNgExtranetCDGrpPfxLen": vRtrPimNgExtranetCDGrpPfxLen,
       "vRtrPimNgExtranetCDMvpnId": vRtrPimNgExtranetCDMvpnId,
       "vRtrPimNgExtranetCDRowStatus": vRtrPimNgExtranetCDRowStatus,
       "vRtrPimNgExtranetCDRowLstChg": vRtrPimNgExtranetCDRowLstChg,
       "vRtrPimNgIfObjs": vRtrPimNgIfObjs,
       "vRtrPimNgIfTableLastChanged": vRtrPimNgIfTableLastChanged,
       "vRtrPimNgIfTable": vRtrPimNgIfTable,
       "vRtrPimNgIfEntry": vRtrPimNgIfEntry,
       "vRtrPimNgIfRowStatus": vRtrPimNgIfRowStatus,
       "vRtrPimNgIfLastChangeTime": vRtrPimNgIfLastChangeTime,
       "vRtrPimNgIfAdminState": vRtrPimNgIfAdminState,
       "vRtrPimNgIfOperState": vRtrPimNgIfOperState,
       "vRtrPimNgIfHelloInterval": vRtrPimNgIfHelloInterval,
       "vRtrPimNgIfTrackingSupport": vRtrPimNgIfTrackingSupport,
       "vRtrPimNgIfMulticastSenders": vRtrPimNgIfMulticastSenders,
       "vRtrPimNgIfAutoCreated": vRtrPimNgIfAutoCreated,
       "vRtrPimNgIfBSMCheckRouterAlert": vRtrPimNgIfBSMCheckRouterAlert,
       "vRtrPimNgIfHelloMultiplier": vRtrPimNgIfHelloMultiplier,
       "vRtrPimNgIfImprovedAssert": vRtrPimNgIfImprovedAssert,
       "vRtrPimNgIfStickyDR": vRtrPimNgIfStickyDR,
       "vRtrPimNgIfStickyDRPriority": vRtrPimNgIfStickyDRPriority,
       "vRtrPimNgIfMaxGroups": vRtrPimNgIfMaxGroups,
       "vRtrPimNgIfEnableBfd": vRtrPimNgIfEnableBfd,
       "vRtrPimNgIfThreeWayHello": vRtrPimNgIfThreeWayHello,
       "vRtrPimNgIfMcacPolicyName": vRtrPimNgIfMcacPolicyName,
       "vRtrPimNgIfMcacUnconstrainedBW": vRtrPimNgIfMcacUnconstrainedBW,
       "vRtrPimNgIfMcacConstAdminState": vRtrPimNgIfMcacConstAdminState,
       "vRtrPimNgIfMcacPreRsvdMandBW": vRtrPimNgIfMcacPreRsvdMandBW,
       "vRtrPimNgIfMcacinUseMandBw": vRtrPimNgIfMcacinUseMandBw,
       "vRtrPimNgIfMcacinUseOpnlBw": vRtrPimNgIfMcacinUseOpnlBw,
       "vRtrPimNgIfMcacAvailMandBw": vRtrPimNgIfMcacAvailMandBw,
       "vRtrPimNgIfMcacAvailOpnlBw": vRtrPimNgIfMcacAvailOpnlBw,
       "vRtrPimNgIfMcacValuesInTransit": vRtrPimNgIfMcacValuesInTransit,
       "vRtrPimNgIfDRPriority": vRtrPimNgIfDRPriority,
       "vRtrPimNgIfAssertPeriod": vRtrPimNgIfAssertPeriod,
       "vRtrPimNgIfInstantPruneEcho": vRtrPimNgIfInstantPruneEcho,
       "vRtrPimNgIfIpv6EnableBfd": vRtrPimNgIfIpv6EnableBfd,
       "vRtrPimNgIfP2mpLdpTreeJoin": vRtrPimNgIfP2mpLdpTreeJoin,
       "vRtrPimNgIfExtranetType": vRtrPimNgIfExtranetType,
       "vRtrPimNgIfExtranetMvpnId": vRtrPimNgIfExtranetMvpnId,
       "vRtrPimNgIfMcacUseLagPortWeight": vRtrPimNgIfMcacUseLagPortWeight,
       "vRtrPimNgAFIfTable": vRtrPimNgAFIfTable,
       "vRtrPimNgAFIfEntry": vRtrPimNgAFIfEntry,
       "vRtrPimNgAFIfAFType": vRtrPimNgAFIfAFType,
       "vRtrPimNgAFIfAdminState": vRtrPimNgAFIfAdminState,
       "vRtrPimNgAFIfOperState": vRtrPimNgAFIfOperState,
       "vRtrPimNgAFIfMdtDefGrpAddrType": vRtrPimNgAFIfMdtDefGrpAddrType,
       "vRtrPimNgAFIfMdtDefGrpAddress": vRtrPimNgAFIfMdtDefGrpAddress,
       "vRtrPimNgAFIfNextHelloTime": vRtrPimNgAFIfNextHelloTime,
       "vRtrPimNgAFIfOperDRPriority": vRtrPimNgAFIfOperDRPriority,
       "vRtrPimNgAFIfCurrentGroups": vRtrPimNgAFIfCurrentGroups,
       "vRtrPimNgAFIfMaxGroupsTillNow": vRtrPimNgAFIfMaxGroupsTillNow,
       "vRtrPimNgAFIfDRType": vRtrPimNgAFIfDRType,
       "vRtrPimNgAFIfDR": vRtrPimNgAFIfDR,
       "vRtrPimNgAFIfTrackSprtOperState": vRtrPimNgAFIfTrackSprtOperState,
       "vRtrPimNgIfNeighborTable": vRtrPimNgIfNeighborTable,
       "vRtrPimNgIfNeighborEntry": vRtrPimNgIfNeighborEntry,
       "vRtrPimNgIfNeighborAddressType": vRtrPimNgIfNeighborAddressType,
       "vRtrPimNgIfNeighborAddress": vRtrPimNgIfNeighborAddress,
       "vRtrPimNgIfNeighborUpTime": vRtrPimNgIfNeighborUpTime,
       "vRtrPimNgIfNeighborExpiryTime": vRtrPimNgIfNeighborExpiryTime,
       "vRtrPimNgIfNeighborGenId": vRtrPimNgIfNeighborGenId,
       "vRtrPimNgIfNeighborDrPriority": vRtrPimNgIfNeighborDrPriority,
       "vRtrPimNgIfNeighborDrPriorPrsnt": vRtrPimNgIfNeighborDrPriorPrsnt,
       "vRtrPimNgIfNeighborLanDelay": vRtrPimNgIfNeighborLanDelay,
       "vRtrPimNgIfNeighborLanDlayPrsnt": vRtrPimNgIfNeighborLanDlayPrsnt,
       "vRtrPimNgIfNeighborTrckngSpprt": vRtrPimNgIfNeighborTrckngSpprt,
       "vRtrPimNgIfNeighborHoldTime": vRtrPimNgIfNeighborHoldTime,
       "vRtrPimNgIfNeighborOvrdeIntrvl": vRtrPimNgIfNeighborOvrdeIntrvl,
       "vRtrPimNgIfNeighborJASupport": vRtrPimNgIfNeighborJASupport,
       "vRtrPimNgIfGrpSrcTable": vRtrPimNgIfGrpSrcTable,
       "vRtrPimNgIfGrpSrcEntry": vRtrPimNgIfGrpSrcEntry,
       "vRtrPimNgIfGrpSrcType": vRtrPimNgIfGrpSrcType,
       "vRtrPimNgIfGrpSrcGroupAddrType": vRtrPimNgIfGrpSrcGroupAddrType,
       "vRtrPimNgIfGrpSrcGroupAddress": vRtrPimNgIfGrpSrcGroupAddress,
       "vRtrPimNgIfGrpSrcSourceAddrType": vRtrPimNgIfGrpSrcSourceAddrType,
       "vRtrPimNgIfGrpSrcSourceAddress": vRtrPimNgIfGrpSrcSourceAddress,
       "vRtrPimNgIfGrpSrcRPAddrType": vRtrPimNgIfGrpSrcRPAddrType,
       "vRtrPimNgIfGrpSrcRPAddress": vRtrPimNgIfGrpSrcRPAddress,
       "vRtrPimNgIfGrpSrcJPState": vRtrPimNgIfGrpSrcJPState,
       "vRtrPimNgIfGrpSrcPrunePendTimer": vRtrPimNgIfGrpSrcPrunePendTimer,
       "vRtrPimNgIfGrpSrcJoinPruneTimer": vRtrPimNgIfGrpSrcJoinPruneTimer,
       "vRtrPimNgIfGrpSrcJPRptState": vRtrPimNgIfGrpSrcJPRptState,
       "vRtrPimNgIfGrpSrcRptPrnePendTmr": vRtrPimNgIfGrpSrcRptPrnePendTmr,
       "vRtrPimNgIfGrpSrcRptJoinPrneTmr": vRtrPimNgIfGrpSrcRptJoinPrneTmr,
       "vRtrPimNgIfGrpSrcAssertState": vRtrPimNgIfGrpSrcAssertState,
       "vRtrPimNgIfGrpSrcAssertTimer": vRtrPimNgIfGrpSrcAssertTimer,
       "vRtrPimNgIfGrpSrcAssertMetric": vRtrPimNgIfGrpSrcAssertMetric,
       "vRtrPimNgIfGrpSrcAsrtMetricPref": vRtrPimNgIfGrpSrcAsrtMetricPref,
       "vRtrPimNgIfGrpSrcAssertRPTBit": vRtrPimNgIfGrpSrcAssertRPTBit,
       "vRtrPimNgIfGrpSrcAsrtWinnerMtrc": vRtrPimNgIfGrpSrcAsrtWinnerMtrc,
       "vRtrPimNgIfGrpSrcAsrtWnrMtrcPrf": vRtrPimNgIfGrpSrcAsrtWnrMtrcPrf,
       "vRtrPimNgIfGrpSrcAsrtWnrRPTBit": vRtrPimNgIfGrpSrcAsrtWnrRPTBit,
       "vRtrPimNgIfGrpSrcAsrtWnrAddrTyp": vRtrPimNgIfGrpSrcAsrtWnrAddrTyp,
       "vRtrPimNgIfGrpSrcAsrtWinnerAddr": vRtrPimNgIfGrpSrcAsrtWinnerAddr,
       "vRtrPimNgIfGrpSrcUpTime": vRtrPimNgIfGrpSrcUpTime,
       "vRtrPimNgIfGrpSrcDataMtIfIndex": vRtrPimNgIfGrpSrcDataMtIfIndex,
       "vRtrPimNgIfStatsTable": vRtrPimNgIfStatsTable,
       "vRtrPimNgIfStatsEntry": vRtrPimNgIfStatsEntry,
       "vRtrPimNgIfTxPkts": vRtrPimNgIfTxPkts,
       "vRtrPimNgIfTxHellos": vRtrPimNgIfTxHellos,
       "vRtrPimNgIfTxAsserts": vRtrPimNgIfTxAsserts,
       "vRtrPimNgIfTxRegisterStops": vRtrPimNgIfTxRegisterStops,
       "vRtrPimNgIfTxRegisterStopErrs": vRtrPimNgIfTxRegisterStopErrs,
       "vRtrPimNgIfTxBsmPdus": vRtrPimNgIfTxBsmPdus,
       "vRtrPimNgIfTxBsmErrs": vRtrPimNgIfTxBsmErrs,
       "vRtrPimNgIfRxPkts": vRtrPimNgIfRxPkts,
       "vRtrPimNgIfRxHellos": vRtrPimNgIfRxHellos,
       "vRtrPimNgIfRxHellosDropped": vRtrPimNgIfRxHellosDropped,
       "vRtrPimNgIfRxNbrUnknown": vRtrPimNgIfRxNbrUnknown,
       "vRtrPimNgIfRxBadChecksumDiscard": vRtrPimNgIfRxBadChecksumDiscard,
       "vRtrPimNgIfRxBadVersionDiscard": vRtrPimNgIfRxBadVersionDiscard,
       "vRtrPimNgIfRxBadEncodings": vRtrPimNgIfRxBadEncodings,
       "vRtrPimNgIfRxAsserts": vRtrPimNgIfRxAsserts,
       "vRtrPimNgIfRxAssertErrs": vRtrPimNgIfRxAssertErrs,
       "vRtrPimNgIfRxRegisters": vRtrPimNgIfRxRegisters,
       "vRtrPimNgIfRxRegisterErrs": vRtrPimNgIfRxRegisterErrs,
       "vRtrPimNgIfRxNullRegisters": vRtrPimNgIfRxNullRegisters,
       "vRtrPimNgIfRxRegisterStops": vRtrPimNgIfRxRegisterStops,
       "vRtrPimNgIfRxRegisterStopErrs": vRtrPimNgIfRxRegisterStopErrs,
       "vRtrPimNgIfRxCRPAdvNoRtrAlert": vRtrPimNgIfRxCRPAdvNoRtrAlert,
       "vRtrPimNgIfRxBsmPdus": vRtrPimNgIfRxBsmPdus,
       "vRtrPimNgIfRxBsmPduDrops": vRtrPimNgIfRxBsmPduDrops,
       "vRtrPimNgIfStarStarRPTypes": vRtrPimNgIfStarStarRPTypes,
       "vRtrPimNgIfStarGTypes": vRtrPimNgIfStarGTypes,
       "vRtrPimNgIfSGTypes": vRtrPimNgIfSGTypes,
       "vRtrPimNgIfJoinPolicyDrops": vRtrPimNgIfJoinPolicyDrops,
       "vRtrPimNgIfRegisterPolicyDrops": vRtrPimNgIfRegisterPolicyDrops,
       "vRtrPimNgIfBtrImpPolicyDrops": vRtrPimNgIfBtrImpPolicyDrops,
       "vRtrPimNgIfBtrExpPolicyDrops": vRtrPimNgIfBtrExpPolicyDrops,
       "vRtrPimNgIfTxJoinPrunes": vRtrPimNgIfTxJoinPrunes,
       "vRtrPimNgIfRxJoinPrunes": vRtrPimNgIfRxJoinPrunes,
       "vRtrPimNgIfRxInvalidJoinPrunes": vRtrPimNgIfRxInvalidJoinPrunes,
       "vRtrPimNgIfRxInvalidRegisters": vRtrPimNgIfRxInvalidRegisters,
       "vRtrPimNgIfRxUnknownPdus": vRtrPimNgIfRxUnknownPdus,
       "vRtrPimNgIfRxJoinPruneErrs": vRtrPimNgIfRxJoinPruneErrs,
       "vRtrPimNgIfRxBSMNoRouterAlertDrops": vRtrPimNgIfRxBSMNoRouterAlertDrops,
       "vRtrPimNgIfRxBSMWrongIfDrops": vRtrPimNgIfRxBSMWrongIfDrops,
       "vRtrPimNgIfMcacPolicyDrops": vRtrPimNgIfMcacPolicyDrops,
       "vRtrPimNgIfTxIntraASAD": vRtrPimNgIfTxIntraASAD,
       "vRtrPimNgIfRxIntraASAD": vRtrPimNgIfRxIntraASAD,
       "vRtrPimNgIfRxIntraASADErrs": vRtrPimNgIfRxIntraASADErrs,
       "vRtrPimNgIfTxInterASAD": vRtrPimNgIfTxInterASAD,
       "vRtrPimNgIfRxInterASAD": vRtrPimNgIfRxInterASAD,
       "vRtrPimNgIfRxInterASADErrs": vRtrPimNgIfRxInterASADErrs,
       "vRtrPimNgIfTxSpmsiAD": vRtrPimNgIfTxSpmsiAD,
       "vRtrPimNgIfRxSpmsiAD": vRtrPimNgIfRxSpmsiAD,
       "vRtrPimNgIfRxSpmsiADErrs": vRtrPimNgIfRxSpmsiADErrs,
       "vRtrPimNgIfTxLeafAD": vRtrPimNgIfTxLeafAD,
       "vRtrPimNgIfRxLeafAD": vRtrPimNgIfRxLeafAD,
       "vRtrPimNgIfRxLeafADErrs": vRtrPimNgIfRxLeafADErrs,
       "vRtrPimNgIfTxSrcActAD": vRtrPimNgIfTxSrcActAD,
       "vRtrPimNgIfRxSrcActAD": vRtrPimNgIfRxSrcActAD,
       "vRtrPimNgIfTxSrcActADErrs": vRtrPimNgIfTxSrcActADErrs,
       "vRtrPimNgIfTxSharedTreeJoin": vRtrPimNgIfTxSharedTreeJoin,
       "vRtrPimNgIfRxSharedTreeJoin": vRtrPimNgIfRxSharedTreeJoin,
       "vRtrPimNgIfRxSharedTreeJoinErrs": vRtrPimNgIfRxSharedTreeJoinErrs,
       "vRtrPimNgIfTxSrcTreeJoin": vRtrPimNgIfTxSrcTreeJoin,
       "vRtrPimNgIfRxSrcTreeJoin": vRtrPimNgIfRxSrcTreeJoin,
       "vRtrPimNgIfRxSrcTreeJoinErrs": vRtrPimNgIfRxSrcTreeJoinErrs,
       "vRtrPimNgIfTxBgpPkts": vRtrPimNgIfTxBgpPkts,
       "vRtrPimNgIfRxBgpPkts": vRtrPimNgIfRxBgpPkts,
       "vRtrPimNgIfTxMdtSafi": vRtrPimNgIfTxMdtSafi,
       "vRtrPimNgIfRxMdtSafi": vRtrPimNgIfRxMdtSafi,
       "vRtrPimNgIfRxMdtSafiErrs": vRtrPimNgIfRxMdtSafiErrs,
       "vRtrPimNgIfRxAutoRpGenErrs": vRtrPimNgIfRxAutoRpGenErrs,
       "vRtrPimNgIfRxAutoRpAnnounce": vRtrPimNgIfRxAutoRpAnnounce,
       "vRtrPimNgIfTxAutoRpAnnounce": vRtrPimNgIfTxAutoRpAnnounce,
       "vRtrPimNgIfRxAutoRpAnnounceErrs": vRtrPimNgIfRxAutoRpAnnounceErrs,
       "vRtrPimNgIfTxAutoRpAnnounceErrs": vRtrPimNgIfTxAutoRpAnnounceErrs,
       "vRtrPimNgIfRxAutoRpMapping": vRtrPimNgIfRxAutoRpMapping,
       "vRtrPimNgIfTxAutoRpMapping": vRtrPimNgIfTxAutoRpMapping,
       "vRtrPimNgIfRxAutoRpMappingErrs": vRtrPimNgIfRxAutoRpMappingErrs,
       "vRtrPimNgIfTxAutoRpMappingErrs": vRtrPimNgIfTxAutoRpMappingErrs,
       "vRtrPimNgIfRxJoinPrunesMvpnRpfv": vRtrPimNgIfRxJoinPrunesMvpnRpfv,
       "vRtrPimNgIfTxJoinPrunesMvpnRpfv": vRtrPimNgIfTxJoinPrunesMvpnRpfv,
       "vRtrPimNgIfRxInvalidJPMvpnRpfv": vRtrPimNgIfRxInvalidJPMvpnRpfv,
       "vRtrPimNgDataMtTable": vRtrPimNgDataMtTable,
       "vRtrPimNgDataMtEntry": vRtrPimNgDataMtEntry,
       "vRtrPimNgDataMtMdSourceAddrType": vRtrPimNgDataMtMdSourceAddrType,
       "vRtrPimNgDataMtMdSourceAddress": vRtrPimNgDataMtMdSourceAddress,
       "vRtrPimNgDataMtMdGroupAddrType": vRtrPimNgDataMtMdGroupAddrType,
       "vRtrPimNgDataMtMdGroupAddress": vRtrPimNgDataMtMdGroupAddress,
       "vRtrPimNgDataMtIfIndex": vRtrPimNgDataMtIfIndex,
       "vRtrPimNgDataMtUptime": vRtrPimNgDataMtUptime,
       "vRtrPimNgDataMtNumVpnSGs": vRtrPimNgDataMtNumVpnSGs,
       "vRtrPimNgDataMtCGrpSrcTable": vRtrPimNgDataMtCGrpSrcTable,
       "vRtrPimNgDataMtCGrpSrcEntry": vRtrPimNgDataMtCGrpSrcEntry,
       "vRtrPimNgDataMtCGrpSrcGrpAdType": vRtrPimNgDataMtCGrpSrcGrpAdType,
       "vRtrPimNgDataMtCGrpSrcGroupAddr": vRtrPimNgDataMtCGrpSrcGroupAddr,
       "vRtrPimNgDataMtCGrpSrcSrcAdType": vRtrPimNgDataMtCGrpSrcSrcAdType,
       "vRtrPimNgDataMtCGrpSrcSrcAddr": vRtrPimNgDataMtCGrpSrcSrcAddr,
       "vRtrPimNgDataMtCGrpSrcState": vRtrPimNgDataMtCGrpSrcState,
       "vRtrPimNgDataMtCGrpSrcJoinTimer": vRtrPimNgDataMtCGrpSrcJoinTimer,
       "vRtrPimNgDataMtCGrpSrcHolddownTimer": vRtrPimNgDataMtCGrpSrcHolddownTimer,
       "vRtrPimNgDataMtCGrpSrcExpiryTimer": vRtrPimNgDataMtCGrpSrcExpiryTimer,
       "vRtrPimNgDataMtCGrpSrcUptime": vRtrPimNgDataMtCGrpSrcUptime,
       "vRtrPimNgDataMtCGrpSrcDataMtThreshold": vRtrPimNgDataMtCGrpSrcDataMtThreshold,
       "vRtrPimNgDataMtCGrpSrcIfIndex": vRtrPimNgDataMtCGrpSrcIfIndex,
       "vRtrPimNgIfSecNbrTblLstChanged": vRtrPimNgIfSecNbrTblLstChanged,
       "vRtrPimNgIfSecNbrTable": vRtrPimNgIfSecNbrTable,
       "vRtrPimNgIfSecNbrEntry": vRtrPimNgIfSecNbrEntry,
       "vRtrPimNgIfSecNbrAddrType": vRtrPimNgIfSecNbrAddrType,
       "vRtrPimNgIfSecNbrAddress": vRtrPimNgIfSecNbrAddress,
       "vRtrPimNgRsvpPmsiTable": vRtrPimNgRsvpPmsiTable,
       "vRtrPimNgRsvpPmsiEntry": vRtrPimNgRsvpPmsiEntry,
       "vRtrPimNgRsvpPmsiExtTunlAdrType": vRtrPimNgRsvpPmsiExtTunlAdrType,
       "vRtrPimNgRsvpPmsiExtTunnelAddr": vRtrPimNgRsvpPmsiExtTunnelAddr,
       "vRtrPimNgRsvpPmsiTunnelId": vRtrPimNgRsvpPmsiTunnelId,
       "vRtrPimNgRsvpPmsiP2MPId": vRtrPimNgRsvpPmsiP2MPId,
       "vRtrPimNgRsvpPmsiIfIndex": vRtrPimNgRsvpPmsiIfIndex,
       "vRtrPimNgRsvpPmsiUptime": vRtrPimNgRsvpPmsiUptime,
       "vRtrPimNgRsvpPmsiNumVpnSGs": vRtrPimNgRsvpPmsiNumVpnSGs,
       "vRtrPimNgRsvpPmsiIfType": vRtrPimNgRsvpPmsiIfType,
       "vRtrPimNgRsvpPmsiCGrpSrcTable": vRtrPimNgRsvpPmsiCGrpSrcTable,
       "vRtrPimNgRsvpPmsiCGrpSrcEntry": vRtrPimNgRsvpPmsiCGrpSrcEntry,
       "vRtrPimRsvpPmsiCGrpSrcGrpAdType": vRtrPimRsvpPmsiCGrpSrcGrpAdType,
       "vRtrPimRsvpPmsiCGrpSrcGrpAddr": vRtrPimRsvpPmsiCGrpSrcGrpAddr,
       "vRtrPimRsvpPmsiCGrpSrcSrcAdType": vRtrPimRsvpPmsiCGrpSrcSrcAdType,
       "vRtrPimRsvpPmsiCGrpSrcSrcAddr": vRtrPimRsvpPmsiCGrpSrcSrcAddr,
       "vRtrPimRsvpPmsiCGrpSrcState": vRtrPimRsvpPmsiCGrpSrcState,
       "vRtrPimRsvpPmsiCGrpSrcJoinTimer": vRtrPimRsvpPmsiCGrpSrcJoinTimer,
       "vRtrPimRsvpPmsiCGrpSrcHldDnTimer": vRtrPimRsvpPmsiCGrpSrcHldDnTimer,
       "vRtrPimRsvpPmsiCGrpSrcExpTimer": vRtrPimRsvpPmsiCGrpSrcExpTimer,
       "vRtrPimRsvpPmsiCGrpSrcUptime": vRtrPimRsvpPmsiCGrpSrcUptime,
       "vRtrPimDataMtCGrpSrcDataThresh": vRtrPimDataMtCGrpSrcDataThresh,
       "vRtrPimRsvpPmsiCGrpSrcIfIndex": vRtrPimRsvpPmsiCGrpSrcIfIndex,
       "vRtrPimNgLdpPmsiTable": vRtrPimNgLdpPmsiTable,
       "vRtrPimNgLdpPmsiEntry": vRtrPimNgLdpPmsiEntry,
       "vRtrPimNgLdpPmsiRootAddrType": vRtrPimNgLdpPmsiRootAddrType,
       "vRtrPimNgLdpPmsiRootAddr": vRtrPimNgLdpPmsiRootAddr,
       "vRtrPimNgLdpPmsiLspId": vRtrPimNgLdpPmsiLspId,
       "vRtrPimNgLdpPmsiIfIndex": vRtrPimNgLdpPmsiIfIndex,
       "vRtrPimNgLdpPmsiUptime": vRtrPimNgLdpPmsiUptime,
       "vRtrPimNgLdpPmsiNumVpnSGs": vRtrPimNgLdpPmsiNumVpnSGs,
       "vRtrPimNgLdpPmsiIfType": vRtrPimNgLdpPmsiIfType,
       "vRtrPimNgLdpPmsiCGrpSrcTable": vRtrPimNgLdpPmsiCGrpSrcTable,
       "vRtrPimNgLdpPmsiCGrpSrcEntry": vRtrPimNgLdpPmsiCGrpSrcEntry,
       "vRtrPimLdpPmsiCGrpSrcGrpAdType": vRtrPimLdpPmsiCGrpSrcGrpAdType,
       "vRtrPimLdpPmsiCGrpSrcGrpAddr": vRtrPimLdpPmsiCGrpSrcGrpAddr,
       "vRtrPimLdpPmsiCGrpSrcSrcAdType": vRtrPimLdpPmsiCGrpSrcSrcAdType,
       "vRtrPimLdpPmsiCGrpSrcSrcAddr": vRtrPimLdpPmsiCGrpSrcSrcAddr,
       "vRtrPimLdpPmsiCGrpSrcState": vRtrPimLdpPmsiCGrpSrcState,
       "vRtrPimLdpPmsiCGrpSrcJoinTimer": vRtrPimLdpPmsiCGrpSrcJoinTimer,
       "vRtrPimLdpPmsiCGrpSrcHldDnTimer": vRtrPimLdpPmsiCGrpSrcHldDnTimer,
       "vRtrPimLdpPmsiCGrpSrcExpTimer": vRtrPimLdpPmsiCGrpSrcExpTimer,
       "vRtrPimLdpPmsiCGrpSrcUptime": vRtrPimLdpPmsiCGrpSrcUptime,
       "vRtrPimLdpDataMtCGrpSrcDataThres": vRtrPimLdpDataMtCGrpSrcDataThres,
       "vRtrPimLdpPmsiCGrpSrcIfIndex": vRtrPimLdpPmsiCGrpSrcIfIndex,
       "vRtrPimNgRsvpIPmsiTable": vRtrPimNgRsvpIPmsiTable,
       "vRtrPimNgRsvpIPmsiEntry": vRtrPimNgRsvpIPmsiEntry,
       "vRtrPimNgRsvpIPmsiExtTunlAdrType": vRtrPimNgRsvpIPmsiExtTunlAdrType,
       "vRtrPimNgRsvpIPmsiExtTunnelAddr": vRtrPimNgRsvpIPmsiExtTunnelAddr,
       "vRtrPimNgRsvpIPmsiLspName": vRtrPimNgRsvpIPmsiLspName,
       "vRtrPimNgRsvpIPmsiP2MPId": vRtrPimNgRsvpIPmsiP2MPId,
       "vRtrPimNgRsvpIPmsiTunnelId": vRtrPimNgRsvpIPmsiTunnelId,
       "vRtrPimNgLdpIPmsiTable": vRtrPimNgLdpIPmsiTable,
       "vRtrPimNgLdpIPmsiEntry": vRtrPimNgLdpIPmsiEntry,
       "vRtrPimNgLdpIPmsiRootAddrType": vRtrPimNgLdpIPmsiRootAddrType,
       "vRtrPimNgLdpIPmsiRootAddr": vRtrPimNgLdpIPmsiRootAddr,
       "vRtrPimNgLdpIPmsiLspId": vRtrPimNgLdpIPmsiLspId,
       "vRtrPimNgLdpIPmsiLspName": vRtrPimNgLdpIPmsiLspName,
       "vRtrPimNgMvpnExtranetTable": vRtrPimNgMvpnExtranetTable,
       "vRtrPimNgMvpnExtranetEntry": vRtrPimNgMvpnExtranetEntry,
       "vRtrPimNgMvpnExtranetNHAddrType": vRtrPimNgMvpnExtranetNHAddrType,
       "vRtrPimNgMvpnExtranetNHAddr": vRtrPimNgMvpnExtranetNHAddr,
       "vRtrPimNgMvpnExtranetRD": vRtrPimNgMvpnExtranetRD,
       "vRtrPimNgMvpnExtranetSrcMvpn": vRtrPimNgMvpnExtranetSrcMvpn,
       "vRtrPimNgMvpnExtranetRecvMvpn": vRtrPimNgMvpnExtranetRecvMvpn,
       "vRtrPimNgMvpnExtranetRecvRefCnt": vRtrPimNgMvpnExtranetRecvRefCnt,
       "vRtrPimNgIfGrpSrcRpfvTable": vRtrPimNgIfGrpSrcRpfvTable,
       "vRtrPimNgIfGrpSrcRpfvEntry": vRtrPimNgIfGrpSrcRpfvEntry,
       "vRtrPimNgIfGrpSrcRpfvSGType": vRtrPimNgIfGrpSrcRpfvSGType,
       "vRtrPimNgIfGrpSrcRpfvGrpAddrType": vRtrPimNgIfGrpSrcRpfvGrpAddrType,
       "vRtrPimNgIfGrpSrcRpfvGrpAddress": vRtrPimNgIfGrpSrcRpfvGrpAddress,
       "vRtrPimNgIfGrpSrcRpfvSrcAddrType": vRtrPimNgIfGrpSrcRpfvSrcAddrType,
       "vRtrPimNgIfGrpSrcRpfvSrcAddress": vRtrPimNgIfGrpSrcRpfvSrcAddress,
       "vRtrPimNgIfGrpSrcRpfvNbrAddrType": vRtrPimNgIfGrpSrcRpfvNbrAddrType,
       "vRtrPimNgIfGrpSrcRpfvNbrAddress": vRtrPimNgIfGrpSrcRpfvNbrAddress,
       "vRtrPimNgIfGrpSrcRpfvPrxyAddrTyp": vRtrPimNgIfGrpSrcRpfvPrxyAddrTyp,
       "vRtrPimNgIfGrpSrcRpfvProxyAddr": vRtrPimNgIfGrpSrcRpfvProxyAddr,
       "vRtrPimNgIfGrpSrcRpfvRD": vRtrPimNgIfGrpSrcRpfvRD,
       "vRtrPimNgIfGrpSrcRpfvType": vRtrPimNgIfGrpSrcRpfvType,
       "vRtrPimNgIfGrpSrcRpfvIfWinner": vRtrPimNgIfGrpSrcRpfvIfWinner,
       "vRtrPimNgIfGrpSrcRpfvNbrWinner": vRtrPimNgIfGrpSrcRpfvNbrWinner,
       "vRtrPimNgNotificationObjs": vRtrPimNgNotificationObjs,
       "vRtrPimNgNotifySourceIpType": vRtrPimNgNotifySourceIpType,
       "vRtrPimNgNotifySourceIp": vRtrPimNgNotifySourceIp,
       "vRtrPimNgNotifyGroupAddrType": vRtrPimNgNotifyGroupAddrType,
       "vRtrPimNgNotifyGroupAddr": vRtrPimNgNotifyGroupAddr,
       "vRtrPimNgNotifyRPAddrType": vRtrPimNgNotifyRPAddrType,
       "vRtrPimNgNotifyRPAddr": vRtrPimNgNotifyRPAddr,
       "vRtrPimNgNotifyWrongRPAddrType": vRtrPimNgNotifyWrongRPAddrType,
       "vRtrPimNgNotifyWrongRPAddr": vRtrPimNgNotifyWrongRPAddr,
       "vRtrPimNgNotifyMsgType": vRtrPimNgNotifyMsgType,
       "vRtrPimNgWrongMdtDefGrpAddrType": vRtrPimNgWrongMdtDefGrpAddrType,
       "vRtrPimNgWrongMdtDefGrpAddr": vRtrPimNgWrongMdtDefGrpAddr,
       "vRtrPimNgWrongPmsiType": vRtrPimNgWrongPmsiType,
       "vRtrPimNgWrongPmsiP2mpId": vRtrPimNgWrongPmsiP2mpId,
       "vRtrPimNgWrongPmsiTunnelId": vRtrPimNgWrongPmsiTunnelId,
       "vRtrPimNgWrongPmsiExtTunlAdrTyp": vRtrPimNgWrongPmsiExtTunlAdrTyp,
       "vRtrPimNgWrongPmsiExtTunlAddr": vRtrPimNgWrongPmsiExtTunlAddr,
       "vRtrPimNgWrongVprnId": vRtrPimNgWrongVprnId,
       "vRtrPimNgWrongPmsiLdpLspId": vRtrPimNgWrongPmsiLdpLspId,
       "vRtrPimNgWrongPmsiSenderAdrTyp": vRtrPimNgWrongPmsiSenderAdrTyp,
       "vRtrPimNgWrongPmsiSenderAddr": vRtrPimNgWrongPmsiSenderAddr,
       "vRtrPimNgNotifySourceAddrType": vRtrPimNgNotifySourceAddrType,
       "vRtrPimNgNotifySourceAddr": vRtrPimNgNotifySourceAddr,
       "vRtrPimNgNotifyDescription": vRtrPimNgNotifyDescription,
       "vRtrPimNgNotifyPrefix": vRtrPimNgNotifyPrefix,
       "vRtrPimNgNotifications": vRtrPimNgNotifications,
       "vRtrPimNgIfNeighborLoss": vRtrPimNgIfNeighborLoss,
       "vRtrPimNgIfNeighborUp": vRtrPimNgIfNeighborUp,
       "vRtrPimNgInvalidJoinPrune": vRtrPimNgInvalidJoinPrune,
       "vRtrPimNgInvalidRegister": vRtrPimNgInvalidRegister,
       "vRtrPimNgGrpInSSMRange": vRtrPimNgGrpInSSMRange,
       "vRtrPimNgBSRStateChange": vRtrPimNgBSRStateChange,
       "vRtrPimNgHelloDropped": vRtrPimNgHelloDropped,
       "vRtrPimNgSGLimitExceeded": vRtrPimNgSGLimitExceeded,
       "vRtrPimNgReplicationLmtExceeded": vRtrPimNgReplicationLmtExceeded,
       "vRtrPimNgMDTLimitExceeded": vRtrPimNgMDTLimitExceeded,
       "vRtrPimNgMaxGrpsLimitExceeded": vRtrPimNgMaxGrpsLimitExceeded,
       "vRtrPimNgDataMtReused": vRtrPimNgDataMtReused,
       "vRtrPimNgMcacPlcyDropped": vRtrPimNgMcacPlcyDropped,
       "vRtrPimNgInvalidIPmsiTunnel": vRtrPimNgInvalidIPmsiTunnel}
)
