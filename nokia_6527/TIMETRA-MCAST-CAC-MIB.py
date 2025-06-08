# SNMP MIB module (TIMETRA-MCAST-CAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MCAST-CAC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:47 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRObjs")

(tLagIndex,) = mibBuilder.importSymbols(
    "TIMETRA-LAG-MIB",
    "tLagIndex")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxPortID")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraMcastCacMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 41)
)
if mibBuilder.loadTexts:
    timetraMcastCacMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2008-01-01 00:00",
         "2006-08-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMcacActionTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("discard", 2))
    )



class TmnxMcacReasonTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bundleDisabled", 1),
          ("bundleNoAvailBw", 2),
          ("interfaceNoAvailBw", 3),
          ("noChlInPlcy", 4),
          ("algoPass", 5),
          ("userNoAvailBw", 6),
          ("subscrNoMcacPol", 7))
    )



class TmnxMcacApplTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmp", 1),
          ("pim", 2),
          ("igmpSnpg", 3))
    )



class TmnxMcacChlTypeTc(TextualConvention, Integer32):
    status = "current"
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
          ("notMandatory", 1),
          ("mandatory", 2))
    )



class TmnxMcacChlClassTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMcacConformance_ObjectIdentity = ObjectIdentity
tmnxMcacConformance = _TmnxMcacConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41)
)
_TmnxMcacCompliances_ObjectIdentity = ObjectIdentity
tmnxMcacCompliances = _TmnxMcacCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 1)
)
_TmnxMcacGroups_ObjectIdentity = ObjectIdentity
tmnxMcacGroups = _TmnxMcacGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 2)
)
_TmnxMcacObjects_ObjectIdentity = ObjectIdentity
tmnxMcacObjects = _TmnxMcacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41)
)
_TmnxMcacPolicyTable_Object = MibTable
tmnxMcacPolicyTable = _TmnxMcacPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 1)
)
if mibBuilder.loadTexts:
    tmnxMcacPolicyTable.setStatus("current")
_TmnxMcacPolicyEntry_Object = MibTableRow
tmnxMcacPolicyEntry = _TmnxMcacPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 1, 1)
)
tmnxMcacPolicyEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
)
if mibBuilder.loadTexts:
    tmnxMcacPolicyEntry.setStatus("current")
_TmnxMcacPolicyName_Type = TNamedItem
_TmnxMcacPolicyName_Object = MibTableColumn
tmnxMcacPolicyName = _TmnxMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 1, 1, 1),
    _TmnxMcacPolicyName_Type()
)
tmnxMcacPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacPolicyName.setStatus("current")
_TmnxMcacPolicyRowStatus_Type = RowStatus
_TmnxMcacPolicyRowStatus_Object = MibTableColumn
tmnxMcacPolicyRowStatus = _TmnxMcacPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 1, 1, 2),
    _TmnxMcacPolicyRowStatus_Type()
)
tmnxMcacPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacPolicyRowStatus.setStatus("current")


class _TmnxMcacPolicyDescription_Type(TItemDescription):
    """Custom type tmnxMcacPolicyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMcacPolicyDescription_Type.__name__ = "TItemDescription"
_TmnxMcacPolicyDescription_Object = MibTableColumn
tmnxMcacPolicyDescription = _TmnxMcacPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 1, 1, 3),
    _TmnxMcacPolicyDescription_Type()
)
tmnxMcacPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacPolicyDescription.setStatus("current")


class _TmnxMcacPolicyDefaultAction_Type(TmnxMcacActionTc):
    """Custom type tmnxMcacPolicyDefaultAction based on TmnxMcacActionTc"""
    defaultValue = 2


_TmnxMcacPolicyDefaultAction_Type.__name__ = "TmnxMcacActionTc"
_TmnxMcacPolicyDefaultAction_Object = MibTableColumn
tmnxMcacPolicyDefaultAction = _TmnxMcacPolicyDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 1, 1, 4),
    _TmnxMcacPolicyDefaultAction_Type()
)
tmnxMcacPolicyDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacPolicyDefaultAction.setStatus("current")
_TmnxMcacBundleTable_Object = MibTable
tmnxMcacBundleTable = _TmnxMcacBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2)
)
if mibBuilder.loadTexts:
    tmnxMcacBundleTable.setStatus("current")
_TmnxMcacBundleEntry_Object = MibTableRow
tmnxMcacBundleEntry = _TmnxMcacBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2, 1)
)
tmnxMcacBundleEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleName"),
)
if mibBuilder.loadTexts:
    tmnxMcacBundleEntry.setStatus("current")
_TmnxMcacBundleName_Type = TNamedItem
_TmnxMcacBundleName_Object = MibTableColumn
tmnxMcacBundleName = _TmnxMcacBundleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2, 1, 1),
    _TmnxMcacBundleName_Type()
)
tmnxMcacBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBundleName.setStatus("current")
_TmnxMcacBundleRowStatus_Type = RowStatus
_TmnxMcacBundleRowStatus_Object = MibTableColumn
tmnxMcacBundleRowStatus = _TmnxMcacBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2, 1, 2),
    _TmnxMcacBundleRowStatus_Type()
)
tmnxMcacBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBundleRowStatus.setStatus("current")


class _TmnxMcacBundleDescription_Type(TItemDescription):
    """Custom type tmnxMcacBundleDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMcacBundleDescription_Type.__name__ = "TItemDescription"
_TmnxMcacBundleDescription_Object = MibTableColumn
tmnxMcacBundleDescription = _TmnxMcacBundleDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2, 1, 3),
    _TmnxMcacBundleDescription_Type()
)
tmnxMcacBundleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBundleDescription.setStatus("current")


class _TmnxMcacBundleAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcacBundleAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcacBundleAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcacBundleAdminState_Object = MibTableColumn
tmnxMcacBundleAdminState = _TmnxMcacBundleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2, 1, 4),
    _TmnxMcacBundleAdminState_Type()
)
tmnxMcacBundleAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBundleAdminState.setStatus("current")


class _TmnxMcacBundleBandwidth_Type(Unsigned32):
    """Custom type tmnxMcacBundleBandwidth based on Unsigned32"""
    defaultValue = 100


_TmnxMcacBundleBandwidth_Type.__name__ = "Unsigned32"
_TmnxMcacBundleBandwidth_Object = MibTableColumn
tmnxMcacBundleBandwidth = _TmnxMcacBundleBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2, 1, 5),
    _TmnxMcacBundleBandwidth_Type()
)
tmnxMcacBundleBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBundleBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacBundleBandwidth.setUnits("kbps")


class _TmnxMcacBundleUseLagPortWeight_Type(TruthValue):
    """Custom type tmnxMcacBundleUseLagPortWeight based on TruthValue"""
    defaultValue = 2


_TmnxMcacBundleUseLagPortWeight_Type.__name__ = "TruthValue"
_TmnxMcacBundleUseLagPortWeight_Object = MibTableColumn
tmnxMcacBundleUseLagPortWeight = _TmnxMcacBundleUseLagPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 2, 1, 6),
    _TmnxMcacBundleUseLagPortWeight_Type()
)
tmnxMcacBundleUseLagPortWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBundleUseLagPortWeight.setStatus("current")
_TmnxMcacBdlChlTable_Object = MibTable
tmnxMcacBdlChlTable = _TmnxMcacBdlChlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3)
)
if mibBuilder.loadTexts:
    tmnxMcacBdlChlTable.setStatus("deprecated")
_TmnxMcacBdlChlEntry_Object = MibTableRow
tmnxMcacBdlChlEntry = _TmnxMcacBdlChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1)
)
tmnxMcacBdlChlEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlStartAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlStartAddr"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlEndAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlEndAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcacBdlChlEntry.setStatus("current")
_TmnxMcacBdlChlStartAddrType_Type = InetAddressType
_TmnxMcacBdlChlStartAddrType_Object = MibTableColumn
tmnxMcacBdlChlStartAddrType = _TmnxMcacBdlChlStartAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 1),
    _TmnxMcacBdlChlStartAddrType_Type()
)
tmnxMcacBdlChlStartAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlStartAddrType.setStatus("current")


class _TmnxMcacBdlChlStartAddr_Type(InetAddress):
    """Custom type tmnxMcacBdlChlStartAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcacBdlChlStartAddr_Type.__name__ = "InetAddress"
_TmnxMcacBdlChlStartAddr_Object = MibTableColumn
tmnxMcacBdlChlStartAddr = _TmnxMcacBdlChlStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 2),
    _TmnxMcacBdlChlStartAddr_Type()
)
tmnxMcacBdlChlStartAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlStartAddr.setStatus("current")
_TmnxMcacBdlChlEndAddrType_Type = InetAddressType
_TmnxMcacBdlChlEndAddrType_Object = MibTableColumn
tmnxMcacBdlChlEndAddrType = _TmnxMcacBdlChlEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 3),
    _TmnxMcacBdlChlEndAddrType_Type()
)
tmnxMcacBdlChlEndAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlEndAddrType.setStatus("current")


class _TmnxMcacBdlChlEndAddr_Type(InetAddress):
    """Custom type tmnxMcacBdlChlEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcacBdlChlEndAddr_Type.__name__ = "InetAddress"
