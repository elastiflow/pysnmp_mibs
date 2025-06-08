# SNMP MIB module (TIMETRA-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-PPPOE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:32 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
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

(TmnxPppCpState,) = mibBuilder.importSymbols(
    "TIMETRA-PPP-MIB",
    "TmnxPppCpState")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(iesIfIndex,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "iesIfIndex",
    "svcId")

(tmnxSubPppIndex,) = mibBuilder.importSymbols(
    "TIMETRA-SUBSCRIBER-MGMT-MIB",
    "tmnxSubPppIndex")

(BgpPeeringStatus,
 TBurstSizeBytesOverride,
 TCIRRateOverride,
 TDirection,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRateOverride,
 TPolicyStatementNameOrEmpty,
 TQosOverrideType,
 TmnxAccessLoopEncapDataLink,
 TmnxAccessLoopEncaps1,
 TmnxAccessLoopEncaps2,
 TmnxAncpStringOrZero,
 TmnxAppProfileStringOrEmpty,
 TmnxAuthPassword,
 TmnxBgpAutonomousSystem,
 TmnxDhcpOptionType,
 TmnxManagedRouteStatus,
 TmnxMlpppEpClass,
 TmnxPppoePadoDelay,
 TmnxPppoeSessionId,
 TmnxPppoeSessionInfoOrigin,
 TmnxPppoeSessionType,
 TmnxPppoeUserNameOrEmpty,
 TmnxServId,
 TmnxSlaProfileStringOrEmpty,
 TmnxSubIdentStringOrEmpty,
 TmnxSubMgtIntDestIdOrEmpty,
 TmnxSubProfileStringOrEmpty,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "BgpPeeringStatus",
    "TBurstSizeBytesOverride",
    "TCIRRateOverride",
    "TDirection",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRateOverride",
    "TPolicyStatementNameOrEmpty",
    "TQosOverrideType",
    "TmnxAccessLoopEncapDataLink",
    "TmnxAccessLoopEncaps1",
    "TmnxAccessLoopEncaps2",
    "TmnxAncpStringOrZero",
    "TmnxAppProfileStringOrEmpty",
    "TmnxAuthPassword",
    "TmnxBgpAutonomousSystem",
    "TmnxDhcpOptionType",
    "TmnxManagedRouteStatus",
    "TmnxMlpppEpClass",
    "TmnxPppoePadoDelay",
    "TmnxPppoeSessionId",
    "TmnxPppoeSessionInfoOrigin",
    "TmnxPppoeSessionType",
    "TmnxPppoeUserNameOrEmpty",
    "TmnxServId",
    "TmnxSlaProfileStringOrEmpty",
    "TmnxSubIdentStringOrEmpty",
    "TmnxSubMgtIntDestIdOrEmpty",
    "TmnxSubProfileStringOrEmpty",
    "TmnxVRtrIDOrZero")


# MODULE-IDENTITY

timetraPppoeMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 49)
)
if mibBuilder.loadTexts:
    timetraPppoeMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2009-02-28 00:00",
         "2011-02-01 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPppoeAdminStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_TmnxPppoeConformance_ObjectIdentity = ObjectIdentity
tmnxPppoeConformance = _TmnxPppoeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49)
)
_TmnxPppoeCompliances_ObjectIdentity = ObjectIdentity
tmnxPppoeCompliances = _TmnxPppoeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1)
)
_TmnxPppoeGroups_ObjectIdentity = ObjectIdentity
tmnxPppoeGroups = _TmnxPppoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2)
)
_TmnxPppoe_ObjectIdentity = ObjectIdentity
tmnxPppoe = _TmnxPppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49)
)
_TmnxPppoeObjects_ObjectIdentity = ObjectIdentity
tmnxPppoeObjects = _TmnxPppoeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1)
)
_TmnxPppoePlcyTableLastChanged_Type = TimeStamp
_TmnxPppoePlcyTableLastChanged_Object = MibScalar
tmnxPppoePlcyTableLastChanged = _TmnxPppoePlcyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 1),
    _TmnxPppoePlcyTableLastChanged_Type()
)
tmnxPppoePlcyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoePlcyTableLastChanged.setStatus("current")
_TmnxPppoePlcyTable_Object = MibTable
tmnxPppoePlcyTable = _TmnxPppoePlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxPppoePlcyTable.setStatus("current")
_TmnxPppoePlcyEntry_Object = MibTableRow
tmnxPppoePlcyEntry = _TmnxPppoePlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1)
)
tmnxPppoePlcyEntry.setIndexNames(
    (1, "TIMETRA-PPPOE-MIB", "tmnxPppoePlcyName"),
)
if mibBuilder.loadTexts:
    tmnxPppoePlcyEntry.setStatus("current")
_TmnxPppoePlcyName_Type = TNamedItem
_TmnxPppoePlcyName_Object = MibTableColumn
tmnxPppoePlcyName = _TmnxPppoePlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 1),
    _TmnxPppoePlcyName_Type()
)
tmnxPppoePlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoePlcyName.setStatus("current")
_TmnxPppoePlcyRowStatus_Type = RowStatus
_TmnxPppoePlcyRowStatus_Object = MibTableColumn
tmnxPppoePlcyRowStatus = _TmnxPppoePlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 2),
    _TmnxPppoePlcyRowStatus_Type()
)
tmnxPppoePlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyRowStatus.setStatus("current")
_TmnxPppoePlcyLastMgmtChange_Type = TimeStamp
_TmnxPppoePlcyLastMgmtChange_Object = MibTableColumn
tmnxPppoePlcyLastMgmtChange = _TmnxPppoePlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 3),
    _TmnxPppoePlcyLastMgmtChange_Type()
)
tmnxPppoePlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoePlcyLastMgmtChange.setStatus("current")


class _TmnxPppoePlcyDescription_Type(TItemDescription):
    """Custom type tmnxPppoePlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxPppoePlcyDescription_Type.__name__ = "TItemDescription"
_TmnxPppoePlcyDescription_Object = MibTableColumn
tmnxPppoePlcyDescription = _TmnxPppoePlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 4),
    _TmnxPppoePlcyDescription_Type()
)
tmnxPppoePlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyDescription.setStatus("current")


class _TmnxPppoePlcyPppMtu_Type(Unsigned32):
    """Custom type tmnxPppoePlcyPppMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9212),
    )


_TmnxPppoePlcyPppMtu_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyPppMtu_Object = MibTableColumn
tmnxPppoePlcyPppMtu = _TmnxPppoePlcyPppMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 5),
    _TmnxPppoePlcyPppMtu_Type()
)
tmnxPppoePlcyPppMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppMtu.setStatus("current")


class _TmnxPppoePlcyLcpKaInterval_Type(Unsigned32):
    """Custom type tmnxPppoePlcyLcpKaInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 300),
    )


_TmnxPppoePlcyLcpKaInterval_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyLcpKaInterval_Object = MibTableColumn
tmnxPppoePlcyLcpKaInterval = _TmnxPppoePlcyLcpKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 6),
    _TmnxPppoePlcyLcpKaInterval_Type()
)
tmnxPppoePlcyLcpKaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyLcpKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppoePlcyLcpKaInterval.setUnits("seconds")


class _TmnxPppoePlcyLcpKaHoldUpMplier_Type(Unsigned32):
    """Custom type tmnxPppoePlcyLcpKaHoldUpMplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxPppoePlcyLcpKaHoldUpMplier_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyLcpKaHoldUpMplier_Object = MibTableColumn
tmnxPppoePlcyLcpKaHoldUpMplier = _TmnxPppoePlcyLcpKaHoldUpMplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 7),
    _TmnxPppoePlcyLcpKaHoldUpMplier_Type()
)
tmnxPppoePlcyLcpKaHoldUpMplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyLcpKaHoldUpMplier.setStatus("current")


class _TmnxPppoePlcyDisableAcCookies_Type(TruthValue):
    """Custom type tmnxPppoePlcyDisableAcCookies based on TruthValue"""
    defaultValue = 2


_TmnxPppoePlcyDisableAcCookies_Type.__name__ = "TruthValue"
_TmnxPppoePlcyDisableAcCookies_Object = MibTableColumn
tmnxPppoePlcyDisableAcCookies = _TmnxPppoePlcyDisableAcCookies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 8),
    _TmnxPppoePlcyDisableAcCookies_Type()
)
tmnxPppoePlcyDisableAcCookies.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyDisableAcCookies.setStatus("current")


class _TmnxPppoePlcyPadoDelay_Type(TmnxPppoePadoDelay):
    """Custom type tmnxPppoePlcyPadoDelay based on TmnxPppoePadoDelay"""
    defaultValue = 0


_TmnxPppoePlcyPadoDelay_Type.__name__ = "TmnxPppoePadoDelay"
_TmnxPppoePlcyPadoDelay_Object = MibTableColumn
tmnxPppoePlcyPadoDelay = _TmnxPppoePlcyPadoDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 9),
    _TmnxPppoePlcyPadoDelay_Type()
)
tmnxPppoePlcyPadoDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPadoDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPadoDelay.setUnits("deci-seconds")


class _TmnxPppoePlcyMaxSessionsPerMac_Type(Unsigned32):
    """Custom type tmnxPppoePlcyMaxSessionsPerMac based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_TmnxPppoePlcyMaxSessionsPerMac_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyMaxSessionsPerMac_Object = MibTableColumn
tmnxPppoePlcyMaxSessionsPerMac = _TmnxPppoePlcyMaxSessionsPerMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 10),
    _TmnxPppoePlcyMaxSessionsPerMac_Type()
)
tmnxPppoePlcyMaxSessionsPerMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyMaxSessionsPerMac.setStatus("current")


class _TmnxPppoePlcyReplyOnPadt_Type(TruthValue):
    """Custom type tmnxPppoePlcyReplyOnPadt based on TruthValue"""
    defaultValue = 2


_TmnxPppoePlcyReplyOnPadt_Type.__name__ = "TruthValue"
_TmnxPppoePlcyReplyOnPadt_Object = MibTableColumn
tmnxPppoePlcyReplyOnPadt = _TmnxPppoePlcyReplyOnPadt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 11),
    _TmnxPppoePlcyReplyOnPadt_Type()
)
tmnxPppoePlcyReplyOnPadt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyReplyOnPadt.setStatus("current")


class _TmnxPppoePlcyPppAuthentication_Type(Integer32):
    """Custom type tmnxPppoePlcyPppAuthentication based on Integer32"""
    defaultValue = 3

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
        *(("pap", 1),
          ("chap", 2),
          ("prefChap", 3),
          ("prefPap", 4))
    )


_TmnxPppoePlcyPppAuthentication_Type.__name__ = "Integer32"
_TmnxPppoePlcyPppAuthentication_Object = MibTableColumn
tmnxPppoePlcyPppAuthentication = _TmnxPppoePlcyPppAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 12),
    _TmnxPppoePlcyPppAuthentication_Type()
)
tmnxPppoePlcyPppAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppAuthentication.setStatus("current")


class _TmnxPppoePlcyPppMinChapChallenge_Type(Unsigned32):
    """Custom type tmnxPppoePlcyPppMinChapChallenge based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 64),
    )


_TmnxPppoePlcyPppMinChapChallenge_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyPppMinChapChallenge_Object = MibTableColumn
tmnxPppoePlcyPppMinChapChallenge = _TmnxPppoePlcyPppMinChapChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 13),
    _TmnxPppoePlcyPppMinChapChallenge_Type()
)
tmnxPppoePlcyPppMinChapChallenge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppMinChapChallenge.setStatus("current")


class _TmnxPppoePlcyPppMaxChapChallenge_Type(Unsigned32):
    """Custom type tmnxPppoePlcyPppMaxChapChallenge based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 64),
    )


_TmnxPppoePlcyPppMaxChapChallenge_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyPppMaxChapChallenge_Object = MibTableColumn
tmnxPppoePlcyPppMaxChapChallenge = _TmnxPppoePlcyPppMaxChapChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 14),
    _TmnxPppoePlcyPppMaxChapChallenge_Type()
)
tmnxPppoePlcyPppMaxChapChallenge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppMaxChapChallenge.setStatus("current")


class _TmnxPppoePlcyPppInitialDelay_Type(Unsigned32):
    """Custom type tmnxPppoePlcyPppInitialDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
    )


_TmnxPppoePlcyPppInitialDelay_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyPppInitialDelay_Object = MibTableColumn
tmnxPppoePlcyPppInitialDelay = _TmnxPppoePlcyPppInitialDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 15),
    _TmnxPppoePlcyPppInitialDelay_Type()
)
tmnxPppoePlcyPppInitialDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppInitialDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppInitialDelay.setUnits("hundredths of a second")


class _TmnxPppoePlcyPppIpcpSubnetNeg_Type(TruthValue):
    """Custom type tmnxPppoePlcyPppIpcpSubnetNeg based on TruthValue"""
    defaultValue = 2


_TmnxPppoePlcyPppIpcpSubnetNeg_Type.__name__ = "TruthValue"
_TmnxPppoePlcyPppIpcpSubnetNeg_Object = MibTableColumn
tmnxPppoePlcyPppIpcpSubnetNeg = _TmnxPppoePlcyPppIpcpSubnetNeg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 20),
    _TmnxPppoePlcyPppIpcpSubnetNeg_Type()
)
tmnxPppoePlcyPppIpcpSubnetNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppIpcpSubnetNeg.setStatus("current")


class _TmnxPppoePlcyPadoAcName_Type(DisplayString):
    """Custom type tmnxPppoePlcyPadoAcName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxPppoePlcyPadoAcName_Type.__name__ = "DisplayString"
_TmnxPppoePlcyPadoAcName_Object = MibTableColumn
tmnxPppoePlcyPadoAcName = _TmnxPppoePlcyPadoAcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 21),
    _TmnxPppoePlcyPadoAcName_Type()
)
tmnxPppoePlcyPadoAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPadoAcName.setStatus("current")


class _TmnxPppoePlcyPppMtuForceGt1492_Type(TruthValue):
    """Custom type tmnxPppoePlcyPppMtuForceGt1492 based on TruthValue"""
    defaultValue = 2


_TmnxPppoePlcyPppMtuForceGt1492_Type.__name__ = "TruthValue"
_TmnxPppoePlcyPppMtuForceGt1492_Object = MibTableColumn
tmnxPppoePlcyPppMtuForceGt1492 = _TmnxPppoePlcyPppMtuForceGt1492_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 22),
    _TmnxPppoePlcyPppMtuForceGt1492_Type()
)
tmnxPppoePlcyPppMtuForceGt1492.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppMtuForceGt1492.setStatus("current")


class _TmnxPppoePlcyUniqueSessIdsPerSap_Type(Integer32):
    """Custom type tmnxPppoePlcyUniqueSessIdsPerSap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("perCaptureSap", 1),
          ("disabled", 2),
          ("perMsap", 3))
    )


_TmnxPppoePlcyUniqueSessIdsPerSap_Type.__name__ = "Integer32"
_TmnxPppoePlcyUniqueSessIdsPerSap_Object = MibTableColumn
tmnxPppoePlcyUniqueSessIdsPerSap = _TmnxPppoePlcyUniqueSessIdsPerSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 23),
    _TmnxPppoePlcyUniqueSessIdsPerSap_Type()
)
tmnxPppoePlcyUniqueSessIdsPerSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyUniqueSessIdsPerSap.setStatus("current")


class _TmnxPppoePlcyRejectDisabledNcp_Type(TruthValue):
    """Custom type tmnxPppoePlcyRejectDisabledNcp based on TruthValue"""
    defaultValue = 2


_TmnxPppoePlcyRejectDisabledNcp_Type.__name__ = "TruthValue"
_TmnxPppoePlcyRejectDisabledNcp_Object = MibTableColumn
tmnxPppoePlcyRejectDisabledNcp = _TmnxPppoePlcyRejectDisabledNcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 24),
    _TmnxPppoePlcyRejectDisabledNcp_Type()
)
tmnxPppoePlcyRejectDisabledNcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyRejectDisabledNcp.setStatus("current")


class _TmnxPppoePlcyLcpIgnoreMagic_Type(TruthValue):
    """Custom type tmnxPppoePlcyLcpIgnoreMagic based on TruthValue"""
    defaultValue = 2


_TmnxPppoePlcyLcpIgnoreMagic_Type.__name__ = "TruthValue"
_TmnxPppoePlcyLcpIgnoreMagic_Object = MibTableColumn
tmnxPppoePlcyLcpIgnoreMagic = _TmnxPppoePlcyLcpIgnoreMagic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 30),
    _TmnxPppoePlcyLcpIgnoreMagic_Type()
)
tmnxPppoePlcyLcpIgnoreMagic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyLcpIgnoreMagic.setStatus("current")


class _TmnxPppoePlcySessionTimeout_Type(Unsigned32):
    """Custom type tmnxPppoePlcySessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 31104000),
    )


_TmnxPppoePlcySessionTimeout_Type.__name__ = "Unsigned32"
_TmnxPppoePlcySessionTimeout_Object = MibTableColumn
tmnxPppoePlcySessionTimeout = _TmnxPppoePlcySessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 31),
    _TmnxPppoePlcySessionTimeout_Type()
)
tmnxPppoePlcySessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcySessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppoePlcySessionTimeout.setUnits("seconds")


class _TmnxPppoePlcyAllowSameCidForDhcp_Type(TruthValue):
    """Custom type tmnxPppoePlcyAllowSameCidForDhcp based on TruthValue"""
    defaultValue = 2


_TmnxPppoePlcyAllowSameCidForDhcp_Type.__name__ = "TruthValue"
_TmnxPppoePlcyAllowSameCidForDhcp_Object = MibTableColumn
tmnxPppoePlcyAllowSameCidForDhcp = _TmnxPppoePlcyAllowSameCidForDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 32),
    _TmnxPppoePlcyAllowSameCidForDhcp_Type()
)
tmnxPppoePlcyAllowSameCidForDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyAllowSameCidForDhcp.setStatus("current")


class _TmnxPppoePlcyReestablishSession_Type(Integer32):
    """Custom type tmnxPppoePlcyReestablishSession based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("padr", 2))
    )


_TmnxPppoePlcyReestablishSession_Type.__name__ = "Integer32"
_TmnxPppoePlcyReestablishSession_Object = MibTableColumn
tmnxPppoePlcyReestablishSession = _TmnxPppoePlcyReestablishSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 33),
    _TmnxPppoePlcyReestablishSession_Type()
)
tmnxPppoePlcyReestablishSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyReestablishSession.setStatus("current")


class _TmnxPppoePlcyDefaultUserName_Type(TmnxPppoeUserNameOrEmpty):
    """Custom type tmnxPppoePlcyDefaultUserName based on TmnxPppoeUserNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoePlcyDefaultUserName_Type.__name__ = "TmnxPppoeUserNameOrEmpty"
_TmnxPppoePlcyDefaultUserName_Object = MibTableColumn
tmnxPppoePlcyDefaultUserName = _TmnxPppoePlcyDefaultUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 34),
    _TmnxPppoePlcyDefaultUserName_Type()
)
tmnxPppoePlcyDefaultUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyDefaultUserName.setStatus("current")


class _TmnxPppoePlcyDefaultPapPassword_Type(TmnxAuthPassword):
    """Custom type tmnxPppoePlcyDefaultPapPassword based on TmnxAuthPassword"""
    defaultValue = OctetString("")


_TmnxPppoePlcyDefaultPapPassword_Type.__name__ = "TmnxAuthPassword"
_TmnxPppoePlcyDefaultPapPassword_Object = MibTableColumn
tmnxPppoePlcyDefaultPapPassword = _TmnxPppoePlcyDefaultPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 2, 1, 35),
    _TmnxPppoePlcyDefaultPapPassword_Type()
)
tmnxPppoePlcyDefaultPapPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyDefaultPapPassword.setStatus("current")
_TmnxPppoePlcyPppOptionTblLstChg_Type = TimeStamp
_TmnxPppoePlcyPppOptionTblLstChg_Object = MibScalar
tmnxPppoePlcyPppOptionTblLstChg = _TmnxPppoePlcyPppOptionTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 3),
    _TmnxPppoePlcyPppOptionTblLstChg_Type()
)
tmnxPppoePlcyPppOptionTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppOptionTblLstChg.setStatus("current")
_TmnxPppoePlcyPppOptionTable_Object = MibTable
tmnxPppoePlcyPppOptionTable = _TmnxPppoePlcyPppOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppOptionTable.setStatus("current")
_TmnxPppoePlcyPppOptionEntry_Object = MibTableRow
tmnxPppoePlcyPppOptionEntry = _TmnxPppoePlcyPppOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4, 1)
)
tmnxPppoePlcyPppOptionEntry.setIndexNames(
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoePlcyName"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionProtocol"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionNumber"),
)
if mibBuilder.loadTexts:
    tmnxPppoePlcyPppOptionEntry.setStatus("current")


class _TmnxPppoePlcyOptionProtocol_Type(Integer32):
    """Custom type tmnxPppoePlcyOptionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lcp", 1),
          ("ipcp", 2),
          ("ipv6cp", 3))
    )


_TmnxPppoePlcyOptionProtocol_Type.__name__ = "Integer32"
_TmnxPppoePlcyOptionProtocol_Object = MibTableColumn
tmnxPppoePlcyOptionProtocol = _TmnxPppoePlcyOptionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4, 1, 1),
    _TmnxPppoePlcyOptionProtocol_Type()
)
tmnxPppoePlcyOptionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoePlcyOptionProtocol.setStatus("current")