_TmnxMcacBdlChlEndAddr_Object = MibTableColumn
tmnxMcacBdlChlEndAddr = _TmnxMcacBdlChlEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 4),
    _TmnxMcacBdlChlEndAddr_Type()
)
tmnxMcacBdlChlEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlEndAddr.setStatus("current")
_TmnxMcacBdlChlRowStatus_Type = RowStatus
_TmnxMcacBdlChlRowStatus_Object = MibTableColumn
tmnxMcacBdlChlRowStatus = _TmnxMcacBdlChlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 5),
    _TmnxMcacBdlChlRowStatus_Type()
)
tmnxMcacBdlChlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlRowStatus.setStatus("current")


class _TmnxMcacBdlChlBW_Type(Unsigned32):
    """Custom type tmnxMcacBdlChlBW based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_TmnxMcacBdlChlBW_Type.__name__ = "Unsigned32"
_TmnxMcacBdlChlBW_Object = MibTableColumn
tmnxMcacBdlChlBW = _TmnxMcacBdlChlBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 6),
    _TmnxMcacBdlChlBW_Type()
)
tmnxMcacBdlChlBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlBW.setUnits("kbps")


class _TmnxMcacBdlChlClass_Type(TmnxMcacChlClassTc):
    """Custom type tmnxMcacBdlChlClass based on TmnxMcacChlClassTc"""
    defaultValue = 1


_TmnxMcacBdlChlClass_Type.__name__ = "TmnxMcacChlClassTc"
_TmnxMcacBdlChlClass_Object = MibTableColumn
tmnxMcacBdlChlClass = _TmnxMcacBdlChlClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 7),
    _TmnxMcacBdlChlClass_Type()
)
tmnxMcacBdlChlClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlClass.setStatus("current")


class _TmnxMcacBdlChlType_Type(TmnxMcacChlTypeTc):
    """Custom type tmnxMcacBdlChlType based on TmnxMcacChlTypeTc"""
    defaultValue = 1


_TmnxMcacBdlChlType_Type.__name__ = "TmnxMcacChlTypeTc"
_TmnxMcacBdlChlType_Object = MibTableColumn
tmnxMcacBdlChlType = _TmnxMcacBdlChlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 3, 1, 8),
    _TmnxMcacBdlChlType_Type()
)
tmnxMcacBdlChlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlType.setStatus("current")
_TmnxMcacLevelTable_Object = MibTable
tmnxMcacLevelTable = _TmnxMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 4)
)
if mibBuilder.loadTexts:
    tmnxMcacLevelTable.setStatus("current")
_TmnxMcacLevelEntry_Object = MibTableRow
tmnxMcacLevelEntry = _TmnxMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 4, 1)
)
tmnxMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    tmnxMcacLevelEntry.setStatus("current")


class _TmnxMcacLevelId_Type(Unsigned32):
    """Custom type tmnxMcacLevelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMcacLevelId_Type.__name__ = "Unsigned32"
_TmnxMcacLevelId_Object = MibTableColumn
tmnxMcacLevelId = _TmnxMcacLevelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 4, 1, 1),
    _TmnxMcacLevelId_Type()
)
tmnxMcacLevelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacLevelId.setStatus("current")
_TmnxMcacLevelRowStatus_Type = RowStatus
_TmnxMcacLevelRowStatus_Object = MibTableColumn
tmnxMcacLevelRowStatus = _TmnxMcacLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 4, 1, 2),
    _TmnxMcacLevelRowStatus_Type()
)
tmnxMcacLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacLevelRowStatus.setStatus("current")


class _TmnxMcacLevelBW_Type(Unsigned32):
    """Custom type tmnxMcacLevelBW based on Unsigned32"""
    defaultValue = 1


_TmnxMcacLevelBW_Type.__name__ = "Unsigned32"
_TmnxMcacLevelBW_Object = MibTableColumn
tmnxMcacLevelBW = _TmnxMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 4, 1, 3),
    _TmnxMcacLevelBW_Type()
)
tmnxMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacLevelBW.setUnits("kbps")
_TmnxMcacLagTable_Object = MibTable
tmnxMcacLagTable = _TmnxMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 5)
)
if mibBuilder.loadTexts:
    tmnxMcacLagTable.setStatus("current")
_TmnxMcacLagEntry_Object = MibTableRow
tmnxMcacLagEntry = _TmnxMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 5, 1)
)
tmnxMcacLagEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleName"),
    (0, "TIMETRA-LAG-MIB", "tLagIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    tmnxMcacLagEntry.setStatus("current")


class _TmnxMcacLagPortsDown_Type(Unsigned32):
    """Custom type tmnxMcacLagPortsDown based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmnxMcacLagPortsDown_Type.__name__ = "Unsigned32"
_TmnxMcacLagPortsDown_Object = MibTableColumn
tmnxMcacLagPortsDown = _TmnxMcacLagPortsDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 5, 1, 1),
    _TmnxMcacLagPortsDown_Type()
)
tmnxMcacLagPortsDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacLagPortsDown.setStatus("current")
_TmnxMcacLagRowStatus_Type = RowStatus
_TmnxMcacLagRowStatus_Object = MibTableColumn
tmnxMcacLagRowStatus = _TmnxMcacLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 5, 1, 2),
    _TmnxMcacLagRowStatus_Type()
)
tmnxMcacLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacLagRowStatus.setStatus("current")


class _TmnxMcacLagBundleLevel_Type(Unsigned32):
    """Custom type tmnxMcacLagBundleLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxMcacLagBundleLevel_Type.__name__ = "Unsigned32"
_TmnxMcacLagBundleLevel_Object = MibTableColumn
tmnxMcacLagBundleLevel = _TmnxMcacLagBundleLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 5, 1, 3),
    _TmnxMcacLagBundleLevel_Type()
)
tmnxMcacLagBundleLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacLagBundleLevel.setStatus("current")
_TmnxMcacStatsTable_Object = MibTable
tmnxMcacStatsTable = _TmnxMcacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6)
)
if mibBuilder.loadTexts:
    tmnxMcacStatsTable.setStatus("deprecated")
_TmnxMcacStatsEntry_Object = MibTableRow
tmnxMcacStatsEntry = _TmnxMcacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1)
)
tmnxMcacStatsEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsBundleName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsChlAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsChlAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcacStatsEntry.setStatus("current")
_TmnxMcacStatsBundleName_Type = TNamedItemOrEmpty
_TmnxMcacStatsBundleName_Object = MibTableColumn
tmnxMcacStatsBundleName = _TmnxMcacStatsBundleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 1),
    _TmnxMcacStatsBundleName_Type()
)
tmnxMcacStatsBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsBundleName.setStatus("current")
_TmnxMcacStatsProtocolIndex_Type = TmnxMcacApplTc
_TmnxMcacStatsProtocolIndex_Object = MibTableColumn
tmnxMcacStatsProtocolIndex = _TmnxMcacStatsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 2),
    _TmnxMcacStatsProtocolIndex_Type()
)
tmnxMcacStatsProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsProtocolIndex.setStatus("current")
_TmnxMcacStatsIfIndex_Type = InterfaceIndex
_TmnxMcacStatsIfIndex_Object = MibTableColumn
tmnxMcacStatsIfIndex = _TmnxMcacStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 3),
    _TmnxMcacStatsIfIndex_Type()
)
tmnxMcacStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsIfIndex.setStatus("current")
_TmnxMcacStatsChlAddrType_Type = InetAddressType
_TmnxMcacStatsChlAddrType_Object = MibTableColumn
tmnxMcacStatsChlAddrType = _TmnxMcacStatsChlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 4),
    _TmnxMcacStatsChlAddrType_Type()
)
tmnxMcacStatsChlAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsChlAddrType.setStatus("current")


class _TmnxMcacStatsChlAddr_Type(InetAddress):
    """Custom type tmnxMcacStatsChlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcacStatsChlAddr_Type.__name__ = "InetAddress"
_TmnxMcacStatsChlAddr_Object = MibTableColumn
tmnxMcacStatsChlAddr = _TmnxMcacStatsChlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 5),
    _TmnxMcacStatsChlAddr_Type()
)
tmnxMcacStatsChlAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsChlAddr.setStatus("current")
_TmnxMcacStatsAction_Type = TmnxMcacActionTc
_TmnxMcacStatsAction_Object = MibTableColumn
tmnxMcacStatsAction = _TmnxMcacStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 6),
    _TmnxMcacStatsAction_Type()
)
tmnxMcacStatsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsAction.setStatus("current")
_TmnxMcacStatsReason_Type = TmnxMcacReasonTc
_TmnxMcacStatsReason_Object = MibTableColumn
tmnxMcacStatsReason = _TmnxMcacStatsReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 7),
    _TmnxMcacStatsReason_Type()
)
tmnxMcacStatsReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsReason.setStatus("current")
_TmnxMcacStatsChannelType_Type = TmnxMcacChlTypeTc
_TmnxMcacStatsChannelType_Object = MibTableColumn
tmnxMcacStatsChannelType = _TmnxMcacStatsChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 8),
    _TmnxMcacStatsChannelType_Type()
)
tmnxMcacStatsChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsChannelType.setStatus("current")
_TmnxMcacStatsChannelBW_Type = Unsigned32
_TmnxMcacStatsChannelBW_Object = MibTableColumn
tmnxMcacStatsChannelBW = _TmnxMcacStatsChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 9),
    _TmnxMcacStatsChannelBW_Type()
)
tmnxMcacStatsChannelBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsChannelBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacStatsChannelBW.setUnits("kbps")
_TmnxMcacStatsBundleAvailBW_Type = Unsigned32
_TmnxMcacStatsBundleAvailBW_Object = MibTableColumn
tmnxMcacStatsBundleAvailBW = _TmnxMcacStatsBundleAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 10),
    _TmnxMcacStatsBundleAvailBW_Type()
)
tmnxMcacStatsBundleAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsBundleAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacStatsBundleAvailBW.setUnits("kbps")
_TmnxMcacStatsIntfAvailBW_Type = Unsigned32
_TmnxMcacStatsIntfAvailBW_Object = MibTableColumn
tmnxMcacStatsIntfAvailBW = _TmnxMcacStatsIntfAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 11),
    _TmnxMcacStatsIntfAvailBW_Type()
)
tmnxMcacStatsIntfAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsIntfAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacStatsIntfAvailBW.setUnits("kbps")
_TmnxMcacStatsAlgoReapply_Type = TruthValue
_TmnxMcacStatsAlgoReapply_Object = MibTableColumn
tmnxMcacStatsAlgoReapply = _TmnxMcacStatsAlgoReapply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 12),
    _TmnxMcacStatsAlgoReapply_Type()
)
tmnxMcacStatsAlgoReapply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsAlgoReapply.setStatus("current")
_TmnxMcacStatsApplyAttempts_Type = Counter32
_TmnxMcacStatsApplyAttempts_Object = MibTableColumn
tmnxMcacStatsApplyAttempts = _TmnxMcacStatsApplyAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 13),
    _TmnxMcacStatsApplyAttempts_Type()
)
tmnxMcacStatsApplyAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsApplyAttempts.setStatus("current")
_TmnxMcacStatsTimeStamp_Type = TimeStamp
_TmnxMcacStatsTimeStamp_Object = MibTableColumn
tmnxMcacStatsTimeStamp = _TmnxMcacStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 6, 1, 14),
    _TmnxMcacStatsTimeStamp_Type()
)
tmnxMcacStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsTimeStamp.setStatus("current")
_TmnxMcacOperTable_Object = MibTable
tmnxMcacOperTable = _TmnxMcacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7)
)
if mibBuilder.loadTexts:
    tmnxMcacOperTable.setStatus("current")
_TmnxMcacOperEntry_Object = MibTableRow
tmnxMcacOperEntry = _TmnxMcacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1)
)
tmnxMcacOperEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxMcacOperEntry.setStatus("current")
_TmnxMcacOperActiveChannels_Type = Gauge32
_TmnxMcacOperActiveChannels_Object = MibTableColumn
tmnxMcacOperActiveChannels = _TmnxMcacOperActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 1),
    _TmnxMcacOperActiveChannels_Type()
)
tmnxMcacOperActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperActiveChannels.setStatus("current")
_TmnxMcacOperMaxBw_Type = Unsigned32
_TmnxMcacOperMaxBw_Object = MibTableColumn
tmnxMcacOperMaxBw = _TmnxMcacOperMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 2),
    _TmnxMcacOperMaxBw_Type()
)
tmnxMcacOperMaxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperMaxBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacOperMaxBw.setUnits("kbps")
_TmnxMcacOperAvailOptnlBw_Type = Unsigned32
_TmnxMcacOperAvailOptnlBw_Object = MibTableColumn
tmnxMcacOperAvailOptnlBw = _TmnxMcacOperAvailOptnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 3),
    _TmnxMcacOperAvailOptnlBw_Type()
)
tmnxMcacOperAvailOptnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperAvailOptnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacOperAvailOptnlBw.setUnits("kbps")
_TmnxMcacOperAvailMandBw_Type = Unsigned32
_TmnxMcacOperAvailMandBw_Object = MibTableColumn
tmnxMcacOperAvailMandBw = _TmnxMcacOperAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 4),
    _TmnxMcacOperAvailMandBw_Type()
)
tmnxMcacOperAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacOperAvailMandBw.setUnits("kbps")
_TmnxMcacOperInUseMandBw_Type = Unsigned32
_TmnxMcacOperInUseMandBw_Object = MibTableColumn
tmnxMcacOperInUseMandBw = _TmnxMcacOperInUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 5),
    _TmnxMcacOperInUseMandBw_Type()
)
tmnxMcacOperInUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperInUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacOperInUseMandBw.setUnits("kbps")
_TmnxMcacOperPortsDown_Type = Unsigned32
_TmnxMcacOperPortsDown_Object = MibTableColumn
tmnxMcacOperPortsDown = _TmnxMcacOperPortsDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 6),
    _TmnxMcacOperPortsDown_Type()
)
tmnxMcacOperPortsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperPortsDown.setStatus("current")
_TmnxMcacOperCurrConstrtLvl_Type = Unsigned32
_TmnxMcacOperCurrConstrtLvl_Object = MibTableColumn
tmnxMcacOperCurrConstrtLvl = _TmnxMcacOperCurrConstrtLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 7),
    _TmnxMcacOperCurrConstrtLvl_Type()
)
tmnxMcacOperCurrConstrtLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperCurrConstrtLvl.setStatus("current")
_TmnxMcacOperInUseOptnlBw_Type = Unsigned32
_TmnxMcacOperInUseOptnlBw_Object = MibTableColumn
tmnxMcacOperInUseOptnlBw = _TmnxMcacOperInUseOptnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 8),
    _TmnxMcacOperInUseOptnlBw_Type()
)
tmnxMcacOperInUseOptnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperInUseOptnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacOperInUseOptnlBw.setUnits("kbps")
_TmnxMcacOperValuesInTransit_Type = TruthValue
_TmnxMcacOperValuesInTransit_Object = MibTableColumn
tmnxMcacOperValuesInTransit = _TmnxMcacOperValuesInTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 7, 1, 9),
    _TmnxMcacOperValuesInTransit_Type()
)
tmnxMcacOperValuesInTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacOperValuesInTransit.setStatus("current")
_TmnxMcacServStatsTable_Object = MibTable
tmnxMcacServStatsTable = _TmnxMcacServStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8)
)
if mibBuilder.loadTexts:
    tmnxMcacServStatsTable.setStatus("current")
_TmnxMcacServStatsEntry_Object = MibTableRow
tmnxMcacServStatsEntry = _TmnxMcacServStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1)
)
tmnxMcacServStatsEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsBundleName"),
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsPortId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsChlAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsChlAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcacServStatsEntry.setStatus("current")
_TmnxMcacServStatsPortId_Type = TmnxPortID
_TmnxMcacServStatsPortId_Object = MibTableColumn
tmnxMcacServStatsPortId = _TmnxMcacServStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 1),
    _TmnxMcacServStatsPortId_Type()
)
tmnxMcacServStatsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacServStatsPortId.setStatus("current")
_TmnxMcacServStatsEncapValue_Type = TmnxEncapVal
_TmnxMcacServStatsEncapValue_Object = MibTableColumn
tmnxMcacServStatsEncapValue = _TmnxMcacServStatsEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 2),
    _TmnxMcacServStatsEncapValue_Type()
)
tmnxMcacServStatsEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacServStatsEncapValue.setStatus("current")
_TmnxMcacServStatsAction_Type = TmnxMcacActionTc
_TmnxMcacServStatsAction_Object = MibTableColumn
tmnxMcacServStatsAction = _TmnxMcacServStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 3),
    _TmnxMcacServStatsAction_Type()
)
tmnxMcacServStatsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsAction.setStatus("current")
_TmnxMcacServStatsReason_Type = TmnxMcacReasonTc
_TmnxMcacServStatsReason_Object = MibTableColumn
tmnxMcacServStatsReason = _TmnxMcacServStatsReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 4),
    _TmnxMcacServStatsReason_Type()
)
tmnxMcacServStatsReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsReason.setStatus("current")
_TmnxMcacServStatsChannelType_Type = TmnxMcacChlTypeTc
_TmnxMcacServStatsChannelType_Object = MibTableColumn
tmnxMcacServStatsChannelType = _TmnxMcacServStatsChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 5),
    _TmnxMcacServStatsChannelType_Type()
)
tmnxMcacServStatsChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsChannelType.setStatus("current")
_TmnxMcacServStatsChannelBW_Type = Unsigned32
_TmnxMcacServStatsChannelBW_Object = MibTableColumn
tmnxMcacServStatsChannelBW = _TmnxMcacServStatsChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 6),
    _TmnxMcacServStatsChannelBW_Type()
)
tmnxMcacServStatsChannelBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsChannelBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServStatsChannelBW.setUnits("kbps")
_TmnxMcacServStatsBundleAvailBW_Type = Unsigned32
_TmnxMcacServStatsBundleAvailBW_Object = MibTableColumn
tmnxMcacServStatsBundleAvailBW = _TmnxMcacServStatsBundleAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 7),
    _TmnxMcacServStatsBundleAvailBW_Type()
)
tmnxMcacServStatsBundleAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsBundleAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServStatsBundleAvailBW.setUnits("kbps")
_TmnxMcacServStatsIntfAvailBW_Type = Unsigned32
_TmnxMcacServStatsIntfAvailBW_Object = MibTableColumn
tmnxMcacServStatsIntfAvailBW = _TmnxMcacServStatsIntfAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 8),
    _TmnxMcacServStatsIntfAvailBW_Type()
)
tmnxMcacServStatsIntfAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsIntfAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServStatsIntfAvailBW.setUnits("kbps")
_TmnxMcacServStatsAlgoReapply_Type = TruthValue
_TmnxMcacServStatsAlgoReapply_Object = MibTableColumn
tmnxMcacServStatsAlgoReapply = _TmnxMcacServStatsAlgoReapply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 9),
    _TmnxMcacServStatsAlgoReapply_Type()
)
tmnxMcacServStatsAlgoReapply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsAlgoReapply.setStatus("current")
_TmnxMcacServStatsApplyAttempts_Type = Counter32
_TmnxMcacServStatsApplyAttempts_Object = MibTableColumn
tmnxMcacServStatsApplyAttempts = _TmnxMcacServStatsApplyAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 10),
    _TmnxMcacServStatsApplyAttempts_Type()
)
tmnxMcacServStatsApplyAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsApplyAttempts.setStatus("current")
_TmnxMcacServStatsTimeStamp_Type = TimeStamp
_TmnxMcacServStatsTimeStamp_Object = MibTableColumn
tmnxMcacServStatsTimeStamp = _TmnxMcacServStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 8, 1, 11),
    _TmnxMcacServStatsTimeStamp_Type()
)
tmnxMcacServStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsTimeStamp.setStatus("current")
_TmnxMcacServOperTable_Object = MibTable
tmnxMcacServOperTable = _TmnxMcacServOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9)
)
if mibBuilder.loadTexts:
    tmnxMcacServOperTable.setStatus("current")
_TmnxMcacServOperEntry_Object = MibTableRow
tmnxMcacServOperEntry = _TmnxMcacServOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1)
)
tmnxMcacServOperEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleName"),
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsPortId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxMcacServOperEntry.setStatus("current")
_TmnxMcacServOperActiveChannels_Type = Gauge32
_TmnxMcacServOperActiveChannels_Object = MibTableColumn
tmnxMcacServOperActiveChannels = _TmnxMcacServOperActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 1),
    _TmnxMcacServOperActiveChannels_Type()
)
tmnxMcacServOperActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperActiveChannels.setStatus("current")
_TmnxMcacServOperMaxBw_Type = Unsigned32
_TmnxMcacServOperMaxBw_Object = MibTableColumn
tmnxMcacServOperMaxBw = _TmnxMcacServOperMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 2),
    _TmnxMcacServOperMaxBw_Type()
)
tmnxMcacServOperMaxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperMaxBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServOperMaxBw.setUnits("kbps")
_TmnxMcacServOperAvailOptnlBw_Type = Unsigned32
_TmnxMcacServOperAvailOptnlBw_Object = MibTableColumn
tmnxMcacServOperAvailOptnlBw = _TmnxMcacServOperAvailOptnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 3),
    _TmnxMcacServOperAvailOptnlBw_Type()
)
tmnxMcacServOperAvailOptnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperAvailOptnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServOperAvailOptnlBw.setUnits("kbps")
_TmnxMcacServOperAvailMandBw_Type = Unsigned32
_TmnxMcacServOperAvailMandBw_Object = MibTableColumn
tmnxMcacServOperAvailMandBw = _TmnxMcacServOperAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 4),
    _TmnxMcacServOperAvailMandBw_Type()
)
tmnxMcacServOperAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServOperAvailMandBw.setUnits("kbps")
_TmnxMcacServOperInUseMandBw_Type = Unsigned32
_TmnxMcacServOperInUseMandBw_Object = MibTableColumn
tmnxMcacServOperInUseMandBw = _TmnxMcacServOperInUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 5),
    _TmnxMcacServOperInUseMandBw_Type()
)
tmnxMcacServOperInUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperInUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServOperInUseMandBw.setUnits("kbps")
_TmnxMcacServOperPortsDown_Type = Unsigned32
_TmnxMcacServOperPortsDown_Object = MibTableColumn
tmnxMcacServOperPortsDown = _TmnxMcacServOperPortsDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 6),
    _TmnxMcacServOperPortsDown_Type()
)
tmnxMcacServOperPortsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperPortsDown.setStatus("current")
_TmnxMcacServOperCurrConstrtLvl_Type = Unsigned32
_TmnxMcacServOperCurrConstrtLvl_Object = MibTableColumn
tmnxMcacServOperCurrConstrtLvl = _TmnxMcacServOperCurrConstrtLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 7),
    _TmnxMcacServOperCurrConstrtLvl_Type()
)
tmnxMcacServOperCurrConstrtLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperCurrConstrtLvl.setStatus("current")
_TmnxMcacServOperInUseOptnlBw_Type = Unsigned32
_TmnxMcacServOperInUseOptnlBw_Object = MibTableColumn
tmnxMcacServOperInUseOptnlBw = _TmnxMcacServOperInUseOptnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 8),
    _TmnxMcacServOperInUseOptnlBw_Type()
)
tmnxMcacServOperInUseOptnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperInUseOptnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServOperInUseOptnlBw.setUnits("kbps")
_TmnxMcacServOperValuesInTransit_Type = TruthValue
_TmnxMcacServOperValuesInTransit_Object = MibTableColumn
tmnxMcacServOperValuesInTransit = _TmnxMcacServOperValuesInTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 9, 1, 9),
    _TmnxMcacServOperValuesInTransit_Type()
)
tmnxMcacServOperValuesInTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServOperValuesInTransit.setStatus("current")
_TmnxMcacPolicyUserTable_Object = MibTable
tmnxMcacPolicyUserTable = _TmnxMcacPolicyUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 10)
)
if mibBuilder.loadTexts:
    tmnxMcacPolicyUserTable.setStatus("current")
_TmnxMcacPolicyUserEntry_Object = MibTableRow
tmnxMcacPolicyUserEntry = _TmnxMcacPolicyUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 10, 1)
)
tmnxMcacPolicyUserEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxMcacPolicyUserEntry.setStatus("current")
_TmnxMcacPolicyUserConfigured_Type = TruthValue
_TmnxMcacPolicyUserConfigured_Object = MibTableColumn
tmnxMcacPolicyUserConfigured = _TmnxMcacPolicyUserConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 10, 1, 1),
    _TmnxMcacPolicyUserConfigured_Type()
)
tmnxMcacPolicyUserConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacPolicyUserConfigured.setStatus("current")
_TmnxMcacPolicyServUserTable_Object = MibTable
tmnxMcacPolicyServUserTable = _TmnxMcacPolicyServUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 11)
)
if mibBuilder.loadTexts:
    tmnxMcacPolicyServUserTable.setStatus("current")
_TmnxMcacPolicyServUserEntry_Object = MibTableRow
tmnxMcacPolicyServUserEntry = _TmnxMcacPolicyServUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 11, 1)
)
tmnxMcacPolicyServUserEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsPortId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxMcacPolicyServUserEntry.setStatus("current")
_TmnxMcacPolicyServUserConfigured_Type = TruthValue
_TmnxMcacPolicyServUserConfigured_Object = MibTableColumn
tmnxMcacPolicyServUserConfigured = _TmnxMcacPolicyServUserConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 11, 1, 1),
    _TmnxMcacPolicyServUserConfigured_Type()
)
tmnxMcacPolicyServUserConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacPolicyServUserConfigured.setStatus("current")
_TmnxMcacBdlChlNgTable_Object = MibTable
tmnxMcacBdlChlNgTable = _TmnxMcacBdlChlNgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12)
)
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgTable.setStatus("current")
_TmnxMcacBdlChlNgEntry_Object = MibTableRow
tmnxMcacBdlChlNgEntry = _TmnxMcacBdlChlNgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1)
)
tmnxMcacBdlChlNgEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgStartAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgStartAddr"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgEndAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgEndAddr"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgSrcPfxType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgSrcPfx"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgSrcPfxLen"),
)
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgEntry.setStatus("current")
_TmnxMcacBdlChlNgStartAddrType_Type = InetAddressType
_TmnxMcacBdlChlNgStartAddrType_Object = MibTableColumn
tmnxMcacBdlChlNgStartAddrType = _TmnxMcacBdlChlNgStartAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 1),
    _TmnxMcacBdlChlNgStartAddrType_Type()
)
tmnxMcacBdlChlNgStartAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgStartAddrType.setStatus("current")


class _TmnxMcacBdlChlNgStartAddr_Type(InetAddress):
    """Custom type tmnxMcacBdlChlNgStartAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcacBdlChlNgStartAddr_Type.__name__ = "InetAddress"