class _TmnxPppoePlcyOptionNumber_Type(Unsigned32):
    """Custom type tmnxPppoePlcyOptionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxPppoePlcyOptionNumber_Type.__name__ = "Unsigned32"
_TmnxPppoePlcyOptionNumber_Object = MibTableColumn
tmnxPppoePlcyOptionNumber = _TmnxPppoePlcyOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4, 1, 2),
    _TmnxPppoePlcyOptionNumber_Type()
)
tmnxPppoePlcyOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoePlcyOptionNumber.setStatus("current")
_TmnxPppoePlcyOptionRowStatus_Type = RowStatus
_TmnxPppoePlcyOptionRowStatus_Object = MibTableColumn
tmnxPppoePlcyOptionRowStatus = _TmnxPppoePlcyOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4, 1, 3),
    _TmnxPppoePlcyOptionRowStatus_Type()
)
tmnxPppoePlcyOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyOptionRowStatus.setStatus("current")
_TmnxPppoePlcyOptionLstMgmtChange_Type = TimeStamp
_TmnxPppoePlcyOptionLstMgmtChange_Object = MibTableColumn
tmnxPppoePlcyOptionLstMgmtChange = _TmnxPppoePlcyOptionLstMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4, 1, 4),
    _TmnxPppoePlcyOptionLstMgmtChange_Type()
)
tmnxPppoePlcyOptionLstMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoePlcyOptionLstMgmtChange.setStatus("current")
_TmnxPppoePlcyOptionType_Type = TmnxDhcpOptionType
_TmnxPppoePlcyOptionType_Object = MibTableColumn
tmnxPppoePlcyOptionType = _TmnxPppoePlcyOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4, 1, 5),
    _TmnxPppoePlcyOptionType_Type()
)
tmnxPppoePlcyOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyOptionType.setStatus("current")


class _TmnxPppoePlcyOptionValue_Type(OctetString):
    """Custom type tmnxPppoePlcyOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxPppoePlcyOptionValue_Type.__name__ = "OctetString"
_TmnxPppoePlcyOptionValue_Object = MibTableColumn
tmnxPppoePlcyOptionValue = _TmnxPppoePlcyOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 4, 1, 6),
    _TmnxPppoePlcyOptionValue_Type()
)
tmnxPppoePlcyOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppoePlcyOptionValue.setStatus("current")
_TmnxPppoeIesIfInfoTableLastChg_Type = TimeStamp
_TmnxPppoeIesIfInfoTableLastChg_Object = MibScalar
tmnxPppoeIesIfInfoTableLastChg = _TmnxPppoeIesIfInfoTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 5),
    _TmnxPppoeIesIfInfoTableLastChg_Type()
)
tmnxPppoeIesIfInfoTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfInfoTableLastChg.setStatus("current")
_TmnxPppoeIesIfInfoTable_Object = MibTable
tmnxPppoeIesIfInfoTable = _TmnxPppoeIesIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxPppoeIesIfInfoTable.setStatus("current")
_TmnxPppoeIesIfInfoEntry_Object = MibTableRow
tmnxPppoeIesIfInfoEntry = _TmnxPppoeIesIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1)
)
tmnxPppoeIesIfInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxPppoeIesIfInfoEntry.setStatus("current")
_TmnxPppoeIesIfLastChg_Type = TimeStamp
_TmnxPppoeIesIfLastChg_Object = MibTableColumn
tmnxPppoeIesIfLastChg = _TmnxPppoeIesIfLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 1),
    _TmnxPppoeIesIfLastChg_Type()
)
tmnxPppoeIesIfLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfLastChg.setStatus("current")


class _TmnxPppoeIesIfDescription_Type(TItemDescription):
    """Custom type tmnxPppoeIesIfDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxPppoeIesIfDescription_Type.__name__ = "TItemDescription"
_TmnxPppoeIesIfDescription_Object = MibTableColumn
tmnxPppoeIesIfDescription = _TmnxPppoeIesIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 2),
    _TmnxPppoeIesIfDescription_Type()
)
tmnxPppoeIesIfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfDescription.setStatus("current")
_TmnxPppoeIesIfAdminState_Type = TmnxPppoeAdminStatus
_TmnxPppoeIesIfAdminState_Object = MibTableColumn
tmnxPppoeIesIfAdminState = _TmnxPppoeIesIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 3),
    _TmnxPppoeIesIfAdminState_Type()
)
tmnxPppoeIesIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfAdminState.setStatus("current")


class _TmnxPppoeIesIfPolicy_Type(TNamedItem):
    """Custom type tmnxPppoeIesIfPolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxPppoeIesIfPolicy_Type.__name__ = "TNamedItem"
_TmnxPppoeIesIfPolicy_Object = MibTableColumn
tmnxPppoeIesIfPolicy = _TmnxPppoeIesIfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 4),
    _TmnxPppoeIesIfPolicy_Type()
)
tmnxPppoeIesIfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfPolicy.setStatus("current")


class _TmnxPppoeIesIfSessionLimit_Type(Unsigned32):
    """Custom type tmnxPppoeIesIfSessionLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262143),
    )


_TmnxPppoeIesIfSessionLimit_Type.__name__ = "Unsigned32"
_TmnxPppoeIesIfSessionLimit_Object = MibTableColumn
tmnxPppoeIesIfSessionLimit = _TmnxPppoeIesIfSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 5),
    _TmnxPppoeIesIfSessionLimit_Type()
)
tmnxPppoeIesIfSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfSessionLimit.setStatus("current")


class _TmnxPppoeIesIfSapSessionLimit_Type(Unsigned32):
    """Custom type tmnxPppoeIesIfSapSessionLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxPppoeIesIfSapSessionLimit_Type.__name__ = "Unsigned32"
_TmnxPppoeIesIfSapSessionLimit_Object = MibTableColumn
tmnxPppoeIesIfSapSessionLimit = _TmnxPppoeIesIfSapSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 6),
    _TmnxPppoeIesIfSapSessionLimit_Type()
)
tmnxPppoeIesIfSapSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfSapSessionLimit.setStatus("current")


class _TmnxPppoeIesIfPapChapUserDb_Type(TNamedItemOrEmpty):
    """Custom type tmnxPppoeIesIfPapChapUserDb based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoeIesIfPapChapUserDb_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPppoeIesIfPapChapUserDb_Object = MibTableColumn
tmnxPppoeIesIfPapChapUserDb = _TmnxPppoeIesIfPapChapUserDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 7),
    _TmnxPppoeIesIfPapChapUserDb_Type()
)
tmnxPppoeIesIfPapChapUserDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfPapChapUserDb.setStatus("obsolete")


class _TmnxPppoeIesIfUserDb_Type(TNamedItemOrEmpty):
    """Custom type tmnxPppoeIesIfUserDb based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoeIesIfUserDb_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPppoeIesIfUserDb_Object = MibTableColumn
tmnxPppoeIesIfUserDb = _TmnxPppoeIesIfUserDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 8),
    _TmnxPppoeIesIfUserDb_Type()
)
tmnxPppoeIesIfUserDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfUserDb.setStatus("current")


class _TmnxPppoeIesIfDhcpcCcagOriginSap_Type(TruthValue):
    """Custom type tmnxPppoeIesIfDhcpcCcagOriginSap based on TruthValue"""
    defaultValue = 2


_TmnxPppoeIesIfDhcpcCcagOriginSap_Type.__name__ = "TruthValue"
_TmnxPppoeIesIfDhcpcCcagOriginSap_Object = MibTableColumn
tmnxPppoeIesIfDhcpcCcagOriginSap = _TmnxPppoeIesIfDhcpcCcagOriginSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 9),
    _TmnxPppoeIesIfDhcpcCcagOriginSap_Type()
)
tmnxPppoeIesIfDhcpcCcagOriginSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfDhcpcCcagOriginSap.setStatus("current")


class _TmnxPppoeIesIfAntiSpoofing_Type(Integer32):
    """Custom type tmnxPppoeIesIfAntiSpoofing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macSid", 1),
          ("macSidIp", 2))
    )


_TmnxPppoeIesIfAntiSpoofing_Type.__name__ = "Integer32"
_TmnxPppoeIesIfAntiSpoofing_Object = MibTableColumn
tmnxPppoeIesIfAntiSpoofing = _TmnxPppoeIesIfAntiSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 10),
    _TmnxPppoeIesIfAntiSpoofing_Type()
)
tmnxPppoeIesIfAntiSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfAntiSpoofing.setStatus("current")


class _TmnxPppoeIesIfDhcpcInclOptString_Type(DisplayString):
    """Custom type tmnxPppoeIesIfDhcpcInclOptString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxPppoeIesIfDhcpcInclOptString_Type.__name__ = "DisplayString"
_TmnxPppoeIesIfDhcpcInclOptString_Object = MibTableColumn
tmnxPppoeIesIfDhcpcInclOptString = _TmnxPppoeIesIfDhcpcInclOptString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 6, 1, 11),
    _TmnxPppoeIesIfDhcpcInclOptString_Type()
)
tmnxPppoeIesIfDhcpcInclOptString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeIesIfDhcpcInclOptString.setStatus("obsolete")
_TmnxPppoeSapStatsTable_Object = MibTable
tmnxPppoeSapStatsTable = _TmnxPppoeSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxPppoeSapStatsTable.setStatus("current")
_TmnxPppoeSapStatsEntry_Object = MibTableRow
tmnxPppoeSapStatsEntry = _TmnxPppoeSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1)
)
tmnxPppoeSapStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxPppoeSapStatsEntry.setStatus("current")
_TmnxPppoeSapRxPadi_Type = Counter32
_TmnxPppoeSapRxPadi_Object = MibTableColumn
tmnxPppoeSapRxPadi = _TmnxPppoeSapRxPadi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 1),
    _TmnxPppoeSapRxPadi_Type()
)
tmnxPppoeSapRxPadi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxPadi.setStatus("current")
_TmnxPppoeSapRxPadr_Type = Counter32
_TmnxPppoeSapRxPadr_Object = MibTableColumn
tmnxPppoeSapRxPadr = _TmnxPppoeSapRxPadr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 2),
    _TmnxPppoeSapRxPadr_Type()
)
tmnxPppoeSapRxPadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxPadr.setStatus("current")
_TmnxPppoeSapRxPadt_Type = Counter32
_TmnxPppoeSapRxPadt_Object = MibTableColumn
tmnxPppoeSapRxPadt = _TmnxPppoeSapRxPadt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 3),
    _TmnxPppoeSapRxPadt_Type()
)
tmnxPppoeSapRxPadt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxPadt.setStatus("current")
_TmnxPppoeSapRxSession_Type = Counter32
_TmnxPppoeSapRxSession_Object = MibTableColumn
tmnxPppoeSapRxSession = _TmnxPppoeSapRxSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 4),
    _TmnxPppoeSapRxSession_Type()
)
tmnxPppoeSapRxSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxSession.setStatus("current")
_TmnxPppoeSapRxInvalidVersion_Type = Counter32
_TmnxPppoeSapRxInvalidVersion_Object = MibTableColumn
tmnxPppoeSapRxInvalidVersion = _TmnxPppoeSapRxInvalidVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 5),
    _TmnxPppoeSapRxInvalidVersion_Type()
)
tmnxPppoeSapRxInvalidVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidVersion.setStatus("current")
_TmnxPppoeSapRxInvalidType_Type = Counter32
_TmnxPppoeSapRxInvalidType_Object = MibTableColumn
tmnxPppoeSapRxInvalidType = _TmnxPppoeSapRxInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 6),
    _TmnxPppoeSapRxInvalidType_Type()
)
tmnxPppoeSapRxInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidType.setStatus("current")
_TmnxPppoeSapRxInvalidCode_Type = Counter32
_TmnxPppoeSapRxInvalidCode_Object = MibTableColumn
tmnxPppoeSapRxInvalidCode = _TmnxPppoeSapRxInvalidCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 7),
    _TmnxPppoeSapRxInvalidCode_Type()
)
tmnxPppoeSapRxInvalidCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidCode.setStatus("current")
_TmnxPppoeSapRxInvalidSession_Type = Counter32
_TmnxPppoeSapRxInvalidSession_Object = MibTableColumn
tmnxPppoeSapRxInvalidSession = _TmnxPppoeSapRxInvalidSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 8),
    _TmnxPppoeSapRxInvalidSession_Type()
)
tmnxPppoeSapRxInvalidSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidSession.setStatus("current")
_TmnxPppoeSapRxInvalidLen_Type = Counter32
_TmnxPppoeSapRxInvalidLen_Object = MibTableColumn
tmnxPppoeSapRxInvalidLen = _TmnxPppoeSapRxInvalidLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 9),
    _TmnxPppoeSapRxInvalidLen_Type()
)
tmnxPppoeSapRxInvalidLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidLen.setStatus("current")
_TmnxPppoeSapRxInvalidTags_Type = Counter32
_TmnxPppoeSapRxInvalidTags_Object = MibTableColumn
tmnxPppoeSapRxInvalidTags = _TmnxPppoeSapRxInvalidTags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 10),
    _TmnxPppoeSapRxInvalidTags_Type()
)
tmnxPppoeSapRxInvalidTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidTags.setStatus("current")
_TmnxPppoeSapRxInvalidAcCookie_Type = Counter32
_TmnxPppoeSapRxInvalidAcCookie_Object = MibTableColumn
tmnxPppoeSapRxInvalidAcCookie = _TmnxPppoeSapRxInvalidAcCookie_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 11),
    _TmnxPppoeSapRxInvalidAcCookie_Type()
)
tmnxPppoeSapRxInvalidAcCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidAcCookie.setStatus("current")
_TmnxPppoeSapRxDropped_Type = Counter32
_TmnxPppoeSapRxDropped_Object = MibTableColumn
tmnxPppoeSapRxDropped = _TmnxPppoeSapRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 12),
    _TmnxPppoeSapRxDropped_Type()
)
tmnxPppoeSapRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxDropped.setStatus("current")
_TmnxPppoeSapTxPado_Type = Counter32
_TmnxPppoeSapTxPado_Object = MibTableColumn
tmnxPppoeSapTxPado = _TmnxPppoeSapTxPado_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 13),
    _TmnxPppoeSapTxPado_Type()
)
tmnxPppoeSapTxPado.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapTxPado.setStatus("current")
_TmnxPppoeSapTxPads_Type = Counter32
_TmnxPppoeSapTxPads_Object = MibTableColumn
tmnxPppoeSapTxPads = _TmnxPppoeSapTxPads_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 14),
    _TmnxPppoeSapTxPads_Type()
)
tmnxPppoeSapTxPads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapTxPads.setStatus("current")
_TmnxPppoeSapTxPadt_Type = Counter32
_TmnxPppoeSapTxPadt_Object = MibTableColumn
tmnxPppoeSapTxPadt = _TmnxPppoeSapTxPadt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 15),
    _TmnxPppoeSapTxPadt_Type()
)
tmnxPppoeSapTxPadt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapTxPadt.setStatus("current")
_TmnxPppoeSapTxSession_Type = Counter32
_TmnxPppoeSapTxSession_Object = MibTableColumn
tmnxPppoeSapTxSession = _TmnxPppoeSapTxSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 16),
    _TmnxPppoeSapTxSession_Type()
)
tmnxPppoeSapTxSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapTxSession.setStatus("current")
_TmnxPppoeSapRxInvalidMac_Type = Counter32
_TmnxPppoeSapRxInvalidMac_Object = MibTableColumn
tmnxPppoeSapRxInvalidMac = _TmnxPppoeSapRxInvalidMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 7, 1, 17),
    _TmnxPppoeSapRxInvalidMac_Type()
)
tmnxPppoeSapRxInvalidMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSapRxInvalidMac.setStatus("current")
_TmnxPppoeSessionTable_Object = MibTable
tmnxPppoeSessionTable = _TmnxPppoeSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionTable.setStatus("current")
_TmnxPppoeSessionEntry_Object = MibTableRow
tmnxPppoeSessionEntry = _TmnxPppoeSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1)
)
tmnxPppoeSessionEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionMac"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionId"),
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionEntry.setStatus("current")
_TmnxPppoeSessionMac_Type = MacAddress
_TmnxPppoeSessionMac_Object = MibTableColumn
tmnxPppoeSessionMac = _TmnxPppoeSessionMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 1),
    _TmnxPppoeSessionMac_Type()
)
tmnxPppoeSessionMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeSessionMac.setStatus("current")
_TmnxPppoeSessionId_Type = TmnxPppoeSessionId
_TmnxPppoeSessionId_Object = MibTableColumn
tmnxPppoeSessionId = _TmnxPppoeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 2),
    _TmnxPppoeSessionId_Type()
)
tmnxPppoeSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeSessionId.setStatus("current")
_TmnxPppoeSessionUpTime_Type = TimeTicks
_TmnxPppoeSessionUpTime_Object = MibTableColumn
tmnxPppoeSessionUpTime = _TmnxPppoeSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 3),
    _TmnxPppoeSessionUpTime_Type()
)
tmnxPppoeSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionUpTime.setStatus("obsolete")
_TmnxPppoeSessionLcpState_Type = TmnxPppCpState
_TmnxPppoeSessionLcpState_Object = MibTableColumn
tmnxPppoeSessionLcpState = _TmnxPppoeSessionLcpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 4),
    _TmnxPppoeSessionLcpState_Type()
)
tmnxPppoeSessionLcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionLcpState.setStatus("obsolete")
_TmnxPppoeSessionIpcpState_Type = TmnxPppCpState
_TmnxPppoeSessionIpcpState_Object = MibTableColumn
tmnxPppoeSessionIpcpState = _TmnxPppoeSessionIpcpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 5),
    _TmnxPppoeSessionIpcpState_Type()
)
tmnxPppoeSessionIpcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpcpState.setStatus("obsolete")
_TmnxPppoeSessionPppMtu_Type = Unsigned32
_TmnxPppoeSessionPppMtu_Object = MibTableColumn
tmnxPppoeSessionPppMtu = _TmnxPppoeSessionPppMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 6),
    _TmnxPppoeSessionPppMtu_Type()
)
tmnxPppoeSessionPppMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPppMtu.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPppMtu.setUnits("bytes")


class _TmnxPppoeSessionPppAuthProtocol_Type(Integer32):
    """Custom type tmnxPppoeSessionPppAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pap", 2),
          ("chap", 3))
    )


_TmnxPppoeSessionPppAuthProtocol_Type.__name__ = "Integer32"
_TmnxPppoeSessionPppAuthProtocol_Object = MibTableColumn
tmnxPppoeSessionPppAuthProtocol = _TmnxPppoeSessionPppAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 7),
    _TmnxPppoeSessionPppAuthProtocol_Type()
)
tmnxPppoeSessionPppAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPppAuthProtocol.setStatus("obsolete")
_TmnxPppoeSessionPppUserName_Type = TmnxPppoeUserNameOrEmpty
_TmnxPppoeSessionPppUserName_Object = MibTableColumn
tmnxPppoeSessionPppUserName = _TmnxPppoeSessionPppUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 8),
    _TmnxPppoeSessionPppUserName_Type()
)
tmnxPppoeSessionPppUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPppUserName.setStatus("obsolete")
_TmnxPppoeSessionSubIdent_Type = TmnxSubIdentStringOrEmpty
_TmnxPppoeSessionSubIdent_Object = MibTableColumn
tmnxPppoeSessionSubIdent = _TmnxPppoeSessionSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 9),
    _TmnxPppoeSessionSubIdent_Type()
)
tmnxPppoeSessionSubIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSubIdent.setStatus("obsolete")
_TmnxPppoeSessionOriginSubIdent_Type = TmnxPppoeSessionInfoOrigin
_TmnxPppoeSessionOriginSubIdent_Object = MibTableColumn
tmnxPppoeSessionOriginSubIdent = _TmnxPppoeSessionOriginSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 10),
    _TmnxPppoeSessionOriginSubIdent_Type()
)
tmnxPppoeSessionOriginSubIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOriginSubIdent.setStatus("obsolete")
_TmnxPppoeSessionSubProfString_Type = TmnxSubProfileStringOrEmpty
_TmnxPppoeSessionSubProfString_Object = MibTableColumn
tmnxPppoeSessionSubProfString = _TmnxPppoeSessionSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 11),
    _TmnxPppoeSessionSubProfString_Type()
)
tmnxPppoeSessionSubProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSubProfString.setStatus("obsolete")
_TmnxPppoeSessionSlaProfString_Type = TmnxSlaProfileStringOrEmpty
_TmnxPppoeSessionSlaProfString_Object = MibTableColumn
tmnxPppoeSessionSlaProfString = _TmnxPppoeSessionSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 12),
    _TmnxPppoeSessionSlaProfString_Type()
)
tmnxPppoeSessionSlaProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSlaProfString.setStatus("obsolete")
_TmnxPppoeSessionAncpString_Type = TmnxAncpStringOrZero
_TmnxPppoeSessionAncpString_Object = MibTableColumn
tmnxPppoeSessionAncpString = _TmnxPppoeSessionAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 13),
    _TmnxPppoeSessionAncpString_Type()
)
tmnxPppoeSessionAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionAncpString.setStatus("obsolete")
_TmnxPppoeSessionInterDestId_Type = TmnxSubMgtIntDestIdOrEmpty
_TmnxPppoeSessionInterDestId_Object = MibTableColumn
tmnxPppoeSessionInterDestId = _TmnxPppoeSessionInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 14),
    _TmnxPppoeSessionInterDestId_Type()
)
tmnxPppoeSessionInterDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionInterDestId.setStatus("obsolete")
_TmnxPppoeSessionAppProfString_Type = TmnxAppProfileStringOrEmpty
_TmnxPppoeSessionAppProfString_Object = MibTableColumn
tmnxPppoeSessionAppProfString = _TmnxPppoeSessionAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 15),
    _TmnxPppoeSessionAppProfString_Type()
)
tmnxPppoeSessionAppProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionAppProfString.setStatus("obsolete")
_TmnxPppoeSessionOriginStrings_Type = TmnxPppoeSessionInfoOrigin
_TmnxPppoeSessionOriginStrings_Object = MibTableColumn
tmnxPppoeSessionOriginStrings = _TmnxPppoeSessionOriginStrings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 16),
    _TmnxPppoeSessionOriginStrings_Type()
)
tmnxPppoeSessionOriginStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOriginStrings.setStatus("obsolete")


class _TmnxPppoeSessionSessionTimeout_Type(Unsigned32):
    """Custom type tmnxPppoeSessionSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxPppoeSessionSessionTimeout_Type.__name__ = "Unsigned32"