_TmnxMcacBdlChlNgStartAddr_Object = MibTableColumn
tmnxMcacBdlChlNgStartAddr = _TmnxMcacBdlChlNgStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 2),
    _TmnxMcacBdlChlNgStartAddr_Type()
)
tmnxMcacBdlChlNgStartAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgStartAddr.setStatus("current")
_TmnxMcacBdlChlNgEndAddrType_Type = InetAddressType
_TmnxMcacBdlChlNgEndAddrType_Object = MibTableColumn
tmnxMcacBdlChlNgEndAddrType = _TmnxMcacBdlChlNgEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 3),
    _TmnxMcacBdlChlNgEndAddrType_Type()
)
tmnxMcacBdlChlNgEndAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgEndAddrType.setStatus("current")


class _TmnxMcacBdlChlNgEndAddr_Type(InetAddress):
    """Custom type tmnxMcacBdlChlNgEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcacBdlChlNgEndAddr_Type.__name__ = "InetAddress"
_TmnxMcacBdlChlNgEndAddr_Object = MibTableColumn
tmnxMcacBdlChlNgEndAddr = _TmnxMcacBdlChlNgEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 4),
    _TmnxMcacBdlChlNgEndAddr_Type()
)
tmnxMcacBdlChlNgEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgEndAddr.setStatus("current")


class _TmnxMcacBdlChlNgSrcPfxType_Type(InetAddressType):
    """Custom type tmnxMcacBdlChlNgSrcPfxType based on InetAddressType"""
    defaultValue = 0


_TmnxMcacBdlChlNgSrcPfxType_Type.__name__ = "InetAddressType"
_TmnxMcacBdlChlNgSrcPfxType_Object = MibTableColumn
tmnxMcacBdlChlNgSrcPfxType = _TmnxMcacBdlChlNgSrcPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 5),
    _TmnxMcacBdlChlNgSrcPfxType_Type()
)
tmnxMcacBdlChlNgSrcPfxType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgSrcPfxType.setStatus("current")


class _TmnxMcacBdlChlNgSrcPfx_Type(InetAddress):
    """Custom type tmnxMcacBdlChlNgSrcPfx based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcacBdlChlNgSrcPfx_Type.__name__ = "InetAddress"
_TmnxMcacBdlChlNgSrcPfx_Object = MibTableColumn
tmnxMcacBdlChlNgSrcPfx = _TmnxMcacBdlChlNgSrcPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 6),
    _TmnxMcacBdlChlNgSrcPfx_Type()
)
tmnxMcacBdlChlNgSrcPfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgSrcPfx.setStatus("current")


class _TmnxMcacBdlChlNgSrcPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxMcacBdlChlNgSrcPfxLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxMcacBdlChlNgSrcPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxMcacBdlChlNgSrcPfxLen_Object = MibTableColumn
tmnxMcacBdlChlNgSrcPfxLen = _TmnxMcacBdlChlNgSrcPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 7),
    _TmnxMcacBdlChlNgSrcPfxLen_Type()
)
tmnxMcacBdlChlNgSrcPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgSrcPfxLen.setStatus("current")
_TmnxMcacBdlChlNgRowStatus_Type = RowStatus
_TmnxMcacBdlChlNgRowStatus_Object = MibTableColumn
tmnxMcacBdlChlNgRowStatus = _TmnxMcacBdlChlNgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 8),
    _TmnxMcacBdlChlNgRowStatus_Type()
)
tmnxMcacBdlChlNgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgRowStatus.setStatus("current")


class _TmnxMcacBdlChlNgBW_Type(Unsigned32):
    """Custom type tmnxMcacBdlChlNgBW based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_TmnxMcacBdlChlNgBW_Type.__name__ = "Unsigned32"
_TmnxMcacBdlChlNgBW_Object = MibTableColumn
tmnxMcacBdlChlNgBW = _TmnxMcacBdlChlNgBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 9),
    _TmnxMcacBdlChlNgBW_Type()
)
tmnxMcacBdlChlNgBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgBW.setUnits("kbps")


class _TmnxMcacBdlChlNgClass_Type(TmnxMcacChlClassTc):
    """Custom type tmnxMcacBdlChlNgClass based on TmnxMcacChlClassTc"""
    defaultValue = 1


_TmnxMcacBdlChlNgClass_Type.__name__ = "TmnxMcacChlClassTc"
_TmnxMcacBdlChlNgClass_Object = MibTableColumn
tmnxMcacBdlChlNgClass = _TmnxMcacBdlChlNgClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 10),
    _TmnxMcacBdlChlNgClass_Type()
)
tmnxMcacBdlChlNgClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgClass.setStatus("current")


class _TmnxMcacBdlChlNgType_Type(TmnxMcacChlTypeTc):
    """Custom type tmnxMcacBdlChlNgType based on TmnxMcacChlTypeTc"""
    defaultValue = 1


_TmnxMcacBdlChlNgType_Type.__name__ = "TmnxMcacChlTypeTc"
_TmnxMcacBdlChlNgType_Object = MibTableColumn
tmnxMcacBdlChlNgType = _TmnxMcacBdlChlNgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 12, 1, 11),
    _TmnxMcacBdlChlNgType_Type()
)
tmnxMcacBdlChlNgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcacBdlChlNgType.setStatus("current")
_TmnxMcacStatsNgTable_Object = MibTable
tmnxMcacStatsNgTable = _TmnxMcacStatsNgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13)
)
if mibBuilder.loadTexts:
    tmnxMcacStatsNgTable.setStatus("current")
_TmnxMcacStatsNgEntry_Object = MibTableRow
tmnxMcacStatsNgEntry = _TmnxMcacStatsNgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1)
)
tmnxMcacStatsNgEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgBundleName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgIfIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgChlAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgChlAddr"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgSrcAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgSrcAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcacStatsNgEntry.setStatus("current")
_TmnxMcacStatsNgBundleName_Type = TNamedItemOrEmpty
_TmnxMcacStatsNgBundleName_Object = MibTableColumn
tmnxMcacStatsNgBundleName = _TmnxMcacStatsNgBundleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 1),
    _TmnxMcacStatsNgBundleName_Type()
)
tmnxMcacStatsNgBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgBundleName.setStatus("current")
_TmnxMcacStatsNgProtocolIndex_Type = TmnxMcacApplTc
_TmnxMcacStatsNgProtocolIndex_Object = MibTableColumn
tmnxMcacStatsNgProtocolIndex = _TmnxMcacStatsNgProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 2),
    _TmnxMcacStatsNgProtocolIndex_Type()
)
tmnxMcacStatsNgProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgProtocolIndex.setStatus("current")
_TmnxMcacStatsNgIfIndex_Type = InterfaceIndex
_TmnxMcacStatsNgIfIndex_Object = MibTableColumn
tmnxMcacStatsNgIfIndex = _TmnxMcacStatsNgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 3),
    _TmnxMcacStatsNgIfIndex_Type()
)
tmnxMcacStatsNgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgIfIndex.setStatus("current")
_TmnxMcacStatsNgChlAddrType_Type = InetAddressType
_TmnxMcacStatsNgChlAddrType_Object = MibTableColumn
tmnxMcacStatsNgChlAddrType = _TmnxMcacStatsNgChlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 4),
    _TmnxMcacStatsNgChlAddrType_Type()
)
tmnxMcacStatsNgChlAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgChlAddrType.setStatus("current")


class _TmnxMcacStatsNgChlAddr_Type(InetAddress):
    """Custom type tmnxMcacStatsNgChlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcacStatsNgChlAddr_Type.__name__ = "InetAddress"
_TmnxMcacStatsNgChlAddr_Object = MibTableColumn
tmnxMcacStatsNgChlAddr = _TmnxMcacStatsNgChlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 5),
    _TmnxMcacStatsNgChlAddr_Type()
)
tmnxMcacStatsNgChlAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgChlAddr.setStatus("current")