_TmnxPppoeSessionSessionTimeout_Object = MibTableColumn
tmnxPppoeSessionSessionTimeout = _TmnxPppoeSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 17),
    _TmnxPppoeSessionSessionTimeout_Type()
)
tmnxPppoeSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSessionTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSessionTimeout.setUnits("seconds")
_TmnxPppoeSessionIpAddrType_Type = InetAddressType
_TmnxPppoeSessionIpAddrType_Object = MibTableColumn
tmnxPppoeSessionIpAddrType = _TmnxPppoeSessionIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 18),
    _TmnxPppoeSessionIpAddrType_Type()
)
tmnxPppoeSessionIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpAddrType.setStatus("obsolete")


class _TmnxPppoeSessionIpAddr_Type(InetAddress):
    """Custom type tmnxPppoeSessionIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPppoeSessionIpAddr_Type.__name__ = "InetAddress"
_TmnxPppoeSessionIpAddr_Object = MibTableColumn
tmnxPppoeSessionIpAddr = _TmnxPppoeSessionIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 19),
    _TmnxPppoeSessionIpAddr_Type()
)
tmnxPppoeSessionIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpAddr.setStatus("obsolete")
_TmnxPppoeSessionPrimaryDnsType_Type = InetAddressType
_TmnxPppoeSessionPrimaryDnsType_Object = MibTableColumn
tmnxPppoeSessionPrimaryDnsType = _TmnxPppoeSessionPrimaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 20),
    _TmnxPppoeSessionPrimaryDnsType_Type()
)
tmnxPppoeSessionPrimaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPrimaryDnsType.setStatus("obsolete")


class _TmnxPppoeSessionPrimaryDns_Type(InetAddress):
    """Custom type tmnxPppoeSessionPrimaryDns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPppoeSessionPrimaryDns_Type.__name__ = "InetAddress"
_TmnxPppoeSessionPrimaryDns_Object = MibTableColumn
tmnxPppoeSessionPrimaryDns = _TmnxPppoeSessionPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 21),
    _TmnxPppoeSessionPrimaryDns_Type()
)
tmnxPppoeSessionPrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPrimaryDns.setStatus("obsolete")
_TmnxPppoeSessionSecondryDnsType_Type = InetAddressType
_TmnxPppoeSessionSecondryDnsType_Object = MibTableColumn
tmnxPppoeSessionSecondryDnsType = _TmnxPppoeSessionSecondryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 22),
    _TmnxPppoeSessionSecondryDnsType_Type()
)
tmnxPppoeSessionSecondryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSecondryDnsType.setStatus("obsolete")


class _TmnxPppoeSessionSecondryDns_Type(InetAddress):
    """Custom type tmnxPppoeSessionSecondryDns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPppoeSessionSecondryDns_Type.__name__ = "InetAddress"
_TmnxPppoeSessionSecondryDns_Object = MibTableColumn
tmnxPppoeSessionSecondryDns = _TmnxPppoeSessionSecondryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 23),
    _TmnxPppoeSessionSecondryDns_Type()
)
tmnxPppoeSessionSecondryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSecondryDns.setStatus("obsolete")
_TmnxPppoeSessionPrimaryNbnsType_Type = InetAddressType
_TmnxPppoeSessionPrimaryNbnsType_Object = MibTableColumn
tmnxPppoeSessionPrimaryNbnsType = _TmnxPppoeSessionPrimaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 24),
    _TmnxPppoeSessionPrimaryNbnsType_Type()
)
tmnxPppoeSessionPrimaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPrimaryNbnsType.setStatus("obsolete")


class _TmnxPppoeSessionPrimaryNbns_Type(InetAddress):
    """Custom type tmnxPppoeSessionPrimaryNbns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPppoeSessionPrimaryNbns_Type.__name__ = "InetAddress"
_TmnxPppoeSessionPrimaryNbns_Object = MibTableColumn
tmnxPppoeSessionPrimaryNbns = _TmnxPppoeSessionPrimaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 25),
    _TmnxPppoeSessionPrimaryNbns_Type()
)
tmnxPppoeSessionPrimaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionPrimaryNbns.setStatus("obsolete")
_TmnxPppoeSessionSecondryNbnsType_Type = InetAddressType
_TmnxPppoeSessionSecondryNbnsType_Object = MibTableColumn
tmnxPppoeSessionSecondryNbnsType = _TmnxPppoeSessionSecondryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 26),
    _TmnxPppoeSessionSecondryNbnsType_Type()
)
tmnxPppoeSessionSecondryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSecondryNbnsType.setStatus("obsolete")


class _TmnxPppoeSessionSecondryNbns_Type(InetAddress):
    """Custom type tmnxPppoeSessionSecondryNbns based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPppoeSessionSecondryNbns_Type.__name__ = "InetAddress"
_TmnxPppoeSessionSecondryNbns_Object = MibTableColumn
tmnxPppoeSessionSecondryNbns = _TmnxPppoeSessionSecondryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 27),
    _TmnxPppoeSessionSecondryNbns_Type()
)
tmnxPppoeSessionSecondryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSecondryNbns.setStatus("obsolete")
_TmnxPppoeSessionOriginIpcpInfo_Type = TmnxPppoeSessionInfoOrigin
_TmnxPppoeSessionOriginIpcpInfo_Object = MibTableColumn
tmnxPppoeSessionOriginIpcpInfo = _TmnxPppoeSessionOriginIpcpInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 28),
    _TmnxPppoeSessionOriginIpcpInfo_Type()
)
tmnxPppoeSessionOriginIpcpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOriginIpcpInfo.setStatus("obsolete")


class _TmnxPppoeSessionCircuitId_Type(OctetString):
    """Custom type tmnxPppoeSessionCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxPppoeSessionCircuitId_Type.__name__ = "OctetString"
_TmnxPppoeSessionCircuitId_Object = MibTableColumn
tmnxPppoeSessionCircuitId = _TmnxPppoeSessionCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 29),
    _TmnxPppoeSessionCircuitId_Type()
)
tmnxPppoeSessionCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionCircuitId.setStatus("obsolete")


class _TmnxPppoeSessionRemoteId_Type(OctetString):
    """Custom type tmnxPppoeSessionRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxPppoeSessionRemoteId_Type.__name__ = "OctetString"
_TmnxPppoeSessionRemoteId_Object = MibTableColumn
tmnxPppoeSessionRemoteId = _TmnxPppoeSessionRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 30),
    _TmnxPppoeSessionRemoteId_Type()
)
tmnxPppoeSessionRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRemoteId.setStatus("obsolete")


class _TmnxPppoeSessionAddressPool_Type(DisplayString):
    """Custom type tmnxPppoeSessionAddressPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxPppoeSessionAddressPool_Type.__name__ = "DisplayString"
_TmnxPppoeSessionAddressPool_Object = MibTableColumn
tmnxPppoeSessionAddressPool = _TmnxPppoeSessionAddressPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 31),
    _TmnxPppoeSessionAddressPool_Type()
)
tmnxPppoeSessionAddressPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionAddressPool.setStatus("obsolete")
_TmnxPppoeSessionType_Type = TmnxPppoeSessionType
_TmnxPppoeSessionType_Object = MibTableColumn
tmnxPppoeSessionType = _TmnxPppoeSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 32),
    _TmnxPppoeSessionType_Type()
)
tmnxPppoeSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionType.setStatus("obsolete")
_TmnxPppoeSessionRetailerSvcId_Type = TmnxServId
_TmnxPppoeSessionRetailerSvcId_Object = MibTableColumn
tmnxPppoeSessionRetailerSvcId = _TmnxPppoeSessionRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 33),
    _TmnxPppoeSessionRetailerSvcId_Type()
)
tmnxPppoeSessionRetailerSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRetailerSvcId.setStatus("obsolete")
_TmnxPppoeSessionRetailerIf_Type = InterfaceIndexOrZero
_TmnxPppoeSessionRetailerIf_Object = MibTableColumn
tmnxPppoeSessionRetailerIf = _TmnxPppoeSessionRetailerIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 34),
    _TmnxPppoeSessionRetailerIf_Type()
)
tmnxPppoeSessionRetailerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRetailerIf.setStatus("obsolete")
_TmnxPppoeSessionL2tpVrtrId_Type = TmnxVRtrIDOrZero
_TmnxPppoeSessionL2tpVrtrId_Object = MibTableColumn
tmnxPppoeSessionL2tpVrtrId = _TmnxPppoeSessionL2tpVrtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 35),
    _TmnxPppoeSessionL2tpVrtrId_Type()
)
tmnxPppoeSessionL2tpVrtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionL2tpVrtrId.setStatus("obsolete")
_TmnxPppoeSessionL2tpConnectionId_Type = Unsigned32
_TmnxPppoeSessionL2tpConnectionId_Object = MibTableColumn
tmnxPppoeSessionL2tpConnectionId = _TmnxPppoeSessionL2tpConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 36),
    _TmnxPppoeSessionL2tpConnectionId_Type()
)
tmnxPppoeSessionL2tpConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionL2tpConnectionId.setStatus("obsolete")


class _TmnxPppoeSessionServiceName_Type(DisplayString):
    """Custom type tmnxPppoeSessionServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxPppoeSessionServiceName_Type.__name__ = "DisplayString"
_TmnxPppoeSessionServiceName_Object = MibTableColumn
tmnxPppoeSessionServiceName = _TmnxPppoeSessionServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 37),
    _TmnxPppoeSessionServiceName_Type()
)
tmnxPppoeSessionServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionServiceName.setStatus("current")
_TmnxPppoeSessionCategoryMapName_Type = TNamedItemOrEmpty
_TmnxPppoeSessionCategoryMapName_Object = MibTableColumn
tmnxPppoeSessionCategoryMapName = _TmnxPppoeSessionCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 38),
    _TmnxPppoeSessionCategoryMapName_Type()
)
tmnxPppoeSessionCategoryMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionCategoryMapName.setStatus("obsolete")


class _TmnxPppoeSessionRadiusClassAttr_Type(OctetString):
    """Custom type tmnxPppoeSessionRadiusClassAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxPppoeSessionRadiusClassAttr_Type.__name__ = "OctetString"
_TmnxPppoeSessionRadiusClassAttr_Object = MibTableColumn
tmnxPppoeSessionRadiusClassAttr = _TmnxPppoeSessionRadiusClassAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 39),
    _TmnxPppoeSessionRadiusClassAttr_Type()
)
tmnxPppoeSessionRadiusClassAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRadiusClassAttr.setStatus("obsolete")


class _TmnxPppoeSessionRadiusUserName_Type(DisplayString):
    """Custom type tmnxPppoeSessionRadiusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxPppoeSessionRadiusUserName_Type.__name__ = "DisplayString"
_TmnxPppoeSessionRadiusUserName_Object = MibTableColumn
tmnxPppoeSessionRadiusUserName = _TmnxPppoeSessionRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 40),
    _TmnxPppoeSessionRadiusUserName_Type()
)
tmnxPppoeSessionRadiusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRadiusUserName.setStatus("obsolete")
_TmnxPppoeSessionIpv6cpState_Type = TmnxPppCpState
_TmnxPppoeSessionIpv6cpState_Object = MibTableColumn
tmnxPppoeSessionIpv6cpState = _TmnxPppoeSessionIpv6cpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 41),
    _TmnxPppoeSessionIpv6cpState_Type()
)
tmnxPppoeSessionIpv6cpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6cpState.setStatus("obsolete")


class _TmnxPppoeSessionInterfaceId_Type(OctetString):
    """Custom type tmnxPppoeSessionInterfaceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxPppoeSessionInterfaceId_Type.__name__ = "OctetString"
_TmnxPppoeSessionInterfaceId_Object = MibTableColumn
tmnxPppoeSessionInterfaceId = _TmnxPppoeSessionInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 42),
    _TmnxPppoeSessionInterfaceId_Type()
)
tmnxPppoeSessionInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionInterfaceId.setStatus("obsolete")
_TmnxPppoeSessionOriginIpv6cpInfo_Type = TmnxPppoeSessionInfoOrigin
_TmnxPppoeSessionOriginIpv6cpInfo_Object = MibTableColumn
tmnxPppoeSessionOriginIpv6cpInfo = _TmnxPppoeSessionOriginIpv6cpInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 43),
    _TmnxPppoeSessionOriginIpv6cpInfo_Type()
)
tmnxPppoeSessionOriginIpv6cpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOriginIpv6cpInfo.setStatus("obsolete")
_TmnxPppoeSessionIpv6DnsType_Type = InetAddressType
_TmnxPppoeSessionIpv6DnsType_Object = MibTableColumn
tmnxPppoeSessionIpv6DnsType = _TmnxPppoeSessionIpv6DnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 44),
    _TmnxPppoeSessionIpv6DnsType_Type()
)
tmnxPppoeSessionIpv6DnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6DnsType.setStatus("obsolete")


class _TmnxPppoeSessionIpv6Dns1_Type(InetAddress):
    """Custom type tmnxPppoeSessionIpv6Dns1 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxPppoeSessionIpv6Dns1_Type.__name__ = "InetAddress"
_TmnxPppoeSessionIpv6Dns1_Object = MibTableColumn
tmnxPppoeSessionIpv6Dns1 = _TmnxPppoeSessionIpv6Dns1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 45),
    _TmnxPppoeSessionIpv6Dns1_Type()
)
tmnxPppoeSessionIpv6Dns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6Dns1.setStatus("obsolete")


class _TmnxPppoeSessionIpv6Dns2_Type(InetAddress):
    """Custom type tmnxPppoeSessionIpv6Dns2 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxPppoeSessionIpv6Dns2_Type.__name__ = "InetAddress"
_TmnxPppoeSessionIpv6Dns2_Object = MibTableColumn
tmnxPppoeSessionIpv6Dns2 = _TmnxPppoeSessionIpv6Dns2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 46),
    _TmnxPppoeSessionIpv6Dns2_Type()
)
tmnxPppoeSessionIpv6Dns2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6Dns2.setStatus("obsolete")
_TmnxPppoeSessionIpv6DelPfxType_Type = InetAddressType
_TmnxPppoeSessionIpv6DelPfxType_Object = MibTableColumn
tmnxPppoeSessionIpv6DelPfxType = _TmnxPppoeSessionIpv6DelPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 47),
    _TmnxPppoeSessionIpv6DelPfxType_Type()
)
tmnxPppoeSessionIpv6DelPfxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6DelPfxType.setStatus("obsolete")


class _TmnxPppoeSessionIpv6DelPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxPppoeSessionIpv6DelPfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxPppoeSessionIpv6DelPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxPppoeSessionIpv6DelPfxLen_Object = MibTableColumn
tmnxPppoeSessionIpv6DelPfxLen = _TmnxPppoeSessionIpv6DelPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 48),
    _TmnxPppoeSessionIpv6DelPfxLen_Type()
)
tmnxPppoeSessionIpv6DelPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6DelPfxLen.setStatus("obsolete")


class _TmnxPppoeSessionIpv6DelPfx_Type(InetAddress):
    """Custom type tmnxPppoeSessionIpv6DelPfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxPppoeSessionIpv6DelPfx_Type.__name__ = "InetAddress"
_TmnxPppoeSessionIpv6DelPfx_Object = MibTableColumn
tmnxPppoeSessionIpv6DelPfx = _TmnxPppoeSessionIpv6DelPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 49),
    _TmnxPppoeSessionIpv6DelPfx_Type()
)
tmnxPppoeSessionIpv6DelPfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6DelPfx.setStatus("obsolete")
_TmnxPppoeSessionIpv6PrefixType_Type = InetAddressType
_TmnxPppoeSessionIpv6PrefixType_Object = MibTableColumn
tmnxPppoeSessionIpv6PrefixType = _TmnxPppoeSessionIpv6PrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 50),
    _TmnxPppoeSessionIpv6PrefixType_Type()
)
tmnxPppoeSessionIpv6PrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6PrefixType.setStatus("obsolete")


class _TmnxPppoeSessionIpv6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxPppoeSessionIpv6PrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxPppoeSessionIpv6PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxPppoeSessionIpv6PrefixLen_Object = MibTableColumn
tmnxPppoeSessionIpv6PrefixLen = _TmnxPppoeSessionIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 51),
    _TmnxPppoeSessionIpv6PrefixLen_Type()
)
tmnxPppoeSessionIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6PrefixLen.setStatus("obsolete")


class _TmnxPppoeSessionIpv6Prefix_Type(InetAddress):
    """Custom type tmnxPppoeSessionIpv6Prefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxPppoeSessionIpv6Prefix_Type.__name__ = "InetAddress"
_TmnxPppoeSessionIpv6Prefix_Object = MibTableColumn
tmnxPppoeSessionIpv6Prefix = _TmnxPppoeSessionIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 52),
    _TmnxPppoeSessionIpv6Prefix_Type()
)
tmnxPppoeSessionIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionIpv6Prefix.setStatus("obsolete")
_TmnxPppoeSessionSubPppIndex_Type = Unsigned32
_TmnxPppoeSessionSubPppIndex_Object = MibTableColumn
tmnxPppoeSessionSubPppIndex = _TmnxPppoeSessionSubPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 8, 1, 53),
    _TmnxPppoeSessionSubPppIndex_Type()
)
tmnxPppoeSessionSubPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionSubPppIndex.setStatus("current")
_TmnxPppoeSessionModifyTable_Object = MibTable
tmnxPppoeSessionModifyTable = _TmnxPppoeSessionModifyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionModifyTable.setStatus("obsolete")
_TmnxPppoeSessionModifyEntry_Object = MibTableRow
tmnxPppoeSessionModifyEntry = _TmnxPppoeSessionModifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionModifyEntry.setStatus("obsolete")


class _TmnxPppoeSessionModSubIdent_Type(TmnxSubIdentStringOrEmpty):
    """Custom type tmnxPppoeSessionModSubIdent based on TmnxSubIdentStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoeSessionModSubIdent_Type.__name__ = "TmnxSubIdentStringOrEmpty"
_TmnxPppoeSessionModSubIdent_Object = MibTableColumn
tmnxPppoeSessionModSubIdent = _TmnxPppoeSessionModSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1, 1),
    _TmnxPppoeSessionModSubIdent_Type()
)
tmnxPppoeSessionModSubIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeSessionModSubIdent.setStatus("obsolete")


class _TmnxPppoeSessionModSubProfStr_Type(TmnxSubProfileStringOrEmpty):
    """Custom type tmnxPppoeSessionModSubProfStr based on TmnxSubProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoeSessionModSubProfStr_Type.__name__ = "TmnxSubProfileStringOrEmpty"
_TmnxPppoeSessionModSubProfStr_Object = MibTableColumn
tmnxPppoeSessionModSubProfStr = _TmnxPppoeSessionModSubProfStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1, 2),
    _TmnxPppoeSessionModSubProfStr_Type()
)
tmnxPppoeSessionModSubProfStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeSessionModSubProfStr.setStatus("obsolete")


class _TmnxPppoeSessionModSlaProfStr_Type(TmnxSlaProfileStringOrEmpty):
    """Custom type tmnxPppoeSessionModSlaProfStr based on TmnxSlaProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoeSessionModSlaProfStr_Type.__name__ = "TmnxSlaProfileStringOrEmpty"
_TmnxPppoeSessionModSlaProfStr_Object = MibTableColumn
tmnxPppoeSessionModSlaProfStr = _TmnxPppoeSessionModSlaProfStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1, 3),
    _TmnxPppoeSessionModSlaProfStr_Type()
)
tmnxPppoeSessionModSlaProfStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeSessionModSlaProfStr.setStatus("obsolete")


class _TmnxPppoeSessionModAncpStr_Type(TmnxAncpStringOrZero):
    """Custom type tmnxPppoeSessionModAncpStr based on TmnxAncpStringOrZero"""
    defaultValue = OctetString("")


_TmnxPppoeSessionModAncpStr_Type.__name__ = "TmnxAncpStringOrZero"
_TmnxPppoeSessionModAncpStr_Object = MibTableColumn
tmnxPppoeSessionModAncpStr = _TmnxPppoeSessionModAncpStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1, 4),
    _TmnxPppoeSessionModAncpStr_Type()
)
tmnxPppoeSessionModAncpStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeSessionModAncpStr.setStatus("obsolete")


class _TmnxPppoeSessionModInterDestId_Type(TmnxSubMgtIntDestIdOrEmpty):
    """Custom type tmnxPppoeSessionModInterDestId based on TmnxSubMgtIntDestIdOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoeSessionModInterDestId_Type.__name__ = "TmnxSubMgtIntDestIdOrEmpty"