class _TmnxMcacStatsNgSrcAddrType_Type(InetAddressType):
    """Custom type tmnxMcacStatsNgSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcacStatsNgSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxMcacStatsNgSrcAddrType_Object = MibTableColumn
tmnxMcacStatsNgSrcAddrType = _TmnxMcacStatsNgSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 6),
    _TmnxMcacStatsNgSrcAddrType_Type()
)
tmnxMcacStatsNgSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgSrcAddrType.setStatus("current")


class _TmnxMcacStatsNgSrcAddr_Type(InetAddress):
    """Custom type tmnxMcacStatsNgSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMcacStatsNgSrcAddr_Type.__name__ = "InetAddress"
_TmnxMcacStatsNgSrcAddr_Object = MibTableColumn
tmnxMcacStatsNgSrcAddr = _TmnxMcacStatsNgSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 7),
    _TmnxMcacStatsNgSrcAddr_Type()
)
tmnxMcacStatsNgSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgSrcAddr.setStatus("current")
_TmnxMcacStatsNgAction_Type = TmnxMcacActionTc
_TmnxMcacStatsNgAction_Object = MibTableColumn
tmnxMcacStatsNgAction = _TmnxMcacStatsNgAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 8),
    _TmnxMcacStatsNgAction_Type()
)
tmnxMcacStatsNgAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgAction.setStatus("current")
_TmnxMcacStatsNgReason_Type = TmnxMcacReasonTc
_TmnxMcacStatsNgReason_Object = MibTableColumn
tmnxMcacStatsNgReason = _TmnxMcacStatsNgReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 9),
    _TmnxMcacStatsNgReason_Type()
)
tmnxMcacStatsNgReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgReason.setStatus("current")
_TmnxMcacStatsNgChannelType_Type = TmnxMcacChlTypeTc
_TmnxMcacStatsNgChannelType_Object = MibTableColumn
tmnxMcacStatsNgChannelType = _TmnxMcacStatsNgChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 10),
    _TmnxMcacStatsNgChannelType_Type()
)
tmnxMcacStatsNgChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgChannelType.setStatus("current")
_TmnxMcacStatsNgChannelBW_Type = Unsigned32
_TmnxMcacStatsNgChannelBW_Object = MibTableColumn
tmnxMcacStatsNgChannelBW = _TmnxMcacStatsNgChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 11),
    _TmnxMcacStatsNgChannelBW_Type()
)
tmnxMcacStatsNgChannelBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgChannelBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgChannelBW.setUnits("kbps")
_TmnxMcacStatsNgBundleAvailBW_Type = Unsigned32
_TmnxMcacStatsNgBundleAvailBW_Object = MibTableColumn
tmnxMcacStatsNgBundleAvailBW = _TmnxMcacStatsNgBundleAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 12),
    _TmnxMcacStatsNgBundleAvailBW_Type()
)
tmnxMcacStatsNgBundleAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgBundleAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgBundleAvailBW.setUnits("kbps")
_TmnxMcacStatsNgIntfAvailBW_Type = Unsigned32
_TmnxMcacStatsNgIntfAvailBW_Object = MibTableColumn
tmnxMcacStatsNgIntfAvailBW = _TmnxMcacStatsNgIntfAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 13),
    _TmnxMcacStatsNgIntfAvailBW_Type()
)
tmnxMcacStatsNgIntfAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgIntfAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgIntfAvailBW.setUnits("kbps")
_TmnxMcacStatsNgAlgoReapply_Type = TruthValue
_TmnxMcacStatsNgAlgoReapply_Object = MibTableColumn
tmnxMcacStatsNgAlgoReapply = _TmnxMcacStatsNgAlgoReapply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 14),
    _TmnxMcacStatsNgAlgoReapply_Type()
)
tmnxMcacStatsNgAlgoReapply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgAlgoReapply.setStatus("current")
_TmnxMcacStatsNgApplyAttempts_Type = Counter32
_TmnxMcacStatsNgApplyAttempts_Object = MibTableColumn
tmnxMcacStatsNgApplyAttempts = _TmnxMcacStatsNgApplyAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 15),
    _TmnxMcacStatsNgApplyAttempts_Type()
)
tmnxMcacStatsNgApplyAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgApplyAttempts.setStatus("current")
_TmnxMcacStatsNgTimeStamp_Type = TimeStamp
_TmnxMcacStatsNgTimeStamp_Object = MibTableColumn
tmnxMcacStatsNgTimeStamp = _TmnxMcacStatsNgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 13, 1, 16),
    _TmnxMcacStatsNgTimeStamp_Type()
)
tmnxMcacStatsNgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacStatsNgTimeStamp.setStatus("current")
_TmnxMcacServStatsNgTable_Object = MibTable
tmnxMcacServStatsNgTable = _TmnxMcacServStatsNgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14)
)
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgTable.setStatus("current")
_TmnxMcacServStatsNgEntry_Object = MibTableRow
tmnxMcacServStatsNgEntry = _TmnxMcacServStatsNgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1)
)
tmnxMcacServStatsNgEntry.setIndexNames(
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyName"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgBundleName"),
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgProtocolIndex"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgPortId"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgChlAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgChlAddr"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgSrcAddrType"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgSrcAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgEntry.setStatus("current")
_TmnxMcacServStatsNgPortId_Type = TmnxPortID
_TmnxMcacServStatsNgPortId_Object = MibTableColumn
tmnxMcacServStatsNgPortId = _TmnxMcacServStatsNgPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 1),
    _TmnxMcacServStatsNgPortId_Type()
)
tmnxMcacServStatsNgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgPortId.setStatus("current")
_TmnxMcacServStatsNgEncapValue_Type = TmnxEncapVal
_TmnxMcacServStatsNgEncapValue_Object = MibTableColumn
tmnxMcacServStatsNgEncapValue = _TmnxMcacServStatsNgEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 2),
    _TmnxMcacServStatsNgEncapValue_Type()
)
tmnxMcacServStatsNgEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgEncapValue.setStatus("current")
_TmnxMcacServStatsNgAction_Type = TmnxMcacActionTc
_TmnxMcacServStatsNgAction_Object = MibTableColumn
tmnxMcacServStatsNgAction = _TmnxMcacServStatsNgAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 3),
    _TmnxMcacServStatsNgAction_Type()
)
tmnxMcacServStatsNgAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgAction.setStatus("current")
_TmnxMcacServStatsNgReason_Type = TmnxMcacReasonTc
_TmnxMcacServStatsNgReason_Object = MibTableColumn
tmnxMcacServStatsNgReason = _TmnxMcacServStatsNgReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 4),
    _TmnxMcacServStatsNgReason_Type()
)
tmnxMcacServStatsNgReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgReason.setStatus("current")
_TmnxMcacServStatsNgChannelType_Type = TmnxMcacChlTypeTc
_TmnxMcacServStatsNgChannelType_Object = MibTableColumn
tmnxMcacServStatsNgChannelType = _TmnxMcacServStatsNgChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 5),
    _TmnxMcacServStatsNgChannelType_Type()
)
tmnxMcacServStatsNgChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgChannelType.setStatus("current")
_TmnxMcacServStatsNgChannelBW_Type = Unsigned32
_TmnxMcacServStatsNgChannelBW_Object = MibTableColumn
tmnxMcacServStatsNgChannelBW = _TmnxMcacServStatsNgChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 6),
    _TmnxMcacServStatsNgChannelBW_Type()
)
tmnxMcacServStatsNgChannelBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgChannelBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgChannelBW.setUnits("kbps")
_TmnxMcacServStatsNgBundleAvailBW_Type = Unsigned32
_TmnxMcacServStatsNgBundleAvailBW_Object = MibTableColumn
tmnxMcacServStatsNgBundleAvailBW = _TmnxMcacServStatsNgBundleAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 7),
    _TmnxMcacServStatsNgBundleAvailBW_Type()
)
tmnxMcacServStatsNgBundleAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgBundleAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgBundleAvailBW.setUnits("kbps")
_TmnxMcacServStatsNgIntfAvailBW_Type = Unsigned32
_TmnxMcacServStatsNgIntfAvailBW_Object = MibTableColumn
tmnxMcacServStatsNgIntfAvailBW = _TmnxMcacServStatsNgIntfAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 8),
    _TmnxMcacServStatsNgIntfAvailBW_Type()
)
tmnxMcacServStatsNgIntfAvailBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgIntfAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgIntfAvailBW.setUnits("kbps")
_TmnxMcacServStatsNgAlgoReapply_Type = TruthValue
_TmnxMcacServStatsNgAlgoReapply_Object = MibTableColumn
tmnxMcacServStatsNgAlgoReapply = _TmnxMcacServStatsNgAlgoReapply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 9),
    _TmnxMcacServStatsNgAlgoReapply_Type()
)
tmnxMcacServStatsNgAlgoReapply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgAlgoReapply.setStatus("current")
_TmnxMcacServStatsNgApplyAttempts_Type = Counter32
_TmnxMcacServStatsNgApplyAttempts_Object = MibTableColumn
tmnxMcacServStatsNgApplyAttempts = _TmnxMcacServStatsNgApplyAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 10),
    _TmnxMcacServStatsNgApplyAttempts_Type()
)
tmnxMcacServStatsNgApplyAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgApplyAttempts.setStatus("current")
_TmnxMcacServStatsNgTimeStamp_Type = TimeStamp
_TmnxMcacServStatsNgTimeStamp_Object = MibTableColumn
tmnxMcacServStatsNgTimeStamp = _TmnxMcacServStatsNgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 41, 14, 1, 11),
    _TmnxMcacServStatsNgTimeStamp_Type()
)
tmnxMcacServStatsNgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcacServStatsNgTimeStamp.setStatus("current")