_TmnxPppoeSessionModInterDestId_Object = MibTableColumn
tmnxPppoeSessionModInterDestId = _TmnxPppoeSessionModInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1, 5),
    _TmnxPppoeSessionModInterDestId_Type()
)
tmnxPppoeSessionModInterDestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeSessionModInterDestId.setStatus("obsolete")


class _TmnxPppoeSessionModAppProfStr_Type(TmnxAppProfileStringOrEmpty):
    """Custom type tmnxPppoeSessionModAppProfStr based on TmnxAppProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppoeSessionModAppProfStr_Type.__name__ = "TmnxAppProfileStringOrEmpty"
_TmnxPppoeSessionModAppProfStr_Object = MibTableColumn
tmnxPppoeSessionModAppProfStr = _TmnxPppoeSessionModAppProfStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1, 6),
    _TmnxPppoeSessionModAppProfStr_Type()
)
tmnxPppoeSessionModAppProfStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeSessionModAppProfStr.setStatus("obsolete")


class _TmnxPppoeSessionEvaluateState_Type(TruthValue):
    """Custom type tmnxPppoeSessionEvaluateState based on TruthValue"""
    defaultValue = 2


_TmnxPppoeSessionEvaluateState_Type.__name__ = "TruthValue"
_TmnxPppoeSessionEvaluateState_Object = MibTableColumn
tmnxPppoeSessionEvaluateState = _TmnxPppoeSessionEvaluateState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 9, 1, 7),
    _TmnxPppoeSessionEvaluateState_Type()
)
tmnxPppoeSessionEvaluateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppoeSessionEvaluateState.setStatus("obsolete")
_TmnxPppoeSessionStatsTable_Object = MibTable
tmnxPppoeSessionStatsTable = _TmnxPppoeSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionStatsTable.setStatus("obsolete")
_TmnxPppoeSessionStatsEntry_Object = MibTableRow
tmnxPppoeSessionStatsEntry = _TmnxPppoeSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1)
)
tmnxPppoeSessionStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionMac"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionId"),
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionStatsEntry.setStatus("obsolete")
_TmnxPppoeSessionRxUnknownProto_Type = Counter32
_TmnxPppoeSessionRxUnknownProto_Object = MibTableColumn
tmnxPppoeSessionRxUnknownProto = _TmnxPppoeSessionRxUnknownProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 1),
    _TmnxPppoeSessionRxUnknownProto_Type()
)
tmnxPppoeSessionRxUnknownProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxUnknownProto.setStatus("obsolete")
_TmnxPppoeSessionRxLcpConfReq_Type = Counter32
_TmnxPppoeSessionRxLcpConfReq_Object = MibTableColumn
tmnxPppoeSessionRxLcpConfReq = _TmnxPppoeSessionRxLcpConfReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 2),
    _TmnxPppoeSessionRxLcpConfReq_Type()
)
tmnxPppoeSessionRxLcpConfReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpConfReq.setStatus("obsolete")
_TmnxPppoeSessionRxLcpConfAck_Type = Counter32
_TmnxPppoeSessionRxLcpConfAck_Object = MibTableColumn
tmnxPppoeSessionRxLcpConfAck = _TmnxPppoeSessionRxLcpConfAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 3),
    _TmnxPppoeSessionRxLcpConfAck_Type()
)
tmnxPppoeSessionRxLcpConfAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpConfAck.setStatus("obsolete")
_TmnxPppoeSessionRxLcpConfNak_Type = Counter32
_TmnxPppoeSessionRxLcpConfNak_Object = MibTableColumn
tmnxPppoeSessionRxLcpConfNak = _TmnxPppoeSessionRxLcpConfNak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 4),
    _TmnxPppoeSessionRxLcpConfNak_Type()
)
tmnxPppoeSessionRxLcpConfNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpConfNak.setStatus("obsolete")
_TmnxPppoeSessionRxLcpConfRej_Type = Counter32
_TmnxPppoeSessionRxLcpConfRej_Object = MibTableColumn
tmnxPppoeSessionRxLcpConfRej = _TmnxPppoeSessionRxLcpConfRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 5),
    _TmnxPppoeSessionRxLcpConfRej_Type()
)
tmnxPppoeSessionRxLcpConfRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpConfRej.setStatus("obsolete")
_TmnxPppoeSessionRxLcpTermReq_Type = Counter32
_TmnxPppoeSessionRxLcpTermReq_Object = MibTableColumn
tmnxPppoeSessionRxLcpTermReq = _TmnxPppoeSessionRxLcpTermReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 6),
    _TmnxPppoeSessionRxLcpTermReq_Type()
)
tmnxPppoeSessionRxLcpTermReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpTermReq.setStatus("obsolete")
_TmnxPppoeSessionRxLcpTermAck_Type = Counter32
_TmnxPppoeSessionRxLcpTermAck_Object = MibTableColumn
tmnxPppoeSessionRxLcpTermAck = _TmnxPppoeSessionRxLcpTermAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 7),
    _TmnxPppoeSessionRxLcpTermAck_Type()
)
tmnxPppoeSessionRxLcpTermAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpTermAck.setStatus("obsolete")
_TmnxPppoeSessionRxLcpCodeRej_Type = Counter32
_TmnxPppoeSessionRxLcpCodeRej_Object = MibTableColumn
tmnxPppoeSessionRxLcpCodeRej = _TmnxPppoeSessionRxLcpCodeRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 8),
    _TmnxPppoeSessionRxLcpCodeRej_Type()
)
tmnxPppoeSessionRxLcpCodeRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpCodeRej.setStatus("obsolete")
_TmnxPppoeSessionRxLcpEchoReq_Type = Counter32
_TmnxPppoeSessionRxLcpEchoReq_Object = MibTableColumn
tmnxPppoeSessionRxLcpEchoReq = _TmnxPppoeSessionRxLcpEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 9),
    _TmnxPppoeSessionRxLcpEchoReq_Type()
)
tmnxPppoeSessionRxLcpEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpEchoReq.setStatus("obsolete")
_TmnxPppoeSessionRxLcpEchoRep_Type = Counter32
_TmnxPppoeSessionRxLcpEchoRep_Object = MibTableColumn
tmnxPppoeSessionRxLcpEchoRep = _TmnxPppoeSessionRxLcpEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 10),
    _TmnxPppoeSessionRxLcpEchoRep_Type()
)
tmnxPppoeSessionRxLcpEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpEchoRep.setStatus("obsolete")
_TmnxPppoeSessionRxLcpProtRej_Type = Counter32
_TmnxPppoeSessionRxLcpProtRej_Object = MibTableColumn
tmnxPppoeSessionRxLcpProtRej = _TmnxPppoeSessionRxLcpProtRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 11),
    _TmnxPppoeSessionRxLcpProtRej_Type()
)
tmnxPppoeSessionRxLcpProtRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpProtRej.setStatus("obsolete")
_TmnxPppoeSessionRxLcpDiscReq_Type = Counter32
_TmnxPppoeSessionRxLcpDiscReq_Object = MibTableColumn
tmnxPppoeSessionRxLcpDiscReq = _TmnxPppoeSessionRxLcpDiscReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 12),
    _TmnxPppoeSessionRxLcpDiscReq_Type()
)
tmnxPppoeSessionRxLcpDiscReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxLcpDiscReq.setStatus("obsolete")
_TmnxPppoeSessionTxLcpConfReq_Type = Counter32
_TmnxPppoeSessionTxLcpConfReq_Object = MibTableColumn
tmnxPppoeSessionTxLcpConfReq = _TmnxPppoeSessionTxLcpConfReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 13),
    _TmnxPppoeSessionTxLcpConfReq_Type()
)
tmnxPppoeSessionTxLcpConfReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpConfReq.setStatus("obsolete")
_TmnxPppoeSessionTxLcpConfAck_Type = Counter32
_TmnxPppoeSessionTxLcpConfAck_Object = MibTableColumn
tmnxPppoeSessionTxLcpConfAck = _TmnxPppoeSessionTxLcpConfAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 14),
    _TmnxPppoeSessionTxLcpConfAck_Type()
)
tmnxPppoeSessionTxLcpConfAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpConfAck.setStatus("obsolete")
_TmnxPppoeSessionTxLcpConfNak_Type = Counter32
_TmnxPppoeSessionTxLcpConfNak_Object = MibTableColumn
tmnxPppoeSessionTxLcpConfNak = _TmnxPppoeSessionTxLcpConfNak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 15),
    _TmnxPppoeSessionTxLcpConfNak_Type()
)
tmnxPppoeSessionTxLcpConfNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpConfNak.setStatus("obsolete")
_TmnxPppoeSessionTxLcpConfRej_Type = Counter32
_TmnxPppoeSessionTxLcpConfRej_Object = MibTableColumn
tmnxPppoeSessionTxLcpConfRej = _TmnxPppoeSessionTxLcpConfRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 16),
    _TmnxPppoeSessionTxLcpConfRej_Type()
)
tmnxPppoeSessionTxLcpConfRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpConfRej.setStatus("obsolete")
_TmnxPppoeSessionTxLcpTermReq_Type = Counter32
_TmnxPppoeSessionTxLcpTermReq_Object = MibTableColumn
tmnxPppoeSessionTxLcpTermReq = _TmnxPppoeSessionTxLcpTermReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 17),
    _TmnxPppoeSessionTxLcpTermReq_Type()
)
tmnxPppoeSessionTxLcpTermReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpTermReq.setStatus("obsolete")
_TmnxPppoeSessionTxLcpTermAck_Type = Counter32
_TmnxPppoeSessionTxLcpTermAck_Object = MibTableColumn
tmnxPppoeSessionTxLcpTermAck = _TmnxPppoeSessionTxLcpTermAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 18),
    _TmnxPppoeSessionTxLcpTermAck_Type()
)
tmnxPppoeSessionTxLcpTermAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpTermAck.setStatus("obsolete")
_TmnxPppoeSessionTxLcpCodeRej_Type = Counter32
_TmnxPppoeSessionTxLcpCodeRej_Object = MibTableColumn
tmnxPppoeSessionTxLcpCodeRej = _TmnxPppoeSessionTxLcpCodeRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 19),
    _TmnxPppoeSessionTxLcpCodeRej_Type()
)
tmnxPppoeSessionTxLcpCodeRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpCodeRej.setStatus("obsolete")
_TmnxPppoeSessionTxLcpEchoReq_Type = Counter32
_TmnxPppoeSessionTxLcpEchoReq_Object = MibTableColumn
tmnxPppoeSessionTxLcpEchoReq = _TmnxPppoeSessionTxLcpEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 20),
    _TmnxPppoeSessionTxLcpEchoReq_Type()
)
tmnxPppoeSessionTxLcpEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpEchoReq.setStatus("obsolete")
_TmnxPppoeSessionTxLcpEchoRep_Type = Counter32
_TmnxPppoeSessionTxLcpEchoRep_Object = MibTableColumn
tmnxPppoeSessionTxLcpEchoRep = _TmnxPppoeSessionTxLcpEchoRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 21),
    _TmnxPppoeSessionTxLcpEchoRep_Type()
)
tmnxPppoeSessionTxLcpEchoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpEchoRep.setStatus("obsolete")
_TmnxPppoeSessionTxLcpProtRej_Type = Counter32
_TmnxPppoeSessionTxLcpProtRej_Object = MibTableColumn
tmnxPppoeSessionTxLcpProtRej = _TmnxPppoeSessionTxLcpProtRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 22),
    _TmnxPppoeSessionTxLcpProtRej_Type()
)
tmnxPppoeSessionTxLcpProtRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpProtRej.setStatus("obsolete")
_TmnxPppoeSessionTxLcpDiscReq_Type = Counter32
_TmnxPppoeSessionTxLcpDiscReq_Object = MibTableColumn
tmnxPppoeSessionTxLcpDiscReq = _TmnxPppoeSessionTxLcpDiscReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 23),
    _TmnxPppoeSessionTxLcpDiscReq_Type()
)
tmnxPppoeSessionTxLcpDiscReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxLcpDiscReq.setStatus("obsolete")
_TmnxPppoeSessionRxPapAuthReq_Type = Counter32
_TmnxPppoeSessionRxPapAuthReq_Object = MibTableColumn
tmnxPppoeSessionRxPapAuthReq = _TmnxPppoeSessionRxPapAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 24),
    _TmnxPppoeSessionRxPapAuthReq_Type()
)
tmnxPppoeSessionRxPapAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxPapAuthReq.setStatus("obsolete")
_TmnxPppoeSessionTxPapAuthAck_Type = Counter32
_TmnxPppoeSessionTxPapAuthAck_Object = MibTableColumn
tmnxPppoeSessionTxPapAuthAck = _TmnxPppoeSessionTxPapAuthAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 25),
    _TmnxPppoeSessionTxPapAuthAck_Type()
)
tmnxPppoeSessionTxPapAuthAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxPapAuthAck.setStatus("obsolete")
_TmnxPppoeSessionTxPapAuthNak_Type = Counter32
_TmnxPppoeSessionTxPapAuthNak_Object = MibTableColumn
tmnxPppoeSessionTxPapAuthNak = _TmnxPppoeSessionTxPapAuthNak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 26),
    _TmnxPppoeSessionTxPapAuthNak_Type()
)
tmnxPppoeSessionTxPapAuthNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxPapAuthNak.setStatus("obsolete")
_TmnxPppoeSessionRxChapResponse_Type = Counter32
_TmnxPppoeSessionRxChapResponse_Object = MibTableColumn
tmnxPppoeSessionRxChapResponse = _TmnxPppoeSessionRxChapResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 27),
    _TmnxPppoeSessionRxChapResponse_Type()
)
tmnxPppoeSessionRxChapResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxChapResponse.setStatus("obsolete")
_TmnxPppoeSessionTxChapChallenge_Type = Counter32
_TmnxPppoeSessionTxChapChallenge_Object = MibTableColumn
tmnxPppoeSessionTxChapChallenge = _TmnxPppoeSessionTxChapChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 28),
    _TmnxPppoeSessionTxChapChallenge_Type()
)
tmnxPppoeSessionTxChapChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxChapChallenge.setStatus("obsolete")
_TmnxPppoeSessionTxChapSuccess_Type = Counter32
_TmnxPppoeSessionTxChapSuccess_Object = MibTableColumn
tmnxPppoeSessionTxChapSuccess = _TmnxPppoeSessionTxChapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 29),
    _TmnxPppoeSessionTxChapSuccess_Type()
)
tmnxPppoeSessionTxChapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxChapSuccess.setStatus("obsolete")
_TmnxPppoeSessionTxChapFailure_Type = Counter32
_TmnxPppoeSessionTxChapFailure_Object = MibTableColumn
tmnxPppoeSessionTxChapFailure = _TmnxPppoeSessionTxChapFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 30),
    _TmnxPppoeSessionTxChapFailure_Type()
)
tmnxPppoeSessionTxChapFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxChapFailure.setStatus("obsolete")
_TmnxPppoeSessionRxIpcpConfReq_Type = Counter32
_TmnxPppoeSessionRxIpcpConfReq_Object = MibTableColumn
tmnxPppoeSessionRxIpcpConfReq = _TmnxPppoeSessionRxIpcpConfReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 31),
    _TmnxPppoeSessionRxIpcpConfReq_Type()
)
tmnxPppoeSessionRxIpcpConfReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpcpConfReq.setStatus("obsolete")
_TmnxPppoeSessionRxIpcpConfAck_Type = Counter32
_TmnxPppoeSessionRxIpcpConfAck_Object = MibTableColumn
tmnxPppoeSessionRxIpcpConfAck = _TmnxPppoeSessionRxIpcpConfAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 32),
    _TmnxPppoeSessionRxIpcpConfAck_Type()
)
tmnxPppoeSessionRxIpcpConfAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpcpConfAck.setStatus("obsolete")
_TmnxPppoeSessionRxIpcpConfNak_Type = Counter32
_TmnxPppoeSessionRxIpcpConfNak_Object = MibTableColumn
tmnxPppoeSessionRxIpcpConfNak = _TmnxPppoeSessionRxIpcpConfNak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 33),
    _TmnxPppoeSessionRxIpcpConfNak_Type()
)
tmnxPppoeSessionRxIpcpConfNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpcpConfNak.setStatus("obsolete")
_TmnxPppoeSessionRxIpcpConfRej_Type = Counter32
_TmnxPppoeSessionRxIpcpConfRej_Object = MibTableColumn
tmnxPppoeSessionRxIpcpConfRej = _TmnxPppoeSessionRxIpcpConfRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 34),
    _TmnxPppoeSessionRxIpcpConfRej_Type()
)
tmnxPppoeSessionRxIpcpConfRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpcpConfRej.setStatus("obsolete")
_TmnxPppoeSessionRxIpcpTermReq_Type = Counter32
_TmnxPppoeSessionRxIpcpTermReq_Object = MibTableColumn
tmnxPppoeSessionRxIpcpTermReq = _TmnxPppoeSessionRxIpcpTermReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 35),
    _TmnxPppoeSessionRxIpcpTermReq_Type()
)
tmnxPppoeSessionRxIpcpTermReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpcpTermReq.setStatus("obsolete")
_TmnxPppoeSessionRxIpcpTermAck_Type = Counter32
_TmnxPppoeSessionRxIpcpTermAck_Object = MibTableColumn
tmnxPppoeSessionRxIpcpTermAck = _TmnxPppoeSessionRxIpcpTermAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 36),
    _TmnxPppoeSessionRxIpcpTermAck_Type()
)
tmnxPppoeSessionRxIpcpTermAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpcpTermAck.setStatus("obsolete")
_TmnxPppoeSessionRxIpcpCodeRej_Type = Counter32
_TmnxPppoeSessionRxIpcpCodeRej_Object = MibTableColumn
tmnxPppoeSessionRxIpcpCodeRej = _TmnxPppoeSessionRxIpcpCodeRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 37),
    _TmnxPppoeSessionRxIpcpCodeRej_Type()
)
tmnxPppoeSessionRxIpcpCodeRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpcpCodeRej.setStatus("obsolete")
_TmnxPppoeSessionTxIpcpConfReq_Type = Counter32
_TmnxPppoeSessionTxIpcpConfReq_Object = MibTableColumn
tmnxPppoeSessionTxIpcpConfReq = _TmnxPppoeSessionTxIpcpConfReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 38),
    _TmnxPppoeSessionTxIpcpConfReq_Type()
)
tmnxPppoeSessionTxIpcpConfReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpcpConfReq.setStatus("obsolete")
_TmnxPppoeSessionTxIpcpConfAck_Type = Counter32
_TmnxPppoeSessionTxIpcpConfAck_Object = MibTableColumn
tmnxPppoeSessionTxIpcpConfAck = _TmnxPppoeSessionTxIpcpConfAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 39),
    _TmnxPppoeSessionTxIpcpConfAck_Type()
)
tmnxPppoeSessionTxIpcpConfAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpcpConfAck.setStatus("obsolete")
_TmnxPppoeSessionTxIpcpConfNak_Type = Counter32
_TmnxPppoeSessionTxIpcpConfNak_Object = MibTableColumn
tmnxPppoeSessionTxIpcpConfNak = _TmnxPppoeSessionTxIpcpConfNak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 40),
    _TmnxPppoeSessionTxIpcpConfNak_Type()
)
tmnxPppoeSessionTxIpcpConfNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpcpConfNak.setStatus("obsolete")
_TmnxPppoeSessionTxIpcpConfRej_Type = Counter32
_TmnxPppoeSessionTxIpcpConfRej_Object = MibTableColumn
tmnxPppoeSessionTxIpcpConfRej = _TmnxPppoeSessionTxIpcpConfRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 41),
    _TmnxPppoeSessionTxIpcpConfRej_Type()
)
tmnxPppoeSessionTxIpcpConfRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpcpConfRej.setStatus("obsolete")
_TmnxPppoeSessionTxIpcpTermReq_Type = Counter32
_TmnxPppoeSessionTxIpcpTermReq_Object = MibTableColumn
tmnxPppoeSessionTxIpcpTermReq = _TmnxPppoeSessionTxIpcpTermReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 42),
    _TmnxPppoeSessionTxIpcpTermReq_Type()
)
tmnxPppoeSessionTxIpcpTermReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpcpTermReq.setStatus("obsolete")
_TmnxPppoeSessionTxIpcpTermAck_Type = Counter32
_TmnxPppoeSessionTxIpcpTermAck_Object = MibTableColumn
tmnxPppoeSessionTxIpcpTermAck = _TmnxPppoeSessionTxIpcpTermAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 43),
    _TmnxPppoeSessionTxIpcpTermAck_Type()
)
tmnxPppoeSessionTxIpcpTermAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpcpTermAck.setStatus("obsolete")
_TmnxPppoeSessionTxIpcpCodeRej_Type = Counter32
_TmnxPppoeSessionTxIpcpCodeRej_Object = MibTableColumn
tmnxPppoeSessionTxIpcpCodeRej = _TmnxPppoeSessionTxIpcpCodeRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 44),
    _TmnxPppoeSessionTxIpcpCodeRej_Type()
)
tmnxPppoeSessionTxIpcpCodeRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpcpCodeRej.setStatus("obsolete")
_TmnxPppoeSessionRxIpv6cpConfReq_Type = Counter32
_TmnxPppoeSessionRxIpv6cpConfReq_Object = MibTableColumn
tmnxPppoeSessionRxIpv6cpConfReq = _TmnxPppoeSessionRxIpv6cpConfReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 45),
    _TmnxPppoeSessionRxIpv6cpConfReq_Type()
)
tmnxPppoeSessionRxIpv6cpConfReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpv6cpConfReq.setStatus("obsolete")
_TmnxPppoeSessionRxIpv6cpConfAck_Type = Counter32
_TmnxPppoeSessionRxIpv6cpConfAck_Object = MibTableColumn
tmnxPppoeSessionRxIpv6cpConfAck = _TmnxPppoeSessionRxIpv6cpConfAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 46),
    _TmnxPppoeSessionRxIpv6cpConfAck_Type()
)
tmnxPppoeSessionRxIpv6cpConfAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpv6cpConfAck.setStatus("obsolete")
_TmnxPppoeSessionRxIpv6cpConfNak_Type = Counter32
_TmnxPppoeSessionRxIpv6cpConfNak_Object = MibTableColumn
tmnxPppoeSessionRxIpv6cpConfNak = _TmnxPppoeSessionRxIpv6cpConfNak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 47),
    _TmnxPppoeSessionRxIpv6cpConfNak_Type()
)
tmnxPppoeSessionRxIpv6cpConfNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpv6cpConfNak.setStatus("obsolete")
_TmnxPppoeSessionRxIpv6cpConfRej_Type = Counter32
_TmnxPppoeSessionRxIpv6cpConfRej_Object = MibTableColumn
tmnxPppoeSessionRxIpv6cpConfRej = _TmnxPppoeSessionRxIpv6cpConfRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 48),
    _TmnxPppoeSessionRxIpv6cpConfRej_Type()
)
tmnxPppoeSessionRxIpv6cpConfRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpv6cpConfRej.setStatus("obsolete")
_TmnxPppoeSessionRxIpv6cpTermReq_Type = Counter32
_TmnxPppoeSessionRxIpv6cpTermReq_Object = MibTableColumn
tmnxPppoeSessionRxIpv6cpTermReq = _TmnxPppoeSessionRxIpv6cpTermReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 49),
    _TmnxPppoeSessionRxIpv6cpTermReq_Type()
)
tmnxPppoeSessionRxIpv6cpTermReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpv6cpTermReq.setStatus("obsolete")
_TmnxPppoeSessionRxIpv6cpTermAck_Type = Counter32
_TmnxPppoeSessionRxIpv6cpTermAck_Object = MibTableColumn
tmnxPppoeSessionRxIpv6cpTermAck = _TmnxPppoeSessionRxIpv6cpTermAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 50),
    _TmnxPppoeSessionRxIpv6cpTermAck_Type()
)
tmnxPppoeSessionRxIpv6cpTermAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpv6cpTermAck.setStatus("obsolete")
_TmnxPppoeSessionRxIpv6cpCodeRej_Type = Counter32
_TmnxPppoeSessionRxIpv6cpCodeRej_Object = MibTableColumn
tmnxPppoeSessionRxIpv6cpCodeRej = _TmnxPppoeSessionRxIpv6cpCodeRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 51),
    _TmnxPppoeSessionRxIpv6cpCodeRej_Type()
)
tmnxPppoeSessionRxIpv6cpCodeRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionRxIpv6cpCodeRej.setStatus("obsolete")
_TmnxPppoeSessionTxIpv6cpConfReq_Type = Counter32
_TmnxPppoeSessionTxIpv6cpConfReq_Object = MibTableColumn
tmnxPppoeSessionTxIpv6cpConfReq = _TmnxPppoeSessionTxIpv6cpConfReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 52),
    _TmnxPppoeSessionTxIpv6cpConfReq_Type()
)
tmnxPppoeSessionTxIpv6cpConfReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpv6cpConfReq.setStatus("obsolete")
_TmnxPppoeSessionTxIpv6cpConfAck_Type = Counter32
_TmnxPppoeSessionTxIpv6cpConfAck_Object = MibTableColumn
tmnxPppoeSessionTxIpv6cpConfAck = _TmnxPppoeSessionTxIpv6cpConfAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 53),
    _TmnxPppoeSessionTxIpv6cpConfAck_Type()
)
tmnxPppoeSessionTxIpv6cpConfAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpv6cpConfAck.setStatus("obsolete")
_TmnxPppoeSessionTxIpv6cpConfNak_Type = Counter32
_TmnxPppoeSessionTxIpv6cpConfNak_Object = MibTableColumn
tmnxPppoeSessionTxIpv6cpConfNak = _TmnxPppoeSessionTxIpv6cpConfNak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 54),
    _TmnxPppoeSessionTxIpv6cpConfNak_Type()
)
tmnxPppoeSessionTxIpv6cpConfNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpv6cpConfNak.setStatus("obsolete")
_TmnxPppoeSessionTxIpv6cpConfRej_Type = Counter32
_TmnxPppoeSessionTxIpv6cpConfRej_Object = MibTableColumn
tmnxPppoeSessionTxIpv6cpConfRej = _TmnxPppoeSessionTxIpv6cpConfRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 55),
    _TmnxPppoeSessionTxIpv6cpConfRej_Type()
)
tmnxPppoeSessionTxIpv6cpConfRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpv6cpConfRej.setStatus("obsolete")
_TmnxPppoeSessionTxIpv6cpTermReq_Type = Counter32
_TmnxPppoeSessionTxIpv6cpTermReq_Object = MibTableColumn
tmnxPppoeSessionTxIpv6cpTermReq = _TmnxPppoeSessionTxIpv6cpTermReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 56),
    _TmnxPppoeSessionTxIpv6cpTermReq_Type()
)
tmnxPppoeSessionTxIpv6cpTermReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpv6cpTermReq.setStatus("obsolete")
_TmnxPppoeSessionTxIpv6cpTermAck_Type = Counter32
_TmnxPppoeSessionTxIpv6cpTermAck_Object = MibTableColumn
tmnxPppoeSessionTxIpv6cpTermAck = _TmnxPppoeSessionTxIpv6cpTermAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 57),
    _TmnxPppoeSessionTxIpv6cpTermAck_Type()
)
tmnxPppoeSessionTxIpv6cpTermAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpv6cpTermAck.setStatus("obsolete")
_TmnxPppoeSessionTxIpv6cpCodeRej_Type = Counter32
_TmnxPppoeSessionTxIpv6cpCodeRej_Object = MibTableColumn
tmnxPppoeSessionTxIpv6cpCodeRej = _TmnxPppoeSessionTxIpv6cpCodeRej_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 10, 1, 58),
    _TmnxPppoeSessionTxIpv6cpCodeRej_Type()
)
tmnxPppoeSessionTxIpv6cpCodeRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionTxIpv6cpCodeRej.setStatus("obsolete")
_TmnxPppoeManagedRouteTable_Object = MibTable
tmnxPppoeManagedRouteTable = _TmnxPppoeManagedRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxPppoeManagedRouteTable.setStatus("obsolete")
_TmnxPppoeManagedRouteEntry_Object = MibTableRow
tmnxPppoeManagedRouteEntry = _TmnxPppoeManagedRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 11, 1)
)
tmnxPppoeManagedRouteEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionMac"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionId"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeManagedRouteAddrType"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeManagedRouteAddr"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeManagedRoutePrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxPppoeManagedRouteEntry.setStatus("obsolete")
_TmnxPppoeManagedRouteAddrType_Type = InetAddressType
_TmnxPppoeManagedRouteAddrType_Object = MibTableColumn
tmnxPppoeManagedRouteAddrType = _TmnxPppoeManagedRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 11, 1, 1),
    _TmnxPppoeManagedRouteAddrType_Type()
)
tmnxPppoeManagedRouteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeManagedRouteAddrType.setStatus("obsolete")


class _TmnxPppoeManagedRouteAddr_Type(InetAddress):
    """Custom type tmnxPppoeManagedRouteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPppoeManagedRouteAddr_Type.__name__ = "InetAddress"
_TmnxPppoeManagedRouteAddr_Object = MibTableColumn
tmnxPppoeManagedRouteAddr = _TmnxPppoeManagedRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 11, 1, 2),
    _TmnxPppoeManagedRouteAddr_Type()
)
tmnxPppoeManagedRouteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeManagedRouteAddr.setStatus("obsolete")


class _TmnxPppoeManagedRoutePrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxPppoeManagedRoutePrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxPppoeManagedRoutePrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxPppoeManagedRoutePrefixLen_Object = MibTableColumn
tmnxPppoeManagedRoutePrefixLen = _TmnxPppoeManagedRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 11, 1, 3),
    _TmnxPppoeManagedRoutePrefixLen_Type()
)
tmnxPppoeManagedRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeManagedRoutePrefixLen.setStatus("obsolete")
_TmnxPppoeManagedRouteStatus_Type = TmnxManagedRouteStatus
_TmnxPppoeManagedRouteStatus_Object = MibTableColumn
tmnxPppoeManagedRouteStatus = _TmnxPppoeManagedRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 11, 1, 4),
    _TmnxPppoeManagedRouteStatus_Type()
)
tmnxPppoeManagedRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeManagedRouteStatus.setStatus("obsolete")
_TmnxPppoeSessionBgpTable_Object = MibTable
tmnxPppoeSessionBgpTable = _TmnxPppoeSessionBgpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpTable.setStatus("obsolete")
_TmnxPppoeSessionBgpEntry_Object = MibTableRow
tmnxPppoeSessionBgpEntry = _TmnxPppoeSessionBgpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpEntry.setStatus("obsolete")
_TmnxPppoeSessionBgpPrngPlcyName_Type = TNamedItemOrEmpty
_TmnxPppoeSessionBgpPrngPlcyName_Object = MibTableColumn
tmnxPppoeSessionBgpPrngPlcyName = _TmnxPppoeSessionBgpPrngPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1, 1),
    _TmnxPppoeSessionBgpPrngPlcyName_Type()
)
tmnxPppoeSessionBgpPrngPlcyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpPrngPlcyName.setStatus("obsolete")
_TmnxPppoeSessionBgpAuthKeyChain_Type = TNamedItemOrEmpty
_TmnxPppoeSessionBgpAuthKeyChain_Object = MibTableColumn
tmnxPppoeSessionBgpAuthKeyChain = _TmnxPppoeSessionBgpAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1, 2),
    _TmnxPppoeSessionBgpAuthKeyChain_Type()
)
tmnxPppoeSessionBgpAuthKeyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpAuthKeyChain.setStatus("obsolete")


class _TmnxPppoeSessionBgpMD5AuthKey_Type(OctetString):
    """Custom type tmnxPppoeSessionBgpMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxPppoeSessionBgpMD5AuthKey_Type.__name__ = "OctetString"
_TmnxPppoeSessionBgpMD5AuthKey_Object = MibTableColumn
tmnxPppoeSessionBgpMD5AuthKey = _TmnxPppoeSessionBgpMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1, 3),
    _TmnxPppoeSessionBgpMD5AuthKey_Type()
)
tmnxPppoeSessionBgpMD5AuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpMD5AuthKey.setStatus("obsolete")
_TmnxPppoeSessionBgpImportPolicy_Type = TPolicyStatementNameOrEmpty
_TmnxPppoeSessionBgpImportPolicy_Object = MibTableColumn
tmnxPppoeSessionBgpImportPolicy = _TmnxPppoeSessionBgpImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1, 4),
    _TmnxPppoeSessionBgpImportPolicy_Type()
)
tmnxPppoeSessionBgpImportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpImportPolicy.setStatus("obsolete")
_TmnxPppoeSessionBgpExportPolicy_Type = TPolicyStatementNameOrEmpty
_TmnxPppoeSessionBgpExportPolicy_Object = MibTableColumn
tmnxPppoeSessionBgpExportPolicy = _TmnxPppoeSessionBgpExportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1, 5),
    _TmnxPppoeSessionBgpExportPolicy_Type()
)
tmnxPppoeSessionBgpExportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpExportPolicy.setStatus("obsolete")
_TmnxPppoeSessionBgpPeerAS_Type = InetAutonomousSystemNumber
_TmnxPppoeSessionBgpPeerAS_Object = MibTableColumn
tmnxPppoeSessionBgpPeerAS = _TmnxPppoeSessionBgpPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1, 6),
    _TmnxPppoeSessionBgpPeerAS_Type()
)
tmnxPppoeSessionBgpPeerAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpPeerAS.setStatus("obsolete")
_TmnxPppoeSessionBgpPeeringStatus_Type = BgpPeeringStatus
_TmnxPppoeSessionBgpPeeringStatus_Object = MibTableColumn
tmnxPppoeSessionBgpPeeringStatus = _TmnxPppoeSessionBgpPeeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 12, 1, 7),
    _TmnxPppoeSessionBgpPeeringStatus_Type()
)
tmnxPppoeSessionBgpPeeringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionBgpPeeringStatus.setStatus("obsolete")
_TmnxPppoeSessionOverridesTable_Object = MibTable
tmnxPppoeSessionOverridesTable = _TmnxPppoeSessionOverridesTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionOverridesTable.setStatus("obsolete")
_TmnxPppoeSessionOverridesEntry_Object = MibTableRow
tmnxPppoeSessionOverridesEntry = _TmnxPppoeSessionOverridesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1)
)
tmnxPppoeSessionOverridesEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionMac"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionId"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrDirection"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrType"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrTypeId"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrTypeName"),
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionOverridesEntry.setStatus("obsolete")


class _TmnxPppoeSessionOvrDirection_Type(TDirection):
    """Custom type tmnxPppoeSessionOvrDirection based on TDirection"""
    subtypeSpec = TDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_TmnxPppoeSessionOvrDirection_Type.__name__ = "TDirection"
_TmnxPppoeSessionOvrDirection_Object = MibTableColumn
tmnxPppoeSessionOvrDirection = _TmnxPppoeSessionOvrDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 1),
    _TmnxPppoeSessionOvrDirection_Type()
)
tmnxPppoeSessionOvrDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrDirection.setStatus("obsolete")
_TmnxPppoeSessionOvrType_Type = TQosOverrideType
_TmnxPppoeSessionOvrType_Object = MibTableColumn
tmnxPppoeSessionOvrType = _TmnxPppoeSessionOvrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 2),
    _TmnxPppoeSessionOvrType_Type()
)
tmnxPppoeSessionOvrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrType.setStatus("obsolete")
_TmnxPppoeSessionOvrTypeId_Type = Integer32
_TmnxPppoeSessionOvrTypeId_Object = MibTableColumn
tmnxPppoeSessionOvrTypeId = _TmnxPppoeSessionOvrTypeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 3),
    _TmnxPppoeSessionOvrTypeId_Type()
)
tmnxPppoeSessionOvrTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrTypeId.setStatus("obsolete")
_TmnxPppoeSessionOvrTypeName_Type = TNamedItemOrEmpty
_TmnxPppoeSessionOvrTypeName_Object = MibTableColumn
tmnxPppoeSessionOvrTypeName = _TmnxPppoeSessionOvrTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 4),
    _TmnxPppoeSessionOvrTypeName_Type()
)
tmnxPppoeSessionOvrTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrTypeName.setStatus("obsolete")
_TmnxPppoeSessionOvrPIR_Type = TPIRRateOverride
_TmnxPppoeSessionOvrPIR_Object = MibTableColumn
tmnxPppoeSessionOvrPIR = _TmnxPppoeSessionOvrPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 5),
    _TmnxPppoeSessionOvrPIR_Type()
)
tmnxPppoeSessionOvrPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrPIR.setStatus("obsolete")
_TmnxPppoeSessionOvrCIR_Type = TCIRRateOverride
_TmnxPppoeSessionOvrCIR_Object = MibTableColumn
tmnxPppoeSessionOvrCIR = _TmnxPppoeSessionOvrCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 6),
    _TmnxPppoeSessionOvrCIR_Type()
)
tmnxPppoeSessionOvrCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrCIR.setStatus("obsolete")
_TmnxPppoeSessionOvrCBS_Type = TBurstSizeBytesOverride
_TmnxPppoeSessionOvrCBS_Object = MibTableColumn
tmnxPppoeSessionOvrCBS = _TmnxPppoeSessionOvrCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 7),
    _TmnxPppoeSessionOvrCBS_Type()
)
tmnxPppoeSessionOvrCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrCBS.setStatus("obsolete")
_TmnxPppoeSessionOvrMBS_Type = TBurstSizeBytesOverride
_TmnxPppoeSessionOvrMBS_Object = MibTableColumn
tmnxPppoeSessionOvrMBS = _TmnxPppoeSessionOvrMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 13, 1, 8),
    _TmnxPppoeSessionOvrMBS_Type()
)
tmnxPppoeSessionOvrMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionOvrMBS.setStatus("obsolete")
_TmnxPppoeSessionAleTable_Object = MibTable
tmnxPppoeSessionAleTable = _TmnxPppoeSessionAleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionAleTable.setStatus("obsolete")
_TmnxPppoeSessionAleEntry_Object = MibTableRow
tmnxPppoeSessionAleEntry = _TmnxPppoeSessionAleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 15, 1)
)
tmnxPppoeSessionAleEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionMac"),
    (0, "TIMETRA-PPPOE-MIB", "tmnxPppoeSessionId"),
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionAleEntry.setStatus("obsolete")
_TmnxPppoeSessionAleDatalink_Type = TmnxAccessLoopEncapDataLink
_TmnxPppoeSessionAleDatalink_Object = MibTableColumn
tmnxPppoeSessionAleDatalink = _TmnxPppoeSessionAleDatalink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 15, 1, 1),
    _TmnxPppoeSessionAleDatalink_Type()
)
tmnxPppoeSessionAleDatalink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionAleDatalink.setStatus("obsolete")
_TmnxPppoeSessionAleEncaps1_Type = TmnxAccessLoopEncaps1
_TmnxPppoeSessionAleEncaps1_Object = MibTableColumn
tmnxPppoeSessionAleEncaps1 = _TmnxPppoeSessionAleEncaps1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 15, 1, 2),
    _TmnxPppoeSessionAleEncaps1_Type()
)
tmnxPppoeSessionAleEncaps1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionAleEncaps1.setStatus("obsolete")
_TmnxPppoeSessionAleEncaps2_Type = TmnxAccessLoopEncaps2
_TmnxPppoeSessionAleEncaps2_Object = MibTableColumn
tmnxPppoeSessionAleEncaps2 = _TmnxPppoeSessionAleEncaps2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 1, 15, 1, 3),
    _TmnxPppoeSessionAleEncaps2_Type()
)
tmnxPppoeSessionAleEncaps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppoeSessionAleEncaps2.setStatus("obsolete")
_TmnxPppoeNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxPppoeNotificationObjs = _TmnxPppoeNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 2)
)
_TmnxPppoeSessionFailureReason_Type = DisplayString
_TmnxPppoeSessionFailureReason_Object = MibScalar
tmnxPppoeSessionFailureReason = _TmnxPppoeSessionFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 2, 1),
    _TmnxPppoeSessionFailureReason_Type()
)
tmnxPppoeSessionFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPppoeSessionFailureReason.setStatus("current")


class _TmnxPppoeNcpFailureProtocol_Type(Integer32):
    """Custom type tmnxPppoeNcpFailureProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipcp", 1),
          ("ipv6cp", 2))
    )


_TmnxPppoeNcpFailureProtocol_Type.__name__ = "Integer32"
_TmnxPppoeNcpFailureProtocol_Object = MibScalar
tmnxPppoeNcpFailureProtocol = _TmnxPppoeNcpFailureProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 2, 2),
    _TmnxPppoeNcpFailureProtocol_Type()
)
tmnxPppoeNcpFailureProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPppoeNcpFailureProtocol.setStatus("current")
_TmnxPppoeNcpFailureReason_Type = DisplayString
_TmnxPppoeNcpFailureReason_Object = MibScalar
tmnxPppoeNcpFailureReason = _TmnxPppoeNcpFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 2, 3),
    _TmnxPppoeNcpFailureReason_Type()
)
tmnxPppoeNcpFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPppoeNcpFailureReason.setStatus("current")
_TmnxPppoeNotifyDescription_Type = DisplayString
_TmnxPppoeNotifyDescription_Object = MibScalar
tmnxPppoeNotifyDescription = _TmnxPppoeNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 2, 4),
    _TmnxPppoeNotifyDescription_Type()
)
tmnxPppoeNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPppoeNotifyDescription.setStatus("current")
_TmnxPppObjects_ObjectIdentity = ObjectIdentity
tmnxPppObjects = _TmnxPppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3)
)
_TmnxPppIesIfTableLastChg_Type = TimeStamp
_TmnxPppIesIfTableLastChg_Object = MibScalar
tmnxPppIesIfTableLastChg = _TmnxPppIesIfTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 1),
    _TmnxPppIesIfTableLastChg_Type()
)
tmnxPppIesIfTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppIesIfTableLastChg.setStatus("current")
_TmnxPppIesIfTable_Object = MibTable
tmnxPppIesIfTable = _TmnxPppIesIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxPppIesIfTable.setStatus("current")
_TmnxPppIesIfEntry_Object = MibTableRow
tmnxPppIesIfEntry = _TmnxPppIesIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2, 1)
)
tmnxPppIesIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxPppIesIfEntry.setStatus("current")
_TmnxPppIesIfLastChg_Type = TimeStamp
_TmnxPppIesIfLastChg_Object = MibTableColumn
tmnxPppIesIfLastChg = _TmnxPppIesIfLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2, 1, 1),
    _TmnxPppIesIfLastChg_Type()
)
tmnxPppIesIfLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppIesIfLastChg.setStatus("current")