# Managed Objects groups

tmnxMcacV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 2, 1)
)
tmnxMcacV5v0Group.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyRowStatus"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyDescription"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyDefaultAction"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleRowStatus"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleDescription"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleAdminState"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleBandwidth"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlRowStatus"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlClass"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlType"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelRowStatus"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagRowStatus"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagBundleLevel"))
)
if mibBuilder.loadTexts:
    tmnxMcacV5v0Group.setStatus("current")

tmnxMcacStatV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 2, 2)
)
tmnxMcacStatV5v0Group.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsAction"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsReason"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsChannelType"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsChannelBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsBundleAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsIntfAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsAlgoReapply"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsApplyAttempts"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsTimeStamp"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsAction"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsReason"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsChannelType"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsChannelBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsBundleAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsIntfAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsAlgoReapply"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsApplyAttempts"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsTimeStamp"))
)
if mibBuilder.loadTexts:
    tmnxMcacStatV5v0Group.setStatus("current")

tmnxMcacOperV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 2, 3)
)
tmnxMcacOperV5v0Group.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperActiveChannels"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperMaxBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperAvailOptnlBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperAvailMandBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperInUseMandBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperPortsDown"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperCurrConstrtLvl"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperInUseOptnlBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperValuesInTransit"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperActiveChannels"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperMaxBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperAvailOptnlBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperAvailMandBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperInUseMandBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperPortsDown"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperCurrConstrtLvl"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperInUseOptnlBw"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServOperValuesInTransit"))
)
if mibBuilder.loadTexts:
    tmnxMcacOperV5v0Group.setStatus("current")

tmnxMcacPolicyUserV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 2, 4)
)
tmnxMcacPolicyUserV5v0Group.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyUserConfigured"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyServUserConfigured"))
)
if mibBuilder.loadTexts:
    tmnxMcacPolicyUserV5v0Group.setStatus("current")

tmnxMcacV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 2, 5)
)
tmnxMcacV12v0Group.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgRowStatus"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgClass"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBdlChlNgType"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacBundleUseLagPortWeight"))
)
if mibBuilder.loadTexts:
    tmnxMcacV12v0Group.setStatus("current")