class _TmnxPppIesIfDescription_Type(TItemDescription):
    """Custom type tmnxPppIesIfDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxPppIesIfDescription_Type.__name__ = "TItemDescription"
_TmnxPppIesIfDescription_Object = MibTableColumn
tmnxPppIesIfDescription = _TmnxPppIesIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2, 1, 2),
    _TmnxPppIesIfDescription_Type()
)
tmnxPppIesIfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppIesIfDescription.setStatus("current")


class _TmnxPppIesIfAdminState_Type(TmnxPppoeAdminStatus):
    """Custom type tmnxPppIesIfAdminState based on TmnxPppoeAdminStatus"""
    defaultValue = 2


_TmnxPppIesIfAdminState_Type.__name__ = "TmnxPppoeAdminStatus"
_TmnxPppIesIfAdminState_Object = MibTableColumn
tmnxPppIesIfAdminState = _TmnxPppIesIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2, 1, 3),
    _TmnxPppIesIfAdminState_Type()
)
tmnxPppIesIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppIesIfAdminState.setStatus("current")


class _TmnxPppIesIfPolicy_Type(TNamedItem):
    """Custom type tmnxPppIesIfPolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxPppIesIfPolicy_Type.__name__ = "TNamedItem"
_TmnxPppIesIfPolicy_Object = MibTableColumn
tmnxPppIesIfPolicy = _TmnxPppIesIfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2, 1, 4),
    _TmnxPppIesIfPolicy_Type()
)
tmnxPppIesIfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppIesIfPolicy.setStatus("current")


class _TmnxPppIesIfSessionLimit_Type(Unsigned32):
    """Custom type tmnxPppIesIfSessionLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxPppIesIfSessionLimit_Type.__name__ = "Unsigned32"
_TmnxPppIesIfSessionLimit_Object = MibTableColumn
tmnxPppIesIfSessionLimit = _TmnxPppIesIfSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2, 1, 5),
    _TmnxPppIesIfSessionLimit_Type()
)
tmnxPppIesIfSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppIesIfSessionLimit.setStatus("current")


class _TmnxPppIesIfUserDb_Type(TNamedItemOrEmpty):
    """Custom type tmnxPppIesIfUserDb based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxPppIesIfUserDb_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPppIesIfUserDb_Object = MibTableColumn
tmnxPppIesIfUserDb = _TmnxPppIesIfUserDb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 2, 1, 8),
    _TmnxPppIesIfUserDb_Type()
)
tmnxPppIesIfUserDb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppIesIfUserDb.setStatus("current")
_TmnxMlpppObjects_ObjectIdentity = ObjectIdentity
tmnxMlpppObjects = _TmnxMlpppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3)
)
_TmnxMlpppBundleTable_Object = MibTable
tmnxMlpppBundleTable = _TmnxMlpppBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxMlpppBundleTable.setStatus("current")
_TmnxMlpppBundleEntry_Object = MibTableRow
tmnxMlpppBundleEntry = _TmnxMlpppBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1)
)
tmnxMlpppBundleEntry.setIndexNames(
    (0, "TIMETRA-PPPOE-MIB", "tmnxMlpppBundleIndex"),
)
if mibBuilder.loadTexts:
    tmnxMlpppBundleEntry.setStatus("current")
_TmnxMlpppBundleIndex_Type = Unsigned32
_TmnxMlpppBundleIndex_Object = MibTableColumn
tmnxMlpppBundleIndex = _TmnxMlpppBundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 1),
    _TmnxMlpppBundleIndex_Type()
)
tmnxMlpppBundleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMlpppBundleIndex.setStatus("current")
_TmnxMlpppBundleLocEpClass_Type = TmnxMlpppEpClass
_TmnxMlpppBundleLocEpClass_Object = MibTableColumn
tmnxMlpppBundleLocEpClass = _TmnxMlpppBundleLocEpClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 2),
    _TmnxMlpppBundleLocEpClass_Type()
)
tmnxMlpppBundleLocEpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleLocEpClass.setStatus("current")


class _TmnxMlpppBundleLocEpAddress_Type(OctetString):
    """Custom type tmnxMlpppBundleLocEpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMlpppBundleLocEpAddress_Type.__name__ = "OctetString"
_TmnxMlpppBundleLocEpAddress_Object = MibTableColumn
tmnxMlpppBundleLocEpAddress = _TmnxMlpppBundleLocEpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 3),
    _TmnxMlpppBundleLocEpAddress_Type()
)
tmnxMlpppBundleLocEpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleLocEpAddress.setStatus("current")
_TmnxMlpppBundleRemEpClass_Type = TmnxMlpppEpClass
_TmnxMlpppBundleRemEpClass_Object = MibTableColumn
tmnxMlpppBundleRemEpClass = _TmnxMlpppBundleRemEpClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 4),
    _TmnxMlpppBundleRemEpClass_Type()
)
tmnxMlpppBundleRemEpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleRemEpClass.setStatus("current")


class _TmnxMlpppBundleRemEpAddress_Type(OctetString):
    """Custom type tmnxMlpppBundleRemEpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMlpppBundleRemEpAddress_Type.__name__ = "OctetString"
_TmnxMlpppBundleRemEpAddress_Object = MibTableColumn
tmnxMlpppBundleRemEpAddress = _TmnxMlpppBundleRemEpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 5),
    _TmnxMlpppBundleRemEpAddress_Type()
)
tmnxMlpppBundleRemEpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleRemEpAddress.setStatus("current")
_TmnxMlpppBundleSubPppIndex_Type = Unsigned32
_TmnxMlpppBundleSubPppIndex_Object = MibTableColumn
tmnxMlpppBundleSubPppIndex = _TmnxMlpppBundleSubPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 6),
    _TmnxMlpppBundleSubPppIndex_Type()
)
tmnxMlpppBundleSubPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleSubPppIndex.setStatus("current")
_TmnxMlpppBundleMaxLinks_Type = Unsigned32
_TmnxMlpppBundleMaxLinks_Object = MibTableColumn
tmnxMlpppBundleMaxLinks = _TmnxMlpppBundleMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 7),
    _TmnxMlpppBundleMaxLinks_Type()
)
tmnxMlpppBundleMaxLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleMaxLinks.setStatus("current")
_TmnxMlpppBundleActualLinks_Type = Gauge32
_TmnxMlpppBundleActualLinks_Object = MibTableColumn
tmnxMlpppBundleActualLinks = _TmnxMlpppBundleActualLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 8),
    _TmnxMlpppBundleActualLinks_Type()
)
tmnxMlpppBundleActualLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleActualLinks.setStatus("current")
_TmnxMlpppBundleRemMrru_Type = Unsigned32
_TmnxMlpppBundleRemMrru_Object = MibTableColumn
tmnxMlpppBundleRemMrru = _TmnxMlpppBundleRemMrru_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 9),
    _TmnxMlpppBundleRemMrru_Type()
)
tmnxMlpppBundleRemMrru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleRemMrru.setStatus("current")
_TmnxMlpppBundleLocMrru_Type = Unsigned32
_TmnxMlpppBundleLocMrru_Object = MibTableColumn
tmnxMlpppBundleLocMrru = _TmnxMlpppBundleLocMrru_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 10),
    _TmnxMlpppBundleLocMrru_Type()
)
tmnxMlpppBundleLocMrru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleLocMrru.setStatus("current")


class _TmnxMlpppBundleIndicators_Type(Bits):
    """Custom type tmnxMlpppBundleIndicators based on Bits"""
    namedValues = NamedValues(
        *(("lfiCfg", 0),
          ("lfi", 1),
          ("shortSeqNrRx", 2),
          ("shortSeqNrTx", 3))
    )

_TmnxMlpppBundleIndicators_Type.__name__ = "Bits"
_TmnxMlpppBundleIndicators_Object = MibTableColumn
tmnxMlpppBundleIndicators = _TmnxMlpppBundleIndicators_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 11),
    _TmnxMlpppBundleIndicators_Type()
)
tmnxMlpppBundleIndicators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleIndicators.setStatus("current")
_TmnxMlpppBundleFragmentSize_Type = Unsigned32
_TmnxMlpppBundleFragmentSize_Object = MibTableColumn
tmnxMlpppBundleFragmentSize = _TmnxMlpppBundleFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 12),
    _TmnxMlpppBundleFragmentSize_Type()
)
tmnxMlpppBundleFragmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleFragmentSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMlpppBundleFragmentSize.setUnits("bytes")
_TmnxMlpppBundleMaxDelayCfg_Type = Unsigned32
_TmnxMlpppBundleMaxDelayCfg_Object = MibTableColumn
tmnxMlpppBundleMaxDelayCfg = _TmnxMlpppBundleMaxDelayCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 13),
    _TmnxMlpppBundleMaxDelayCfg_Type()
)
tmnxMlpppBundleMaxDelayCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleMaxDelayCfg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMlpppBundleMaxDelayCfg.setUnits("milliseconds")
_TmnxMlpppBundleMaxDelay_Type = Unsigned32
_TmnxMlpppBundleMaxDelay_Object = MibTableColumn
tmnxMlpppBundleMaxDelay = _TmnxMlpppBundleMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 14),
    _TmnxMlpppBundleMaxDelay_Type()
)
tmnxMlpppBundleMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMlpppBundleMaxDelay.setUnits("milliseconds")
_TmnxMlpppBundleReassemblyTo_Type = Unsigned32
_TmnxMlpppBundleReassemblyTo_Object = MibTableColumn
tmnxMlpppBundleReassemblyTo = _TmnxMlpppBundleReassemblyTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 15),
    _TmnxMlpppBundleReassemblyTo_Type()
)
tmnxMlpppBundleReassemblyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleReassemblyTo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMlpppBundleReassemblyTo.setUnits("milliseconds")
_TmnxMlpppBundleEgressRate_Type = Unsigned32
_TmnxMlpppBundleEgressRate_Object = MibTableColumn
tmnxMlpppBundleEgressRate = _TmnxMlpppBundleEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 1, 1, 16),
    _TmnxMlpppBundleEgressRate_Type()
)
tmnxMlpppBundleEgressRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppBundleEgressRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMlpppBundleEgressRate.setUnits("kbps")
_TmnxMlpppLinkTable_Object = MibTable
tmnxMlpppLinkTable = _TmnxMlpppLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxMlpppLinkTable.setStatus("current")
_TmnxMlpppLinkEntry_Object = MibTableRow
tmnxMlpppLinkEntry = _TmnxMlpppLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 2, 1)
)
tmnxMlpppLinkEntry.setIndexNames(
    (0, "TIMETRA-PPPOE-MIB", "tmnxMlpppBundleIndex"),
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubPppIndex"),
)
if mibBuilder.loadTexts:
    tmnxMlpppLinkEntry.setStatus("current")
_TmnxMlpppLinkRemMrru_Type = Unsigned32
_TmnxMlpppLinkRemMrru_Object = MibTableColumn
tmnxMlpppLinkRemMrru = _TmnxMlpppLinkRemMrru_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 2, 1, 1),
    _TmnxMlpppLinkRemMrru_Type()
)
tmnxMlpppLinkRemMrru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMlpppLinkRemMrru.setStatus("current")
_TmnxPppPlcyMlpppTableLastCh_Type = TimeStamp
_TmnxPppPlcyMlpppTableLastCh_Object = MibScalar
tmnxPppPlcyMlpppTableLastCh = _TmnxPppPlcyMlpppTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 3),
    _TmnxPppPlcyMlpppTableLastCh_Type()
)
tmnxPppPlcyMlpppTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppTableLastCh.setStatus("current")
_TmnxPppPlcyMlpppTable_Object = MibTable
tmnxPppPlcyMlpppTable = _TmnxPppPlcyMlpppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppTable.setStatus("current")
_TmnxPppPlcyMlpppEntry_Object = MibTableRow
tmnxPppPlcyMlpppEntry = _TmnxPppPlcyMlpppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppEntry.setStatus("current")
_TmnxPppPlcyMlpppLastCh_Type = TimeStamp
_TmnxPppPlcyMlpppLastCh_Object = MibTableColumn
tmnxPppPlcyMlpppLastCh = _TmnxPppPlcyMlpppLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4, 1, 1),
    _TmnxPppPlcyMlpppLastCh_Type()
)
tmnxPppPlcyMlpppLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppLastCh.setStatus("current")


class _TmnxPppPlcyMlpppAcceptMrru_Type(TruthValue):
    """Custom type tmnxPppPlcyMlpppAcceptMrru based on TruthValue"""
    defaultValue = 2


_TmnxPppPlcyMlpppAcceptMrru_Type.__name__ = "TruthValue"
_TmnxPppPlcyMlpppAcceptMrru_Object = MibTableColumn
tmnxPppPlcyMlpppAcceptMrru = _TmnxPppPlcyMlpppAcceptMrru_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4, 1, 2),
    _TmnxPppPlcyMlpppAcceptMrru_Type()
)
tmnxPppPlcyMlpppAcceptMrru.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppAcceptMrru.setStatus("current")


class _TmnxPppPlcyMlpppEpClass_Type(TmnxMlpppEpClass):
    """Custom type tmnxPppPlcyMlpppEpClass based on TmnxMlpppEpClass"""
    defaultValue = 0

    subtypeSpec = TmnxMlpppEpClass.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("ipv4Address", 2),
          ("macAddress", 3))
    )


_TmnxPppPlcyMlpppEpClass_Type.__name__ = "TmnxMlpppEpClass"
_TmnxPppPlcyMlpppEpClass_Object = MibTableColumn
tmnxPppPlcyMlpppEpClass = _TmnxPppPlcyMlpppEpClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4, 1, 3),
    _TmnxPppPlcyMlpppEpClass_Type()
)
tmnxPppPlcyMlpppEpClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppEpClass.setStatus("current")


class _TmnxPppPlcyMlpppEpIpv4Address_Type(InetAddressIPv4):
    """Custom type tmnxPppPlcyMlpppEpIpv4Address based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_TmnxPppPlcyMlpppEpIpv4Address_Type.__name__ = "InetAddressIPv4"
_TmnxPppPlcyMlpppEpIpv4Address_Object = MibTableColumn
tmnxPppPlcyMlpppEpIpv4Address = _TmnxPppPlcyMlpppEpIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4, 1, 4),
    _TmnxPppPlcyMlpppEpIpv4Address_Type()
)
tmnxPppPlcyMlpppEpIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppEpIpv4Address.setStatus("current")


class _TmnxPppPlcyMlpppEpMacAddress_Type(MacAddress):
    """Custom type tmnxPppPlcyMlpppEpMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxPppPlcyMlpppEpMacAddress_Type.__name__ = "MacAddress"
_TmnxPppPlcyMlpppEpMacAddress_Object = MibTableColumn
tmnxPppPlcyMlpppEpMacAddress = _TmnxPppPlcyMlpppEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4, 1, 5),
    _TmnxPppPlcyMlpppEpMacAddress_Type()
)
tmnxPppPlcyMlpppEpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppEpMacAddress.setStatus("current")


class _TmnxPppPlcyMlpppShortSeqNumberRx_Type(TruthValue):
    """Custom type tmnxPppPlcyMlpppShortSeqNumberRx based on TruthValue"""
    defaultValue = 2


_TmnxPppPlcyMlpppShortSeqNumberRx_Type.__name__ = "TruthValue"
_TmnxPppPlcyMlpppShortSeqNumberRx_Object = MibTableColumn
tmnxPppPlcyMlpppShortSeqNumberRx = _TmnxPppPlcyMlpppShortSeqNumberRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 49, 3, 3, 4, 1, 6),
    _TmnxPppPlcyMlpppShortSeqNumberRx_Type()
)
tmnxPppPlcyMlpppShortSeqNumberRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPppPlcyMlpppShortSeqNumberRx.setStatus("current")
_TmnxPppoeNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPppoeNotifyPrefix = _TmnxPppoeNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 49)
)
_TmnxPppoeNotifications_ObjectIdentity = ObjectIdentity
tmnxPppoeNotifications = _TmnxPppoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 49, 0)
)
tmnxPppoeSessionEntry.registerAugmentions(
    ("TIMETRA-PPPOE-MIB",
     "tmnxPppoeSessionModifyEntry")
)
tmnxPppoeSessionModifyEntry.setIndexNames(*tmnxPppoeSessionEntry.getIndexNames())
tmnxPppoeSessionEntry.registerAugmentions(
    ("TIMETRA-PPPOE-MIB",
     "tmnxPppoeSessionBgpEntry")
)
tmnxPppoeSessionBgpEntry.setIndexNames(*tmnxPppoeSessionEntry.getIndexNames())
tmnxPppoePlcyEntry.registerAugmentions(
    ("TIMETRA-PPPOE-MIB",
     "tmnxPppPlcyMlpppEntry")
)
tmnxPppPlcyMlpppEntry.setIndexNames(*tmnxPppoePlcyEntry.getIndexNames())

# Managed Objects groups

tmnxPPPoEV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 1)
)
tmnxPPPoEV6v0Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyTableLastChanged"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLastMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaInterval"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaHoldUpMplier"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDisableAcCookies"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPadoDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyMaxSessionsPerMac"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyReplyOnPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppOptionTblLstChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionLstMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionValue"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfInfoTableLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfAdminState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSapSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfPapChapUserDb"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadi"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidVersion"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidCode"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidTags"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidAcCookie"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxDropped"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPado"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPads"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionUpTime"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionLcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppAuthProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSlaProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAncpString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginStrings"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSessionTimeout"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddrType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginIpcpInfo"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCircuitId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRemoteId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSlaProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAncpStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionEvaluateState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxUnknownProto"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxPapAuthReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxChapResponse"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapSuccess"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpCodeRej"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV6v0Group.setStatus("obsolete")

tmnxPPPoEV6v0NotificationObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 3)
)
tmnxPPPoEV6v0NotificationObjGroup.setObjects(
    ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionFailureReason")
)
if mibBuilder.loadTexts:
    tmnxPPPoEV6v0NotificationObjGroup.setStatus("obsolete")

tmnxPPPoEV6v0BsxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 4)
)
tmnxPPPoEV6v0BsxGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAppProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAppProfStr"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV6v0BsxGroup.setStatus("current")

tmnxPPPoEManagedRoutesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 5)
)
tmnxPPPoEManagedRoutesGroup.setObjects(
    ("TIMETRA-PPPOE-MIB", "tmnxPppoeManagedRouteStatus")
)
if mibBuilder.loadTexts:
    tmnxPPPoEManagedRoutesGroup.setStatus("obsolete")

tmnxPPPoEV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 6)
)
tmnxPPPoEV6v1Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyTableLastChanged"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLastMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaInterval"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaHoldUpMplier"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDisableAcCookies"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPadoDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyMaxSessionsPerMac"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyReplyOnPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppAuthentication"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppInitialDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppOptionTblLstChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionLstMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionValue"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfInfoTableLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfAdminState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSapSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfPapChapUserDb"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadi"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidVersion"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidCode"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidTags"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidAcCookie"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxDropped"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPado"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPads"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionUpTime"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionLcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppAuthProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSlaProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAncpString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginStrings"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSessionTimeout"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddrType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginIpcpInfo"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCircuitId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRemoteId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAddressPool"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSlaProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAncpStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionEvaluateState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxUnknownProto"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxPapAuthReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxChapResponse"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapSuccess"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpCodeRej"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV6v1Group.setStatus("obsolete")

tmnxPPPoEV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 7)
)
tmnxPPPoEV7v0Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyTableLastChanged"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLastMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaInterval"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaHoldUpMplier"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDisableAcCookies"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPadoDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyMaxSessionsPerMac"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyReplyOnPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppAuthentication"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppInitialDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMinChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMaxChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppOptionTblLstChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionLstMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionValue"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfInfoTableLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfAdminState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSapSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfUserDb"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDhcpcCcagOriginSap"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadi"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidVersion"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidCode"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidTags"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidAcCookie"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxDropped"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPado"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPads"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionUpTime"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionLcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppAuthProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSlaProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAncpString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginStrings"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSessionTimeout"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddrType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginIpcpInfo"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCircuitId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRemoteId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAddressPool"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRetailerSvcId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRetailerIf"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionL2tpVrtrId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionL2tpConnectionId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionServiceName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCategoryMapName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRadiusClassAttr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRadiusUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSlaProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAncpStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionEvaluateState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxUnknownProto"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxPapAuthReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxChapResponse"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapSuccess"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpCodeRej"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV7v0Group.setStatus("obsolete")

tmnxPPPoESessionBGPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 8)
)
tmnxPPPoESessionBGPGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPrngPlcyName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpAuthKeyChain"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpMD5AuthKey"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpImportPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpExportPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPeerAS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPeeringStatus"))
)
if mibBuilder.loadTexts:
    tmnxPPPoESessionBGPGroup.setStatus("obsolete")

tmnxPPPoEV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 10)
)
tmnxPPPoEV8v0Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyTableLastChanged"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLastMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaInterval"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpKaHoldUpMplier"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDisableAcCookies"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPadoDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyMaxSessionsPerMac"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyReplyOnPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppAuthentication"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppInitialDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMinChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMaxChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppOptionTblLstChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionRowStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionLstMgmtChange"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyOptionValue"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfInfoTableLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfAdminState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfSapSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfUserDb"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDhcpcCcagOriginSap"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfAntiSpoofing"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadi"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidVersion"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidCode"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidTags"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidAcCookie"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxDropped"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPado"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPads"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxPadt"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSapTxSession"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionUpTime"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionLcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppAuthProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSlaProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAncpString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginStrings"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSessionTimeout"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddrType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginIpcpInfo"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCircuitId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRemoteId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAddressPool"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRetailerSvcId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRetailerIf"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionL2tpVrtrId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionL2tpConnectionId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionServiceName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCategoryMapName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRadiusClassAttr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRadiusUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6cpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionInterfaceId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginIpv6cpInfo"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6Dns1"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6Dns2"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DelPfxType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DelPfxLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DelPfx"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6PrefixType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6PrefixLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6Prefix"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSlaProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAncpStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionEvaluateState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxUnknownProto"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxPapAuthReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxChapResponse"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapSuccess"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrPIR"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrCIR"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrCBS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrMBS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleDatalink"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleEncaps1"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleEncaps2"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV8v0Group.setStatus("current")

tmnxPPPoEV8v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 12)
)
tmnxPPPoEV8v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionFailureReason"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailureProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV8v0NotifyObjsGroup.setStatus("obsolete")

tmnxPPPoEV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 15)
)
tmnxPPPoEV9v0Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppIpcpSubnetNeg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPadoAcName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyPppMtuForceGt1492"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyUniqueSessIdsPerSap"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV9v0Group.setStatus("current")

tmnxPPPV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 16)
)
tmnxPPPV9v0Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppIesIfTableLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppIesIfLastChg"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppIesIfDescription"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppIesIfAdminState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppIesIfPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppIesIfSessionLimit"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppIesIfUserDb"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubPppIndex"))
)
if mibBuilder.loadTexts:
    tmnxPPPV9v0Group.setStatus("current")

tmnxPPPMlpppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 20)
)
tmnxPPPMlpppGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleLocEpClass"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleLocEpAddress"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleRemEpClass"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleRemEpAddress"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleSubPppIndex"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleMaxLinks"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleActualLinks"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleRemMrru"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleLocMrru"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleIndicators"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleFragmentSize"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleMaxDelayCfg"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleMaxDelay"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleReassemblyTo"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleEgressRate"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppPlcyMlpppTableLastCh"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppLinkRemMrru"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppPlcyMlpppLastCh"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppPlcyMlpppAcceptMrru"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppPlcyMlpppEpClass"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppPlcyMlpppEpIpv4Address"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppPlcyMlpppEpMacAddress"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppPlcyMlpppShortSeqNumberRx"))
)
if mibBuilder.loadTexts:
    tmnxPPPMlpppGroup.setStatus("current")

tmnxPPPRejectDisabledNcp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 21)
)
tmnxPPPRejectDisabledNcp.setObjects(
    ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyRejectDisabledNcp")
)
if mibBuilder.loadTexts:
    tmnxPPPRejectDisabledNcp.setStatus("current")

tmnxPPPoEV10v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 22)
)
tmnxPPPoEV10v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionFailureReason"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailureProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailureReason"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV10v0NotifyObjsGroup.setStatus("current")

tmnxPPPLcpIgnoreMagic = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 25)
)
tmnxPPPLcpIgnoreMagic.setObjects(
    ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyLcpIgnoreMagic")
)
if mibBuilder.loadTexts:
    tmnxPPPLcpIgnoreMagic.setStatus("current")

tmnxPPPoEV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 26)
)
tmnxPPPoEV11v0Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidMac"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcySessionTimeout"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDhcpcInclOptString"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV11v0Group.setStatus("obsolete")

tmnxPPPPlcyAllowSameCidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 27)
)
tmnxPPPPlcyAllowSameCidGroup.setObjects(
    ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyAllowSameCidForDhcp")
)
if mibBuilder.loadTexts:
    tmnxPPPPlcyAllowSameCidGroup.setStatus("current")

tmnxPPPoEV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 30)
)
tmnxPPPoEV12v0Group.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSapRxInvalidMac"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcySessionTimeout"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyReestablishSession"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV12v0Group.setStatus("current")

tmnxPPPoEDefaultUsernameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 31)
)
tmnxPPPoEDefaultUsernameGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDefaultUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoePlcyDefaultPapPassword"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEDefaultUsernameGroup.setStatus("current")

tmnxPPPoEObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 98)
)
tmnxPPPoEObsoletedGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfPapChapUserDb"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeManagedRouteStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleDatalink"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleEncaps1"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleEncaps2"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpAuthKeyChain"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpExportPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpImportPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpMD5AuthKey"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPeerAS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPeeringStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPrngPlcyName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionEvaluateState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAncpStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAppProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSlaProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrCBS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrCIR"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrMBS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrPIR"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxChapResponse"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxIpv6cpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxPapAuthReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRxUnknownProto"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapChallenge"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxChapSuccess"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxIpv6cpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpCodeRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpConfReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpDiscReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoRep"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpEchoReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpProtRej"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxLcpTermReq"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthAck"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionTxPapAuthNak"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeManagedRouteStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleDatalink"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleEncaps1"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAleEncaps2"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpAuthKeyChain"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpExportPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpImportPolicy"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpMD5AuthKey"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPeerAS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPeeringStatus"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionBgpPrngPlcyName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionEvaluateState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAncpStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModAppProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSlaProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionModSubProfStr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrCBS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrCIR"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrMBS"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOvrPIR"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionUpTime"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionLcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpcpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppMtu"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppAuthProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPppUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginSubIdent"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSubProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSlaProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAncpString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionInterDestId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAppProfString"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginStrings"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSessionTimeout"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddrType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpAddr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryDns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionPrimaryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionSecondryNbns"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginIpcpInfo"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCircuitId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRemoteId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionAddressPool"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRetailerSvcId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRetailerIf"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionL2tpVrtrId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionL2tpConnectionId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionCategoryMapName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRadiusClassAttr"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionRadiusUserName"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6cpState"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionInterfaceId"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionOriginIpv6cpInfo"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DnsType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6Dns1"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6Dns2"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DelPfxType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DelPfxLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6DelPfx"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6PrefixType"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6PrefixLen"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionIpv6Prefix"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeIesIfDhcpcInclOptString"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEObsoletedGroup.setStatus("current")


# Notification objects

tmnxPppoeSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 49, 0, 1)
)
tmnxPppoeSessionFailure.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxPppoeSessionFailure.setStatus(
        "current"
    )

tmnxPppoeNcpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 49, 0, 2)
)
tmnxPppoeNcpFailure.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailureProtocol"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxPppoeNcpFailure.setStatus(
        "current"
    )

tmnxMlpppBundleIndicatorsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 49, 0, 3)
)
tmnxMlpppBundleIndicatorsChange.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleIndicators"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxMlpppBundleIndicatorsChange.setStatus(
        "current"
    )


# Notifications groups

tmnxPPPoEV6v0NotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 2)
)
tmnxPPPoEV6v0NotifyGroup.setObjects(
    ("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionFailure")
)
if mibBuilder.loadTexts:
    tmnxPPPoEV6v0NotifyGroup.setStatus(
        "obsolete"
    )

tmnxPPPoEV8v0NotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 11)
)
tmnxPPPoEV8v0NotifyGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailure"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV8v0NotifyGroup.setStatus(
        "obsolete"
    )

tmnxPPPoEV10v0NotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 2, 23)
)
tmnxPPPoEV10v0NotifyGroup.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPppoeSessionFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxPppoeNcpFailure"),
        ("TIMETRA-PPPOE-MIB", "tmnxMlpppBundleIndicatorsChange"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV10v0NotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPPPoE77x0V6v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 1)
)
tmnxPPPoE77x0V6v0MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"))
)
if mibBuilder.loadTexts:
    tmnxPPPoE77x0V6v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxPPPoE77x0V6v1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 2)
)
tmnxPPPoE77x0V6v1MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v1Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEManagedRoutesGroup"))
)
if mibBuilder.loadTexts:
    tmnxPPPoE77x0V6v1MIBCompliance.setStatus(
        "obsolete"
    )

tmnxPPPoE77x0V7v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 3)
)
tmnxPPPoE77x0V7v0MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV7v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0NotificationObjGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEManagedRoutesGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoESessionBGPGroup"))
)
if mibBuilder.loadTexts:
    tmnxPPPoE77x0V7v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxPPPoE77x0V8v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 4)
)
tmnxPPPoE77x0V8v0MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV8v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV8v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEManagedRoutesGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoESessionBGPGroup"))
)
if mibBuilder.loadTexts:
    tmnxPPPoE77x0V8v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxPPPoE77x0V9v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 5)
)
tmnxPPPoE77x0V9v0MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV8v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV8v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPPlcyAllowSameCidGroup"))
)
if mibBuilder.loadTexts:
    tmnxPPPoE77x0V9v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxPPPoEV10v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 6)
)
tmnxPPPoEV10v0MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV8v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV10v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPMlpppGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPRejectDisabledNcp"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPPlcyAllowSameCidGroup"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV10v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxPPPoEV11v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 7)
)
tmnxPPPoEV11v0MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV8v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV10v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPMlpppGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPRejectDisabledNcp"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPLcpIgnoreMagic"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPPlcyAllowSameCidGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV11v0MIBCompliance.setStatus(
        "obsolete"
    )