tmnxMcacStatV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 2, 6)
)
tmnxMcacStatV12v0Group.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgAction"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgReason"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgChannelType"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgChannelBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgBundleAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgIntfAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgAlgoReapply"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgApplyAttempts"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatsNgTimeStamp"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgAction"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgReason"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgChannelType"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgChannelBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgBundleAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgIntfAvailBW"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgAlgoReapply"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgApplyAttempts"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacServStatsNgTimeStamp"))
)
if mibBuilder.loadTexts:
    tmnxMcacStatV12v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxMcacV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 1, 1)
)
tmnxMcacV5v0Compliance.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyUserV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcacV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcacV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 1, 2)
)
tmnxMcacV6v0Compliance.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyUserV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcacV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcacV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 41, 1, 3)
)
tmnxMcacV12v0Compliance.setObjects(
      *(("TIMETRA-MCAST-CAC-MIB", "tmnxMcacV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacV12v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacStatV12v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacOperV5v0Group"),
        ("TIMETRA-MCAST-CAC-MIB", "tmnxMcacPolicyUserV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcacV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MCAST-CAC-MIB",
    **{"TmnxMcacActionTc": TmnxMcacActionTc,
       "TmnxMcacReasonTc": TmnxMcacReasonTc,
       "TmnxMcacApplTc": TmnxMcacApplTc,
       "TmnxMcacChlTypeTc": TmnxMcacChlTypeTc,
       "TmnxMcacChlClassTc": TmnxMcacChlClassTc,
       "timetraMcastCacMIBModule": timetraMcastCacMIBModule,
       "tmnxMcacConformance": tmnxMcacConformance,
       "tmnxMcacCompliances": tmnxMcacCompliances,
       "tmnxMcacV5v0Compliance": tmnxMcacV5v0Compliance,
       "tmnxMcacV6v0Compliance": tmnxMcacV6v0Compliance,
       "tmnxMcacV12v0Compliance": tmnxMcacV12v0Compliance,
       "tmnxMcacGroups": tmnxMcacGroups,
       "tmnxMcacV5v0Group": tmnxMcacV5v0Group,
       "tmnxMcacStatV5v0Group": tmnxMcacStatV5v0Group,
       "tmnxMcacOperV5v0Group": tmnxMcacOperV5v0Group,
       "tmnxMcacPolicyUserV5v0Group": tmnxMcacPolicyUserV5v0Group,
       "tmnxMcacV12v0Group": tmnxMcacV12v0Group,
       "tmnxMcacStatV12v0Group": tmnxMcacStatV12v0Group,
       "tmnxMcacObjects": tmnxMcacObjects,
       "tmnxMcacPolicyTable": tmnxMcacPolicyTable,
       "tmnxMcacPolicyEntry": tmnxMcacPolicyEntry,
       "tmnxMcacPolicyName": tmnxMcacPolicyName,
       "tmnxMcacPolicyRowStatus": tmnxMcacPolicyRowStatus,
       "tmnxMcacPolicyDescription": tmnxMcacPolicyDescription,
       "tmnxMcacPolicyDefaultAction": tmnxMcacPolicyDefaultAction,
       "tmnxMcacBundleTable": tmnxMcacBundleTable,
       "tmnxMcacBundleEntry": tmnxMcacBundleEntry,
       "tmnxMcacBundleName": tmnxMcacBundleName,
       "tmnxMcacBundleRowStatus": tmnxMcacBundleRowStatus,
       "tmnxMcacBundleDescription": tmnxMcacBundleDescription,
       "tmnxMcacBundleAdminState": tmnxMcacBundleAdminState,
       "tmnxMcacBundleBandwidth": tmnxMcacBundleBandwidth,
       "tmnxMcacBundleUseLagPortWeight": tmnxMcacBundleUseLagPortWeight,
       "tmnxMcacBdlChlTable": tmnxMcacBdlChlTable,
       "tmnxMcacBdlChlEntry": tmnxMcacBdlChlEntry,
       "tmnxMcacBdlChlStartAddrType": tmnxMcacBdlChlStartAddrType,
       "tmnxMcacBdlChlStartAddr": tmnxMcacBdlChlStartAddr,
       "tmnxMcacBdlChlEndAddrType": tmnxMcacBdlChlEndAddrType,
       "tmnxMcacBdlChlEndAddr": tmnxMcacBdlChlEndAddr,
       "tmnxMcacBdlChlRowStatus": tmnxMcacBdlChlRowStatus,
       "tmnxMcacBdlChlBW": tmnxMcacBdlChlBW,
       "tmnxMcacBdlChlClass": tmnxMcacBdlChlClass,
       "tmnxMcacBdlChlType": tmnxMcacBdlChlType,
       "tmnxMcacLevelTable": tmnxMcacLevelTable,
       "tmnxMcacLevelEntry": tmnxMcacLevelEntry,
       "tmnxMcacLevelId": tmnxMcacLevelId,
       "tmnxMcacLevelRowStatus": tmnxMcacLevelRowStatus,
       "tmnxMcacLevelBW": tmnxMcacLevelBW,
       "tmnxMcacLagTable": tmnxMcacLagTable,
       "tmnxMcacLagEntry": tmnxMcacLagEntry,
       "tmnxMcacLagPortsDown": tmnxMcacLagPortsDown,
       "tmnxMcacLagRowStatus": tmnxMcacLagRowStatus,
       "tmnxMcacLagBundleLevel": tmnxMcacLagBundleLevel,
       "tmnxMcacStatsTable": tmnxMcacStatsTable,
       "tmnxMcacStatsEntry": tmnxMcacStatsEntry,
       "tmnxMcacStatsBundleName": tmnxMcacStatsBundleName,
       "tmnxMcacStatsProtocolIndex": tmnxMcacStatsProtocolIndex,
       "tmnxMcacStatsIfIndex": tmnxMcacStatsIfIndex,
       "tmnxMcacStatsChlAddrType": tmnxMcacStatsChlAddrType,
       "tmnxMcacStatsChlAddr": tmnxMcacStatsChlAddr,
       "tmnxMcacStatsAction": tmnxMcacStatsAction,
       "tmnxMcacStatsReason": tmnxMcacStatsReason,
       "tmnxMcacStatsChannelType": tmnxMcacStatsChannelType,
       "tmnxMcacStatsChannelBW": tmnxMcacStatsChannelBW,
       "tmnxMcacStatsBundleAvailBW": tmnxMcacStatsBundleAvailBW,
       "tmnxMcacStatsIntfAvailBW": tmnxMcacStatsIntfAvailBW,
       "tmnxMcacStatsAlgoReapply": tmnxMcacStatsAlgoReapply,
       "tmnxMcacStatsApplyAttempts": tmnxMcacStatsApplyAttempts,
       "tmnxMcacStatsTimeStamp": tmnxMcacStatsTimeStamp,
       "tmnxMcacOperTable": tmnxMcacOperTable,
       "tmnxMcacOperEntry": tmnxMcacOperEntry,
       "tmnxMcacOperActiveChannels": tmnxMcacOperActiveChannels,
       "tmnxMcacOperMaxBw": tmnxMcacOperMaxBw,
       "tmnxMcacOperAvailOptnlBw": tmnxMcacOperAvailOptnlBw,
       "tmnxMcacOperAvailMandBw": tmnxMcacOperAvailMandBw,
       "tmnxMcacOperInUseMandBw": tmnxMcacOperInUseMandBw,
       "tmnxMcacOperPortsDown": tmnxMcacOperPortsDown,
       "tmnxMcacOperCurrConstrtLvl": tmnxMcacOperCurrConstrtLvl,
       "tmnxMcacOperInUseOptnlBw": tmnxMcacOperInUseOptnlBw,
       "tmnxMcacOperValuesInTransit": tmnxMcacOperValuesInTransit,
       "tmnxMcacServStatsTable": tmnxMcacServStatsTable,
       "tmnxMcacServStatsEntry": tmnxMcacServStatsEntry,
       "tmnxMcacServStatsPortId": tmnxMcacServStatsPortId,
       "tmnxMcacServStatsEncapValue": tmnxMcacServStatsEncapValue,
       "tmnxMcacServStatsAction": tmnxMcacServStatsAction,
       "tmnxMcacServStatsReason": tmnxMcacServStatsReason,
       "tmnxMcacServStatsChannelType": tmnxMcacServStatsChannelType,
       "tmnxMcacServStatsChannelBW": tmnxMcacServStatsChannelBW,
       "tmnxMcacServStatsBundleAvailBW": tmnxMcacServStatsBundleAvailBW,
       "tmnxMcacServStatsIntfAvailBW": tmnxMcacServStatsIntfAvailBW,
       "tmnxMcacServStatsAlgoReapply": tmnxMcacServStatsAlgoReapply,
       "tmnxMcacServStatsApplyAttempts": tmnxMcacServStatsApplyAttempts,
       "tmnxMcacServStatsTimeStamp": tmnxMcacServStatsTimeStamp,
       "tmnxMcacServOperTable": tmnxMcacServOperTable,
       "tmnxMcacServOperEntry": tmnxMcacServOperEntry,
       "tmnxMcacServOperActiveChannels": tmnxMcacServOperActiveChannels,
       "tmnxMcacServOperMaxBw": tmnxMcacServOperMaxBw,
       "tmnxMcacServOperAvailOptnlBw": tmnxMcacServOperAvailOptnlBw,
       "tmnxMcacServOperAvailMandBw": tmnxMcacServOperAvailMandBw,
       "tmnxMcacServOperInUseMandBw": tmnxMcacServOperInUseMandBw,
       "tmnxMcacServOperPortsDown": tmnxMcacServOperPortsDown,
       "tmnxMcacServOperCurrConstrtLvl": tmnxMcacServOperCurrConstrtLvl,
       "tmnxMcacServOperInUseOptnlBw": tmnxMcacServOperInUseOptnlBw,
       "tmnxMcacServOperValuesInTransit": tmnxMcacServOperValuesInTransit,
       "tmnxMcacPolicyUserTable": tmnxMcacPolicyUserTable,
       "tmnxMcacPolicyUserEntry": tmnxMcacPolicyUserEntry,
       "tmnxMcacPolicyUserConfigured": tmnxMcacPolicyUserConfigured,
       "tmnxMcacPolicyServUserTable": tmnxMcacPolicyServUserTable,
       "tmnxMcacPolicyServUserEntry": tmnxMcacPolicyServUserEntry,
       "tmnxMcacPolicyServUserConfigured": tmnxMcacPolicyServUserConfigured,
       "tmnxMcacBdlChlNgTable": tmnxMcacBdlChlNgTable,
       "tmnxMcacBdlChlNgEntry": tmnxMcacBdlChlNgEntry,
       "tmnxMcacBdlChlNgStartAddrType": tmnxMcacBdlChlNgStartAddrType,
       "tmnxMcacBdlChlNgStartAddr": tmnxMcacBdlChlNgStartAddr,
       "tmnxMcacBdlChlNgEndAddrType": tmnxMcacBdlChlNgEndAddrType,
       "tmnxMcacBdlChlNgEndAddr": tmnxMcacBdlChlNgEndAddr,
       "tmnxMcacBdlChlNgSrcPfxType": tmnxMcacBdlChlNgSrcPfxType,
       "tmnxMcacBdlChlNgSrcPfx": tmnxMcacBdlChlNgSrcPfx,
       "tmnxMcacBdlChlNgSrcPfxLen": tmnxMcacBdlChlNgSrcPfxLen,
       "tmnxMcacBdlChlNgRowStatus": tmnxMcacBdlChlNgRowStatus,
       "tmnxMcacBdlChlNgBW": tmnxMcacBdlChlNgBW,
       "tmnxMcacBdlChlNgClass": tmnxMcacBdlChlNgClass,
       "tmnxMcacBdlChlNgType": tmnxMcacBdlChlNgType,
       "tmnxMcacStatsNgTable": tmnxMcacStatsNgTable,
       "tmnxMcacStatsNgEntry": tmnxMcacStatsNgEntry,
       "tmnxMcacStatsNgBundleName": tmnxMcacStatsNgBundleName,
       "tmnxMcacStatsNgProtocolIndex": tmnxMcacStatsNgProtocolIndex,
       "tmnxMcacStatsNgIfIndex": tmnxMcacStatsNgIfIndex,
       "tmnxMcacStatsNgChlAddrType": tmnxMcacStatsNgChlAddrType,
       "tmnxMcacStatsNgChlAddr": tmnxMcacStatsNgChlAddr,
       "tmnxMcacStatsNgSrcAddrType": tmnxMcacStatsNgSrcAddrType,
       "tmnxMcacStatsNgSrcAddr": tmnxMcacStatsNgSrcAddr,
       "tmnxMcacStatsNgAction": tmnxMcacStatsNgAction,
       "tmnxMcacStatsNgReason": tmnxMcacStatsNgReason,
       "tmnxMcacStatsNgChannelType": tmnxMcacStatsNgChannelType,
       "tmnxMcacStatsNgChannelBW": tmnxMcacStatsNgChannelBW,
       "tmnxMcacStatsNgBundleAvailBW": tmnxMcacStatsNgBundleAvailBW,
       "tmnxMcacStatsNgIntfAvailBW": tmnxMcacStatsNgIntfAvailBW,
       "tmnxMcacStatsNgAlgoReapply": tmnxMcacStatsNgAlgoReapply,
       "tmnxMcacStatsNgApplyAttempts": tmnxMcacStatsNgApplyAttempts,
       "tmnxMcacStatsNgTimeStamp": tmnxMcacStatsNgTimeStamp,
       "tmnxMcacServStatsNgTable": tmnxMcacServStatsNgTable,
       "tmnxMcacServStatsNgEntry": tmnxMcacServStatsNgEntry,
       "tmnxMcacServStatsNgPortId": tmnxMcacServStatsNgPortId,
       "tmnxMcacServStatsNgEncapValue": tmnxMcacServStatsNgEncapValue,
       "tmnxMcacServStatsNgAction": tmnxMcacServStatsNgAction,
       "tmnxMcacServStatsNgReason": tmnxMcacServStatsNgReason,
       "tmnxMcacServStatsNgChannelType": tmnxMcacServStatsNgChannelType,
       "tmnxMcacServStatsNgChannelBW": tmnxMcacServStatsNgChannelBW,
       "tmnxMcacServStatsNgBundleAvailBW": tmnxMcacServStatsNgBundleAvailBW,
       "tmnxMcacServStatsNgIntfAvailBW": tmnxMcacServStatsNgIntfAvailBW,
       "tmnxMcacServStatsNgAlgoReapply": tmnxMcacServStatsNgAlgoReapply,
       "tmnxMcacServStatsNgApplyAttempts": tmnxMcacServStatsNgApplyAttempts,
       "tmnxMcacServStatsNgTimeStamp": tmnxMcacServStatsNgTimeStamp}
)