tmnxPPPoEV12v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 49, 1, 8)
)
tmnxPPPoEV12v0MIBCompliance.setObjects(
      *(("TIMETRA-PPPOE-MIB", "tmnxPPPoEV8v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV10v0NotifyGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV6v0BsxGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPV9v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPMlpppGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPRejectDisabledNcp"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPLcpIgnoreMagic"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPPlcyAllowSameCidGroup"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEV12v0Group"),
        ("TIMETRA-PPPOE-MIB", "tmnxPPPoEDefaultUsernameGroup"))
)
if mibBuilder.loadTexts:
    tmnxPPPoEV12v0MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PPPOE-MIB",
    **{"TmnxPppoeAdminStatus": TmnxPppoeAdminStatus,
       "timetraPppoeMIBModule": timetraPppoeMIBModule,
       "tmnxPppoeConformance": tmnxPppoeConformance,
       "tmnxPppoeCompliances": tmnxPppoeCompliances,
       "tmnxPPPoE77x0V6v0MIBCompliance": tmnxPPPoE77x0V6v0MIBCompliance,
       "tmnxPPPoE77x0V6v1MIBCompliance": tmnxPPPoE77x0V6v1MIBCompliance,
       "tmnxPPPoE77x0V7v0MIBCompliance": tmnxPPPoE77x0V7v0MIBCompliance,
       "tmnxPPPoE77x0V8v0MIBCompliance": tmnxPPPoE77x0V8v0MIBCompliance,
       "tmnxPPPoE77x0V9v0MIBCompliance": tmnxPPPoE77x0V9v0MIBCompliance,
       "tmnxPPPoEV10v0MIBCompliance": tmnxPPPoEV10v0MIBCompliance,
       "tmnxPPPoEV11v0MIBCompliance": tmnxPPPoEV11v0MIBCompliance,
       "tmnxPPPoEV12v0MIBCompliance": tmnxPPPoEV12v0MIBCompliance,
       "tmnxPppoeGroups": tmnxPppoeGroups,
       "tmnxPPPoEV6v0Group": tmnxPPPoEV6v0Group,
       "tmnxPPPoEV6v0NotifyGroup": tmnxPPPoEV6v0NotifyGroup,
       "tmnxPPPoEV6v0NotificationObjGroup": tmnxPPPoEV6v0NotificationObjGroup,
       "tmnxPPPoEV6v0BsxGroup": tmnxPPPoEV6v0BsxGroup,
       "tmnxPPPoEManagedRoutesGroup": tmnxPPPoEManagedRoutesGroup,
       "tmnxPPPoEV6v1Group": tmnxPPPoEV6v1Group,
       "tmnxPPPoEV7v0Group": tmnxPPPoEV7v0Group,
       "tmnxPPPoESessionBGPGroup": tmnxPPPoESessionBGPGroup,
       "tmnxPPPoEV8v0Group": tmnxPPPoEV8v0Group,
       "tmnxPPPoEV8v0NotifyGroup": tmnxPPPoEV8v0NotifyGroup,
       "tmnxPPPoEV8v0NotifyObjsGroup": tmnxPPPoEV8v0NotifyObjsGroup,
       "tmnxPPPoEV9v0Group": tmnxPPPoEV9v0Group,
       "tmnxPPPV9v0Group": tmnxPPPV9v0Group,
       "tmnxPPPMlpppGroup": tmnxPPPMlpppGroup,
       "tmnxPPPRejectDisabledNcp": tmnxPPPRejectDisabledNcp,
       "tmnxPPPoEV10v0NotifyObjsGroup": tmnxPPPoEV10v0NotifyObjsGroup,
       "tmnxPPPoEV10v0NotifyGroup": tmnxPPPoEV10v0NotifyGroup,
       "tmnxPPPLcpIgnoreMagic": tmnxPPPLcpIgnoreMagic,
       "tmnxPPPoEV11v0Group": tmnxPPPoEV11v0Group,
       "tmnxPPPPlcyAllowSameCidGroup": tmnxPPPPlcyAllowSameCidGroup,
       "tmnxPPPoEV12v0Group": tmnxPPPoEV12v0Group,
       "tmnxPPPoEDefaultUsernameGroup": tmnxPPPoEDefaultUsernameGroup,
       "tmnxPPPoEObsoletedGroup": tmnxPPPoEObsoletedGroup,
       "tmnxPppoe": tmnxPppoe,
       "tmnxPppoeObjects": tmnxPppoeObjects,
       "tmnxPppoePlcyTableLastChanged": tmnxPppoePlcyTableLastChanged,
       "tmnxPppoePlcyTable": tmnxPppoePlcyTable,
       "tmnxPppoePlcyEntry": tmnxPppoePlcyEntry,
       "tmnxPppoePlcyName": tmnxPppoePlcyName,
       "tmnxPppoePlcyRowStatus": tmnxPppoePlcyRowStatus,
       "tmnxPppoePlcyLastMgmtChange": tmnxPppoePlcyLastMgmtChange,
       "tmnxPppoePlcyDescription": tmnxPppoePlcyDescription,
       "tmnxPppoePlcyPppMtu": tmnxPppoePlcyPppMtu,
       "tmnxPppoePlcyLcpKaInterval": tmnxPppoePlcyLcpKaInterval,
       "tmnxPppoePlcyLcpKaHoldUpMplier": tmnxPppoePlcyLcpKaHoldUpMplier,
       "tmnxPppoePlcyDisableAcCookies": tmnxPppoePlcyDisableAcCookies,
       "tmnxPppoePlcyPadoDelay": tmnxPppoePlcyPadoDelay,
       "tmnxPppoePlcyMaxSessionsPerMac": tmnxPppoePlcyMaxSessionsPerMac,
       "tmnxPppoePlcyReplyOnPadt": tmnxPppoePlcyReplyOnPadt,
       "tmnxPppoePlcyPppAuthentication": tmnxPppoePlcyPppAuthentication,
       "tmnxPppoePlcyPppMinChapChallenge": tmnxPppoePlcyPppMinChapChallenge,
       "tmnxPppoePlcyPppMaxChapChallenge": tmnxPppoePlcyPppMaxChapChallenge,
       "tmnxPppoePlcyPppInitialDelay": tmnxPppoePlcyPppInitialDelay,
       "tmnxPppoePlcyPppIpcpSubnetNeg": tmnxPppoePlcyPppIpcpSubnetNeg,
       "tmnxPppoePlcyPadoAcName": tmnxPppoePlcyPadoAcName,
       "tmnxPppoePlcyPppMtuForceGt1492": tmnxPppoePlcyPppMtuForceGt1492,
       "tmnxPppoePlcyUniqueSessIdsPerSap": tmnxPppoePlcyUniqueSessIdsPerSap,
       "tmnxPppoePlcyRejectDisabledNcp": tmnxPppoePlcyRejectDisabledNcp,
       "tmnxPppoePlcyLcpIgnoreMagic": tmnxPppoePlcyLcpIgnoreMagic,
       "tmnxPppoePlcySessionTimeout": tmnxPppoePlcySessionTimeout,
       "tmnxPppoePlcyAllowSameCidForDhcp": tmnxPppoePlcyAllowSameCidForDhcp,
       "tmnxPppoePlcyReestablishSession": tmnxPppoePlcyReestablishSession,
       "tmnxPppoePlcyDefaultUserName": tmnxPppoePlcyDefaultUserName,
       "tmnxPppoePlcyDefaultPapPassword": tmnxPppoePlcyDefaultPapPassword,
       "tmnxPppoePlcyPppOptionTblLstChg": tmnxPppoePlcyPppOptionTblLstChg,
       "tmnxPppoePlcyPppOptionTable": tmnxPppoePlcyPppOptionTable,
       "tmnxPppoePlcyPppOptionEntry": tmnxPppoePlcyPppOptionEntry,
       "tmnxPppoePlcyOptionProtocol": tmnxPppoePlcyOptionProtocol,
       "tmnxPppoePlcyOptionNumber": tmnxPppoePlcyOptionNumber,
       "tmnxPppoePlcyOptionRowStatus": tmnxPppoePlcyOptionRowStatus,
       "tmnxPppoePlcyOptionLstMgmtChange": tmnxPppoePlcyOptionLstMgmtChange,
       "tmnxPppoePlcyOptionType": tmnxPppoePlcyOptionType,
       "tmnxPppoePlcyOptionValue": tmnxPppoePlcyOptionValue,
       "tmnxPppoeIesIfInfoTableLastChg": tmnxPppoeIesIfInfoTableLastChg,
       "tmnxPppoeIesIfInfoTable": tmnxPppoeIesIfInfoTable,
       "tmnxPppoeIesIfInfoEntry": tmnxPppoeIesIfInfoEntry,
       "tmnxPppoeIesIfLastChg": tmnxPppoeIesIfLastChg,
       "tmnxPppoeIesIfDescription": tmnxPppoeIesIfDescription,
       "tmnxPppoeIesIfAdminState": tmnxPppoeIesIfAdminState,
       "tmnxPppoeIesIfPolicy": tmnxPppoeIesIfPolicy,
       "tmnxPppoeIesIfSessionLimit": tmnxPppoeIesIfSessionLimit,
       "tmnxPppoeIesIfSapSessionLimit": tmnxPppoeIesIfSapSessionLimit,
       "tmnxPppoeIesIfPapChapUserDb": tmnxPppoeIesIfPapChapUserDb,
       "tmnxPppoeIesIfUserDb": tmnxPppoeIesIfUserDb,
       "tmnxPppoeIesIfDhcpcCcagOriginSap": tmnxPppoeIesIfDhcpcCcagOriginSap,
       "tmnxPppoeIesIfAntiSpoofing": tmnxPppoeIesIfAntiSpoofing,
       "tmnxPppoeIesIfDhcpcInclOptString": tmnxPppoeIesIfDhcpcInclOptString,
       "tmnxPppoeSapStatsTable": tmnxPppoeSapStatsTable,
       "tmnxPppoeSapStatsEntry": tmnxPppoeSapStatsEntry,
       "tmnxPppoeSapRxPadi": tmnxPppoeSapRxPadi,
       "tmnxPppoeSapRxPadr": tmnxPppoeSapRxPadr,
       "tmnxPppoeSapRxPadt": tmnxPppoeSapRxPadt,
       "tmnxPppoeSapRxSession": tmnxPppoeSapRxSession,
       "tmnxPppoeSapRxInvalidVersion": tmnxPppoeSapRxInvalidVersion,
       "tmnxPppoeSapRxInvalidType": tmnxPppoeSapRxInvalidType,
       "tmnxPppoeSapRxInvalidCode": tmnxPppoeSapRxInvalidCode,
       "tmnxPppoeSapRxInvalidSession": tmnxPppoeSapRxInvalidSession,
       "tmnxPppoeSapRxInvalidLen": tmnxPppoeSapRxInvalidLen,
       "tmnxPppoeSapRxInvalidTags": tmnxPppoeSapRxInvalidTags,
       "tmnxPppoeSapRxInvalidAcCookie": tmnxPppoeSapRxInvalidAcCookie,
       "tmnxPppoeSapRxDropped": tmnxPppoeSapRxDropped,
       "tmnxPppoeSapTxPado": tmnxPppoeSapTxPado,
       "tmnxPppoeSapTxPads": tmnxPppoeSapTxPads,
       "tmnxPppoeSapTxPadt": tmnxPppoeSapTxPadt,
       "tmnxPppoeSapTxSession": tmnxPppoeSapTxSession,
       "tmnxPppoeSapRxInvalidMac": tmnxPppoeSapRxInvalidMac,
       "tmnxPppoeSessionTable": tmnxPppoeSessionTable,
       "tmnxPppoeSessionEntry": tmnxPppoeSessionEntry,
       "tmnxPppoeSessionMac": tmnxPppoeSessionMac,
       "tmnxPppoeSessionId": tmnxPppoeSessionId,
       "tmnxPppoeSessionUpTime": tmnxPppoeSessionUpTime,
       "tmnxPppoeSessionLcpState": tmnxPppoeSessionLcpState,
       "tmnxPppoeSessionIpcpState": tmnxPppoeSessionIpcpState,
       "tmnxPppoeSessionPppMtu": tmnxPppoeSessionPppMtu,
       "tmnxPppoeSessionPppAuthProtocol": tmnxPppoeSessionPppAuthProtocol,
       "tmnxPppoeSessionPppUserName": tmnxPppoeSessionPppUserName,
       "tmnxPppoeSessionSubIdent": tmnxPppoeSessionSubIdent,
       "tmnxPppoeSessionOriginSubIdent": tmnxPppoeSessionOriginSubIdent,
       "tmnxPppoeSessionSubProfString": tmnxPppoeSessionSubProfString,
       "tmnxPppoeSessionSlaProfString": tmnxPppoeSessionSlaProfString,
       "tmnxPppoeSessionAncpString": tmnxPppoeSessionAncpString,
       "tmnxPppoeSessionInterDestId": tmnxPppoeSessionInterDestId,
       "tmnxPppoeSessionAppProfString": tmnxPppoeSessionAppProfString,
       "tmnxPppoeSessionOriginStrings": tmnxPppoeSessionOriginStrings,
       "tmnxPppoeSessionSessionTimeout": tmnxPppoeSessionSessionTimeout,
       "tmnxPppoeSessionIpAddrType": tmnxPppoeSessionIpAddrType,
       "tmnxPppoeSessionIpAddr": tmnxPppoeSessionIpAddr,
       "tmnxPppoeSessionPrimaryDnsType": tmnxPppoeSessionPrimaryDnsType,
       "tmnxPppoeSessionPrimaryDns": tmnxPppoeSessionPrimaryDns,
       "tmnxPppoeSessionSecondryDnsType": tmnxPppoeSessionSecondryDnsType,
       "tmnxPppoeSessionSecondryDns": tmnxPppoeSessionSecondryDns,
       "tmnxPppoeSessionPrimaryNbnsType": tmnxPppoeSessionPrimaryNbnsType,
       "tmnxPppoeSessionPrimaryNbns": tmnxPppoeSessionPrimaryNbns,
       "tmnxPppoeSessionSecondryNbnsType": tmnxPppoeSessionSecondryNbnsType,
       "tmnxPppoeSessionSecondryNbns": tmnxPppoeSessionSecondryNbns,
       "tmnxPppoeSessionOriginIpcpInfo": tmnxPppoeSessionOriginIpcpInfo,
       "tmnxPppoeSessionCircuitId": tmnxPppoeSessionCircuitId,
       "tmnxPppoeSessionRemoteId": tmnxPppoeSessionRemoteId,
       "tmnxPppoeSessionAddressPool": tmnxPppoeSessionAddressPool,
       "tmnxPppoeSessionType": tmnxPppoeSessionType,
       "tmnxPppoeSessionRetailerSvcId": tmnxPppoeSessionRetailerSvcId,
       "tmnxPppoeSessionRetailerIf": tmnxPppoeSessionRetailerIf,
       "tmnxPppoeSessionL2tpVrtrId": tmnxPppoeSessionL2tpVrtrId,
       "tmnxPppoeSessionL2tpConnectionId": tmnxPppoeSessionL2tpConnectionId,
       "tmnxPppoeSessionServiceName": tmnxPppoeSessionServiceName,
       "tmnxPppoeSessionCategoryMapName": tmnxPppoeSessionCategoryMapName,
       "tmnxPppoeSessionRadiusClassAttr": tmnxPppoeSessionRadiusClassAttr,
       "tmnxPppoeSessionRadiusUserName": tmnxPppoeSessionRadiusUserName,
       "tmnxPppoeSessionIpv6cpState": tmnxPppoeSessionIpv6cpState,
       "tmnxPppoeSessionInterfaceId": tmnxPppoeSessionInterfaceId,
       "tmnxPppoeSessionOriginIpv6cpInfo": tmnxPppoeSessionOriginIpv6cpInfo,
       "tmnxPppoeSessionIpv6DnsType": tmnxPppoeSessionIpv6DnsType,
       "tmnxPppoeSessionIpv6Dns1": tmnxPppoeSessionIpv6Dns1,
       "tmnxPppoeSessionIpv6Dns2": tmnxPppoeSessionIpv6Dns2,
       "tmnxPppoeSessionIpv6DelPfxType": tmnxPppoeSessionIpv6DelPfxType,
       "tmnxPppoeSessionIpv6DelPfxLen": tmnxPppoeSessionIpv6DelPfxLen,
       "tmnxPppoeSessionIpv6DelPfx": tmnxPppoeSessionIpv6DelPfx,
       "tmnxPppoeSessionIpv6PrefixType": tmnxPppoeSessionIpv6PrefixType,
       "tmnxPppoeSessionIpv6PrefixLen": tmnxPppoeSessionIpv6PrefixLen,
       "tmnxPppoeSessionIpv6Prefix": tmnxPppoeSessionIpv6Prefix,
       "tmnxPppoeSessionSubPppIndex": tmnxPppoeSessionSubPppIndex,
       "tmnxPppoeSessionModifyTable": tmnxPppoeSessionModifyTable,
       "tmnxPppoeSessionModifyEntry": tmnxPppoeSessionModifyEntry,
       "tmnxPppoeSessionModSubIdent": tmnxPppoeSessionModSubIdent,
       "tmnxPppoeSessionModSubProfStr": tmnxPppoeSessionModSubProfStr,
       "tmnxPppoeSessionModSlaProfStr": tmnxPppoeSessionModSlaProfStr,
       "tmnxPppoeSessionModAncpStr": tmnxPppoeSessionModAncpStr,
       "tmnxPppoeSessionModInterDestId": tmnxPppoeSessionModInterDestId,
       "tmnxPppoeSessionModAppProfStr": tmnxPppoeSessionModAppProfStr,
       "tmnxPppoeSessionEvaluateState": tmnxPppoeSessionEvaluateState,
       "tmnxPppoeSessionStatsTable": tmnxPppoeSessionStatsTable,
       "tmnxPppoeSessionStatsEntry": tmnxPppoeSessionStatsEntry,
       "tmnxPppoeSessionRxUnknownProto": tmnxPppoeSessionRxUnknownProto,
       "tmnxPppoeSessionRxLcpConfReq": tmnxPppoeSessionRxLcpConfReq,
       "tmnxPppoeSessionRxLcpConfAck": tmnxPppoeSessionRxLcpConfAck,
       "tmnxPppoeSessionRxLcpConfNak": tmnxPppoeSessionRxLcpConfNak,
       "tmnxPppoeSessionRxLcpConfRej": tmnxPppoeSessionRxLcpConfRej,
       "tmnxPppoeSessionRxLcpTermReq": tmnxPppoeSessionRxLcpTermReq,
       "tmnxPppoeSessionRxLcpTermAck": tmnxPppoeSessionRxLcpTermAck,
       "tmnxPppoeSessionRxLcpCodeRej": tmnxPppoeSessionRxLcpCodeRej,
       "tmnxPppoeSessionRxLcpEchoReq": tmnxPppoeSessionRxLcpEchoReq,
       "tmnxPppoeSessionRxLcpEchoRep": tmnxPppoeSessionRxLcpEchoRep,
       "tmnxPppoeSessionRxLcpProtRej": tmnxPppoeSessionRxLcpProtRej,
       "tmnxPppoeSessionRxLcpDiscReq": tmnxPppoeSessionRxLcpDiscReq,
       "tmnxPppoeSessionTxLcpConfReq": tmnxPppoeSessionTxLcpConfReq,
       "tmnxPppoeSessionTxLcpConfAck": tmnxPppoeSessionTxLcpConfAck,
       "tmnxPppoeSessionTxLcpConfNak": tmnxPppoeSessionTxLcpConfNak,
       "tmnxPppoeSessionTxLcpConfRej": tmnxPppoeSessionTxLcpConfRej,
       "tmnxPppoeSessionTxLcpTermReq": tmnxPppoeSessionTxLcpTermReq,
       "tmnxPppoeSessionTxLcpTermAck": tmnxPppoeSessionTxLcpTermAck,
       "tmnxPppoeSessionTxLcpCodeRej": tmnxPppoeSessionTxLcpCodeRej,
       "tmnxPppoeSessionTxLcpEchoReq": tmnxPppoeSessionTxLcpEchoReq,
       "tmnxPppoeSessionTxLcpEchoRep": tmnxPppoeSessionTxLcpEchoRep,
       "tmnxPppoeSessionTxLcpProtRej": tmnxPppoeSessionTxLcpProtRej,
       "tmnxPppoeSessionTxLcpDiscReq": tmnxPppoeSessionTxLcpDiscReq,
       "tmnxPppoeSessionRxPapAuthReq": tmnxPppoeSessionRxPapAuthReq,
       "tmnxPppoeSessionTxPapAuthAck": tmnxPppoeSessionTxPapAuthAck,
       "tmnxPppoeSessionTxPapAuthNak": tmnxPppoeSessionTxPapAuthNak,
       "tmnxPppoeSessionRxChapResponse": tmnxPppoeSessionRxChapResponse,
       "tmnxPppoeSessionTxChapChallenge": tmnxPppoeSessionTxChapChallenge,
       "tmnxPppoeSessionTxChapSuccess": tmnxPppoeSessionTxChapSuccess,
       "tmnxPppoeSessionTxChapFailure": tmnxPppoeSessionTxChapFailure,
       "tmnxPppoeSessionRxIpcpConfReq": tmnxPppoeSessionRxIpcpConfReq,
       "tmnxPppoeSessionRxIpcpConfAck": tmnxPppoeSessionRxIpcpConfAck,
       "tmnxPppoeSessionRxIpcpConfNak": tmnxPppoeSessionRxIpcpConfNak,
       "tmnxPppoeSessionRxIpcpConfRej": tmnxPppoeSessionRxIpcpConfRej,
       "tmnxPppoeSessionRxIpcpTermReq": tmnxPppoeSessionRxIpcpTermReq,
       "tmnxPppoeSessionRxIpcpTermAck": tmnxPppoeSessionRxIpcpTermAck,
       "tmnxPppoeSessionRxIpcpCodeRej": tmnxPppoeSessionRxIpcpCodeRej,
       "tmnxPppoeSessionTxIpcpConfReq": tmnxPppoeSessionTxIpcpConfReq,
       "tmnxPppoeSessionTxIpcpConfAck": tmnxPppoeSessionTxIpcpConfAck,
       "tmnxPppoeSessionTxIpcpConfNak": tmnxPppoeSessionTxIpcpConfNak,
       "tmnxPppoeSessionTxIpcpConfRej": tmnxPppoeSessionTxIpcpConfRej,
       "tmnxPppoeSessionTxIpcpTermReq": tmnxPppoeSessionTxIpcpTermReq,
       "tmnxPppoeSessionTxIpcpTermAck": tmnxPppoeSessionTxIpcpTermAck,
       "tmnxPppoeSessionTxIpcpCodeRej": tmnxPppoeSessionTxIpcpCodeRej,
       "tmnxPppoeSessionRxIpv6cpConfReq": tmnxPppoeSessionRxIpv6cpConfReq,
       "tmnxPppoeSessionRxIpv6cpConfAck": tmnxPppoeSessionRxIpv6cpConfAck,
       "tmnxPppoeSessionRxIpv6cpConfNak": tmnxPppoeSessionRxIpv6cpConfNak,
       "tmnxPppoeSessionRxIpv6cpConfRej": tmnxPppoeSessionRxIpv6cpConfRej,
       "tmnxPppoeSessionRxIpv6cpTermReq": tmnxPppoeSessionRxIpv6cpTermReq,
       "tmnxPppoeSessionRxIpv6cpTermAck": tmnxPppoeSessionRxIpv6cpTermAck,
       "tmnxPppoeSessionRxIpv6cpCodeRej": tmnxPppoeSessionRxIpv6cpCodeRej,
       "tmnxPppoeSessionTxIpv6cpConfReq": tmnxPppoeSessionTxIpv6cpConfReq,
       "tmnxPppoeSessionTxIpv6cpConfAck": tmnxPppoeSessionTxIpv6cpConfAck,
       "tmnxPppoeSessionTxIpv6cpConfNak": tmnxPppoeSessionTxIpv6cpConfNak,
       "tmnxPppoeSessionTxIpv6cpConfRej": tmnxPppoeSessionTxIpv6cpConfRej,
       "tmnxPppoeSessionTxIpv6cpTermReq": tmnxPppoeSessionTxIpv6cpTermReq,
       "tmnxPppoeSessionTxIpv6cpTermAck": tmnxPppoeSessionTxIpv6cpTermAck,
       "tmnxPppoeSessionTxIpv6cpCodeRej": tmnxPppoeSessionTxIpv6cpCodeRej,
       "tmnxPppoeManagedRouteTable": tmnxPppoeManagedRouteTable,
       "tmnxPppoeManagedRouteEntry": tmnxPppoeManagedRouteEntry,
       "tmnxPppoeManagedRouteAddrType": tmnxPppoeManagedRouteAddrType,
       "tmnxPppoeManagedRouteAddr": tmnxPppoeManagedRouteAddr,
       "tmnxPppoeManagedRoutePrefixLen": tmnxPppoeManagedRoutePrefixLen,
       "tmnxPppoeManagedRouteStatus": tmnxPppoeManagedRouteStatus,
       "tmnxPppoeSessionBgpTable": tmnxPppoeSessionBgpTable,
       "tmnxPppoeSessionBgpEntry": tmnxPppoeSessionBgpEntry,
       "tmnxPppoeSessionBgpPrngPlcyName": tmnxPppoeSessionBgpPrngPlcyName,
       "tmnxPppoeSessionBgpAuthKeyChain": tmnxPppoeSessionBgpAuthKeyChain,
       "tmnxPppoeSessionBgpMD5AuthKey": tmnxPppoeSessionBgpMD5AuthKey,
       "tmnxPppoeSessionBgpImportPolicy": tmnxPppoeSessionBgpImportPolicy,
       "tmnxPppoeSessionBgpExportPolicy": tmnxPppoeSessionBgpExportPolicy,
       "tmnxPppoeSessionBgpPeerAS": tmnxPppoeSessionBgpPeerAS,
       "tmnxPppoeSessionBgpPeeringStatus": tmnxPppoeSessionBgpPeeringStatus,
       "tmnxPppoeSessionOverridesTable": tmnxPppoeSessionOverridesTable,
       "tmnxPppoeSessionOverridesEntry": tmnxPppoeSessionOverridesEntry,
       "tmnxPppoeSessionOvrDirection": tmnxPppoeSessionOvrDirection,
       "tmnxPppoeSessionOvrType": tmnxPppoeSessionOvrType,
       "tmnxPppoeSessionOvrTypeId": tmnxPppoeSessionOvrTypeId,
       "tmnxPppoeSessionOvrTypeName": tmnxPppoeSessionOvrTypeName,
       "tmnxPppoeSessionOvrPIR": tmnxPppoeSessionOvrPIR,
       "tmnxPppoeSessionOvrCIR": tmnxPppoeSessionOvrCIR,
       "tmnxPppoeSessionOvrCBS": tmnxPppoeSessionOvrCBS,
       "tmnxPppoeSessionOvrMBS": tmnxPppoeSessionOvrMBS,
       "tmnxPppoeSessionAleTable": tmnxPppoeSessionAleTable,
       "tmnxPppoeSessionAleEntry": tmnxPppoeSessionAleEntry,
       "tmnxPppoeSessionAleDatalink": tmnxPppoeSessionAleDatalink,
       "tmnxPppoeSessionAleEncaps1": tmnxPppoeSessionAleEncaps1,
       "tmnxPppoeSessionAleEncaps2": tmnxPppoeSessionAleEncaps2,
       "tmnxPppoeNotificationObjs": tmnxPppoeNotificationObjs,
       "tmnxPppoeSessionFailureReason": tmnxPppoeSessionFailureReason,
       "tmnxPppoeNcpFailureProtocol": tmnxPppoeNcpFailureProtocol,
       "tmnxPppoeNcpFailureReason": tmnxPppoeNcpFailureReason,
       "tmnxPppoeNotifyDescription": tmnxPppoeNotifyDescription,
       "tmnxPppObjects": tmnxPppObjects,
       "tmnxPppIesIfTableLastChg": tmnxPppIesIfTableLastChg,
       "tmnxPppIesIfTable": tmnxPppIesIfTable,
       "tmnxPppIesIfEntry": tmnxPppIesIfEntry,
       "tmnxPppIesIfLastChg": tmnxPppIesIfLastChg,
       "tmnxPppIesIfDescription": tmnxPppIesIfDescription,
       "tmnxPppIesIfAdminState": tmnxPppIesIfAdminState,
       "tmnxPppIesIfPolicy": tmnxPppIesIfPolicy,
       "tmnxPppIesIfSessionLimit": tmnxPppIesIfSessionLimit,
       "tmnxPppIesIfUserDb": tmnxPppIesIfUserDb,
       "tmnxMlpppObjects": tmnxMlpppObjects,
       "tmnxMlpppBundleTable": tmnxMlpppBundleTable,
       "tmnxMlpppBundleEntry": tmnxMlpppBundleEntry,
       "tmnxMlpppBundleIndex": tmnxMlpppBundleIndex,
       "tmnxMlpppBundleLocEpClass": tmnxMlpppBundleLocEpClass,
       "tmnxMlpppBundleLocEpAddress": tmnxMlpppBundleLocEpAddress,
       "tmnxMlpppBundleRemEpClass": tmnxMlpppBundleRemEpClass,
       "tmnxMlpppBundleRemEpAddress": tmnxMlpppBundleRemEpAddress,
       "tmnxMlpppBundleSubPppIndex": tmnxMlpppBundleSubPppIndex,
       "tmnxMlpppBundleMaxLinks": tmnxMlpppBundleMaxLinks,
       "tmnxMlpppBundleActualLinks": tmnxMlpppBundleActualLinks,
       "tmnxMlpppBundleRemMrru": tmnxMlpppBundleRemMrru,
       "tmnxMlpppBundleLocMrru": tmnxMlpppBundleLocMrru,
       "tmnxMlpppBundleIndicators": tmnxMlpppBundleIndicators,
       "tmnxMlpppBundleFragmentSize": tmnxMlpppBundleFragmentSize,
       "tmnxMlpppBundleMaxDelayCfg": tmnxMlpppBundleMaxDelayCfg,
       "tmnxMlpppBundleMaxDelay": tmnxMlpppBundleMaxDelay,
       "tmnxMlpppBundleReassemblyTo": tmnxMlpppBundleReassemblyTo,
       "tmnxMlpppBundleEgressRate": tmnxMlpppBundleEgressRate,
       "tmnxMlpppLinkTable": tmnxMlpppLinkTable,
       "tmnxMlpppLinkEntry": tmnxMlpppLinkEntry,
       "tmnxMlpppLinkRemMrru": tmnxMlpppLinkRemMrru,
       "tmnxPppPlcyMlpppTableLastCh": tmnxPppPlcyMlpppTableLastCh,
       "tmnxPppPlcyMlpppTable": tmnxPppPlcyMlpppTable,
       "tmnxPppPlcyMlpppEntry": tmnxPppPlcyMlpppEntry,
       "tmnxPppPlcyMlpppLastCh": tmnxPppPlcyMlpppLastCh,
       "tmnxPppPlcyMlpppAcceptMrru": tmnxPppPlcyMlpppAcceptMrru,
       "tmnxPppPlcyMlpppEpClass": tmnxPppPlcyMlpppEpClass,
       "tmnxPppPlcyMlpppEpIpv4Address": tmnxPppPlcyMlpppEpIpv4Address,
       "tmnxPppPlcyMlpppEpMacAddress": tmnxPppPlcyMlpppEpMacAddress,
       "tmnxPppPlcyMlpppShortSeqNumberRx": tmnxPppPlcyMlpppShortSeqNumberRx,
       "tmnxPppoeNotifyPrefix": tmnxPppoeNotifyPrefix,
       "tmnxPppoeNotifications": tmnxPppoeNotifications,
       "tmnxPppoeSessionFailure": tmnxPppoeSessionFailure,
       "tmnxPppoeNcpFailure": tmnxPppoeNcpFailure,
       "tmnxMlpppBundleIndicatorsChange": tmnxMlpppBundleIndicatorsChange}
)
