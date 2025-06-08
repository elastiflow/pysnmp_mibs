# SNMP MIB module (TIMETRA-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-DHCP-SERVER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:31 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
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

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxCreateOrigin,
 TmnxDhcpOptionType,
 TmnxDhcpServerDUIDTypeCode,
 TmnxPppoeUserNameOrEmpty,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxCreateOrigin",
    "TmnxDhcpOptionType",
    "TmnxDhcpServerDUIDTypeCode",
    "TmnxPppoeUserNameOrEmpty",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraDhcpServerMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 47)
)
if mibBuilder.loadTexts:
    timetraDhcpServerMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-02-28 12:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxDhcpSvrOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("waitPersistence", 5))
    )



class TmnxDhcpSvrClientType(TextualConvention, Integer32):
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
        *(("dhcp", 0),
          ("ppp", 1),
          ("ipoe", 2))
    )



class TmnxDhcpSvrFailCtrlType(TextualConvention, Integer32):
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
        *(("local", 1),
          ("remote", 2),
          ("access-driven", 3))
    )



class TmnxDhcpsFoState(TextualConvention, Integer32):
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("init", 2),
          ("startUp", 3),
          ("noCommunication", 4),
          ("partnerDown", 5),
          ("normal", 6),
          ("shutdown", 7),
          ("transition", 8),
          ("preNormal", 9))
    )



class TmnxDhcpsFoLeaseFailureReason(TextualConvention, Integer32):
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("foShutdown", 1),
          ("expired", 2),
          ("maxReached", 3),
          ("subnetNotFound", 4),
          ("rangeNotFound", 5),
          ("hostConflict", 6),
          ("addressConflict", 7),
          ("peerConflict", 8),
          ("persistenceCongested", 9))
    )



class TmnxDhcpsFoActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("forcePartnerDown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDhcpServerConformance_ObjectIdentity = ObjectIdentity
tmnxDhcpServerConformance = _TmnxDhcpServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47)
)
_TmnxDhcpServerCompliances_ObjectIdentity = ObjectIdentity
tmnxDhcpServerCompliances = _TmnxDhcpServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1)
)
_TmnxDhcpServerGroups_ObjectIdentity = ObjectIdentity
tmnxDhcpServerGroups = _TmnxDhcpServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2)
)
_TmnxDhcpServerNotifGroups_ObjectIdentity = ObjectIdentity
tmnxDhcpServerNotifGroups = _TmnxDhcpServerNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 3)
)
_TmnxDhcpServer_ObjectIdentity = ObjectIdentity
tmnxDhcpServer = _TmnxDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47)
)
_TmnxDhcpServerObjs_ObjectIdentity = ObjectIdentity
tmnxDhcpServerObjs = _TmnxDhcpServerObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1)
)
_TmnxDhcpServerConfigTableLastCh_Type = TimeStamp
_TmnxDhcpServerConfigTableLastCh_Object = MibScalar
tmnxDhcpServerConfigTableLastCh = _TmnxDhcpServerConfigTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 1),
    _TmnxDhcpServerConfigTableLastCh_Type()
)
tmnxDhcpServerConfigTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerConfigTableLastCh.setStatus("current")
_TmnxDhcpServerConfigTable_Object = MibTable
tmnxDhcpServerConfigTable = _TmnxDhcpServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxDhcpServerConfigTable.setStatus("current")
_TmnxDhcpServerConfigEntry_Object = MibTableRow
tmnxDhcpServerConfigEntry = _TmnxDhcpServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1)
)
tmnxDhcpServerConfigEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
)
if mibBuilder.loadTexts:
    tmnxDhcpServerConfigEntry.setStatus("current")
_TmnxDhcpServerCfgServerName_Type = TNamedItem
_TmnxDhcpServerCfgServerName_Object = MibTableColumn
tmnxDhcpServerCfgServerName = _TmnxDhcpServerCfgServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 1),
    _TmnxDhcpServerCfgServerName_Type()
)
tmnxDhcpServerCfgServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgServerName.setStatus("current")
_TmnxDhcpServerCfgRowStatus_Type = RowStatus
_TmnxDhcpServerCfgRowStatus_Object = MibTableColumn
tmnxDhcpServerCfgRowStatus = _TmnxDhcpServerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 2),
    _TmnxDhcpServerCfgRowStatus_Type()
)
tmnxDhcpServerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgRowStatus.setStatus("current")
_TmnxDhcpServerCfgLastChangeTime_Type = TimeStamp
_TmnxDhcpServerCfgLastChangeTime_Object = MibTableColumn
tmnxDhcpServerCfgLastChangeTime = _TmnxDhcpServerCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 3),
    _TmnxDhcpServerCfgLastChangeTime_Type()
)
tmnxDhcpServerCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgLastChangeTime.setStatus("current")


class _TmnxDhcpServerCfgAdminState_Type(TmnxAdminState):
    """Custom type tmnxDhcpServerCfgAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxDhcpServerCfgAdminState_Type.__name__ = "TmnxAdminState"
_TmnxDhcpServerCfgAdminState_Object = MibTableColumn
tmnxDhcpServerCfgAdminState = _TmnxDhcpServerCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 4),
    _TmnxDhcpServerCfgAdminState_Type()
)
tmnxDhcpServerCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgAdminState.setStatus("current")


class _TmnxDhcpServerCfgDescription_Type(TItemDescription):
    """Custom type tmnxDhcpServerCfgDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDhcpServerCfgDescription_Type.__name__ = "TItemDescription"
_TmnxDhcpServerCfgDescription_Object = MibTableColumn
tmnxDhcpServerCfgDescription = _TmnxDhcpServerCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 5),
    _TmnxDhcpServerCfgDescription_Type()
)
tmnxDhcpServerCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgDescription.setStatus("current")


class _TmnxDhcpServerCfgUserDatabase_Type(TNamedItemOrEmpty):
    """Custom type tmnxDhcpServerCfgUserDatabase based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDhcpServerCfgUserDatabase_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDhcpServerCfgUserDatabase_Object = MibTableColumn
tmnxDhcpServerCfgUserDatabase = _TmnxDhcpServerCfgUserDatabase_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 6),
    _TmnxDhcpServerCfgUserDatabase_Type()
)
tmnxDhcpServerCfgUserDatabase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgUserDatabase.setStatus("current")


class _TmnxDhcpServerCfgUseGiAddress_Type(TruthValue):
    """Custom type tmnxDhcpServerCfgUseGiAddress based on TruthValue"""
    defaultValue = 2


_TmnxDhcpServerCfgUseGiAddress_Type.__name__ = "TruthValue"
_TmnxDhcpServerCfgUseGiAddress_Object = MibTableColumn
tmnxDhcpServerCfgUseGiAddress = _TmnxDhcpServerCfgUseGiAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 7),
    _TmnxDhcpServerCfgUseGiAddress_Type()
)
tmnxDhcpServerCfgUseGiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgUseGiAddress.setStatus("current")


class _TmnxDhcpServerCfgSendForceRenews_Type(TruthValue):
    """Custom type tmnxDhcpServerCfgSendForceRenews based on TruthValue"""
    defaultValue = 2


_TmnxDhcpServerCfgSendForceRenews_Type.__name__ = "TruthValue"
_TmnxDhcpServerCfgSendForceRenews_Object = MibTableColumn
tmnxDhcpServerCfgSendForceRenews = _TmnxDhcpServerCfgSendForceRenews_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 8),
    _TmnxDhcpServerCfgSendForceRenews_Type()
)
tmnxDhcpServerCfgSendForceRenews.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgSendForceRenews.setStatus("current")


class _TmnxDhcpServerCfgUseClientPool_Type(TruthValue):
    """Custom type tmnxDhcpServerCfgUseClientPool based on TruthValue"""
    defaultValue = 2


_TmnxDhcpServerCfgUseClientPool_Type.__name__ = "TruthValue"
_TmnxDhcpServerCfgUseClientPool_Object = MibTableColumn
tmnxDhcpServerCfgUseClientPool = _TmnxDhcpServerCfgUseClientPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 9),
    _TmnxDhcpServerCfgUseClientPool_Type()
)
tmnxDhcpServerCfgUseClientPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgUseClientPool.setStatus("current")
_TmnxDhcpServerCfgOperState_Type = TmnxDhcpSvrOperState
_TmnxDhcpServerCfgOperState_Object = MibTableColumn
tmnxDhcpServerCfgOperState = _TmnxDhcpServerCfgOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 10),
    _TmnxDhcpServerCfgOperState_Type()
)
tmnxDhcpServerCfgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgOperState.setStatus("current")


class _TmnxDhcpServerCfgAddrType_Type(InetAddressType):
    """Custom type tmnxDhcpServerCfgAddrType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_TmnxDhcpServerCfgAddrType_Type.__name__ = "InetAddressType"
_TmnxDhcpServerCfgAddrType_Object = MibTableColumn
tmnxDhcpServerCfgAddrType = _TmnxDhcpServerCfgAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 20),
    _TmnxDhcpServerCfgAddrType_Type()
)
tmnxDhcpServerCfgAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgAddrType.setStatus("current")


class _TmnxDhcpServerCfgLeaseHoldTime_Type(Unsigned32):
    """Custom type tmnxDhcpServerCfgLeaseHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 315446399),
    )


_TmnxDhcpServerCfgLeaseHoldTime_Type.__name__ = "Unsigned32"
_TmnxDhcpServerCfgLeaseHoldTime_Object = MibTableColumn
tmnxDhcpServerCfgLeaseHoldTime = _TmnxDhcpServerCfgLeaseHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 21),
    _TmnxDhcpServerCfgLeaseHoldTime_Type()
)
tmnxDhcpServerCfgLeaseHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgLeaseHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgLeaseHoldTime.setUnits("seconds")


class _TmnxDhcpServerCfgUseGiScope_Type(Integer32):
    """Custom type tmnxDhcpServerCfgUseGiScope based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("subnet", 0),
          ("pool", 1))
    )


_TmnxDhcpServerCfgUseGiScope_Type.__name__ = "Integer32"
_TmnxDhcpServerCfgUseGiScope_Object = MibTableColumn
tmnxDhcpServerCfgUseGiScope = _TmnxDhcpServerCfgUseGiScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 22),
    _TmnxDhcpServerCfgUseGiScope_Type()
)
tmnxDhcpServerCfgUseGiScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgUseGiScope.setStatus("current")


class _TmnxDhcpServerCfgIgnRapidCommit_Type(TruthValue):
    """Custom type tmnxDhcpServerCfgIgnRapidCommit based on TruthValue"""
    defaultValue = 2


_TmnxDhcpServerCfgIgnRapidCommit_Type.__name__ = "TruthValue"
_TmnxDhcpServerCfgIgnRapidCommit_Object = MibTableColumn
tmnxDhcpServerCfgIgnRapidCommit = _TmnxDhcpServerCfgIgnRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 23),
    _TmnxDhcpServerCfgIgnRapidCommit_Type()
)
tmnxDhcpServerCfgIgnRapidCommit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgIgnRapidCommit.setStatus("current")


class _TmnxDhcpServerCfgUserIdent_Type(Integer32):
    """Custom type tmnxDhcpServerCfgUserIdent based on Integer32"""
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
        *(("macCircuitId", 1),
          ("duid", 2),
          ("interfaceId", 3),
          ("interfaceIdLinkLocal", 4))
    )


_TmnxDhcpServerCfgUserIdent_Type.__name__ = "Integer32"
_TmnxDhcpServerCfgUserIdent_Object = MibTableColumn
tmnxDhcpServerCfgUserIdent = _TmnxDhcpServerCfgUserIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 24),
    _TmnxDhcpServerCfgUserIdent_Type()
)
tmnxDhcpServerCfgUserIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgUserIdent.setStatus("current")


class _TmnxDhcpServerCfgItfIdMapping_Type(TruthValue):
    """Custom type tmnxDhcpServerCfgItfIdMapping based on TruthValue"""
    defaultValue = 2


_TmnxDhcpServerCfgItfIdMapping_Type.__name__ = "TruthValue"
_TmnxDhcpServerCfgItfIdMapping_Object = MibTableColumn
tmnxDhcpServerCfgItfIdMapping = _TmnxDhcpServerCfgItfIdMapping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 25),
    _TmnxDhcpServerCfgItfIdMapping_Type()
)
tmnxDhcpServerCfgItfIdMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgItfIdMapping.setStatus("current")


class _TmnxDhcpServerCfgUseCPDelimiter_Type(DisplayString):
    """Custom type tmnxDhcpServerCfgUseCPDelimiter based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_TmnxDhcpServerCfgUseCPDelimiter_Type.__name__ = "DisplayString"
_TmnxDhcpServerCfgUseCPDelimiter_Object = MibTableColumn
tmnxDhcpServerCfgUseCPDelimiter = _TmnxDhcpServerCfgUseCPDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 26),
    _TmnxDhcpServerCfgUseCPDelimiter_Type()
)
tmnxDhcpServerCfgUseCPDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgUseCPDelimiter.setStatus("current")
_TmnxDhcpServerCfgCreationOrigin_Type = TmnxCreateOrigin
_TmnxDhcpServerCfgCreationOrigin_Object = MibTableColumn
tmnxDhcpServerCfgCreationOrigin = _TmnxDhcpServerCfgCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 2, 1, 27),
    _TmnxDhcpServerCfgCreationOrigin_Type()
)
tmnxDhcpServerCfgCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerCfgCreationOrigin.setStatus("current")
_TmnxDhcpServerPoolTableLastCh_Type = TimeStamp
_TmnxDhcpServerPoolTableLastCh_Object = MibScalar
tmnxDhcpServerPoolTableLastCh = _TmnxDhcpServerPoolTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 3),
    _TmnxDhcpServerPoolTableLastCh_Type()
)
tmnxDhcpServerPoolTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolTableLastCh.setStatus("current")
_TmnxDhcpServerPoolTable_Object = MibTable
tmnxDhcpServerPoolTable = _TmnxDhcpServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolTable.setStatus("current")
_TmnxDhcpServerPoolEntry_Object = MibTableRow
tmnxDhcpServerPoolEntry = _TmnxDhcpServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1)
)
tmnxDhcpServerPoolEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
)
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolEntry.setStatus("current")
_TmnxDhcpServerPoolName_Type = TNamedItem
_TmnxDhcpServerPoolName_Object = MibTableColumn
tmnxDhcpServerPoolName = _TmnxDhcpServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 1),
    _TmnxDhcpServerPoolName_Type()
)
tmnxDhcpServerPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolName.setStatus("current")
_TmnxDhcpServerPoolRowStatus_Type = RowStatus
_TmnxDhcpServerPoolRowStatus_Object = MibTableColumn
tmnxDhcpServerPoolRowStatus = _TmnxDhcpServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 2),
    _TmnxDhcpServerPoolRowStatus_Type()
)
tmnxDhcpServerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolRowStatus.setStatus("current")
_TmnxDhcpServerPoolLastChangeTime_Type = TimeStamp
_TmnxDhcpServerPoolLastChangeTime_Object = MibTableColumn
tmnxDhcpServerPoolLastChangeTime = _TmnxDhcpServerPoolLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 3),
    _TmnxDhcpServerPoolLastChangeTime_Type()
)
tmnxDhcpServerPoolLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolLastChangeTime.setStatus("current")


class _TmnxDhcpServerPoolDescription_Type(TItemDescription):
    """Custom type tmnxDhcpServerPoolDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDhcpServerPoolDescription_Type.__name__ = "TItemDescription"
_TmnxDhcpServerPoolDescription_Object = MibTableColumn
tmnxDhcpServerPoolDescription = _TmnxDhcpServerPoolDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 4),
    _TmnxDhcpServerPoolDescription_Type()
)
tmnxDhcpServerPoolDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolDescription.setStatus("current")


class _TmnxDhcpServerPoolMinLeaseTime_Type(Unsigned32):
    """Custom type tmnxDhcpServerPoolMinLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 315446399),
    )


_TmnxDhcpServerPoolMinLeaseTime_Type.__name__ = "Unsigned32"
_TmnxDhcpServerPoolMinLeaseTime_Object = MibTableColumn
tmnxDhcpServerPoolMinLeaseTime = _TmnxDhcpServerPoolMinLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 5),
    _TmnxDhcpServerPoolMinLeaseTime_Type()
)
tmnxDhcpServerPoolMinLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolMinLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolMinLeaseTime.setUnits("seconds")


class _TmnxDhcpServerPoolMaxLeaseTime_Type(Unsigned32):
    """Custom type tmnxDhcpServerPoolMaxLeaseTime based on Unsigned32"""
    defaultValue = 864000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 315446399),
    )


_TmnxDhcpServerPoolMaxLeaseTime_Type.__name__ = "Unsigned32"
_TmnxDhcpServerPoolMaxLeaseTime_Object = MibTableColumn
tmnxDhcpServerPoolMaxLeaseTime = _TmnxDhcpServerPoolMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 6),
    _TmnxDhcpServerPoolMaxLeaseTime_Type()
)
tmnxDhcpServerPoolMaxLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolMaxLeaseTime.setUnits("seconds")


class _TmnxDhcpServerPoolOfferTime_Type(Unsigned32):
    """Custom type tmnxDhcpServerPoolOfferTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_TmnxDhcpServerPoolOfferTime_Type.__name__ = "Unsigned32"
_TmnxDhcpServerPoolOfferTime_Object = MibTableColumn
tmnxDhcpServerPoolOfferTime = _TmnxDhcpServerPoolOfferTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 7),
    _TmnxDhcpServerPoolOfferTime_Type()
)
tmnxDhcpServerPoolOfferTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolOfferTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolOfferTime.setUnits("seconds")


class _TmnxDhcpServerPoolMinFree_Type(Unsigned32):
    """Custom type tmnxDhcpServerPoolMinFree based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDhcpServerPoolMinFree_Type.__name__ = "Unsigned32"
_TmnxDhcpServerPoolMinFree_Object = MibTableColumn
tmnxDhcpServerPoolMinFree = _TmnxDhcpServerPoolMinFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 8),
    _TmnxDhcpServerPoolMinFree_Type()
)
tmnxDhcpServerPoolMinFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolMinFree.setStatus("current")


class _TmnxDhcpServerPoolMinFreeType_Type(Integer32):
    """Custom type tmnxDhcpServerPoolMinFreeType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 0),
          ("percent", 1))
    )


_TmnxDhcpServerPoolMinFreeType_Type.__name__ = "Integer32"
_TmnxDhcpServerPoolMinFreeType_Object = MibTableColumn
tmnxDhcpServerPoolMinFreeType = _TmnxDhcpServerPoolMinFreeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 9),
    _TmnxDhcpServerPoolMinFreeType_Type()
)
tmnxDhcpServerPoolMinFreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolMinFreeType.setStatus("current")


class _TmnxDhcpServerPoolDepletedEvent_Type(TruthValue):
    """Custom type tmnxDhcpServerPoolDepletedEvent based on TruthValue"""
    defaultValue = 2


_TmnxDhcpServerPoolDepletedEvent_Type.__name__ = "TruthValue"
_TmnxDhcpServerPoolDepletedEvent_Object = MibTableColumn
tmnxDhcpServerPoolDepletedEvent = _TmnxDhcpServerPoolDepletedEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 10),
    _TmnxDhcpServerPoolDepletedEvent_Type()
)
tmnxDhcpServerPoolDepletedEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolDepletedEvent.setStatus("current")


class _TmnxDhcpServerPoolDlgatedPfxLen_Type(Unsigned32):
    """Custom type tmnxDhcpServerPoolDlgatedPfxLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 64),
    )


_TmnxDhcpServerPoolDlgatedPfxLen_Type.__name__ = "Unsigned32"
_TmnxDhcpServerPoolDlgatedPfxLen_Object = MibTableColumn
tmnxDhcpServerPoolDlgatedPfxLen = _TmnxDhcpServerPoolDlgatedPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 11),
    _TmnxDhcpServerPoolDlgatedPfxLen_Type()
)
tmnxDhcpServerPoolDlgatedPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolDlgatedPfxLen.setStatus("current")


class _TmnxDhcpServerPoolSubnetBindKey_Type(Integer32):
    """Custom type tmnxDhcpServerPoolSubnetBindKey based on Integer32"""
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
        *(("none", 0),
          ("sysIdSvcId", 1),
          ("sysId", 2),
          ("string", 3))
    )


_TmnxDhcpServerPoolSubnetBindKey_Type.__name__ = "Integer32"
_TmnxDhcpServerPoolSubnetBindKey_Object = MibTableColumn
tmnxDhcpServerPoolSubnetBindKey = _TmnxDhcpServerPoolSubnetBindKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 12),
    _TmnxDhcpServerPoolSubnetBindKey_Type()
)
tmnxDhcpServerPoolSubnetBindKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolSubnetBindKey.setStatus("obsolete")


class _TmnxDhcpServerPoolSubnetBindDly_Type(Unsigned32):
    """Custom type tmnxDhcpServerPoolSubnetBindDly based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_TmnxDhcpServerPoolSubnetBindDly_Type.__name__ = "Unsigned32"
_TmnxDhcpServerPoolSubnetBindDly_Object = MibTableColumn
tmnxDhcpServerPoolSubnetBindDly = _TmnxDhcpServerPoolSubnetBindDly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 4, 1, 13),
    _TmnxDhcpServerPoolSubnetBindDly_Type()
)
tmnxDhcpServerPoolSubnetBindDly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolSubnetBindDly.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxDhcpServerPoolSubnetBindDly.setUnits("seconds")
_TmnxDhcpSvrPoolOptionTableLastCh_Type = TimeStamp
_TmnxDhcpSvrPoolOptionTableLastCh_Object = MibScalar
tmnxDhcpSvrPoolOptionTableLastCh = _TmnxDhcpSvrPoolOptionTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 5),
    _TmnxDhcpSvrPoolOptionTableLastCh_Type()
)
tmnxDhcpSvrPoolOptionTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionTableLastCh.setStatus("current")
_TmnxDhcpSvrPoolOptionTable_Object = MibTable
tmnxDhcpSvrPoolOptionTable = _TmnxDhcpSvrPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionTable.setStatus("current")
_TmnxDhcpSvrPoolOptionEntry_Object = MibTableRow
tmnxDhcpSvrPoolOptionEntry = _TmnxDhcpSvrPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 6, 1)
)
tmnxDhcpSvrPoolOptionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionNumber"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionEntry.setStatus("current")


class _TmnxDhcpSvrPoolOptionNumber_Type(Unsigned32):
    """Custom type tmnxDhcpSvrPoolOptionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxDhcpSvrPoolOptionNumber_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrPoolOptionNumber_Object = MibTableColumn
tmnxDhcpSvrPoolOptionNumber = _TmnxDhcpSvrPoolOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 6, 1, 1),
    _TmnxDhcpSvrPoolOptionNumber_Type()
)
tmnxDhcpSvrPoolOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionNumber.setStatus("current")
_TmnxDhcpSvrPoolOptionRowStatus_Type = RowStatus
_TmnxDhcpSvrPoolOptionRowStatus_Object = MibTableColumn
tmnxDhcpSvrPoolOptionRowStatus = _TmnxDhcpSvrPoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 6, 1, 2),
    _TmnxDhcpSvrPoolOptionRowStatus_Type()
)
tmnxDhcpSvrPoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionRowStatus.setStatus("current")
_TmnxDhcpSvrPoolOptionLastCh_Type = TimeStamp
_TmnxDhcpSvrPoolOptionLastCh_Object = MibTableColumn
tmnxDhcpSvrPoolOptionLastCh = _TmnxDhcpSvrPoolOptionLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 6, 1, 3),
    _TmnxDhcpSvrPoolOptionLastCh_Type()
)
tmnxDhcpSvrPoolOptionLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionLastCh.setStatus("current")
_TmnxDhcpSvrPoolOptionType_Type = TmnxDhcpOptionType
_TmnxDhcpSvrPoolOptionType_Object = MibTableColumn
tmnxDhcpSvrPoolOptionType = _TmnxDhcpSvrPoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 6, 1, 4),
    _TmnxDhcpSvrPoolOptionType_Type()
)
tmnxDhcpSvrPoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionType.setStatus("current")


class _TmnxDhcpSvrPoolOptionValue_Type(OctetString):
    """Custom type tmnxDhcpSvrPoolOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxDhcpSvrPoolOptionValue_Type.__name__ = "OctetString"
_TmnxDhcpSvrPoolOptionValue_Object = MibTableColumn
tmnxDhcpSvrPoolOptionValue = _TmnxDhcpSvrPoolOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 6, 1, 5),
    _TmnxDhcpSvrPoolOptionValue_Type()
)
tmnxDhcpSvrPoolOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolOptionValue.setStatus("current")
_TmnxDhcpServerSubnetTableLastCh_Type = TimeStamp
_TmnxDhcpServerSubnetTableLastCh_Object = MibScalar
tmnxDhcpServerSubnetTableLastCh = _TmnxDhcpServerSubnetTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 7),
    _TmnxDhcpServerSubnetTableLastCh_Type()
)
tmnxDhcpServerSubnetTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerSubnetTableLastCh.setStatus("current")
_TmnxDhcpServerSubnetTable_Object = MibTable
tmnxDhcpServerSubnetTable = _TmnxDhcpServerSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxDhcpServerSubnetTable.setStatus("current")
_TmnxDhcpServerSubnetEntry_Object = MibTableRow
tmnxDhcpServerSubnetEntry = _TmnxDhcpServerSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1)
)
tmnxDhcpServerSubnetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxDhcpServerSubnetEntry.setStatus("current")
_TmnxDhcpSvrSubnetAddrType_Type = InetAddressType
_TmnxDhcpSvrSubnetAddrType_Object = MibTableColumn
tmnxDhcpSvrSubnetAddrType = _TmnxDhcpSvrSubnetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 1),
    _TmnxDhcpSvrSubnetAddrType_Type()
)
tmnxDhcpSvrSubnetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetAddrType.setStatus("current")


class _TmnxDhcpSvrSubnetAddress_Type(InetAddress):
    """Custom type tmnxDhcpSvrSubnetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrSubnetAddress_Type.__name__ = "InetAddress"
_TmnxDhcpSvrSubnetAddress_Object = MibTableColumn
tmnxDhcpSvrSubnetAddress = _TmnxDhcpSvrSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 2),
    _TmnxDhcpSvrSubnetAddress_Type()
)
tmnxDhcpSvrSubnetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetAddress.setStatus("current")


class _TmnxDhcpSvrSubnetPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxDhcpSvrSubnetPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxDhcpSvrSubnetPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxDhcpSvrSubnetPrefixLength_Object = MibTableColumn
tmnxDhcpSvrSubnetPrefixLength = _TmnxDhcpSvrSubnetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 3),
    _TmnxDhcpSvrSubnetPrefixLength_Type()
)
tmnxDhcpSvrSubnetPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetPrefixLength.setStatus("current")
_TmnxDhcpSvrSubnetRowStatus_Type = RowStatus
_TmnxDhcpSvrSubnetRowStatus_Object = MibTableColumn
tmnxDhcpSvrSubnetRowStatus = _TmnxDhcpSvrSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 4),
    _TmnxDhcpSvrSubnetRowStatus_Type()
)
tmnxDhcpSvrSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRowStatus.setStatus("current")
_TmnxDhcpSvrSubnetLastChangeTime_Type = TimeStamp
_TmnxDhcpSvrSubnetLastChangeTime_Object = MibTableColumn
tmnxDhcpSvrSubnetLastChangeTime = _TmnxDhcpSvrSubnetLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 5),
    _TmnxDhcpSvrSubnetLastChangeTime_Type()
)
tmnxDhcpSvrSubnetLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetLastChangeTime.setStatus("current")


class _TmnxDhcpSvrSubnetMinFree_Type(Unsigned32):
    """Custom type tmnxDhcpSvrSubnetMinFree based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDhcpSvrSubnetMinFree_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrSubnetMinFree_Object = MibTableColumn
tmnxDhcpSvrSubnetMinFree = _TmnxDhcpSvrSubnetMinFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 6),
    _TmnxDhcpSvrSubnetMinFree_Type()
)
tmnxDhcpSvrSubnetMinFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetMinFree.setStatus("current")


class _TmnxDhcpSvrSubnetMaxDeclined_Type(Unsigned32):
    """Custom type tmnxDhcpSvrSubnetMaxDeclined based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxDhcpSvrSubnetMaxDeclined_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrSubnetMaxDeclined_Object = MibTableColumn
tmnxDhcpSvrSubnetMaxDeclined = _TmnxDhcpSvrSubnetMaxDeclined_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 7),
    _TmnxDhcpSvrSubnetMaxDeclined_Type()
)
tmnxDhcpSvrSubnetMaxDeclined.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetMaxDeclined.setStatus("current")


class _TmnxDhcpSvrSubnetMinFreeType_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetMinFreeType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 0),
          ("percent", 1))
    )


_TmnxDhcpSvrSubnetMinFreeType_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetMinFreeType_Object = MibTableColumn
tmnxDhcpSvrSubnetMinFreeType = _TmnxDhcpSvrSubnetMinFreeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 8),
    _TmnxDhcpSvrSubnetMinFreeType_Type()
)
tmnxDhcpSvrSubnetMinFreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetMinFreeType.setStatus("current")


class _TmnxDhcpSvrSubnetRenewTimer_Type(Unsigned32):
    """Custom type tmnxDhcpSvrSubnetRenewTimer based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_TmnxDhcpSvrSubnetRenewTimer_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrSubnetRenewTimer_Object = MibTableColumn
tmnxDhcpSvrSubnetRenewTimer = _TmnxDhcpSvrSubnetRenewTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 9),
    _TmnxDhcpSvrSubnetRenewTimer_Type()
)
tmnxDhcpSvrSubnetRenewTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRenewTimer.setStatus("current")


class _TmnxDhcpSvrSubnetRebindTimer_Type(Unsigned32):
    """Custom type tmnxDhcpSvrSubnetRebindTimer based on Unsigned32"""
    defaultValue = 2880

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209600),
    )


_TmnxDhcpSvrSubnetRebindTimer_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrSubnetRebindTimer_Object = MibTableColumn
tmnxDhcpSvrSubnetRebindTimer = _TmnxDhcpSvrSubnetRebindTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 10),
    _TmnxDhcpSvrSubnetRebindTimer_Type()
)
tmnxDhcpSvrSubnetRebindTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRebindTimer.setStatus("current")


class _TmnxDhcpSvrSubnetValidLifetime_Type(Unsigned32):
    """Custom type tmnxDhcpSvrSubnetValidLifetime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 315446399),
    )


_TmnxDhcpSvrSubnetValidLifetime_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrSubnetValidLifetime_Object = MibTableColumn
tmnxDhcpSvrSubnetValidLifetime = _TmnxDhcpSvrSubnetValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 11),
    _TmnxDhcpSvrSubnetValidLifetime_Type()
)
tmnxDhcpSvrSubnetValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetValidLifetime.setUnits("seconds")


class _TmnxDhcpSvrSubnetPrefLifetime_Type(Unsigned32):
    """Custom type tmnxDhcpSvrSubnetPrefLifetime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 315446399),
    )


_TmnxDhcpSvrSubnetPrefLifetime_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrSubnetPrefLifetime_Object = MibTableColumn
tmnxDhcpSvrSubnetPrefLifetime = _TmnxDhcpSvrSubnetPrefLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 12),
    _TmnxDhcpSvrSubnetPrefLifetime_Type()
)
tmnxDhcpSvrSubnetPrefLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetPrefLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetPrefLifetime.setUnits("seconds")


class _TmnxDhcpSvrSubnetFailCtrl_Type(TmnxDhcpSvrFailCtrlType):
    """Custom type tmnxDhcpSvrSubnetFailCtrl based on TmnxDhcpSvrFailCtrlType"""
    defaultValue = 1


_TmnxDhcpSvrSubnetFailCtrl_Type.__name__ = "TmnxDhcpSvrFailCtrlType"
_TmnxDhcpSvrSubnetFailCtrl_Object = MibTableColumn
tmnxDhcpSvrSubnetFailCtrl = _TmnxDhcpSvrSubnetFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 13),
    _TmnxDhcpSvrSubnetFailCtrl_Type()
)
tmnxDhcpSvrSubnetFailCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetFailCtrl.setStatus("current")


class _TmnxDhcpSvrSubnetPrefixType_Type(Bits):
    """Custom type tmnxDhcpSvrSubnetPrefixType based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("pd", 0),
          ("wan-host", 1))
    )

_TmnxDhcpSvrSubnetPrefixType_Type.__name__ = "Bits"
_TmnxDhcpSvrSubnetPrefixType_Object = MibTableColumn
tmnxDhcpSvrSubnetPrefixType = _TmnxDhcpSvrSubnetPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 14),
    _TmnxDhcpSvrSubnetPrefixType_Type()
)
tmnxDhcpSvrSubnetPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetPrefixType.setStatus("current")


class _TmnxDhcpSvrSubnetDepletedEvent_Type(TruthValue):
    """Custom type tmnxDhcpSvrSubnetDepletedEvent based on TruthValue"""
    defaultValue = 2


_TmnxDhcpSvrSubnetDepletedEvent_Type.__name__ = "TruthValue"
_TmnxDhcpSvrSubnetDepletedEvent_Object = MibTableColumn
tmnxDhcpSvrSubnetDepletedEvent = _TmnxDhcpSvrSubnetDepletedEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 15),
    _TmnxDhcpSvrSubnetDepletedEvent_Type()
)
tmnxDhcpSvrSubnetDepletedEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetDepletedEvent.setStatus("current")


class _TmnxDhcpSvrSubnetDrain_Type(TruthValue):
    """Custom type tmnxDhcpSvrSubnetDrain based on TruthValue"""
    defaultValue = 2


_TmnxDhcpSvrSubnetDrain_Type.__name__ = "TruthValue"
_TmnxDhcpSvrSubnetDrain_Object = MibTableColumn
tmnxDhcpSvrSubnetDrain = _TmnxDhcpSvrSubnetDrain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 8, 1, 16),
    _TmnxDhcpSvrSubnetDrain_Type()
)
tmnxDhcpSvrSubnetDrain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetDrain.setStatus("current")
_TmnxDhcpSvrSubnetRangesTblLastCh_Type = TimeStamp
_TmnxDhcpSvrSubnetRangesTblLastCh_Object = MibScalar
tmnxDhcpSvrSubnetRangesTblLastCh = _TmnxDhcpSvrSubnetRangesTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 9),
    _TmnxDhcpSvrSubnetRangesTblLastCh_Type()
)
tmnxDhcpSvrSubnetRangesTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRangesTblLastCh.setStatus("current")
_TmnxDhcpSvrSubnetRangesTable_Object = MibTable
tmnxDhcpSvrSubnetRangesTable = _TmnxDhcpSvrSubnetRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRangesTable.setStatus("current")
_TmnxDhcpSvrSubnetRangesEntry_Object = MibTableRow
tmnxDhcpSvrSubnetRangesEntry = _TmnxDhcpSvrSubnetRangesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1)
)
tmnxDhcpSvrSubnetRangesEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangeType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStartAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStartAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetEndAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetEndAddress"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRangesEntry.setStatus("current")


class _TmnxDhcpSvrSubnetRangeType_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1))
    )


_TmnxDhcpSvrSubnetRangeType_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetRangeType_Object = MibTableColumn
tmnxDhcpSvrSubnetRangeType = _TmnxDhcpSvrSubnetRangeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 1),
    _TmnxDhcpSvrSubnetRangeType_Type()
)
tmnxDhcpSvrSubnetRangeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRangeType.setStatus("current")
_TmnxDhcpSvrSubnetStartAddrType_Type = InetAddressType
_TmnxDhcpSvrSubnetStartAddrType_Object = MibTableColumn
tmnxDhcpSvrSubnetStartAddrType = _TmnxDhcpSvrSubnetStartAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 2),
    _TmnxDhcpSvrSubnetStartAddrType_Type()
)
tmnxDhcpSvrSubnetStartAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStartAddrType.setStatus("current")


class _TmnxDhcpSvrSubnetStartAddress_Type(InetAddress):
    """Custom type tmnxDhcpSvrSubnetStartAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrSubnetStartAddress_Type.__name__ = "InetAddress"
_TmnxDhcpSvrSubnetStartAddress_Object = MibTableColumn
tmnxDhcpSvrSubnetStartAddress = _TmnxDhcpSvrSubnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 3),
    _TmnxDhcpSvrSubnetStartAddress_Type()
)
tmnxDhcpSvrSubnetStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStartAddress.setStatus("current")
_TmnxDhcpSvrSubnetEndAddrType_Type = InetAddressType
_TmnxDhcpSvrSubnetEndAddrType_Object = MibTableColumn
tmnxDhcpSvrSubnetEndAddrType = _TmnxDhcpSvrSubnetEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 4),
    _TmnxDhcpSvrSubnetEndAddrType_Type()
)
tmnxDhcpSvrSubnetEndAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetEndAddrType.setStatus("current")


class _TmnxDhcpSvrSubnetEndAddress_Type(InetAddress):
    """Custom type tmnxDhcpSvrSubnetEndAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrSubnetEndAddress_Type.__name__ = "InetAddress"
_TmnxDhcpSvrSubnetEndAddress_Object = MibTableColumn
tmnxDhcpSvrSubnetEndAddress = _TmnxDhcpSvrSubnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 5),
    _TmnxDhcpSvrSubnetEndAddress_Type()
)
tmnxDhcpSvrSubnetEndAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetEndAddress.setStatus("current")
_TmnxDhcpSvrSubnetRangesRowStatus_Type = RowStatus
_TmnxDhcpSvrSubnetRangesRowStatus_Object = MibTableColumn
tmnxDhcpSvrSubnetRangesRowStatus = _TmnxDhcpSvrSubnetRangesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 6),
    _TmnxDhcpSvrSubnetRangesRowStatus_Type()
)
tmnxDhcpSvrSubnetRangesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRangesRowStatus.setStatus("current")
_TmnxDhcpSvrSubnetRangesLastCh_Type = TimeStamp
_TmnxDhcpSvrSubnetRangesLastCh_Object = MibTableColumn
tmnxDhcpSvrSubnetRangesLastCh = _TmnxDhcpSvrSubnetRangesLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 7),
    _TmnxDhcpSvrSubnetRangesLastCh_Type()
)
tmnxDhcpSvrSubnetRangesLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRangesLastCh.setStatus("current")


class _TmnxDhcpSvrSubnetRangeFailCtrl_Type(TmnxDhcpSvrFailCtrlType):
    """Custom type tmnxDhcpSvrSubnetRangeFailCtrl based on TmnxDhcpSvrFailCtrlType"""
    defaultValue = 1


_TmnxDhcpSvrSubnetRangeFailCtrl_Type.__name__ = "TmnxDhcpSvrFailCtrlType"
_TmnxDhcpSvrSubnetRangeFailCtrl_Object = MibTableColumn
tmnxDhcpSvrSubnetRangeFailCtrl = _TmnxDhcpSvrSubnetRangeFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 10, 1, 8),
    _TmnxDhcpSvrSubnetRangeFailCtrl_Type()
)
tmnxDhcpSvrSubnetRangeFailCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetRangeFailCtrl.setStatus("current")
_TmnxDhcpSvrSubnetOptionTblLastCh_Type = TimeStamp
_TmnxDhcpSvrSubnetOptionTblLastCh_Object = MibScalar
tmnxDhcpSvrSubnetOptionTblLastCh = _TmnxDhcpSvrSubnetOptionTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 11),
    _TmnxDhcpSvrSubnetOptionTblLastCh_Type()
)
tmnxDhcpSvrSubnetOptionTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionTblLastCh.setStatus("current")
_TmnxDhcpSvrSubnetOptionTable_Object = MibTable
tmnxDhcpSvrSubnetOptionTable = _TmnxDhcpSvrSubnetOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionTable.setStatus("current")
_TmnxDhcpSvrSubnetOptionEntry_Object = MibTableRow
tmnxDhcpSvrSubnetOptionEntry = _TmnxDhcpSvrSubnetOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 12, 1)
)
tmnxDhcpSvrSubnetOptionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionNumber"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionEntry.setStatus("current")


class _TmnxDhcpSvrSubnetOptionNumber_Type(Unsigned32):
    """Custom type tmnxDhcpSvrSubnetOptionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxDhcpSvrSubnetOptionNumber_Type.__name__ = "Unsigned32"
_TmnxDhcpSvrSubnetOptionNumber_Object = MibTableColumn
tmnxDhcpSvrSubnetOptionNumber = _TmnxDhcpSvrSubnetOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 12, 1, 1),
    _TmnxDhcpSvrSubnetOptionNumber_Type()
)
tmnxDhcpSvrSubnetOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionNumber.setStatus("current")
_TmnxDhcpSvrSubnetOptionRowStatus_Type = RowStatus
_TmnxDhcpSvrSubnetOptionRowStatus_Object = MibTableColumn
tmnxDhcpSvrSubnetOptionRowStatus = _TmnxDhcpSvrSubnetOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 12, 1, 2),
    _TmnxDhcpSvrSubnetOptionRowStatus_Type()
)
tmnxDhcpSvrSubnetOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionRowStatus.setStatus("current")
_TmnxDhcpSvrSubnetOptionLastCh_Type = TimeStamp
_TmnxDhcpSvrSubnetOptionLastCh_Object = MibTableColumn
tmnxDhcpSvrSubnetOptionLastCh = _TmnxDhcpSvrSubnetOptionLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 12, 1, 3),
    _TmnxDhcpSvrSubnetOptionLastCh_Type()
)
tmnxDhcpSvrSubnetOptionLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionLastCh.setStatus("current")
_TmnxDhcpSvrSubnetOptionType_Type = TmnxDhcpOptionType
_TmnxDhcpSvrSubnetOptionType_Object = MibTableColumn
tmnxDhcpSvrSubnetOptionType = _TmnxDhcpSvrSubnetOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 12, 1, 4),
    _TmnxDhcpSvrSubnetOptionType_Type()
)
tmnxDhcpSvrSubnetOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionType.setStatus("current")


class _TmnxDhcpSvrSubnetOptionValue_Type(OctetString):
    """Custom type tmnxDhcpSvrSubnetOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxDhcpSvrSubnetOptionValue_Type.__name__ = "OctetString"
_TmnxDhcpSvrSubnetOptionValue_Object = MibTableColumn
tmnxDhcpSvrSubnetOptionValue = _TmnxDhcpSvrSubnetOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 12, 1, 5),
    _TmnxDhcpSvrSubnetOptionValue_Type()
)
tmnxDhcpSvrSubnetOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetOptionValue.setStatus("current")
_TmnxDhcpSvrLeaseTable_Object = MibTable
tmnxDhcpSvrLeaseTable = _TmnxDhcpSvrLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseTable.setStatus("current")
_TmnxDhcpSvrLeaseEntry_Object = MibTableRow
tmnxDhcpSvrLeaseEntry = _TmnxDhcpSvrLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1)
)
tmnxDhcpSvrLeaseEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseClientAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseClientAddress"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseEntry.setStatus("current")
_TmnxDhcpSvrLeaseClientAddrType_Type = InetAddressType
_TmnxDhcpSvrLeaseClientAddrType_Object = MibTableColumn
tmnxDhcpSvrLeaseClientAddrType = _TmnxDhcpSvrLeaseClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 1),
    _TmnxDhcpSvrLeaseClientAddrType_Type()
)
tmnxDhcpSvrLeaseClientAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseClientAddrType.setStatus("current")


class _TmnxDhcpSvrLeaseClientAddress_Type(InetAddress):
    """Custom type tmnxDhcpSvrLeaseClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrLeaseClientAddress_Type.__name__ = "InetAddress"
_TmnxDhcpSvrLeaseClientAddress_Object = MibTableColumn
tmnxDhcpSvrLeaseClientAddress = _TmnxDhcpSvrLeaseClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 2),
    _TmnxDhcpSvrLeaseClientAddress_Type()
)
tmnxDhcpSvrLeaseClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseClientAddress.setStatus("current")


class _TmnxDhcpSvrLeaseState_Type(Integer32):
    """Custom type tmnxDhcpSvrLeaseState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("offered", 0),
          ("stable", 1),
          ("forceRenewPending", 2),
          ("removePending", 3),
          ("held", 4),
          ("internal", 5),
          ("internalOrphan", 6),
          ("internalOffered", 7))
    )


_TmnxDhcpSvrLeaseState_Type.__name__ = "Integer32"
_TmnxDhcpSvrLeaseState_Object = MibTableColumn
tmnxDhcpSvrLeaseState = _TmnxDhcpSvrLeaseState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 3),
    _TmnxDhcpSvrLeaseState_Type()
)
tmnxDhcpSvrLeaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseState.setStatus("current")
_TmnxDhcpSvrLeaseStart_Type = DateAndTime
_TmnxDhcpSvrLeaseStart_Object = MibTableColumn
tmnxDhcpSvrLeaseStart = _TmnxDhcpSvrLeaseStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 4),
    _TmnxDhcpSvrLeaseStart_Type()
)
tmnxDhcpSvrLeaseStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseStart.setStatus("current")
_TmnxDhcpSvrLeaseLastRenew_Type = DateAndTime
_TmnxDhcpSvrLeaseLastRenew_Object = MibTableColumn
tmnxDhcpSvrLeaseLastRenew = _TmnxDhcpSvrLeaseLastRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 5),
    _TmnxDhcpSvrLeaseLastRenew_Type()
)
tmnxDhcpSvrLeaseLastRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseLastRenew.setStatus("current")
_TmnxDhcpSvrLeaseRemainLeaseTime_Type = Unsigned32
_TmnxDhcpSvrLeaseRemainLeaseTime_Object = MibTableColumn
tmnxDhcpSvrLeaseRemainLeaseTime = _TmnxDhcpSvrLeaseRemainLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 6),
    _TmnxDhcpSvrLeaseRemainLeaseTime_Type()
)
tmnxDhcpSvrLeaseRemainLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseRemainLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseRemainLeaseTime.setUnits("seconds")
_TmnxDhcpSvrLeaseRemPotentExpTime_Type = Unsigned32
_TmnxDhcpSvrLeaseRemPotentExpTime_Object = MibTableColumn
tmnxDhcpSvrLeaseRemPotentExpTime = _TmnxDhcpSvrLeaseRemPotentExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 7),
    _TmnxDhcpSvrLeaseRemPotentExpTime_Type()
)
tmnxDhcpSvrLeaseRemPotentExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseRemPotentExpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseRemPotentExpTime.setUnits("seconds")
_TmnxDhcpSvrLeaseClientHwAddress_Type = MacAddress
_TmnxDhcpSvrLeaseClientHwAddress_Object = MibTableColumn
tmnxDhcpSvrLeaseClientHwAddress = _TmnxDhcpSvrLeaseClientHwAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 8),
    _TmnxDhcpSvrLeaseClientHwAddress_Type()
)
tmnxDhcpSvrLeaseClientHwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseClientHwAddress.setStatus("current")
_TmnxDhcpSvrLeaseXid_Type = Unsigned32
_TmnxDhcpSvrLeaseXid_Object = MibTableColumn
tmnxDhcpSvrLeaseXid = _TmnxDhcpSvrLeaseXid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 9),
    _TmnxDhcpSvrLeaseXid_Type()
)
tmnxDhcpSvrLeaseXid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseXid.setStatus("current")
_TmnxDhcpSvrLeaseOption82_Type = OctetString
_TmnxDhcpSvrLeaseOption82_Object = MibTableColumn
tmnxDhcpSvrLeaseOption82 = _TmnxDhcpSvrLeaseOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 10),
    _TmnxDhcpSvrLeaseOption82_Type()
)
tmnxDhcpSvrLeaseOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseOption82.setStatus("current")
_TmnxDhcpSvrLeaseClientType_Type = TmnxDhcpSvrClientType
_TmnxDhcpSvrLeaseClientType_Object = MibTableColumn
tmnxDhcpSvrLeaseClientType = _TmnxDhcpSvrLeaseClientType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 11),
    _TmnxDhcpSvrLeaseClientType_Type()
)
tmnxDhcpSvrLeaseClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseClientType.setStatus("current")
_TmnxDhcpSvrLeasePPPoEUserName_Type = TmnxPppoeUserNameOrEmpty
_TmnxDhcpSvrLeasePPPoEUserName_Object = MibTableColumn
tmnxDhcpSvrLeasePPPoEUserName = _TmnxDhcpSvrLeasePPPoEUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 12),
    _TmnxDhcpSvrLeasePPPoEUserName_Type()
)
tmnxDhcpSvrLeasePPPoEUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeasePPPoEUserName.setStatus("current")


class _TmnxDhcpSvrLeaseOpt82CircId_Type(OctetString):
    """Custom type tmnxDhcpSvrLeaseOpt82CircId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrLeaseOpt82CircId_Type.__name__ = "OctetString"
_TmnxDhcpSvrLeaseOpt82CircId_Object = MibTableColumn
tmnxDhcpSvrLeaseOpt82CircId = _TmnxDhcpSvrLeaseOpt82CircId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 13),
    _TmnxDhcpSvrLeaseOpt82CircId_Type()
)
tmnxDhcpSvrLeaseOpt82CircId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseOpt82CircId.setStatus("current")
_TmnxDhcpSvrLeaseFailCtrl_Type = TmnxDhcpSvrFailCtrlType
_TmnxDhcpSvrLeaseFailCtrl_Object = MibTableColumn
tmnxDhcpSvrLeaseFailCtrl = _TmnxDhcpSvrLeaseFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 14),
    _TmnxDhcpSvrLeaseFailCtrl_Type()
)
tmnxDhcpSvrLeaseFailCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseFailCtrl.setStatus("current")
_TmnxDhcpSvrLeaseOption60_Type = OctetString
_TmnxDhcpSvrLeaseOption60_Object = MibTableColumn
tmnxDhcpSvrLeaseOption60 = _TmnxDhcpSvrLeaseOption60_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 15),
    _TmnxDhcpSvrLeaseOption60_Type()
)
tmnxDhcpSvrLeaseOption60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseOption60.setStatus("current")


class _TmnxDhcpSvrLeaseClientPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxDhcpSvrLeaseClientPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxDhcpSvrLeaseClientPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxDhcpSvrLeaseClientPrefixLen_Object = MibTableColumn
tmnxDhcpSvrLeaseClientPrefixLen = _TmnxDhcpSvrLeaseClientPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 16),
    _TmnxDhcpSvrLeaseClientPrefixLen_Type()
)
tmnxDhcpSvrLeaseClientPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseClientPrefixLen.setStatus("current")


class _TmnxDhcpSvrLeaseIAOptionType_Type(Integer32):
    """Custom type tmnxDhcpSvrLeaseIAOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("iaNa", 1),
          ("iaPd", 2))
    )


_TmnxDhcpSvrLeaseIAOptionType_Type.__name__ = "Integer32"
_TmnxDhcpSvrLeaseIAOptionType_Object = MibTableColumn
tmnxDhcpSvrLeaseIAOptionType = _TmnxDhcpSvrLeaseIAOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 17),
    _TmnxDhcpSvrLeaseIAOptionType_Type()
)
tmnxDhcpSvrLeaseIAOptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseIAOptionType.setStatus("current")
_TmnxDhcpSvrLeaseIAID_Type = Unsigned32
_TmnxDhcpSvrLeaseIAID_Object = MibTableColumn
tmnxDhcpSvrLeaseIAID = _TmnxDhcpSvrLeaseIAID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 18),
    _TmnxDhcpSvrLeaseIAID_Type()
)
tmnxDhcpSvrLeaseIAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseIAID.setStatus("current")


class _TmnxDhcpSvrLeaseDUID_Type(OctetString):
    """Custom type tmnxDhcpSvrLeaseDUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrLeaseDUID_Type.__name__ = "OctetString"
_TmnxDhcpSvrLeaseDUID_Object = MibTableColumn
tmnxDhcpSvrLeaseDUID = _TmnxDhcpSvrLeaseDUID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 19),
    _TmnxDhcpSvrLeaseDUID_Type()
)
tmnxDhcpSvrLeaseDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseDUID.setStatus("current")
_TmnxDhcpSvrLeaseRemainHoldTime_Type = Unsigned32
_TmnxDhcpSvrLeaseRemainHoldTime_Object = MibTableColumn
tmnxDhcpSvrLeaseRemainHoldTime = _TmnxDhcpSvrLeaseRemainHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 20),
    _TmnxDhcpSvrLeaseRemainHoldTime_Type()
)
tmnxDhcpSvrLeaseRemainHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseRemainHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseRemainHoldTime.setUnits("seconds")


class _TmnxDhcpSvrLeaseRelayInterfaceId_Type(OctetString):
    """Custom type tmnxDhcpSvrLeaseRelayInterfaceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrLeaseRelayInterfaceId_Type.__name__ = "OctetString"
_TmnxDhcpSvrLeaseRelayInterfaceId_Object = MibTableColumn
tmnxDhcpSvrLeaseRelayInterfaceId = _TmnxDhcpSvrLeaseRelayInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 21),
    _TmnxDhcpSvrLeaseRelayInterfaceId_Type()
)
tmnxDhcpSvrLeaseRelayInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseRelayInterfaceId.setStatus("current")


class _TmnxDhcpSvrLeaseLDRAInterfaceId_Type(OctetString):
    """Custom type tmnxDhcpSvrLeaseLDRAInterfaceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrLeaseLDRAInterfaceId_Type.__name__ = "OctetString"
_TmnxDhcpSvrLeaseLDRAInterfaceId_Object = MibTableColumn
tmnxDhcpSvrLeaseLDRAInterfaceId = _TmnxDhcpSvrLeaseLDRAInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 22),
    _TmnxDhcpSvrLeaseLDRAInterfaceId_Type()
)
tmnxDhcpSvrLeaseLDRAInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseLDRAInterfaceId.setStatus("current")
_TmnxDhcpSvrLeaseLnkLclAddrType_Type = InetAddressType
_TmnxDhcpSvrLeaseLnkLclAddrType_Object = MibTableColumn
tmnxDhcpSvrLeaseLnkLclAddrType = _TmnxDhcpSvrLeaseLnkLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 23),
    _TmnxDhcpSvrLeaseLnkLclAddrType_Type()
)
tmnxDhcpSvrLeaseLnkLclAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseLnkLclAddrType.setStatus("current")


class _TmnxDhcpSvrLeaseLnkLclAddress_Type(InetAddress):
    """Custom type tmnxDhcpSvrLeaseLnkLclAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrLeaseLnkLclAddress_Type.__name__ = "InetAddress"
_TmnxDhcpSvrLeaseLnkLclAddress_Object = MibTableColumn
tmnxDhcpSvrLeaseLnkLclAddress = _TmnxDhcpSvrLeaseLnkLclAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 24),
    _TmnxDhcpSvrLeaseLnkLclAddress_Type()
)
tmnxDhcpSvrLeaseLnkLclAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseLnkLclAddress.setStatus("current")


class _TmnxDhcpSvrLeaseIntClientType_Type(Integer32):
    """Custom type tmnxDhcpSvrLeaseIntClientType based on Integer32"""
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
        *(("notApplicable", 0),
          ("ipoeWan", 1),
          ("ipoeSlaac", 2),
          ("ppp", 3),
          ("pppSlaac", 4))
    )


_TmnxDhcpSvrLeaseIntClientType_Type.__name__ = "Integer32"
_TmnxDhcpSvrLeaseIntClientType_Object = MibTableColumn
tmnxDhcpSvrLeaseIntClientType = _TmnxDhcpSvrLeaseIntClientType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 13, 1, 25),
    _TmnxDhcpSvrLeaseIntClientType_Type()
)
tmnxDhcpSvrLeaseIntClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseIntClientType.setStatus("current")
_TmnxDhcpServerStatsTable_Object = MibTable
tmnxDhcpServerStatsTable = _TmnxDhcpServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxDhcpServerStatsTable.setStatus("current")
_TmnxDhcpServerStatsEntry_Object = MibTableRow
tmnxDhcpServerStatsEntry = _TmnxDhcpServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1)
)
tmnxDhcpServerStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
)
if mibBuilder.loadTexts:
    tmnxDhcpServerStatsEntry.setStatus("current")
_TmnxDhcpSvrStatsRxDiscovers_Type = Counter64
_TmnxDhcpSvrStatsRxDiscovers_Object = MibTableColumn
tmnxDhcpSvrStatsRxDiscovers = _TmnxDhcpSvrStatsRxDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 1),
    _TmnxDhcpSvrStatsRxDiscovers_Type()
)
tmnxDhcpSvrStatsRxDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsRxDiscovers.setStatus("current")
_TmnxDhcpSvrStatsRxRequests_Type = Counter64
_TmnxDhcpSvrStatsRxRequests_Object = MibTableColumn
tmnxDhcpSvrStatsRxRequests = _TmnxDhcpSvrStatsRxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 2),
    _TmnxDhcpSvrStatsRxRequests_Type()
)
tmnxDhcpSvrStatsRxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsRxRequests.setStatus("current")
_TmnxDhcpSvrStatsRxReleases_Type = Counter64
_TmnxDhcpSvrStatsRxReleases_Object = MibTableColumn
tmnxDhcpSvrStatsRxReleases = _TmnxDhcpSvrStatsRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 3),
    _TmnxDhcpSvrStatsRxReleases_Type()
)
tmnxDhcpSvrStatsRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsRxReleases.setStatus("current")
_TmnxDhcpSvrStatsRxDeclines_Type = Counter64
_TmnxDhcpSvrStatsRxDeclines_Object = MibTableColumn
tmnxDhcpSvrStatsRxDeclines = _TmnxDhcpSvrStatsRxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 4),
    _TmnxDhcpSvrStatsRxDeclines_Type()
)
tmnxDhcpSvrStatsRxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsRxDeclines.setStatus("current")
_TmnxDhcpSvrStatsRxInforms_Type = Counter64
_TmnxDhcpSvrStatsRxInforms_Object = MibTableColumn
tmnxDhcpSvrStatsRxInforms = _TmnxDhcpSvrStatsRxInforms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 5),
    _TmnxDhcpSvrStatsRxInforms_Type()
)
tmnxDhcpSvrStatsRxInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsRxInforms.setStatus("current")
_TmnxDhcpSvrStatsTxOffers_Type = Counter64
_TmnxDhcpSvrStatsTxOffers_Object = MibTableColumn
tmnxDhcpSvrStatsTxOffers = _TmnxDhcpSvrStatsTxOffers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 6),
    _TmnxDhcpSvrStatsTxOffers_Type()
)
tmnxDhcpSvrStatsTxOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsTxOffers.setStatus("current")
_TmnxDhcpSvrStatsTxAcks_Type = Counter64
_TmnxDhcpSvrStatsTxAcks_Object = MibTableColumn
tmnxDhcpSvrStatsTxAcks = _TmnxDhcpSvrStatsTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 7),
    _TmnxDhcpSvrStatsTxAcks_Type()
)
tmnxDhcpSvrStatsTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsTxAcks.setStatus("current")
_TmnxDhcpSvrStatsTxNaks_Type = Counter64
_TmnxDhcpSvrStatsTxNaks_Object = MibTableColumn
tmnxDhcpSvrStatsTxNaks = _TmnxDhcpSvrStatsTxNaks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 8),
    _TmnxDhcpSvrStatsTxNaks_Type()
)
tmnxDhcpSvrStatsTxNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsTxNaks.setStatus("current")
_TmnxDhcpSvrStatsTxForceRenews_Type = Counter64
_TmnxDhcpSvrStatsTxForceRenews_Object = MibTableColumn
tmnxDhcpSvrStatsTxForceRenews = _TmnxDhcpSvrStatsTxForceRenews_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 9),
    _TmnxDhcpSvrStatsTxForceRenews_Type()
)
tmnxDhcpSvrStatsTxForceRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsTxForceRenews.setStatus("current")
_TmnxDhcpSvrStatsDropBadPackets_Type = Counter32
_TmnxDhcpSvrStatsDropBadPackets_Object = MibTableColumn
tmnxDhcpSvrStatsDropBadPackets = _TmnxDhcpSvrStatsDropBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 10),
    _TmnxDhcpSvrStatsDropBadPackets_Type()
)
tmnxDhcpSvrStatsDropBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropBadPackets.setStatus("current")
_TmnxDhcpSvrStatsDropInvalidTypes_Type = Counter32
_TmnxDhcpSvrStatsDropInvalidTypes_Object = MibTableColumn
tmnxDhcpSvrStatsDropInvalidTypes = _TmnxDhcpSvrStatsDropInvalidTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 11),
    _TmnxDhcpSvrStatsDropInvalidTypes_Type()
)
tmnxDhcpSvrStatsDropInvalidTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropInvalidTypes.setStatus("current")
_TmnxDhcpSvrStatsDropNoUsrDbFound_Type = Counter32
_TmnxDhcpSvrStatsDropNoUsrDbFound_Object = MibTableColumn
tmnxDhcpSvrStatsDropNoUsrDbFound = _TmnxDhcpSvrStatsDropNoUsrDbFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 12),
    _TmnxDhcpSvrStatsDropNoUsrDbFound_Type()
)
tmnxDhcpSvrStatsDropNoUsrDbFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropNoUsrDbFound.setStatus("current")
_TmnxDhcpSvrStatsDropUnknownHosts_Type = Counter32
_TmnxDhcpSvrStatsDropUnknownHosts_Object = MibTableColumn
tmnxDhcpSvrStatsDropUnknownHosts = _TmnxDhcpSvrStatsDropUnknownHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 13),
    _TmnxDhcpSvrStatsDropUnknownHosts_Type()
)
tmnxDhcpSvrStatsDropUnknownHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropUnknownHosts.setStatus("current")
_TmnxDhcpSvrStatsDropUserNotAllow_Type = Counter32
_TmnxDhcpSvrStatsDropUserNotAllow_Object = MibTableColumn
tmnxDhcpSvrStatsDropUserNotAllow = _TmnxDhcpSvrStatsDropUserNotAllow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 14),
    _TmnxDhcpSvrStatsDropUserNotAllow_Type()
)
tmnxDhcpSvrStatsDropUserNotAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropUserNotAllow.setStatus("current")
_TmnxDhcpSvrStatsDropLseNotReady_Type = Counter32
_TmnxDhcpSvrStatsDropLseNotReady_Object = MibTableColumn
tmnxDhcpSvrStatsDropLseNotReady = _TmnxDhcpSvrStatsDropLseNotReady_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 15),
    _TmnxDhcpSvrStatsDropLseNotReady_Type()
)
tmnxDhcpSvrStatsDropLseNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropLseNotReady.setStatus("current")
_TmnxDhcpSvrStatsDropNoLeaseFound_Type = Counter32
_TmnxDhcpSvrStatsDropNoLeaseFound_Object = MibTableColumn
tmnxDhcpSvrStatsDropNoLeaseFound = _TmnxDhcpSvrStatsDropNoLeaseFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 16),
    _TmnxDhcpSvrStatsDropNoLeaseFound_Type()
)
tmnxDhcpSvrStatsDropNoLeaseFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropNoLeaseFound.setStatus("current")
_TmnxDhcpSvrStatsDropNotSrvngPool_Type = Counter32
_TmnxDhcpSvrStatsDropNotSrvngPool_Object = MibTableColumn
tmnxDhcpSvrStatsDropNotSrvngPool = _TmnxDhcpSvrStatsDropNotSrvngPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 17),
    _TmnxDhcpSvrStatsDropNotSrvngPool_Type()
)
tmnxDhcpSvrStatsDropNotSrvngPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropNotSrvngPool.setStatus("current")
_TmnxDhcpSvrStatsDropInvalidUsr_Type = Counter32
_TmnxDhcpSvrStatsDropInvalidUsr_Object = MibTableColumn
tmnxDhcpSvrStatsDropInvalidUsr = _TmnxDhcpSvrStatsDropInvalidUsr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 18),
    _TmnxDhcpSvrStatsDropInvalidUsr_Type()
)
tmnxDhcpSvrStatsDropInvalidUsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropInvalidUsr.setStatus("current")
_TmnxDhcpSvrStatsDropOverload_Type = Counter32
_TmnxDhcpSvrStatsDropOverload_Object = MibTableColumn
tmnxDhcpSvrStatsDropOverload = _TmnxDhcpSvrStatsDropOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 19),
    _TmnxDhcpSvrStatsDropOverload_Type()
)
tmnxDhcpSvrStatsDropOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropOverload.setStatus("current")
_TmnxDhcpSvrStatsDropPersOverload_Type = Counter32
_TmnxDhcpSvrStatsDropPersOverload_Object = MibTableColumn
tmnxDhcpSvrStatsDropPersOverload = _TmnxDhcpSvrStatsDropPersOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 20),
    _TmnxDhcpSvrStatsDropPersOverload_Type()
)
tmnxDhcpSvrStatsDropPersOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropPersOverload.setStatus("current")
_TmnxDhcpSvrStatsOffersIgnore_Type = Counter32
_TmnxDhcpSvrStatsOffersIgnore_Object = MibTableColumn
tmnxDhcpSvrStatsOffersIgnore = _TmnxDhcpSvrStatsOffersIgnore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 21),
    _TmnxDhcpSvrStatsOffersIgnore_Type()
)
tmnxDhcpSvrStatsOffersIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsOffersIgnore.setStatus("current")
_TmnxDhcpSvrStatsDropGenError_Type = Counter32
_TmnxDhcpSvrStatsDropGenError_Object = MibTableColumn
tmnxDhcpSvrStatsDropGenError = _TmnxDhcpSvrStatsDropGenError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 22),
    _TmnxDhcpSvrStatsDropGenError_Type()
)
tmnxDhcpSvrStatsDropGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropGenError.setStatus("current")
_TmnxDhcpSvrStatsDropDestOther_Type = Counter32
_TmnxDhcpSvrStatsDropDestOther_Object = MibTableColumn
tmnxDhcpSvrStatsDropDestOther = _TmnxDhcpSvrStatsDropDestOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 23),
    _TmnxDhcpSvrStatsDropDestOther_Type()
)
tmnxDhcpSvrStatsDropDestOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropDestOther.setStatus("current")
_TmnxDhcpSvrStatsDropAddrUnavail_Type = Counter32
_TmnxDhcpSvrStatsDropAddrUnavail_Object = MibTableColumn
tmnxDhcpSvrStatsDropAddrUnavail = _TmnxDhcpSvrStatsDropAddrUnavail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 24),
    _TmnxDhcpSvrStatsDropAddrUnavail_Type()
)
tmnxDhcpSvrStatsDropAddrUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropAddrUnavail.setStatus("current")
_TmnxDhcpSvrStatsDropMaxReached_Type = Counter32
_TmnxDhcpSvrStatsDropMaxReached_Object = MibTableColumn
tmnxDhcpSvrStatsDropMaxReached = _TmnxDhcpSvrStatsDropMaxReached_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 25),
    _TmnxDhcpSvrStatsDropMaxReached_Type()
)
tmnxDhcpSvrStatsDropMaxReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropMaxReached.setStatus("current")
_TmnxDhcpSvrStatsDropSvrDown_Type = Counter32
_TmnxDhcpSvrStatsDropSvrDown_Object = MibTableColumn
tmnxDhcpSvrStatsDropSvrDown = _TmnxDhcpSvrStatsDropSvrDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 26),
    _TmnxDhcpSvrStatsDropSvrDown_Type()
)
tmnxDhcpSvrStatsDropSvrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropSvrDown.setStatus("current")
_TmnxDhcpSvrStatsDropNoSubnet_Type = Counter32
_TmnxDhcpSvrStatsDropNoSubnet_Object = MibTableColumn
tmnxDhcpSvrStatsDropNoSubnet = _TmnxDhcpSvrStatsDropNoSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 27),
    _TmnxDhcpSvrStatsDropNoSubnet_Type()
)
tmnxDhcpSvrStatsDropNoSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropNoSubnet.setStatus("current")
_TmnxDhcpSvrStatsLeasesExpired_Type = Counter32
_TmnxDhcpSvrStatsLeasesExpired_Object = MibTableColumn
tmnxDhcpSvrStatsLeasesExpired = _TmnxDhcpSvrStatsLeasesExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 28),
    _TmnxDhcpSvrStatsLeasesExpired_Type()
)
tmnxDhcpSvrStatsLeasesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsLeasesExpired.setStatus("current")
_TmnxDhcpSvrStatsDropDuplDiffGi_Type = Counter32
_TmnxDhcpSvrStatsDropDuplDiffGi_Object = MibTableColumn
tmnxDhcpSvrStatsDropDuplDiffGi = _TmnxDhcpSvrStatsDropDuplDiffGi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 29),
    _TmnxDhcpSvrStatsDropDuplDiffGi_Type()
)
tmnxDhcpSvrStatsDropDuplDiffGi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropDuplDiffGi.setStatus("current")
_TmnxDhcpSvrStatsRxIntRequests_Type = Counter64
_TmnxDhcpSvrStatsRxIntRequests_Object = MibTableColumn
tmnxDhcpSvrStatsRxIntRequests = _TmnxDhcpSvrStatsRxIntRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 30),
    _TmnxDhcpSvrStatsRxIntRequests_Type()
)
tmnxDhcpSvrStatsRxIntRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsRxIntRequests.setStatus("current")
_TmnxDhcpSvrStatsRxIntReleases_Type = Counter64
_TmnxDhcpSvrStatsRxIntReleases_Object = MibTableColumn
tmnxDhcpSvrStatsRxIntReleases = _TmnxDhcpSvrStatsRxIntReleases_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 31),
    _TmnxDhcpSvrStatsRxIntReleases_Type()
)
tmnxDhcpSvrStatsRxIntReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsRxIntReleases.setStatus("current")
_TmnxDhcpSvrStatsDropIntWithLudb_Type = Counter32
_TmnxDhcpSvrStatsDropIntWithLudb_Object = MibTableColumn
tmnxDhcpSvrStatsDropIntWithLudb = _TmnxDhcpSvrStatsDropIntWithLudb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 32),
    _TmnxDhcpSvrStatsDropIntWithLudb_Type()
)
tmnxDhcpSvrStatsDropIntWithLudb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropIntWithLudb.setStatus("current")
_TmnxDhcpSvrStatsDropIntWithFo_Type = Counter32
_TmnxDhcpSvrStatsDropIntWithFo_Object = MibTableColumn
tmnxDhcpSvrStatsDropIntWithFo = _TmnxDhcpSvrStatsDropIntWithFo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 33),
    _TmnxDhcpSvrStatsDropIntWithFo_Type()
)
tmnxDhcpSvrStatsDropIntWithFo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropIntWithFo.setStatus("current")
_TmnxDhcpSvrStatsDropIntConflicts_Type = Counter32
_TmnxDhcpSvrStatsDropIntConflicts_Object = MibTableColumn
tmnxDhcpSvrStatsDropIntConflicts = _TmnxDhcpSvrStatsDropIntConflicts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 34),
    _TmnxDhcpSvrStatsDropIntConflicts_Type()
)
tmnxDhcpSvrStatsDropIntConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropIntConflicts.setStatus("current")
_TmnxDhcpSvrStatsDropAudit_Type = Counter32
_TmnxDhcpSvrStatsDropAudit_Object = MibTableColumn
tmnxDhcpSvrStatsDropAudit = _TmnxDhcpSvrStatsDropAudit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 14, 1, 35),
    _TmnxDhcpSvrStatsDropAudit_Type()
)
tmnxDhcpSvrStatsDropAudit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStatsDropAudit.setStatus("current")
_TmnxDhcpSvrDeclinedAddrTable_Object = MibTable
tmnxDhcpSvrDeclinedAddrTable = _TmnxDhcpSvrDeclinedAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrTable.setStatus("current")
_TmnxDhcpSvrDeclinedAddrEntry_Object = MibTableRow
tmnxDhcpSvrDeclinedAddrEntry = _TmnxDhcpSvrDeclinedAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1)
)
tmnxDhcpSvrDeclinedAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddress"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrEntry.setStatus("current")
_TmnxDhcpSvrDeclinedAddrType_Type = InetAddressType
_TmnxDhcpSvrDeclinedAddrType_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddrType = _TmnxDhcpSvrDeclinedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 1),
    _TmnxDhcpSvrDeclinedAddrType_Type()
)
tmnxDhcpSvrDeclinedAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrType.setStatus("current")


class _TmnxDhcpSvrDeclinedAddress_Type(InetAddress):
    """Custom type tmnxDhcpSvrDeclinedAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrDeclinedAddress_Type.__name__ = "InetAddress"
_TmnxDhcpSvrDeclinedAddress_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddress = _TmnxDhcpSvrDeclinedAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 2),
    _TmnxDhcpSvrDeclinedAddress_Type()
)
tmnxDhcpSvrDeclinedAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddress.setStatus("current")
_TmnxDhcpSvrDeclinedAddrHwAddress_Type = MacAddress
_TmnxDhcpSvrDeclinedAddrHwAddress_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddrHwAddress = _TmnxDhcpSvrDeclinedAddrHwAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 3),
    _TmnxDhcpSvrDeclinedAddrHwAddress_Type()
)
tmnxDhcpSvrDeclinedAddrHwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrHwAddress.setStatus("current")
_TmnxDhcpSvrDeclinedAddrAddedTime_Type = DateAndTime
_TmnxDhcpSvrDeclinedAddrAddedTime_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddrAddedTime = _TmnxDhcpSvrDeclinedAddrAddedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 4),
    _TmnxDhcpSvrDeclinedAddrAddedTime_Type()
)
tmnxDhcpSvrDeclinedAddrAddedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrAddedTime.setStatus("current")
_TmnxDhcpSvrDeclinedAddrOption82_Type = OctetString
_TmnxDhcpSvrDeclinedAddrOption82_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddrOption82 = _TmnxDhcpSvrDeclinedAddrOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 5),
    _TmnxDhcpSvrDeclinedAddrOption82_Type()
)
tmnxDhcpSvrDeclinedAddrOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrOption82.setStatus("current")
_TmnxDhcpSvrDeclinedAddrClientType_Type = TmnxDhcpSvrClientType
_TmnxDhcpSvrDeclinedAddrClientType_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddrClientType = _TmnxDhcpSvrDeclinedAddrClientType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 6),
    _TmnxDhcpSvrDeclinedAddrClientType_Type()
)
tmnxDhcpSvrDeclinedAddrClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrClientType.setStatus("current")
_TmnxDhcpSvrDeclinedAddrUserName_Type = TmnxPppoeUserNameOrEmpty
_TmnxDhcpSvrDeclinedAddrUserName_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddrUserName = _TmnxDhcpSvrDeclinedAddrUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 7),
    _TmnxDhcpSvrDeclinedAddrUserName_Type()
)
tmnxDhcpSvrDeclinedAddrUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrUserName.setStatus("current")


class _TmnxDhcpSvrDeclinedAddrCircId_Type(OctetString):
    """Custom type tmnxDhcpSvrDeclinedAddrCircId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrDeclinedAddrCircId_Type.__name__ = "OctetString"
_TmnxDhcpSvrDeclinedAddrCircId_Object = MibTableColumn
tmnxDhcpSvrDeclinedAddrCircId = _TmnxDhcpSvrDeclinedAddrCircId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 16, 1, 8),
    _TmnxDhcpSvrDeclinedAddrCircId_Type()
)
tmnxDhcpSvrDeclinedAddrCircId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclinedAddrCircId.setStatus("current")
_TmnxDhcpSvrSubnetStatsTable_Object = MibTable
tmnxDhcpSvrSubnetStatsTable = _TmnxDhcpSvrSubnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsTable.setStatus("current")
_TmnxDhcpSvrSubnetStatsEntry_Object = MibTableRow
tmnxDhcpSvrSubnetStatsEntry = _TmnxDhcpSvrSubnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1)
)
tmnxDhcpSvrSubnetStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsEntry.setStatus("current")
_TmnxDhcpSvrSubnetStatsFree_Type = Counter32
_TmnxDhcpSvrSubnetStatsFree_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFree = _TmnxDhcpSvrSubnetStatsFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 1),
    _TmnxDhcpSvrSubnetStatsFree_Type()
)
tmnxDhcpSvrSubnetStatsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFree.setStatus("current")
_TmnxDhcpSvrSubnetStatsOffered_Type = Counter32
_TmnxDhcpSvrSubnetStatsOffered_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsOffered = _TmnxDhcpSvrSubnetStatsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 2),
    _TmnxDhcpSvrSubnetStatsOffered_Type()
)
tmnxDhcpSvrSubnetStatsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsOffered.setStatus("current")
_TmnxDhcpSvrSubnetStatsStable_Type = Counter32
_TmnxDhcpSvrSubnetStatsStable_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsStable = _TmnxDhcpSvrSubnetStatsStable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 3),
    _TmnxDhcpSvrSubnetStatsStable_Type()
)
tmnxDhcpSvrSubnetStatsStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsStable.setStatus("current")
_TmnxDhcpSvrSubnetStatsFRPending_Type = Counter32
_TmnxDhcpSvrSubnetStatsFRPending_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFRPending = _TmnxDhcpSvrSubnetStatsFRPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 4),
    _TmnxDhcpSvrSubnetStatsFRPending_Type()
)
tmnxDhcpSvrSubnetStatsFRPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFRPending.setStatus("current")
_TmnxDhcpSvrSubnetStatsRemPending_Type = Counter32
_TmnxDhcpSvrSubnetStatsRemPending_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsRemPending = _TmnxDhcpSvrSubnetStatsRemPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 5),
    _TmnxDhcpSvrSubnetStatsRemPending_Type()
)
tmnxDhcpSvrSubnetStatsRemPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsRemPending.setStatus("current")
_TmnxDhcpSvrSubnetStatsDeclined_Type = Counter32
_TmnxDhcpSvrSubnetStatsDeclined_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsDeclined = _TmnxDhcpSvrSubnetStatsDeclined_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 6),
    _TmnxDhcpSvrSubnetStatsDeclined_Type()
)
tmnxDhcpSvrSubnetStatsDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsDeclined.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoFree_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoFree_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoFree = _TmnxDhcpSvrSubnetStatsFoFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 7),
    _TmnxDhcpSvrSubnetStatsFoFree_Type()
)
tmnxDhcpSvrSubnetStatsFoFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoFree.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoOffered_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoOffered_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoOffered = _TmnxDhcpSvrSubnetStatsFoOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 8),
    _TmnxDhcpSvrSubnetStatsFoOffered_Type()
)
tmnxDhcpSvrSubnetStatsFoOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoOffered.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoStable_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoStable_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoStable = _TmnxDhcpSvrSubnetStatsFoStable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 9),
    _TmnxDhcpSvrSubnetStatsFoStable_Type()
)
tmnxDhcpSvrSubnetStatsFoStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoStable.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoFRPend_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoFRPend_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoFRPend = _TmnxDhcpSvrSubnetStatsFoFRPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 10),
    _TmnxDhcpSvrSubnetStatsFoFRPend_Type()
)
tmnxDhcpSvrSubnetStatsFoFRPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoFRPend.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoRemPend_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoRemPend_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoRemPend = _TmnxDhcpSvrSubnetStatsFoRemPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 11),
    _TmnxDhcpSvrSubnetStatsFoRemPend_Type()
)
tmnxDhcpSvrSubnetStatsFoRemPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoRemPend.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoDeclined_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoDeclined_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoDeclined = _TmnxDhcpSvrSubnetStatsFoDeclined_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 12),
    _TmnxDhcpSvrSubnetStatsFoDeclined_Type()
)
tmnxDhcpSvrSubnetStatsFoDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoDeclined.setStatus("current")
_TmnxDhcpSvrSubnetStatsProv_Type = Counter32
_TmnxDhcpSvrSubnetStatsProv_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsProv = _TmnxDhcpSvrSubnetStatsProv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 13),
    _TmnxDhcpSvrSubnetStatsProv_Type()
)
tmnxDhcpSvrSubnetStatsProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsProv.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoProv_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoProv_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoProv = _TmnxDhcpSvrSubnetStatsFoProv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 14),
    _TmnxDhcpSvrSubnetStatsFoProv_Type()
)
tmnxDhcpSvrSubnetStatsFoProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoProv.setStatus("current")
_TmnxDhcpSvrSubnetStatsHasExt_Type = TruthValue
_TmnxDhcpSvrSubnetStatsHasExt_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsHasExt = _TmnxDhcpSvrSubnetStatsHasExt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 15),
    _TmnxDhcpSvrSubnetStatsHasExt_Type()
)
tmnxDhcpSvrSubnetStatsHasExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsHasExt.setStatus("current")
_TmnxDhcpSvrSubnetStatsExtResetT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsExtResetT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsExtResetT = _TmnxDhcpSvrSubnetStatsExtResetT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 16),
    _TmnxDhcpSvrSubnetStatsExtResetT_Type()
)
tmnxDhcpSvrSubnetStatsExtResetT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsExtResetT.setStatus("current")
_TmnxDhcpSvrSubnetStatsStableP_Type = Counter32
_TmnxDhcpSvrSubnetStatsStableP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsStableP = _TmnxDhcpSvrSubnetStatsStableP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 17),
    _TmnxDhcpSvrSubnetStatsStableP_Type()
)
tmnxDhcpSvrSubnetStatsStableP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsStableP.setStatus("current")
_TmnxDhcpSvrSubnetStatsStablePT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsStablePT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsStablePT = _TmnxDhcpSvrSubnetStatsStablePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 18),
    _TmnxDhcpSvrSubnetStatsStablePT_Type()
)
tmnxDhcpSvrSubnetStatsStablePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsStablePT.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoStableP_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoStableP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoStableP = _TmnxDhcpSvrSubnetStatsFoStableP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 19),
    _TmnxDhcpSvrSubnetStatsFoStableP_Type()
)
tmnxDhcpSvrSubnetStatsFoStableP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoStableP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoStablePT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFoStablePT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoStablePT = _TmnxDhcpSvrSubnetStatsFoStablePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 20),
    _TmnxDhcpSvrSubnetStatsFoStablePT_Type()
)
tmnxDhcpSvrSubnetStatsFoStablePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoStablePT.setStatus("current")
_TmnxDhcpSvrSubnetStatsUsed_Type = Counter32
_TmnxDhcpSvrSubnetStatsUsed_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsUsed = _TmnxDhcpSvrSubnetStatsUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 21),
    _TmnxDhcpSvrSubnetStatsUsed_Type()
)
tmnxDhcpSvrSubnetStatsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsUsed.setStatus("current")
_TmnxDhcpSvrSubnetStatsUsedP_Type = Counter32
_TmnxDhcpSvrSubnetStatsUsedP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsUsedP = _TmnxDhcpSvrSubnetStatsUsedP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 22),
    _TmnxDhcpSvrSubnetStatsUsedP_Type()
)
tmnxDhcpSvrSubnetStatsUsedP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsUsedP.setStatus("current")
_TmnxDhcpSvrSubnetStatsUsedPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsUsedPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsUsedPT = _TmnxDhcpSvrSubnetStatsUsedPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 23),
    _TmnxDhcpSvrSubnetStatsUsedPT_Type()
)
tmnxDhcpSvrSubnetStatsUsedPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsUsedPT.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoUsed_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoUsed_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoUsed = _TmnxDhcpSvrSubnetStatsFoUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 24),
    _TmnxDhcpSvrSubnetStatsFoUsed_Type()
)
tmnxDhcpSvrSubnetStatsFoUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoUsed.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoUsedP_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoUsedP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoUsedP = _TmnxDhcpSvrSubnetStatsFoUsedP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 25),
    _TmnxDhcpSvrSubnetStatsFoUsedP_Type()
)
tmnxDhcpSvrSubnetStatsFoUsedP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoUsedP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoUsedPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFoUsedPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoUsedPT = _TmnxDhcpSvrSubnetStatsFoUsedPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 26),
    _TmnxDhcpSvrSubnetStatsFoUsedPT_Type()
)
tmnxDhcpSvrSubnetStatsFoUsedPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoUsedPT.setStatus("current")
_TmnxDhcpSvrSubnetStatsFreeP_Type = Counter32
_TmnxDhcpSvrSubnetStatsFreeP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFreeP = _TmnxDhcpSvrSubnetStatsFreeP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 27),
    _TmnxDhcpSvrSubnetStatsFreeP_Type()
)
tmnxDhcpSvrSubnetStatsFreeP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFreeP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFreePT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFreePT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFreePT = _TmnxDhcpSvrSubnetStatsFreePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 28),
    _TmnxDhcpSvrSubnetStatsFreePT_Type()
)
tmnxDhcpSvrSubnetStatsFreePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFreePT.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoFreeP_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoFreeP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoFreeP = _TmnxDhcpSvrSubnetStatsFoFreeP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 29),
    _TmnxDhcpSvrSubnetStatsFoFreeP_Type()
)
tmnxDhcpSvrSubnetStatsFoFreeP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoFreeP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoFreePT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFoFreePT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoFreePT = _TmnxDhcpSvrSubnetStatsFoFreePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 30),
    _TmnxDhcpSvrSubnetStatsFoFreePT_Type()
)
tmnxDhcpSvrSubnetStatsFoFreePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoFreePT.setStatus("current")


class _TmnxDhcpSvrSubnetStatsUsedPct_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsUsedPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsUsedPct_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsUsedPct_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsUsedPct = _TmnxDhcpSvrSubnetStatsUsedPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 31),
    _TmnxDhcpSvrSubnetStatsUsedPct_Type()
)
tmnxDhcpSvrSubnetStatsUsedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsUsedPct.setStatus("current")


class _TmnxDhcpSvrSubnetStatsUsedPctP_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsUsedPctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsUsedPctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsUsedPctP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsUsedPctP = _TmnxDhcpSvrSubnetStatsUsedPctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 32),
    _TmnxDhcpSvrSubnetStatsUsedPctP_Type()
)
tmnxDhcpSvrSubnetStatsUsedPctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsUsedPctP.setStatus("current")
_TmnxDhcpSvrSubnetStatsUsedPctPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsUsedPctPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsUsedPctPT = _TmnxDhcpSvrSubnetStatsUsedPctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 33),
    _TmnxDhcpSvrSubnetStatsUsedPctPT_Type()
)
tmnxDhcpSvrSubnetStatsUsedPctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsUsedPctPT.setStatus("current")


class _TmnxDhcpSvrSubnetStatsFoUsdPct_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsFoUsdPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsFoUsdPct_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsFoUsdPct_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoUsdPct = _TmnxDhcpSvrSubnetStatsFoUsdPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 34),
    _TmnxDhcpSvrSubnetStatsFoUsdPct_Type()
)
tmnxDhcpSvrSubnetStatsFoUsdPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoUsdPct.setStatus("current")


class _TmnxDhcpSvrSubnetStatsFoUsdPctP_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsFoUsdPctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsFoUsdPctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsFoUsdPctP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoUsdPctP = _TmnxDhcpSvrSubnetStatsFoUsdPctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 35),
    _TmnxDhcpSvrSubnetStatsFoUsdPctP_Type()
)
tmnxDhcpSvrSubnetStatsFoUsdPctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoUsdPctP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoUsdPctPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFoUsdPctPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoUsdPctPT = _TmnxDhcpSvrSubnetStatsFoUsdPctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 36),
    _TmnxDhcpSvrSubnetStatsFoUsdPctPT_Type()
)
tmnxDhcpSvrSubnetStatsFoUsdPctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoUsdPctPT.setStatus("current")


class _TmnxDhcpSvrSubnetStatsFreePct_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsFreePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsFreePct_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsFreePct_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFreePct = _TmnxDhcpSvrSubnetStatsFreePct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 37),
    _TmnxDhcpSvrSubnetStatsFreePct_Type()
)
tmnxDhcpSvrSubnetStatsFreePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFreePct.setStatus("current")


class _TmnxDhcpSvrSubnetStatsFreePctP_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsFreePctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsFreePctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsFreePctP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFreePctP = _TmnxDhcpSvrSubnetStatsFreePctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 38),
    _TmnxDhcpSvrSubnetStatsFreePctP_Type()
)
tmnxDhcpSvrSubnetStatsFreePctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFreePctP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFreePctPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFreePctPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFreePctPT = _TmnxDhcpSvrSubnetStatsFreePctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 39),
    _TmnxDhcpSvrSubnetStatsFreePctPT_Type()
)
tmnxDhcpSvrSubnetStatsFreePctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFreePctPT.setStatus("current")


class _TmnxDhcpSvrSubnetStatsFoFrePct_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsFoFrePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsFoFrePct_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsFoFrePct_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoFrePct = _TmnxDhcpSvrSubnetStatsFoFrePct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 40),
    _TmnxDhcpSvrSubnetStatsFoFrePct_Type()
)
tmnxDhcpSvrSubnetStatsFoFrePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoFrePct.setStatus("current")


class _TmnxDhcpSvrSubnetStatsFoFrePctP_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStatsFoFrePctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStatsFoFrePctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStatsFoFrePctP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoFrePctP = _TmnxDhcpSvrSubnetStatsFoFrePctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 41),
    _TmnxDhcpSvrSubnetStatsFoFrePctP_Type()
)
tmnxDhcpSvrSubnetStatsFoFrePctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoFrePctP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoFrePctPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFoFrePctPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoFrePctPT = _TmnxDhcpSvrSubnetStatsFoFrePctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 42),
    _TmnxDhcpSvrSubnetStatsFoFrePctPT_Type()
)
tmnxDhcpSvrSubnetStatsFoFrePctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoFrePctPT.setStatus("current")
_TmnxDhcpSvrSubnetStatsOfferP_Type = Counter32
_TmnxDhcpSvrSubnetStatsOfferP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsOfferP = _TmnxDhcpSvrSubnetStatsOfferP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 43),
    _TmnxDhcpSvrSubnetStatsOfferP_Type()
)
tmnxDhcpSvrSubnetStatsOfferP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsOfferP.setStatus("current")
_TmnxDhcpSvrSubnetStatsOfferPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsOfferPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsOfferPT = _TmnxDhcpSvrSubnetStatsOfferPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 44),
    _TmnxDhcpSvrSubnetStatsOfferPT_Type()
)
tmnxDhcpSvrSubnetStatsOfferPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsOfferPT.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoOfferP_Type = Counter32
_TmnxDhcpSvrSubnetStatsFoOfferP_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoOfferP = _TmnxDhcpSvrSubnetStatsFoOfferP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 45),
    _TmnxDhcpSvrSubnetStatsFoOfferP_Type()
)
tmnxDhcpSvrSubnetStatsFoOfferP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoOfferP.setStatus("current")
_TmnxDhcpSvrSubnetStatsFoOfferPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStatsFoOfferPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStatsFoOfferPT = _TmnxDhcpSvrSubnetStatsFoOfferPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 17, 1, 46),
    _TmnxDhcpSvrSubnetStatsFoOfferPT_Type()
)
tmnxDhcpSvrSubnetStatsFoOfferPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStatsFoOfferPT.setStatus("current")
_TmnxDhcpsFailoverObjs_ObjectIdentity = ObjectIdentity
tmnxDhcpsFailoverObjs = _TmnxDhcpsFailoverObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18)
)
_TmnxDhcpsFoTableLastChanged_Type = TimeStamp
_TmnxDhcpsFoTableLastChanged_Object = MibScalar
tmnxDhcpsFoTableLastChanged = _TmnxDhcpsFoTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 1),
    _TmnxDhcpsFoTableLastChanged_Type()
)
tmnxDhcpsFoTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoTableLastChanged.setStatus("current")
_TmnxDhcpsFoTable_Object = MibTable
tmnxDhcpsFoTable = _TmnxDhcpsFoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2)
)
if mibBuilder.loadTexts:
    tmnxDhcpsFoTable.setStatus("current")
_TmnxDhcpsFoEntry_Object = MibTableRow
tmnxDhcpsFoEntry = _TmnxDhcpsFoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxDhcpsFoEntry.setStatus("current")
_TmnxDhcpsFoLastChanged_Type = TimeStamp
_TmnxDhcpsFoLastChanged_Object = MibTableColumn
tmnxDhcpsFoLastChanged = _TmnxDhcpsFoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 1),
    _TmnxDhcpsFoLastChanged_Type()
)
tmnxDhcpsFoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoLastChanged.setStatus("current")


class _TmnxDhcpsFoAdminState_Type(TmnxAdminState):
    """Custom type tmnxDhcpsFoAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxDhcpsFoAdminState_Type.__name__ = "TmnxAdminState"
_TmnxDhcpsFoAdminState_Object = MibTableColumn
tmnxDhcpsFoAdminState = _TmnxDhcpsFoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 2),
    _TmnxDhcpsFoAdminState_Type()
)
tmnxDhcpsFoAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsFoAdminState.setStatus("current")


class _TmnxDhcpsFoMaxClientLeadTime_Type(Unsigned32):
    """Custom type tmnxDhcpsFoMaxClientLeadTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86399),
    )


_TmnxDhcpsFoMaxClientLeadTime_Type.__name__ = "Unsigned32"
_TmnxDhcpsFoMaxClientLeadTime_Object = MibTableColumn
tmnxDhcpsFoMaxClientLeadTime = _TmnxDhcpsFoMaxClientLeadTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 3),
    _TmnxDhcpsFoMaxClientLeadTime_Type()
)
tmnxDhcpsFoMaxClientLeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsFoMaxClientLeadTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsFoMaxClientLeadTime.setUnits("seconds")


class _TmnxDhcpsFoOperMaxClientLeadTime_Type(Unsigned32):
    """Custom type tmnxDhcpsFoOperMaxClientLeadTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86399),
    )


_TmnxDhcpsFoOperMaxClientLeadTime_Type.__name__ = "Unsigned32"
_TmnxDhcpsFoOperMaxClientLeadTime_Object = MibTableColumn
tmnxDhcpsFoOperMaxClientLeadTime = _TmnxDhcpsFoOperMaxClientLeadTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 4),
    _TmnxDhcpsFoOperMaxClientLeadTime_Type()
)
tmnxDhcpsFoOperMaxClientLeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoOperMaxClientLeadTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsFoOperMaxClientLeadTime.setUnits("seconds")


class _TmnxDhcpsFoStartupWaitTime_Type(Unsigned32):
    """Custom type tmnxDhcpsFoStartupWaitTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TmnxDhcpsFoStartupWaitTime_Type.__name__ = "Unsigned32"
_TmnxDhcpsFoStartupWaitTime_Object = MibTableColumn
tmnxDhcpsFoStartupWaitTime = _TmnxDhcpsFoStartupWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 5),
    _TmnxDhcpsFoStartupWaitTime_Type()
)
tmnxDhcpsFoStartupWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStartupWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStartupWaitTime.setUnits("seconds")


class _TmnxDhcpsFoPartnerDownDelay_Type(Unsigned32):
    """Custom type tmnxDhcpsFoPartnerDownDelay based on Unsigned32"""
    defaultValue = 86399

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_TmnxDhcpsFoPartnerDownDelay_Type.__name__ = "Unsigned32"
_TmnxDhcpsFoPartnerDownDelay_Object = MibTableColumn
tmnxDhcpsFoPartnerDownDelay = _TmnxDhcpsFoPartnerDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 6),
    _TmnxDhcpsFoPartnerDownDelay_Type()
)
tmnxDhcpsFoPartnerDownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsFoPartnerDownDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsFoPartnerDownDelay.setUnits("seconds")
_TmnxDhcpsFoState_Type = TmnxDhcpsFoState
_TmnxDhcpsFoState_Object = MibTableColumn
tmnxDhcpsFoState = _TmnxDhcpsFoState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 7),
    _TmnxDhcpsFoState_Type()
)
tmnxDhcpsFoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoState.setStatus("current")
_TmnxDhcpsFoTimeLeft_Type = Integer32
_TmnxDhcpsFoTimeLeft_Object = MibTableColumn
tmnxDhcpsFoTimeLeft = _TmnxDhcpsFoTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 8),
    _TmnxDhcpsFoTimeLeft_Type()
)
tmnxDhcpsFoTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsFoTimeLeft.setUnits("seconds")


class _TmnxDhcpsFoIgnoreMclt_Type(TruthValue):
    """Custom type tmnxDhcpsFoIgnoreMclt based on TruthValue"""
    defaultValue = 2


_TmnxDhcpsFoIgnoreMclt_Type.__name__ = "TruthValue"
_TmnxDhcpsFoIgnoreMclt_Object = MibTableColumn
tmnxDhcpsFoIgnoreMclt = _TmnxDhcpsFoIgnoreMclt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 2, 1, 10),
    _TmnxDhcpsFoIgnoreMclt_Type()
)
tmnxDhcpsFoIgnoreMclt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsFoIgnoreMclt.setStatus("current")
_TmnxDhcpsFoStatsTable_Object = MibTable
tmnxDhcpsFoStatsTable = _TmnxDhcpsFoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3)
)
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsTable.setStatus("current")
_TmnxDhcpsFoStatsEntry_Object = MibTableRow
tmnxDhcpsFoStatsEntry = _TmnxDhcpsFoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsEntry.setStatus("current")
_TmnxDhcpsFoStatsLeaseNotFound_Type = Counter32
_TmnxDhcpsFoStatsLeaseNotFound_Object = MibTableColumn
tmnxDhcpsFoStatsLeaseNotFound = _TmnxDhcpsFoStatsLeaseNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 1),
    _TmnxDhcpsFoStatsLeaseNotFound_Type()
)
tmnxDhcpsFoStatsLeaseNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsLeaseNotFound.setStatus("current")
_TmnxDhcpsFoStatsDropInvalidPkts_Type = Counter32
_TmnxDhcpsFoStatsDropInvalidPkts_Object = MibTableColumn
tmnxDhcpsFoStatsDropInvalidPkts = _TmnxDhcpsFoStatsDropInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 2),
    _TmnxDhcpsFoStatsDropInvalidPkts_Type()
)
tmnxDhcpsFoStatsDropInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsDropInvalidPkts.setStatus("current")
_TmnxDhcpsFoStatsFoShutdown_Type = Counter32
_TmnxDhcpsFoStatsFoShutdown_Object = MibTableColumn
tmnxDhcpsFoStatsFoShutdown = _TmnxDhcpsFoStatsFoShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 3),
    _TmnxDhcpsFoStatsFoShutdown_Type()
)
tmnxDhcpsFoStatsFoShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsFoShutdown.setStatus("current")
_TmnxDhcpsFoStatsExpired_Type = Counter32
_TmnxDhcpsFoStatsExpired_Object = MibTableColumn
tmnxDhcpsFoStatsExpired = _TmnxDhcpsFoStatsExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 4),
    _TmnxDhcpsFoStatsExpired_Type()
)
tmnxDhcpsFoStatsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsExpired.setStatus("current")
_TmnxDhcpsFoStatsMaxReached_Type = Counter32
_TmnxDhcpsFoStatsMaxReached_Object = MibTableColumn
tmnxDhcpsFoStatsMaxReached = _TmnxDhcpsFoStatsMaxReached_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 5),
    _TmnxDhcpsFoStatsMaxReached_Type()
)
tmnxDhcpsFoStatsMaxReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsMaxReached.setStatus("current")
_TmnxDhcpsFoStatsSubnetNotFound_Type = Counter32
_TmnxDhcpsFoStatsSubnetNotFound_Object = MibTableColumn
tmnxDhcpsFoStatsSubnetNotFound = _TmnxDhcpsFoStatsSubnetNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 6),
    _TmnxDhcpsFoStatsSubnetNotFound_Type()
)
tmnxDhcpsFoStatsSubnetNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsSubnetNotFound.setStatus("current")
_TmnxDhcpsFoStatsRangeNotFound_Type = Counter32
_TmnxDhcpsFoStatsRangeNotFound_Object = MibTableColumn
tmnxDhcpsFoStatsRangeNotFound = _TmnxDhcpsFoStatsRangeNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 7),
    _TmnxDhcpsFoStatsRangeNotFound_Type()
)
tmnxDhcpsFoStatsRangeNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsRangeNotFound.setStatus("current")
_TmnxDhcpsFoStatsHostConflict_Type = Counter32
_TmnxDhcpsFoStatsHostConflict_Object = MibTableColumn
tmnxDhcpsFoStatsHostConflict = _TmnxDhcpsFoStatsHostConflict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 8),
    _TmnxDhcpsFoStatsHostConflict_Type()
)
tmnxDhcpsFoStatsHostConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsHostConflict.setStatus("current")
_TmnxDhcpsFoStatsAddressConflict_Type = Counter32
_TmnxDhcpsFoStatsAddressConflict_Object = MibTableColumn
tmnxDhcpsFoStatsAddressConflict = _TmnxDhcpsFoStatsAddressConflict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 9),
    _TmnxDhcpsFoStatsAddressConflict_Type()
)
tmnxDhcpsFoStatsAddressConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsAddressConflict.setStatus("current")
_TmnxDhcpsFoStatsPeerConflict_Type = Counter32
_TmnxDhcpsFoStatsPeerConflict_Object = MibTableColumn
tmnxDhcpsFoStatsPeerConflict = _TmnxDhcpsFoStatsPeerConflict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 10),
    _TmnxDhcpsFoStatsPeerConflict_Type()
)
tmnxDhcpsFoStatsPeerConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsPeerConflict.setStatus("current")
_TmnxDhcpsFoStatsPersistCongest_Type = Counter32
_TmnxDhcpsFoStatsPersistCongest_Object = MibTableColumn
tmnxDhcpsFoStatsPersistCongest = _TmnxDhcpsFoStatsPersistCongest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 3, 1, 11),
    _TmnxDhcpsFoStatsPersistCongest_Type()
)
tmnxDhcpsFoStatsPersistCongest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoStatsPersistCongest.setStatus("current")
_TmnxDhcpsFoAction_ObjectIdentity = ObjectIdentity
tmnxDhcpsFoAction = _TmnxDhcpsFoAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4)
)
_TmnxDhcpsFoActionVRtrId_Type = TmnxVRtrIDOrZero
_TmnxDhcpsFoActionVRtrId_Object = MibScalar
tmnxDhcpsFoActionVRtrId = _TmnxDhcpsFoActionVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 1),
    _TmnxDhcpsFoActionVRtrId_Type()
)
tmnxDhcpsFoActionVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionVRtrId.setStatus("current")
_TmnxDhcpsFoActionServerName_Type = TNamedItemOrEmpty
_TmnxDhcpsFoActionServerName_Object = MibScalar
tmnxDhcpsFoActionServerName = _TmnxDhcpsFoActionServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 2),
    _TmnxDhcpsFoActionServerName_Type()
)
tmnxDhcpsFoActionServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionServerName.setStatus("current")
_TmnxDhcpsFoActionType_Type = TmnxDhcpsFoActionType
_TmnxDhcpsFoActionType_Object = MibScalar
tmnxDhcpsFoActionType = _TmnxDhcpsFoActionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 3),
    _TmnxDhcpsFoActionType_Type()
)
tmnxDhcpsFoActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionType.setStatus("current")
_TmnxDhcpsFoActionGo_Type = TmnxActionType
_TmnxDhcpsFoActionGo_Object = MibScalar
tmnxDhcpsFoActionGo = _TmnxDhcpsFoActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 4),
    _TmnxDhcpsFoActionGo_Type()
)
tmnxDhcpsFoActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionGo.setStatus("current")
_TmnxDhcpsFoActionSuccessful_Type = TruthValue
_TmnxDhcpsFoActionSuccessful_Object = MibScalar
tmnxDhcpsFoActionSuccessful = _TmnxDhcpsFoActionSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 5),
    _TmnxDhcpsFoActionSuccessful_Type()
)
tmnxDhcpsFoActionSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionSuccessful.setStatus("current")


class _TmnxDhcpsFoActionErrorMsg_Type(DisplayString):
    """Custom type tmnxDhcpsFoActionErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpsFoActionErrorMsg_Type.__name__ = "DisplayString"
_TmnxDhcpsFoActionErrorMsg_Object = MibScalar
tmnxDhcpsFoActionErrorMsg = _TmnxDhcpsFoActionErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 6),
    _TmnxDhcpsFoActionErrorMsg_Type()
)
tmnxDhcpsFoActionErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionErrorMsg.setStatus("current")
_TmnxDhcpsFoActionTime_Type = TimeStamp
_TmnxDhcpsFoActionTime_Object = MibScalar
tmnxDhcpsFoActionTime = _TmnxDhcpsFoActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 7),
    _TmnxDhcpsFoActionTime_Type()
)
tmnxDhcpsFoActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionTime.setStatus("current")
_TmnxDhcpsFoActionPoolName_Type = TNamedItemOrEmpty
_TmnxDhcpsFoActionPoolName_Object = MibScalar
tmnxDhcpsFoActionPoolName = _TmnxDhcpsFoActionPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 4, 8),
    _TmnxDhcpsFoActionPoolName_Type()
)
tmnxDhcpsFoActionPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDhcpsFoActionPoolName.setStatus("current")
_TmnxDhcpsPoolFoTableLastChanged_Type = TimeStamp
_TmnxDhcpsPoolFoTableLastChanged_Object = MibScalar
tmnxDhcpsPoolFoTableLastChanged = _TmnxDhcpsPoolFoTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 5),
    _TmnxDhcpsPoolFoTableLastChanged_Type()
)
tmnxDhcpsPoolFoTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoTableLastChanged.setStatus("current")
_TmnxDhcpsPoolFoTable_Object = MibTable
tmnxDhcpsPoolFoTable = _TmnxDhcpsPoolFoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6)
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoTable.setStatus("current")
_TmnxDhcpsPoolFoEntry_Object = MibTableRow
tmnxDhcpsPoolFoEntry = _TmnxDhcpsPoolFoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoEntry.setStatus("current")
_TmnxDhcpsPoolFoLastChanged_Type = TimeStamp
_TmnxDhcpsPoolFoLastChanged_Object = MibTableColumn
tmnxDhcpsPoolFoLastChanged = _TmnxDhcpsPoolFoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 1),
    _TmnxDhcpsPoolFoLastChanged_Type()
)
tmnxDhcpsPoolFoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoLastChanged.setStatus("current")


class _TmnxDhcpsPoolFoAdminState_Type(TmnxAdminState):
    """Custom type tmnxDhcpsPoolFoAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxDhcpsPoolFoAdminState_Type.__name__ = "TmnxAdminState"
_TmnxDhcpsPoolFoAdminState_Object = MibTableColumn
tmnxDhcpsPoolFoAdminState = _TmnxDhcpsPoolFoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 2),
    _TmnxDhcpsPoolFoAdminState_Type()
)
tmnxDhcpsPoolFoAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoAdminState.setStatus("current")


class _TmnxDhcpsPoolFoMCLT_Type(Unsigned32):
    """Custom type tmnxDhcpsPoolFoMCLT based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86399),
    )


_TmnxDhcpsPoolFoMCLT_Type.__name__ = "Unsigned32"
_TmnxDhcpsPoolFoMCLT_Object = MibTableColumn
tmnxDhcpsPoolFoMCLT = _TmnxDhcpsPoolFoMCLT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 3),
    _TmnxDhcpsPoolFoMCLT_Type()
)
tmnxDhcpsPoolFoMCLT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoMCLT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoMCLT.setUnits("seconds")


class _TmnxDhcpsPoolFoOperMCLT_Type(Unsigned32):
    """Custom type tmnxDhcpsPoolFoOperMCLT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86399),
    )


_TmnxDhcpsPoolFoOperMCLT_Type.__name__ = "Unsigned32"
_TmnxDhcpsPoolFoOperMCLT_Object = MibTableColumn
tmnxDhcpsPoolFoOperMCLT = _TmnxDhcpsPoolFoOperMCLT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 4),
    _TmnxDhcpsPoolFoOperMCLT_Type()
)
tmnxDhcpsPoolFoOperMCLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoOperMCLT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoOperMCLT.setUnits("seconds")


class _TmnxDhcpsPoolFoStartupWaitTime_Type(Unsigned32):
    """Custom type tmnxDhcpsPoolFoStartupWaitTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_TmnxDhcpsPoolFoStartupWaitTime_Type.__name__ = "Unsigned32"
_TmnxDhcpsPoolFoStartupWaitTime_Object = MibTableColumn
tmnxDhcpsPoolFoStartupWaitTime = _TmnxDhcpsPoolFoStartupWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 5),
    _TmnxDhcpsPoolFoStartupWaitTime_Type()
)
tmnxDhcpsPoolFoStartupWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStartupWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStartupWaitTime.setUnits("seconds")


class _TmnxDhcpsPoolFoPartnerDownDelay_Type(Unsigned32):
    """Custom type tmnxDhcpsPoolFoPartnerDownDelay based on Unsigned32"""
    defaultValue = 86399

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_TmnxDhcpsPoolFoPartnerDownDelay_Type.__name__ = "Unsigned32"
_TmnxDhcpsPoolFoPartnerDownDelay_Object = MibTableColumn
tmnxDhcpsPoolFoPartnerDownDelay = _TmnxDhcpsPoolFoPartnerDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 6),
    _TmnxDhcpsPoolFoPartnerDownDelay_Type()
)
tmnxDhcpsPoolFoPartnerDownDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoPartnerDownDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoPartnerDownDelay.setUnits("seconds")
_TmnxDhcpsPoolFoState_Type = TmnxDhcpsFoState
_TmnxDhcpsPoolFoState_Object = MibTableColumn
tmnxDhcpsPoolFoState = _TmnxDhcpsPoolFoState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 7),
    _TmnxDhcpsPoolFoState_Type()
)
tmnxDhcpsPoolFoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoState.setStatus("current")
_TmnxDhcpsPoolFoTimeLeft_Type = Integer32
_TmnxDhcpsPoolFoTimeLeft_Object = MibTableColumn
tmnxDhcpsPoolFoTimeLeft = _TmnxDhcpsPoolFoTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 8),
    _TmnxDhcpsPoolFoTimeLeft_Type()
)
tmnxDhcpsPoolFoTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoTimeLeft.setUnits("seconds")


class _TmnxDhcpsPoolFoIgnoreMclt_Type(TruthValue):
    """Custom type tmnxDhcpsPoolFoIgnoreMclt based on TruthValue"""
    defaultValue = 2


_TmnxDhcpsPoolFoIgnoreMclt_Type.__name__ = "TruthValue"
_TmnxDhcpsPoolFoIgnoreMclt_Object = MibTableColumn
tmnxDhcpsPoolFoIgnoreMclt = _TmnxDhcpsPoolFoIgnoreMclt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 6, 1, 10),
    _TmnxDhcpsPoolFoIgnoreMclt_Type()
)
tmnxDhcpsPoolFoIgnoreMclt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoIgnoreMclt.setStatus("current")
_TmnxDhcpsPoolFoStatsTable_Object = MibTable
tmnxDhcpsPoolFoStatsTable = _TmnxDhcpsPoolFoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7)
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsTable.setStatus("current")
_TmnxDhcpsPoolFoStatsEntry_Object = MibTableRow
tmnxDhcpsPoolFoStatsEntry = _TmnxDhcpsPoolFoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsEntry.setStatus("current")
_TmnxDhcpsPoolFoStatsLeaseNFound_Type = Counter32
_TmnxDhcpsPoolFoStatsLeaseNFound_Object = MibTableColumn
tmnxDhcpsPoolFoStatsLeaseNFound = _TmnxDhcpsPoolFoStatsLeaseNFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 1),
    _TmnxDhcpsPoolFoStatsLeaseNFound_Type()
)
tmnxDhcpsPoolFoStatsLeaseNFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsLeaseNFound.setStatus("current")
_TmnxDhcpsPoolFoStatsDropInvPkts_Type = Counter32
_TmnxDhcpsPoolFoStatsDropInvPkts_Object = MibTableColumn
tmnxDhcpsPoolFoStatsDropInvPkts = _TmnxDhcpsPoolFoStatsDropInvPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 2),
    _TmnxDhcpsPoolFoStatsDropInvPkts_Type()
)
tmnxDhcpsPoolFoStatsDropInvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsDropInvPkts.setStatus("current")
_TmnxDhcpsPoolFoStatsFoShutdown_Type = Counter32
_TmnxDhcpsPoolFoStatsFoShutdown_Object = MibTableColumn
tmnxDhcpsPoolFoStatsFoShutdown = _TmnxDhcpsPoolFoStatsFoShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 3),
    _TmnxDhcpsPoolFoStatsFoShutdown_Type()
)
tmnxDhcpsPoolFoStatsFoShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsFoShutdown.setStatus("current")
_TmnxDhcpsPoolFoStatsExpired_Type = Counter32
_TmnxDhcpsPoolFoStatsExpired_Object = MibTableColumn
tmnxDhcpsPoolFoStatsExpired = _TmnxDhcpsPoolFoStatsExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 4),
    _TmnxDhcpsPoolFoStatsExpired_Type()
)
tmnxDhcpsPoolFoStatsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsExpired.setStatus("current")
_TmnxDhcpsPoolFoStatsMaxReached_Type = Counter32
_TmnxDhcpsPoolFoStatsMaxReached_Object = MibTableColumn
tmnxDhcpsPoolFoStatsMaxReached = _TmnxDhcpsPoolFoStatsMaxReached_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 5),
    _TmnxDhcpsPoolFoStatsMaxReached_Type()
)
tmnxDhcpsPoolFoStatsMaxReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsMaxReached.setStatus("current")
_TmnxDhcpsPoolFoStatsSubnetNFound_Type = Counter32
_TmnxDhcpsPoolFoStatsSubnetNFound_Object = MibTableColumn
tmnxDhcpsPoolFoStatsSubnetNFound = _TmnxDhcpsPoolFoStatsSubnetNFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 6),
    _TmnxDhcpsPoolFoStatsSubnetNFound_Type()
)
tmnxDhcpsPoolFoStatsSubnetNFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsSubnetNFound.setStatus("current")
_TmnxDhcpsPoolFoStatsRangeNFound_Type = Counter32
_TmnxDhcpsPoolFoStatsRangeNFound_Object = MibTableColumn
tmnxDhcpsPoolFoStatsRangeNFound = _TmnxDhcpsPoolFoStatsRangeNFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 7),
    _TmnxDhcpsPoolFoStatsRangeNFound_Type()
)
tmnxDhcpsPoolFoStatsRangeNFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsRangeNFound.setStatus("current")
_TmnxDhcpsPoolFoStatsHostConflict_Type = Counter32
_TmnxDhcpsPoolFoStatsHostConflict_Object = MibTableColumn
tmnxDhcpsPoolFoStatsHostConflict = _TmnxDhcpsPoolFoStatsHostConflict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 8),
    _TmnxDhcpsPoolFoStatsHostConflict_Type()
)
tmnxDhcpsPoolFoStatsHostConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsHostConflict.setStatus("current")
_TmnxDhcpsPoolFoStatsAddrConflict_Type = Counter32
_TmnxDhcpsPoolFoStatsAddrConflict_Object = MibTableColumn
tmnxDhcpsPoolFoStatsAddrConflict = _TmnxDhcpsPoolFoStatsAddrConflict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 9),
    _TmnxDhcpsPoolFoStatsAddrConflict_Type()
)
tmnxDhcpsPoolFoStatsAddrConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsAddrConflict.setStatus("current")
_TmnxDhcpsPoolFoStatsPeerConflict_Type = Counter32
_TmnxDhcpsPoolFoStatsPeerConflict_Object = MibTableColumn
tmnxDhcpsPoolFoStatsPeerConflict = _TmnxDhcpsPoolFoStatsPeerConflict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 10),
    _TmnxDhcpsPoolFoStatsPeerConflict_Type()
)
tmnxDhcpsPoolFoStatsPeerConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsPeerConflict.setStatus("current")
_TmnxDhcpsPoolFoStatsPersistCong_Type = Counter32
_TmnxDhcpsPoolFoStatsPersistCong_Object = MibTableColumn
tmnxDhcpsPoolFoStatsPersistCong = _TmnxDhcpsPoolFoStatsPersistCong_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 18, 7, 1, 11),
    _TmnxDhcpsPoolFoStatsPersistCong_Type()
)
tmnxDhcpsPoolFoStatsPersistCong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStatsPersistCong.setStatus("current")
_TmnxDhcpSvrFreeAddrTable_Object = MibTable
tmnxDhcpSvrFreeAddrTable = _TmnxDhcpSvrFreeAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrFreeAddrTable.setStatus("current")
_TmnxDhcpSvrFreeAddrEntry_Object = MibTableRow
tmnxDhcpSvrFreeAddrEntry = _TmnxDhcpSvrFreeAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 19, 1)
)
tmnxDhcpSvrFreeAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFreeAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFreeAddress"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrFreeAddrEntry.setStatus("current")
_TmnxDhcpSvrFreeAddrType_Type = InetAddressType
_TmnxDhcpSvrFreeAddrType_Object = MibTableColumn
tmnxDhcpSvrFreeAddrType = _TmnxDhcpSvrFreeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 19, 1, 1),
    _TmnxDhcpSvrFreeAddrType_Type()
)
tmnxDhcpSvrFreeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrFreeAddrType.setStatus("current")


class _TmnxDhcpSvrFreeAddress_Type(InetAddress):
    """Custom type tmnxDhcpSvrFreeAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrFreeAddress_Type.__name__ = "InetAddress"
_TmnxDhcpSvrFreeAddress_Object = MibTableColumn
tmnxDhcpSvrFreeAddress = _TmnxDhcpSvrFreeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 19, 1, 2),
    _TmnxDhcpSvrFreeAddress_Type()
)
tmnxDhcpSvrFreeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDhcpSvrFreeAddress.setStatus("current")
_TmnxDhcpSvrFreeAddrFailCtrl_Type = TmnxDhcpSvrFailCtrlType
_TmnxDhcpSvrFreeAddrFailCtrl_Object = MibTableColumn
tmnxDhcpSvrFreeAddrFailCtrl = _TmnxDhcpSvrFreeAddrFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 19, 1, 3),
    _TmnxDhcpSvrFreeAddrFailCtrl_Type()
)
tmnxDhcpSvrFreeAddrFailCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrFreeAddrFailCtrl.setStatus("current")
_TmnxDhcpSvrActionTable_Object = MibTable
tmnxDhcpSvrActionTable = _TmnxDhcpSvrActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrActionTable.setStatus("current")
_TmnxDhcpSvrActionEntry_Object = MibTableRow
tmnxDhcpSvrActionEntry = _TmnxDhcpSvrActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 20, 1)
)
tmnxDhcpSvrActionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrActionEntry.setStatus("current")
_TmnxDhcpSvrActForceRenewAddrType_Type = InetAddressType
_TmnxDhcpSvrActForceRenewAddrType_Object = MibTableColumn
tmnxDhcpSvrActForceRenewAddrType = _TmnxDhcpSvrActForceRenewAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 20, 1, 1),
    _TmnxDhcpSvrActForceRenewAddrType_Type()
)
tmnxDhcpSvrActForceRenewAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDhcpSvrActForceRenewAddrType.setStatus("current")


class _TmnxDhcpSvrActForceRenewAddr_Type(InetAddress):
    """Custom type tmnxDhcpSvrActForceRenewAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrActForceRenewAddr_Type.__name__ = "InetAddress"
_TmnxDhcpSvrActForceRenewAddr_Object = MibTableColumn
tmnxDhcpSvrActForceRenewAddr = _TmnxDhcpSvrActForceRenewAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 20, 1, 2),
    _TmnxDhcpSvrActForceRenewAddr_Type()
)
tmnxDhcpSvrActForceRenewAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDhcpSvrActForceRenewAddr.setStatus("current")
_TmnxDhcpSvrNumLeases_Type = Gauge32
_TmnxDhcpSvrNumLeases_Object = MibScalar
tmnxDhcpSvrNumLeases = _TmnxDhcpSvrNumLeases_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 21),
    _TmnxDhcpSvrNumLeases_Type()
)
tmnxDhcpSvrNumLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNumLeases.setStatus("current")
_TmnxDhcpSvrMaxLeases_Type = Unsigned32
_TmnxDhcpSvrMaxLeases_Object = MibScalar
tmnxDhcpSvrMaxLeases = _TmnxDhcpSvrMaxLeases_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 22),
    _TmnxDhcpSvrMaxLeases_Type()
)
tmnxDhcpSvrMaxLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrMaxLeases.setStatus("current")
_TmnxDhcpServerStats6Table_Object = MibTable
tmnxDhcpServerStats6Table = _TmnxDhcpServerStats6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23)
)
if mibBuilder.loadTexts:
    tmnxDhcpServerStats6Table.setStatus("current")
_TmnxDhcpServerStats6Entry_Object = MibTableRow
tmnxDhcpServerStats6Entry = _TmnxDhcpServerStats6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1)
)
tmnxDhcpServerStats6Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
)
if mibBuilder.loadTexts:
    tmnxDhcpServerStats6Entry.setStatus("current")
_TmnxDhcpSvrStats6RxSolicits_Type = Counter64
_TmnxDhcpSvrStats6RxSolicits_Object = MibTableColumn
tmnxDhcpSvrStats6RxSolicits = _TmnxDhcpSvrStats6RxSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 1),
    _TmnxDhcpSvrStats6RxSolicits_Type()
)
tmnxDhcpSvrStats6RxSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxSolicits.setStatus("current")
_TmnxDhcpSvrStats6TxAdvertises_Type = Counter64
_TmnxDhcpSvrStats6TxAdvertises_Object = MibTableColumn
tmnxDhcpSvrStats6TxAdvertises = _TmnxDhcpSvrStats6TxAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 2),
    _TmnxDhcpSvrStats6TxAdvertises_Type()
)
tmnxDhcpSvrStats6TxAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6TxAdvertises.setStatus("current")
_TmnxDhcpSvrStats6RxRequests_Type = Counter64
_TmnxDhcpSvrStats6RxRequests_Object = MibTableColumn
tmnxDhcpSvrStats6RxRequests = _TmnxDhcpSvrStats6RxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 3),
    _TmnxDhcpSvrStats6RxRequests_Type()
)
tmnxDhcpSvrStats6RxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxRequests.setStatus("current")
_TmnxDhcpSvrStats6RxConfirms_Type = Counter64
_TmnxDhcpSvrStats6RxConfirms_Object = MibTableColumn
tmnxDhcpSvrStats6RxConfirms = _TmnxDhcpSvrStats6RxConfirms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 4),
    _TmnxDhcpSvrStats6RxConfirms_Type()
)
tmnxDhcpSvrStats6RxConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxConfirms.setStatus("current")
_TmnxDhcpSvrStats6RxRenews_Type = Counter64
_TmnxDhcpSvrStats6RxRenews_Object = MibTableColumn
tmnxDhcpSvrStats6RxRenews = _TmnxDhcpSvrStats6RxRenews_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 5),
    _TmnxDhcpSvrStats6RxRenews_Type()
)
tmnxDhcpSvrStats6RxRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxRenews.setStatus("current")
_TmnxDhcpSvrStats6RxRebinds_Type = Counter64
_TmnxDhcpSvrStats6RxRebinds_Object = MibTableColumn
tmnxDhcpSvrStats6RxRebinds = _TmnxDhcpSvrStats6RxRebinds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 6),
    _TmnxDhcpSvrStats6RxRebinds_Type()
)
tmnxDhcpSvrStats6RxRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxRebinds.setStatus("current")
_TmnxDhcpSvrStats6RxDeclines_Type = Counter64
_TmnxDhcpSvrStats6RxDeclines_Object = MibTableColumn
tmnxDhcpSvrStats6RxDeclines = _TmnxDhcpSvrStats6RxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 7),
    _TmnxDhcpSvrStats6RxDeclines_Type()
)
tmnxDhcpSvrStats6RxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxDeclines.setStatus("current")
_TmnxDhcpSvrStats6RxReleases_Type = Counter64
_TmnxDhcpSvrStats6RxReleases_Object = MibTableColumn
tmnxDhcpSvrStats6RxReleases = _TmnxDhcpSvrStats6RxReleases_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 8),
    _TmnxDhcpSvrStats6RxReleases_Type()
)
tmnxDhcpSvrStats6RxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxReleases.setStatus("current")
_TmnxDhcpSvrStats6TxReplies_Type = Counter64
_TmnxDhcpSvrStats6TxReplies_Object = MibTableColumn
tmnxDhcpSvrStats6TxReplies = _TmnxDhcpSvrStats6TxReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 9),
    _TmnxDhcpSvrStats6TxReplies_Type()
)
tmnxDhcpSvrStats6TxReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6TxReplies.setStatus("current")
_TmnxDhcpSvrStats6TxReconfigures_Type = Counter64
_TmnxDhcpSvrStats6TxReconfigures_Object = MibTableColumn
tmnxDhcpSvrStats6TxReconfigures = _TmnxDhcpSvrStats6TxReconfigures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 10),
    _TmnxDhcpSvrStats6TxReconfigures_Type()
)
tmnxDhcpSvrStats6TxReconfigures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6TxReconfigures.setStatus("current")
_TmnxDhcpSvrStats6RxInfRequests_Type = Counter64
_TmnxDhcpSvrStats6RxInfRequests_Object = MibTableColumn
tmnxDhcpSvrStats6RxInfRequests = _TmnxDhcpSvrStats6RxInfRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 11),
    _TmnxDhcpSvrStats6RxInfRequests_Type()
)
tmnxDhcpSvrStats6RxInfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxInfRequests.setStatus("current")
_TmnxDhcpSvrStats6DropBadPackets_Type = Counter32
_TmnxDhcpSvrStats6DropBadPackets_Object = MibTableColumn
tmnxDhcpSvrStats6DropBadPackets = _TmnxDhcpSvrStats6DropBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 12),
    _TmnxDhcpSvrStats6DropBadPackets_Type()
)
tmnxDhcpSvrStats6DropBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropBadPackets.setStatus("current")
_TmnxDhcpSvrStats6DropInvldTypes_Type = Counter32
_TmnxDhcpSvrStats6DropInvldTypes_Object = MibTableColumn
tmnxDhcpSvrStats6DropInvldTypes = _TmnxDhcpSvrStats6DropInvldTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 13),
    _TmnxDhcpSvrStats6DropInvldTypes_Type()
)
tmnxDhcpSvrStats6DropInvldTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropInvldTypes.setStatus("current")
_TmnxDhcpSvrStats6DropLseNotReady_Type = Counter32
_TmnxDhcpSvrStats6DropLseNotReady_Object = MibTableColumn
tmnxDhcpSvrStats6DropLseNotReady = _TmnxDhcpSvrStats6DropLseNotReady_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 14),
    _TmnxDhcpSvrStats6DropLseNotReady_Type()
)
tmnxDhcpSvrStats6DropLseNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropLseNotReady.setStatus("current")
_TmnxDhcpSvrStats6DropNoSrvngPool_Type = Counter32
_TmnxDhcpSvrStats6DropNoSrvngPool_Object = MibTableColumn
tmnxDhcpSvrStats6DropNoSrvngPool = _TmnxDhcpSvrStats6DropNoSrvngPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 15),
    _TmnxDhcpSvrStats6DropNoSrvngPool_Type()
)
tmnxDhcpSvrStats6DropNoSrvngPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropNoSrvngPool.setStatus("current")
_TmnxDhcpSvrStats6DropOverload_Type = Counter32
_TmnxDhcpSvrStats6DropOverload_Object = MibTableColumn
tmnxDhcpSvrStats6DropOverload = _TmnxDhcpSvrStats6DropOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 16),
    _TmnxDhcpSvrStats6DropOverload_Type()
)
tmnxDhcpSvrStats6DropOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropOverload.setStatus("current")
_TmnxDhcpSvrStats6DropPerOverload_Type = Counter32
_TmnxDhcpSvrStats6DropPerOverload_Object = MibTableColumn
tmnxDhcpSvrStats6DropPerOverload = _TmnxDhcpSvrStats6DropPerOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 17),
    _TmnxDhcpSvrStats6DropPerOverload_Type()
)
tmnxDhcpSvrStats6DropPerOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropPerOverload.setStatus("current")
_TmnxDhcpSvrStats6OffersIgnore_Type = Counter32
_TmnxDhcpSvrStats6OffersIgnore_Object = MibTableColumn
tmnxDhcpSvrStats6OffersIgnore = _TmnxDhcpSvrStats6OffersIgnore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 18),
    _TmnxDhcpSvrStats6OffersIgnore_Type()
)
tmnxDhcpSvrStats6OffersIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6OffersIgnore.setStatus("current")
_TmnxDhcpSvrStats6DropGenError_Type = Counter32
_TmnxDhcpSvrStats6DropGenError_Object = MibTableColumn
tmnxDhcpSvrStats6DropGenError = _TmnxDhcpSvrStats6DropGenError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 19),
    _TmnxDhcpSvrStats6DropGenError_Type()
)
tmnxDhcpSvrStats6DropGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropGenError.setStatus("current")
_TmnxDhcpSvrStats6DropDestOther_Type = Counter32
_TmnxDhcpSvrStats6DropDestOther_Object = MibTableColumn
tmnxDhcpSvrStats6DropDestOther = _TmnxDhcpSvrStats6DropDestOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 20),
    _TmnxDhcpSvrStats6DropDestOther_Type()
)
tmnxDhcpSvrStats6DropDestOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropDestOther.setStatus("current")
_TmnxDhcpSvrStats6DropMaxReached_Type = Counter32
_TmnxDhcpSvrStats6DropMaxReached_Object = MibTableColumn
tmnxDhcpSvrStats6DropMaxReached = _TmnxDhcpSvrStats6DropMaxReached_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 21),
    _TmnxDhcpSvrStats6DropMaxReached_Type()
)
tmnxDhcpSvrStats6DropMaxReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropMaxReached.setStatus("current")
_TmnxDhcpSvrStats6DropSvrDown_Type = Counter32
_TmnxDhcpSvrStats6DropSvrDown_Object = MibTableColumn
tmnxDhcpSvrStats6DropSvrDown = _TmnxDhcpSvrStats6DropSvrDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 22),
    _TmnxDhcpSvrStats6DropSvrDown_Type()
)
tmnxDhcpSvrStats6DropSvrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropSvrDown.setStatus("current")
_TmnxDhcpSvrStats6LeasesExpired_Type = Counter32
_TmnxDhcpSvrStats6LeasesExpired_Object = MibTableColumn
tmnxDhcpSvrStats6LeasesExpired = _TmnxDhcpSvrStats6LeasesExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 23),
    _TmnxDhcpSvrStats6LeasesExpired_Type()
)
tmnxDhcpSvrStats6LeasesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6LeasesExpired.setStatus("current")
_TmnxDhcpSvrStats6DropDuplDiffRly_Type = Counter32
_TmnxDhcpSvrStats6DropDuplDiffRly_Object = MibTableColumn
tmnxDhcpSvrStats6DropDuplDiffRly = _TmnxDhcpSvrStats6DropDuplDiffRly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 24),
    _TmnxDhcpSvrStats6DropDuplDiffRly_Type()
)
tmnxDhcpSvrStats6DropDuplDiffRly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropDuplDiffRly.setStatus("current")
_TmnxDhcpSvrStats6RxIntPppSlaac_Type = Counter64
_TmnxDhcpSvrStats6RxIntPppSlaac_Object = MibTableColumn
tmnxDhcpSvrStats6RxIntPppSlaac = _TmnxDhcpSvrStats6RxIntPppSlaac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 25),
    _TmnxDhcpSvrStats6RxIntPppSlaac_Type()
)
tmnxDhcpSvrStats6RxIntPppSlaac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxIntPppSlaac.setStatus("current")
_TmnxDhcpSvrStats6RxIntReqIpoeWan_Type = Counter64
_TmnxDhcpSvrStats6RxIntReqIpoeWan_Object = MibTableColumn
tmnxDhcpSvrStats6RxIntReqIpoeWan = _TmnxDhcpSvrStats6RxIntReqIpoeWan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 26),
    _TmnxDhcpSvrStats6RxIntReqIpoeWan_Type()
)
tmnxDhcpSvrStats6RxIntReqIpoeWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxIntReqIpoeWan.setStatus("current")
_TmnxDhcpSvrStats6RxIntReleases_Type = Counter64
_TmnxDhcpSvrStats6RxIntReleases_Object = MibTableColumn
tmnxDhcpSvrStats6RxIntReleases = _TmnxDhcpSvrStats6RxIntReleases_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 27),
    _TmnxDhcpSvrStats6RxIntReleases_Type()
)
tmnxDhcpSvrStats6RxIntReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxIntReleases.setStatus("current")
_TmnxDhcpSvrStats6DropIntWFo_Type = Counter32
_TmnxDhcpSvrStats6DropIntWFo_Object = MibTableColumn
tmnxDhcpSvrStats6DropIntWFo = _TmnxDhcpSvrStats6DropIntWFo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 28),
    _TmnxDhcpSvrStats6DropIntWFo_Type()
)
tmnxDhcpSvrStats6DropIntWFo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropIntWFo.setStatus("current")
_TmnxDhcpSvrStats6DropIntWConflct_Type = Counter32
_TmnxDhcpSvrStats6DropIntWConflct_Object = MibTableColumn
tmnxDhcpSvrStats6DropIntWConflct = _TmnxDhcpSvrStats6DropIntWConflct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 29),
    _TmnxDhcpSvrStats6DropIntWConflct_Type()
)
tmnxDhcpSvrStats6DropIntWConflct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropIntWConflct.setStatus("current")
_TmnxDhcpSvrStats6DropIntWIfIdMap_Type = Counter32
_TmnxDhcpSvrStats6DropIntWIfIdMap_Object = MibTableColumn
tmnxDhcpSvrStats6DropIntWIfIdMap = _TmnxDhcpSvrStats6DropIntWIfIdMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 30),
    _TmnxDhcpSvrStats6DropIntWIfIdMap_Type()
)
tmnxDhcpSvrStats6DropIntWIfIdMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropIntWIfIdMap.setStatus("current")
_TmnxDhcpSvrStats6DropIntWUserId_Type = Counter32
_TmnxDhcpSvrStats6DropIntWUserId_Object = MibTableColumn
tmnxDhcpSvrStats6DropIntWUserId = _TmnxDhcpSvrStats6DropIntWUserId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 31),
    _TmnxDhcpSvrStats6DropIntWUserId_Type()
)
tmnxDhcpSvrStats6DropIntWUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropIntWUserId.setStatus("current")
_TmnxDhcpSvrStats6RxIntIpoeSlaac_Type = Counter64
_TmnxDhcpSvrStats6RxIntIpoeSlaac_Object = MibTableColumn
tmnxDhcpSvrStats6RxIntIpoeSlaac = _TmnxDhcpSvrStats6RxIntIpoeSlaac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 32),
    _TmnxDhcpSvrStats6RxIntIpoeSlaac_Type()
)
tmnxDhcpSvrStats6RxIntIpoeSlaac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6RxIntIpoeSlaac.setStatus("current")
_TmnxDhcpSvrStats6DropAudit_Type = Counter64
_TmnxDhcpSvrStats6DropAudit_Object = MibTableColumn
tmnxDhcpSvrStats6DropAudit = _TmnxDhcpSvrStats6DropAudit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 23, 1, 33),
    _TmnxDhcpSvrStats6DropAudit_Type()
)
tmnxDhcpSvrStats6DropAudit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrStats6DropAudit.setStatus("current")
_TmnxDhcpSvrSubnetStats6Table_Object = MibTable
tmnxDhcpSvrSubnetStats6Table = _TmnxDhcpSvrSubnetStats6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6Table.setStatus("current")
_TmnxDhcpSvrSubnetStats6Entry_Object = MibTableRow
tmnxDhcpSvrSubnetStats6Entry = _TmnxDhcpSvrSubnetStats6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1)
)
tmnxDhcpSvrSubnetStats6Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6Entry.setStatus("current")
_TmnxDhcpSvrSubnetStats6Advertise_Type = Counter32
_TmnxDhcpSvrSubnetStats6Advertise_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6Advertise = _TmnxDhcpSvrSubnetStats6Advertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 1),
    _TmnxDhcpSvrSubnetStats6Advertise_Type()
)
tmnxDhcpSvrSubnetStats6Advertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6Advertise.setStatus("current")
_TmnxDhcpSvrSubnetStats6Stable_Type = Counter32
_TmnxDhcpSvrSubnetStats6Stable_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6Stable = _TmnxDhcpSvrSubnetStats6Stable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 2),
    _TmnxDhcpSvrSubnetStats6Stable_Type()
)
tmnxDhcpSvrSubnetStats6Stable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6Stable.setStatus("current")
_TmnxDhcpSvrSubnetStats6RCPending_Type = Counter32
_TmnxDhcpSvrSubnetStats6RCPending_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6RCPending = _TmnxDhcpSvrSubnetStats6RCPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 3),
    _TmnxDhcpSvrSubnetStats6RCPending_Type()
)
tmnxDhcpSvrSubnetStats6RCPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6RCPending.setStatus("current")
_TmnxDhcpSvrSubnetStats6RmPending_Type = Counter32
_TmnxDhcpSvrSubnetStats6RmPending_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6RmPending = _TmnxDhcpSvrSubnetStats6RmPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 4),
    _TmnxDhcpSvrSubnetStats6RmPending_Type()
)
tmnxDhcpSvrSubnetStats6RmPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6RmPending.setStatus("current")
_TmnxDhcpSvrSubnetStats6Declined_Type = Counter32
_TmnxDhcpSvrSubnetStats6Declined_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6Declined = _TmnxDhcpSvrSubnetStats6Declined_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 5),
    _TmnxDhcpSvrSubnetStats6Declined_Type()
)
tmnxDhcpSvrSubnetStats6Declined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6Declined.setStatus("current")
_TmnxDhcpSvrSubnetStats6HasExt_Type = TruthValue
_TmnxDhcpSvrSubnetStats6HasExt_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6HasExt = _TmnxDhcpSvrSubnetStats6HasExt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 6),
    _TmnxDhcpSvrSubnetStats6HasExt_Type()
)
tmnxDhcpSvrSubnetStats6HasExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6HasExt.setStatus("current")
_TmnxDhcpSvrSubnetStats6ExtResetT_Type = TimeStamp
_TmnxDhcpSvrSubnetStats6ExtResetT_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6ExtResetT = _TmnxDhcpSvrSubnetStats6ExtResetT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 7),
    _TmnxDhcpSvrSubnetStats6ExtResetT_Type()
)
tmnxDhcpSvrSubnetStats6ExtResetT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6ExtResetT.setStatus("current")
_TmnxDhcpSvrSubnetStats6StableP_Type = Counter32
_TmnxDhcpSvrSubnetStats6StableP_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6StableP = _TmnxDhcpSvrSubnetStats6StableP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 8),
    _TmnxDhcpSvrSubnetStats6StableP_Type()
)
tmnxDhcpSvrSubnetStats6StableP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6StableP.setStatus("current")
_TmnxDhcpSvrSubnetStats6StablePT_Type = TimeStamp
_TmnxDhcpSvrSubnetStats6StablePT_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6StablePT = _TmnxDhcpSvrSubnetStats6StablePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 9),
    _TmnxDhcpSvrSubnetStats6StablePT_Type()
)
tmnxDhcpSvrSubnetStats6StablePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6StablePT.setStatus("current")
_TmnxDhcpSvrSubnetStats6ProvBlk_Type = Counter64
_TmnxDhcpSvrSubnetStats6ProvBlk_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6ProvBlk = _TmnxDhcpSvrSubnetStats6ProvBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 10),
    _TmnxDhcpSvrSubnetStats6ProvBlk_Type()
)
tmnxDhcpSvrSubnetStats6ProvBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6ProvBlk.setStatus("current")
_TmnxDhcpSvrSubnetStats6UsedBlk_Type = Counter64
_TmnxDhcpSvrSubnetStats6UsedBlk_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6UsedBlk = _TmnxDhcpSvrSubnetStats6UsedBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 11),
    _TmnxDhcpSvrSubnetStats6UsedBlk_Type()
)
tmnxDhcpSvrSubnetStats6UsedBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6UsedBlk.setStatus("current")
_TmnxDhcpSvrSubnetStats6UsedBlkP_Type = Counter64
_TmnxDhcpSvrSubnetStats6UsedBlkP_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6UsedBlkP = _TmnxDhcpSvrSubnetStats6UsedBlkP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 12),
    _TmnxDhcpSvrSubnetStats6UsedBlkP_Type()
)
tmnxDhcpSvrSubnetStats6UsedBlkP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6UsedBlkP.setStatus("current")
_TmnxDhcpSvrSubnetStats6UsedBlkPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStats6UsedBlkPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6UsedBlkPT = _TmnxDhcpSvrSubnetStats6UsedBlkPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 13),
    _TmnxDhcpSvrSubnetStats6UsedBlkPT_Type()
)
tmnxDhcpSvrSubnetStats6UsedBlkPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6UsedBlkPT.setStatus("current")
_TmnxDhcpSvrSubnetStats6FreeBlk_Type = Counter64
_TmnxDhcpSvrSubnetStats6FreeBlk_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6FreeBlk = _TmnxDhcpSvrSubnetStats6FreeBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 14),
    _TmnxDhcpSvrSubnetStats6FreeBlk_Type()
)
tmnxDhcpSvrSubnetStats6FreeBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6FreeBlk.setStatus("current")
_TmnxDhcpSvrSubnetStats6FreeBlkP_Type = Counter64
_TmnxDhcpSvrSubnetStats6FreeBlkP_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6FreeBlkP = _TmnxDhcpSvrSubnetStats6FreeBlkP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 15),
    _TmnxDhcpSvrSubnetStats6FreeBlkP_Type()
)
tmnxDhcpSvrSubnetStats6FreeBlkP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6FreeBlkP.setStatus("current")
_TmnxDhcpSvrSubnetStats6FreeBlkPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStats6FreeBlkPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6FreeBlkPT = _TmnxDhcpSvrSubnetStats6FreeBlkPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 16),
    _TmnxDhcpSvrSubnetStats6FreeBlkPT_Type()
)
tmnxDhcpSvrSubnetStats6FreeBlkPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6FreeBlkPT.setStatus("current")


class _TmnxDhcpSvrSubnetStats6UsedPct_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStats6UsedPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStats6UsedPct_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStats6UsedPct_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6UsedPct = _TmnxDhcpSvrSubnetStats6UsedPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 17),
    _TmnxDhcpSvrSubnetStats6UsedPct_Type()
)
tmnxDhcpSvrSubnetStats6UsedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6UsedPct.setStatus("current")


class _TmnxDhcpSvrSubnetStats6UsedPctP_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStats6UsedPctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStats6UsedPctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStats6UsedPctP_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6UsedPctP = _TmnxDhcpSvrSubnetStats6UsedPctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 18),
    _TmnxDhcpSvrSubnetStats6UsedPctP_Type()
)
tmnxDhcpSvrSubnetStats6UsedPctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6UsedPctP.setStatus("current")
_TmnxDhcpSvrSubnetStats6UsedPctPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStats6UsedPctPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6UsedPctPT = _TmnxDhcpSvrSubnetStats6UsedPctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 19),
    _TmnxDhcpSvrSubnetStats6UsedPctPT_Type()
)
tmnxDhcpSvrSubnetStats6UsedPctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6UsedPctPT.setStatus("current")


class _TmnxDhcpSvrSubnetStats6FreePct_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStats6FreePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStats6FreePct_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStats6FreePct_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6FreePct = _TmnxDhcpSvrSubnetStats6FreePct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 20),
    _TmnxDhcpSvrSubnetStats6FreePct_Type()
)
tmnxDhcpSvrSubnetStats6FreePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6FreePct.setStatus("current")


class _TmnxDhcpSvrSubnetStats6FreePctP_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetStats6FreePctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrSubnetStats6FreePctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetStats6FreePctP_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6FreePctP = _TmnxDhcpSvrSubnetStats6FreePctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 21),
    _TmnxDhcpSvrSubnetStats6FreePctP_Type()
)
tmnxDhcpSvrSubnetStats6FreePctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6FreePctP.setStatus("current")
_TmnxDhcpSvrSubnetStats6FreePctPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStats6FreePctPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6FreePctPT = _TmnxDhcpSvrSubnetStats6FreePctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 22),
    _TmnxDhcpSvrSubnetStats6FreePctPT_Type()
)
tmnxDhcpSvrSubnetStats6FreePctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6FreePctPT.setStatus("current")
_TmnxDhcpSvrSubnetStats6AdvertP_Type = Counter32
_TmnxDhcpSvrSubnetStats6AdvertP_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6AdvertP = _TmnxDhcpSvrSubnetStats6AdvertP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 23),
    _TmnxDhcpSvrSubnetStats6AdvertP_Type()
)
tmnxDhcpSvrSubnetStats6AdvertP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6AdvertP.setStatus("current")
_TmnxDhcpSvrSubnetStats6AdvertPT_Type = TimeStamp
_TmnxDhcpSvrSubnetStats6AdvertPT_Object = MibTableColumn
tmnxDhcpSvrSubnetStats6AdvertPT = _TmnxDhcpSvrSubnetStats6AdvertPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 24, 1, 24),
    _TmnxDhcpSvrSubnetStats6AdvertPT_Type()
)
tmnxDhcpSvrSubnetStats6AdvertPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetStats6AdvertPT.setStatus("current")
_TmnxDhcpSvrPoolStatsTable_Object = MibTable
tmnxDhcpSvrPoolStatsTable = _TmnxDhcpSvrPoolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsTable.setStatus("current")
_TmnxDhcpSvrPoolStatsEntry_Object = MibTableRow
tmnxDhcpSvrPoolStatsEntry = _TmnxDhcpSvrPoolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1)
)
tmnxDhcpSvrPoolStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsEntry.setStatus("current")
_TmnxDhcpSvrPoolStatsFree_Type = Counter32
_TmnxDhcpSvrPoolStatsFree_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFree = _TmnxDhcpSvrPoolStatsFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 1),
    _TmnxDhcpSvrPoolStatsFree_Type()
)
tmnxDhcpSvrPoolStatsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFree.setStatus("current")
_TmnxDhcpSvrPoolStatsOffered_Type = Counter32
_TmnxDhcpSvrPoolStatsOffered_Object = MibTableColumn
tmnxDhcpSvrPoolStatsOffered = _TmnxDhcpSvrPoolStatsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 2),
    _TmnxDhcpSvrPoolStatsOffered_Type()
)
tmnxDhcpSvrPoolStatsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsOffered.setStatus("current")
_TmnxDhcpSvrPoolStatsStable_Type = Counter32
_TmnxDhcpSvrPoolStatsStable_Object = MibTableColumn
tmnxDhcpSvrPoolStatsStable = _TmnxDhcpSvrPoolStatsStable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 3),
    _TmnxDhcpSvrPoolStatsStable_Type()
)
tmnxDhcpSvrPoolStatsStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsStable.setStatus("current")
_TmnxDhcpSvrPoolStatsFRPending_Type = Counter32
_TmnxDhcpSvrPoolStatsFRPending_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFRPending = _TmnxDhcpSvrPoolStatsFRPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 4),
    _TmnxDhcpSvrPoolStatsFRPending_Type()
)
tmnxDhcpSvrPoolStatsFRPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFRPending.setStatus("current")
_TmnxDhcpSvrPoolStatsRemPending_Type = Counter32
_TmnxDhcpSvrPoolStatsRemPending_Object = MibTableColumn
tmnxDhcpSvrPoolStatsRemPending = _TmnxDhcpSvrPoolStatsRemPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 5),
    _TmnxDhcpSvrPoolStatsRemPending_Type()
)
tmnxDhcpSvrPoolStatsRemPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsRemPending.setStatus("current")
_TmnxDhcpSvrPoolStatsDeclined_Type = Counter32
_TmnxDhcpSvrPoolStatsDeclined_Object = MibTableColumn
tmnxDhcpSvrPoolStatsDeclined = _TmnxDhcpSvrPoolStatsDeclined_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 6),
    _TmnxDhcpSvrPoolStatsDeclined_Type()
)
tmnxDhcpSvrPoolStatsDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsDeclined.setStatus("current")
_TmnxDhcpSvrPoolStatsFoFree_Type = Counter32
_TmnxDhcpSvrPoolStatsFoFree_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoFree = _TmnxDhcpSvrPoolStatsFoFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 7),
    _TmnxDhcpSvrPoolStatsFoFree_Type()
)
tmnxDhcpSvrPoolStatsFoFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoFree.setStatus("current")
_TmnxDhcpSvrPoolStatsFoOffered_Type = Counter32
_TmnxDhcpSvrPoolStatsFoOffered_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoOffered = _TmnxDhcpSvrPoolStatsFoOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 8),
    _TmnxDhcpSvrPoolStatsFoOffered_Type()
)
tmnxDhcpSvrPoolStatsFoOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoOffered.setStatus("current")
_TmnxDhcpSvrPoolStatsFoStable_Type = Counter32
_TmnxDhcpSvrPoolStatsFoStable_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoStable = _TmnxDhcpSvrPoolStatsFoStable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 9),
    _TmnxDhcpSvrPoolStatsFoStable_Type()
)
tmnxDhcpSvrPoolStatsFoStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoStable.setStatus("current")
_TmnxDhcpSvrPoolStatsFoFRPend_Type = Counter32
_TmnxDhcpSvrPoolStatsFoFRPend_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoFRPend = _TmnxDhcpSvrPoolStatsFoFRPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 10),
    _TmnxDhcpSvrPoolStatsFoFRPend_Type()
)
tmnxDhcpSvrPoolStatsFoFRPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoFRPend.setStatus("current")
_TmnxDhcpSvrPoolStatsFoRemPend_Type = Counter32
_TmnxDhcpSvrPoolStatsFoRemPend_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoRemPend = _TmnxDhcpSvrPoolStatsFoRemPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 11),
    _TmnxDhcpSvrPoolStatsFoRemPend_Type()
)
tmnxDhcpSvrPoolStatsFoRemPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoRemPend.setStatus("current")
_TmnxDhcpSvrPoolStatsFoDeclined_Type = Counter32
_TmnxDhcpSvrPoolStatsFoDeclined_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoDeclined = _TmnxDhcpSvrPoolStatsFoDeclined_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 12),
    _TmnxDhcpSvrPoolStatsFoDeclined_Type()
)
tmnxDhcpSvrPoolStatsFoDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoDeclined.setStatus("current")
_TmnxDhcpSvrPoolStatsProv_Type = Counter32
_TmnxDhcpSvrPoolStatsProv_Object = MibTableColumn
tmnxDhcpSvrPoolStatsProv = _TmnxDhcpSvrPoolStatsProv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 13),
    _TmnxDhcpSvrPoolStatsProv_Type()
)
tmnxDhcpSvrPoolStatsProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsProv.setStatus("current")
_TmnxDhcpSvrPoolStatsFoProv_Type = Counter32
_TmnxDhcpSvrPoolStatsFoProv_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoProv = _TmnxDhcpSvrPoolStatsFoProv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 14),
    _TmnxDhcpSvrPoolStatsFoProv_Type()
)
tmnxDhcpSvrPoolStatsFoProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoProv.setStatus("current")
_TmnxDhcpSvrPoolStatsHasExt_Type = TruthValue
_TmnxDhcpSvrPoolStatsHasExt_Object = MibTableColumn
tmnxDhcpSvrPoolStatsHasExt = _TmnxDhcpSvrPoolStatsHasExt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 15),
    _TmnxDhcpSvrPoolStatsHasExt_Type()
)
tmnxDhcpSvrPoolStatsHasExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsHasExt.setStatus("current")
_TmnxDhcpSvrPoolStatsExtResetT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsExtResetT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsExtResetT = _TmnxDhcpSvrPoolStatsExtResetT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 16),
    _TmnxDhcpSvrPoolStatsExtResetT_Type()
)
tmnxDhcpSvrPoolStatsExtResetT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsExtResetT.setStatus("current")
_TmnxDhcpSvrPoolStatsStableP_Type = Counter32
_TmnxDhcpSvrPoolStatsStableP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsStableP = _TmnxDhcpSvrPoolStatsStableP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 17),
    _TmnxDhcpSvrPoolStatsStableP_Type()
)
tmnxDhcpSvrPoolStatsStableP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsStableP.setStatus("current")
_TmnxDhcpSvrPoolStatsStablePT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsStablePT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsStablePT = _TmnxDhcpSvrPoolStatsStablePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 18),
    _TmnxDhcpSvrPoolStatsStablePT_Type()
)
tmnxDhcpSvrPoolStatsStablePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsStablePT.setStatus("current")
_TmnxDhcpSvrPoolStatsFoStableP_Type = Counter32
_TmnxDhcpSvrPoolStatsFoStableP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoStableP = _TmnxDhcpSvrPoolStatsFoStableP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 19),
    _TmnxDhcpSvrPoolStatsFoStableP_Type()
)
tmnxDhcpSvrPoolStatsFoStableP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoStableP.setStatus("current")
_TmnxDhcpSvrPoolStatsFoStablePT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFoStablePT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoStablePT = _TmnxDhcpSvrPoolStatsFoStablePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 20),
    _TmnxDhcpSvrPoolStatsFoStablePT_Type()
)
tmnxDhcpSvrPoolStatsFoStablePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoStablePT.setStatus("current")
_TmnxDhcpSvrPoolStatsUsed_Type = Counter32
_TmnxDhcpSvrPoolStatsUsed_Object = MibTableColumn
tmnxDhcpSvrPoolStatsUsed = _TmnxDhcpSvrPoolStatsUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 21),
    _TmnxDhcpSvrPoolStatsUsed_Type()
)
tmnxDhcpSvrPoolStatsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsUsed.setStatus("current")
_TmnxDhcpSvrPoolStatsUsedP_Type = Counter32
_TmnxDhcpSvrPoolStatsUsedP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsUsedP = _TmnxDhcpSvrPoolStatsUsedP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 22),
    _TmnxDhcpSvrPoolStatsUsedP_Type()
)
tmnxDhcpSvrPoolStatsUsedP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsUsedP.setStatus("current")
_TmnxDhcpSvrPoolStatsUsedPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsUsedPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsUsedPT = _TmnxDhcpSvrPoolStatsUsedPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 23),
    _TmnxDhcpSvrPoolStatsUsedPT_Type()
)
tmnxDhcpSvrPoolStatsUsedPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsUsedPT.setStatus("current")
_TmnxDhcpSvrPoolStatsFoUsed_Type = Counter32
_TmnxDhcpSvrPoolStatsFoUsed_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoUsed = _TmnxDhcpSvrPoolStatsFoUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 24),
    _TmnxDhcpSvrPoolStatsFoUsed_Type()
)
tmnxDhcpSvrPoolStatsFoUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoUsed.setStatus("current")
_TmnxDhcpSvrPoolStatsFoUsedP_Type = Counter32
_TmnxDhcpSvrPoolStatsFoUsedP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoUsedP = _TmnxDhcpSvrPoolStatsFoUsedP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 25),
    _TmnxDhcpSvrPoolStatsFoUsedP_Type()
)
tmnxDhcpSvrPoolStatsFoUsedP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoUsedP.setStatus("current")
_TmnxDhcpSvrPoolStatsFoUsedPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFoUsedPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoUsedPT = _TmnxDhcpSvrPoolStatsFoUsedPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 26),
    _TmnxDhcpSvrPoolStatsFoUsedPT_Type()
)
tmnxDhcpSvrPoolStatsFoUsedPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoUsedPT.setStatus("current")
_TmnxDhcpSvrPoolStatsFreeP_Type = Counter32
_TmnxDhcpSvrPoolStatsFreeP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFreeP = _TmnxDhcpSvrPoolStatsFreeP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 27),
    _TmnxDhcpSvrPoolStatsFreeP_Type()
)
tmnxDhcpSvrPoolStatsFreeP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFreeP.setStatus("current")
_TmnxDhcpSvrPoolStatsFreePT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFreePT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFreePT = _TmnxDhcpSvrPoolStatsFreePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 28),
    _TmnxDhcpSvrPoolStatsFreePT_Type()
)
tmnxDhcpSvrPoolStatsFreePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFreePT.setStatus("current")
_TmnxDhcpSvrPoolStatsFoFreeP_Type = Counter32
_TmnxDhcpSvrPoolStatsFoFreeP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoFreeP = _TmnxDhcpSvrPoolStatsFoFreeP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 29),
    _TmnxDhcpSvrPoolStatsFoFreeP_Type()
)
tmnxDhcpSvrPoolStatsFoFreeP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoFreeP.setStatus("current")
_TmnxDhcpSvrPoolStatsFoFreePT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFoFreePT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoFreePT = _TmnxDhcpSvrPoolStatsFoFreePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 30),
    _TmnxDhcpSvrPoolStatsFoFreePT_Type()
)
tmnxDhcpSvrPoolStatsFoFreePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoFreePT.setStatus("current")


class _TmnxDhcpSvrPoolStatsUsedPct_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsUsedPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsUsedPct_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsUsedPct_Object = MibTableColumn
tmnxDhcpSvrPoolStatsUsedPct = _TmnxDhcpSvrPoolStatsUsedPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 31),
    _TmnxDhcpSvrPoolStatsUsedPct_Type()
)
tmnxDhcpSvrPoolStatsUsedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsUsedPct.setStatus("current")


class _TmnxDhcpSvrPoolStatsUsedPctP_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsUsedPctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsUsedPctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsUsedPctP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsUsedPctP = _TmnxDhcpSvrPoolStatsUsedPctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 32),
    _TmnxDhcpSvrPoolStatsUsedPctP_Type()
)
tmnxDhcpSvrPoolStatsUsedPctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsUsedPctP.setStatus("current")
_TmnxDhcpSvrPoolStatsUsedPctPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsUsedPctPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsUsedPctPT = _TmnxDhcpSvrPoolStatsUsedPctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 33),
    _TmnxDhcpSvrPoolStatsUsedPctPT_Type()
)
tmnxDhcpSvrPoolStatsUsedPctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsUsedPctPT.setStatus("current")


class _TmnxDhcpSvrPoolStatsFoUsdPct_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsFoUsdPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsFoUsdPct_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsFoUsdPct_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoUsdPct = _TmnxDhcpSvrPoolStatsFoUsdPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 34),
    _TmnxDhcpSvrPoolStatsFoUsdPct_Type()
)
tmnxDhcpSvrPoolStatsFoUsdPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoUsdPct.setStatus("current")


class _TmnxDhcpSvrPoolStatsFoUsdPctP_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsFoUsdPctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsFoUsdPctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsFoUsdPctP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoUsdPctP = _TmnxDhcpSvrPoolStatsFoUsdPctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 35),
    _TmnxDhcpSvrPoolStatsFoUsdPctP_Type()
)
tmnxDhcpSvrPoolStatsFoUsdPctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoUsdPctP.setStatus("current")
_TmnxDhcpSvrPoolStatsFoUsdPctPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFoUsdPctPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoUsdPctPT = _TmnxDhcpSvrPoolStatsFoUsdPctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 36),
    _TmnxDhcpSvrPoolStatsFoUsdPctPT_Type()
)
tmnxDhcpSvrPoolStatsFoUsdPctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoUsdPctPT.setStatus("current")


class _TmnxDhcpSvrPoolStatsFreePct_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsFreePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsFreePct_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsFreePct_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFreePct = _TmnxDhcpSvrPoolStatsFreePct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 37),
    _TmnxDhcpSvrPoolStatsFreePct_Type()
)
tmnxDhcpSvrPoolStatsFreePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFreePct.setStatus("current")


class _TmnxDhcpSvrPoolStatsFreePctP_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsFreePctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsFreePctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsFreePctP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFreePctP = _TmnxDhcpSvrPoolStatsFreePctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 38),
    _TmnxDhcpSvrPoolStatsFreePctP_Type()
)
tmnxDhcpSvrPoolStatsFreePctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFreePctP.setStatus("current")
_TmnxDhcpSvrPoolStatsFreePctPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFreePctPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFreePctPT = _TmnxDhcpSvrPoolStatsFreePctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 39),
    _TmnxDhcpSvrPoolStatsFreePctPT_Type()
)
tmnxDhcpSvrPoolStatsFreePctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFreePctPT.setStatus("current")


class _TmnxDhcpSvrPoolStatsFoFrePct_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsFoFrePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsFoFrePct_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsFoFrePct_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoFrePct = _TmnxDhcpSvrPoolStatsFoFrePct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 40),
    _TmnxDhcpSvrPoolStatsFoFrePct_Type()
)
tmnxDhcpSvrPoolStatsFoFrePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoFrePct.setStatus("current")


class _TmnxDhcpSvrPoolStatsFoFrePctP_Type(Integer32):
    """Custom type tmnxDhcpSvrPoolStatsFoFrePctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpSvrPoolStatsFoFrePctP_Type.__name__ = "Integer32"
_TmnxDhcpSvrPoolStatsFoFrePctP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoFrePctP = _TmnxDhcpSvrPoolStatsFoFrePctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 41),
    _TmnxDhcpSvrPoolStatsFoFrePctP_Type()
)
tmnxDhcpSvrPoolStatsFoFrePctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoFrePctP.setStatus("current")
_TmnxDhcpSvrPoolStatsFoFrePctPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFoFrePctPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoFrePctPT = _TmnxDhcpSvrPoolStatsFoFrePctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 42),
    _TmnxDhcpSvrPoolStatsFoFrePctPT_Type()
)
tmnxDhcpSvrPoolStatsFoFrePctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoFrePctPT.setStatus("current")
_TmnxDhcpSvrPoolStatsOfferP_Type = Counter32
_TmnxDhcpSvrPoolStatsOfferP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsOfferP = _TmnxDhcpSvrPoolStatsOfferP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 43),
    _TmnxDhcpSvrPoolStatsOfferP_Type()
)
tmnxDhcpSvrPoolStatsOfferP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsOfferP.setStatus("current")
_TmnxDhcpSvrPoolStatsOfferPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsOfferPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsOfferPT = _TmnxDhcpSvrPoolStatsOfferPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 44),
    _TmnxDhcpSvrPoolStatsOfferPT_Type()
)
tmnxDhcpSvrPoolStatsOfferPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsOfferPT.setStatus("current")
_TmnxDhcpSvrPoolStatsFoOfferP_Type = Counter32
_TmnxDhcpSvrPoolStatsFoOfferP_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoOfferP = _TmnxDhcpSvrPoolStatsFoOfferP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 45),
    _TmnxDhcpSvrPoolStatsFoOfferP_Type()
)
tmnxDhcpSvrPoolStatsFoOfferP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoOfferP.setStatus("current")
_TmnxDhcpSvrPoolStatsFoOfferPT_Type = TimeStamp
_TmnxDhcpSvrPoolStatsFoOfferPT_Object = MibTableColumn
tmnxDhcpSvrPoolStatsFoOfferPT = _TmnxDhcpSvrPoolStatsFoOfferPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 25, 1, 46),
    _TmnxDhcpSvrPoolStatsFoOfferPT_Type()
)
tmnxDhcpSvrPoolStatsFoOfferPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolStatsFoOfferPT.setStatus("current")
_TmnxDhcpServerDuidTableLastCh_Type = TimeStamp
_TmnxDhcpServerDuidTableLastCh_Object = MibScalar
tmnxDhcpServerDuidTableLastCh = _TmnxDhcpServerDuidTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 26),
    _TmnxDhcpServerDuidTableLastCh_Type()
)
tmnxDhcpServerDuidTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidTableLastCh.setStatus("current")
_TmnxDhcpServerDuidTable_Object = MibTable
tmnxDhcpServerDuidTable = _TmnxDhcpServerDuidTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 27)
)
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidTable.setStatus("current")
_TmnxDhcpServerDuidEntry_Object = MibTableRow
tmnxDhcpServerDuidEntry = _TmnxDhcpServerDuidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 27, 1)
)
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidEntry.setStatus("current")
_TmnxDhcpServerDuidLastChanged_Type = TimeStamp
_TmnxDhcpServerDuidLastChanged_Object = MibTableColumn
tmnxDhcpServerDuidLastChanged = _TmnxDhcpServerDuidLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 27, 1, 1),
    _TmnxDhcpServerDuidLastChanged_Type()
)
tmnxDhcpServerDuidLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidLastChanged.setStatus("current")


class _TmnxDhcpServerDuidTypeCode_Type(TmnxDhcpServerDUIDTypeCode):
    """Custom type tmnxDhcpServerDuidTypeCode based on TmnxDhcpServerDUIDTypeCode"""
    defaultValue = 3


_TmnxDhcpServerDuidTypeCode_Type.__name__ = "TmnxDhcpServerDUIDTypeCode"
_TmnxDhcpServerDuidTypeCode_Object = MibTableColumn
tmnxDhcpServerDuidTypeCode = _TmnxDhcpServerDuidTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 27, 1, 2),
    _TmnxDhcpServerDuidTypeCode_Type()
)
tmnxDhcpServerDuidTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidTypeCode.setStatus("current")
_TmnxDhcpServerDuidEnNumber_Type = Unsigned32
_TmnxDhcpServerDuidEnNumber_Object = MibTableColumn
tmnxDhcpServerDuidEnNumber = _TmnxDhcpServerDuidEnNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 27, 1, 3),
    _TmnxDhcpServerDuidEnNumber_Type()
)
tmnxDhcpServerDuidEnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidEnNumber.setStatus("current")


class _TmnxDhcpServerDuidEnIdData_Type(OctetString):
    """Custom type tmnxDhcpServerDuidEnIdData based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 58),
    )


_TmnxDhcpServerDuidEnIdData_Type.__name__ = "OctetString"
_TmnxDhcpServerDuidEnIdData_Object = MibTableColumn
tmnxDhcpServerDuidEnIdData = _TmnxDhcpServerDuidEnIdData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 27, 1, 4),
    _TmnxDhcpServerDuidEnIdData_Type()
)
tmnxDhcpServerDuidEnIdData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidEnIdData.setStatus("current")


class _TmnxDhcpServerDuidEnIdDataType_Type(TmnxDhcpOptionType):
    """Custom type tmnxDhcpServerDuidEnIdDataType based on TmnxDhcpOptionType"""
    defaultValue = 2


_TmnxDhcpServerDuidEnIdDataType_Type.__name__ = "TmnxDhcpOptionType"
_TmnxDhcpServerDuidEnIdDataType_Object = MibTableColumn
tmnxDhcpServerDuidEnIdDataType = _TmnxDhcpServerDuidEnIdDataType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 27, 1, 5),
    _TmnxDhcpServerDuidEnIdDataType_Type()
)
tmnxDhcpServerDuidEnIdDataType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidEnIdDataType.setStatus("current")
_TmnxDhcpsPoolStats6Table_Object = MibTable
tmnxDhcpsPoolStats6Table = _TmnxDhcpsPoolStats6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28)
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6Table.setStatus("current")
_TmnxDhcpsPoolStats6Entry_Object = MibTableRow
tmnxDhcpsPoolStats6Entry = _TmnxDhcpsPoolStats6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1)
)
tmnxDhcpsPoolStats6Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6Entry.setStatus("current")
_TmnxDhcpsPoolStats6Stable_Type = Counter32
_TmnxDhcpsPoolStats6Stable_Object = MibTableColumn
tmnxDhcpsPoolStats6Stable = _TmnxDhcpsPoolStats6Stable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 1),
    _TmnxDhcpsPoolStats6Stable_Type()
)
tmnxDhcpsPoolStats6Stable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6Stable.setStatus("current")
_TmnxDhcpsPoolStats6FoStable_Type = Counter32
_TmnxDhcpsPoolStats6FoStable_Object = MibTableColumn
tmnxDhcpsPoolStats6FoStable = _TmnxDhcpsPoolStats6FoStable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 2),
    _TmnxDhcpsPoolStats6FoStable_Type()
)
tmnxDhcpsPoolStats6FoStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoStable.setStatus("current")
_TmnxDhcpsPoolStats6HasExt_Type = TruthValue
_TmnxDhcpsPoolStats6HasExt_Object = MibTableColumn
tmnxDhcpsPoolStats6HasExt = _TmnxDhcpsPoolStats6HasExt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 3),
    _TmnxDhcpsPoolStats6HasExt_Type()
)
tmnxDhcpsPoolStats6HasExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6HasExt.setStatus("current")
_TmnxDhcpsPoolStats6ExtResetT_Type = TimeStamp
_TmnxDhcpsPoolStats6ExtResetT_Object = MibTableColumn
tmnxDhcpsPoolStats6ExtResetT = _TmnxDhcpsPoolStats6ExtResetT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 4),
    _TmnxDhcpsPoolStats6ExtResetT_Type()
)
tmnxDhcpsPoolStats6ExtResetT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6ExtResetT.setStatus("current")
_TmnxDhcpsPoolStats6StableP_Type = Counter32
_TmnxDhcpsPoolStats6StableP_Object = MibTableColumn
tmnxDhcpsPoolStats6StableP = _TmnxDhcpsPoolStats6StableP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 5),
    _TmnxDhcpsPoolStats6StableP_Type()
)
tmnxDhcpsPoolStats6StableP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6StableP.setStatus("current")
_TmnxDhcpsPoolStats6StablePT_Type = TimeStamp
_TmnxDhcpsPoolStats6StablePT_Object = MibTableColumn
tmnxDhcpsPoolStats6StablePT = _TmnxDhcpsPoolStats6StablePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 6),
    _TmnxDhcpsPoolStats6StablePT_Type()
)
tmnxDhcpsPoolStats6StablePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6StablePT.setStatus("current")
_TmnxDhcpsPoolStats6FoStableP_Type = Counter32
_TmnxDhcpsPoolStats6FoStableP_Object = MibTableColumn
tmnxDhcpsPoolStats6FoStableP = _TmnxDhcpsPoolStats6FoStableP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 7),
    _TmnxDhcpsPoolStats6FoStableP_Type()
)
tmnxDhcpsPoolStats6FoStableP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoStableP.setStatus("current")
_TmnxDhcpsPoolStats6FoStablePT_Type = TimeStamp
_TmnxDhcpsPoolStats6FoStablePT_Object = MibTableColumn
tmnxDhcpsPoolStats6FoStablePT = _TmnxDhcpsPoolStats6FoStablePT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 8),
    _TmnxDhcpsPoolStats6FoStablePT_Type()
)
tmnxDhcpsPoolStats6FoStablePT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoStablePT.setStatus("current")
_TmnxDhcpsPoolStats6ProvBlk_Type = Counter64
_TmnxDhcpsPoolStats6ProvBlk_Object = MibTableColumn
tmnxDhcpsPoolStats6ProvBlk = _TmnxDhcpsPoolStats6ProvBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 9),
    _TmnxDhcpsPoolStats6ProvBlk_Type()
)
tmnxDhcpsPoolStats6ProvBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6ProvBlk.setStatus("current")
_TmnxDhcpsPoolStats6FoProvBlk_Type = Counter64
_TmnxDhcpsPoolStats6FoProvBlk_Object = MibTableColumn
tmnxDhcpsPoolStats6FoProvBlk = _TmnxDhcpsPoolStats6FoProvBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 10),
    _TmnxDhcpsPoolStats6FoProvBlk_Type()
)
tmnxDhcpsPoolStats6FoProvBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoProvBlk.setStatus("current")
_TmnxDhcpsPoolStats6UsedBlk_Type = Counter64
_TmnxDhcpsPoolStats6UsedBlk_Object = MibTableColumn
tmnxDhcpsPoolStats6UsedBlk = _TmnxDhcpsPoolStats6UsedBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 11),
    _TmnxDhcpsPoolStats6UsedBlk_Type()
)
tmnxDhcpsPoolStats6UsedBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6UsedBlk.setStatus("current")
_TmnxDhcpsPoolStats6UsedBlkP_Type = Counter64
_TmnxDhcpsPoolStats6UsedBlkP_Object = MibTableColumn
tmnxDhcpsPoolStats6UsedBlkP = _TmnxDhcpsPoolStats6UsedBlkP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 12),
    _TmnxDhcpsPoolStats6UsedBlkP_Type()
)
tmnxDhcpsPoolStats6UsedBlkP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6UsedBlkP.setStatus("current")
_TmnxDhcpsPoolStats6UsedBlkPT_Type = TimeStamp
_TmnxDhcpsPoolStats6UsedBlkPT_Object = MibTableColumn
tmnxDhcpsPoolStats6UsedBlkPT = _TmnxDhcpsPoolStats6UsedBlkPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 13),
    _TmnxDhcpsPoolStats6UsedBlkPT_Type()
)
tmnxDhcpsPoolStats6UsedBlkPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6UsedBlkPT.setStatus("current")
_TmnxDhcpsPoolStats6FoUsedBlk_Type = Counter64
_TmnxDhcpsPoolStats6FoUsedBlk_Object = MibTableColumn
tmnxDhcpsPoolStats6FoUsedBlk = _TmnxDhcpsPoolStats6FoUsedBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 14),
    _TmnxDhcpsPoolStats6FoUsedBlk_Type()
)
tmnxDhcpsPoolStats6FoUsedBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoUsedBlk.setStatus("current")
_TmnxDhcpsPoolStats6FoUsedBlkP_Type = Counter64
_TmnxDhcpsPoolStats6FoUsedBlkP_Object = MibTableColumn
tmnxDhcpsPoolStats6FoUsedBlkP = _TmnxDhcpsPoolStats6FoUsedBlkP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 15),
    _TmnxDhcpsPoolStats6FoUsedBlkP_Type()
)
tmnxDhcpsPoolStats6FoUsedBlkP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoUsedBlkP.setStatus("current")
_TmnxDhcpsPoolStats6FoUsedBlkPT_Type = TimeStamp
_TmnxDhcpsPoolStats6FoUsedBlkPT_Object = MibTableColumn
tmnxDhcpsPoolStats6FoUsedBlkPT = _TmnxDhcpsPoolStats6FoUsedBlkPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 16),
    _TmnxDhcpsPoolStats6FoUsedBlkPT_Type()
)
tmnxDhcpsPoolStats6FoUsedBlkPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoUsedBlkPT.setStatus("current")
_TmnxDhcpsPoolStats6FreeBlk_Type = Counter64
_TmnxDhcpsPoolStats6FreeBlk_Object = MibTableColumn
tmnxDhcpsPoolStats6FreeBlk = _TmnxDhcpsPoolStats6FreeBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 17),
    _TmnxDhcpsPoolStats6FreeBlk_Type()
)
tmnxDhcpsPoolStats6FreeBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FreeBlk.setStatus("current")
_TmnxDhcpsPoolStats6FreeBlkP_Type = Counter64
_TmnxDhcpsPoolStats6FreeBlkP_Object = MibTableColumn
tmnxDhcpsPoolStats6FreeBlkP = _TmnxDhcpsPoolStats6FreeBlkP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 18),
    _TmnxDhcpsPoolStats6FreeBlkP_Type()
)
tmnxDhcpsPoolStats6FreeBlkP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FreeBlkP.setStatus("current")
_TmnxDhcpsPoolStats6FreeBlkPT_Type = TimeStamp
_TmnxDhcpsPoolStats6FreeBlkPT_Object = MibTableColumn
tmnxDhcpsPoolStats6FreeBlkPT = _TmnxDhcpsPoolStats6FreeBlkPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 19),
    _TmnxDhcpsPoolStats6FreeBlkPT_Type()
)
tmnxDhcpsPoolStats6FreeBlkPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FreeBlkPT.setStatus("current")
_TmnxDhcpsPoolStats6FoFreeBlk_Type = Counter64
_TmnxDhcpsPoolStats6FoFreeBlk_Object = MibTableColumn
tmnxDhcpsPoolStats6FoFreeBlk = _TmnxDhcpsPoolStats6FoFreeBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 20),
    _TmnxDhcpsPoolStats6FoFreeBlk_Type()
)
tmnxDhcpsPoolStats6FoFreeBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoFreeBlk.setStatus("current")
_TmnxDhcpsPoolStats6FoFreeBlkP_Type = Counter64
_TmnxDhcpsPoolStats6FoFreeBlkP_Object = MibTableColumn
tmnxDhcpsPoolStats6FoFreeBlkP = _TmnxDhcpsPoolStats6FoFreeBlkP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 21),
    _TmnxDhcpsPoolStats6FoFreeBlkP_Type()
)
tmnxDhcpsPoolStats6FoFreeBlkP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoFreeBlkP.setStatus("current")
_TmnxDhcpsPoolStats6FoFreeBlkPT_Type = TimeStamp
_TmnxDhcpsPoolStats6FoFreeBlkPT_Object = MibTableColumn
tmnxDhcpsPoolStats6FoFreeBlkPT = _TmnxDhcpsPoolStats6FoFreeBlkPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 22),
    _TmnxDhcpsPoolStats6FoFreeBlkPT_Type()
)
tmnxDhcpsPoolStats6FoFreeBlkPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoFreeBlkPT.setStatus("current")


class _TmnxDhcpsPoolStats6UsedPct_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6UsedPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6UsedPct_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6UsedPct_Object = MibTableColumn
tmnxDhcpsPoolStats6UsedPct = _TmnxDhcpsPoolStats6UsedPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 23),
    _TmnxDhcpsPoolStats6UsedPct_Type()
)
tmnxDhcpsPoolStats6UsedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6UsedPct.setStatus("current")


class _TmnxDhcpsPoolStats6UsedPctP_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6UsedPctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6UsedPctP_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6UsedPctP_Object = MibTableColumn
tmnxDhcpsPoolStats6UsedPctP = _TmnxDhcpsPoolStats6UsedPctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 24),
    _TmnxDhcpsPoolStats6UsedPctP_Type()
)
tmnxDhcpsPoolStats6UsedPctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6UsedPctP.setStatus("current")
_TmnxDhcpsPoolStats6UsedPctPT_Type = TimeStamp
_TmnxDhcpsPoolStats6UsedPctPT_Object = MibTableColumn
tmnxDhcpsPoolStats6UsedPctPT = _TmnxDhcpsPoolStats6UsedPctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 25),
    _TmnxDhcpsPoolStats6UsedPctPT_Type()
)
tmnxDhcpsPoolStats6UsedPctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6UsedPctPT.setStatus("current")


class _TmnxDhcpsPoolStats6FoUsedPct_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6FoUsedPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6FoUsedPct_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6FoUsedPct_Object = MibTableColumn
tmnxDhcpsPoolStats6FoUsedPct = _TmnxDhcpsPoolStats6FoUsedPct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 26),
    _TmnxDhcpsPoolStats6FoUsedPct_Type()
)
tmnxDhcpsPoolStats6FoUsedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoUsedPct.setStatus("current")


class _TmnxDhcpsPoolStats6FoUsedPctP_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6FoUsedPctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6FoUsedPctP_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6FoUsedPctP_Object = MibTableColumn
tmnxDhcpsPoolStats6FoUsedPctP = _TmnxDhcpsPoolStats6FoUsedPctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 27),
    _TmnxDhcpsPoolStats6FoUsedPctP_Type()
)
tmnxDhcpsPoolStats6FoUsedPctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoUsedPctP.setStatus("current")
_TmnxDhcpsPoolStats6FoUsedPctPT_Type = TimeStamp
_TmnxDhcpsPoolStats6FoUsedPctPT_Object = MibTableColumn
tmnxDhcpsPoolStats6FoUsedPctPT = _TmnxDhcpsPoolStats6FoUsedPctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 28),
    _TmnxDhcpsPoolStats6FoUsedPctPT_Type()
)
tmnxDhcpsPoolStats6FoUsedPctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoUsedPctPT.setStatus("current")


class _TmnxDhcpsPoolStats6FreePct_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6FreePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6FreePct_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6FreePct_Object = MibTableColumn
tmnxDhcpsPoolStats6FreePct = _TmnxDhcpsPoolStats6FreePct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 29),
    _TmnxDhcpsPoolStats6FreePct_Type()
)
tmnxDhcpsPoolStats6FreePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FreePct.setStatus("current")


class _TmnxDhcpsPoolStats6FreePctP_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6FreePctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6FreePctP_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6FreePctP_Object = MibTableColumn
tmnxDhcpsPoolStats6FreePctP = _TmnxDhcpsPoolStats6FreePctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 30),
    _TmnxDhcpsPoolStats6FreePctP_Type()
)
tmnxDhcpsPoolStats6FreePctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FreePctP.setStatus("current")
_TmnxDhcpsPoolStats6FreePctPT_Type = TimeStamp
_TmnxDhcpsPoolStats6FreePctPT_Object = MibTableColumn
tmnxDhcpsPoolStats6FreePctPT = _TmnxDhcpsPoolStats6FreePctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 31),
    _TmnxDhcpsPoolStats6FreePctPT_Type()
)
tmnxDhcpsPoolStats6FreePctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FreePctPT.setStatus("current")


class _TmnxDhcpsPoolStats6FoFreePct_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6FoFreePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6FoFreePct_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6FoFreePct_Object = MibTableColumn
tmnxDhcpsPoolStats6FoFreePct = _TmnxDhcpsPoolStats6FoFreePct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 32),
    _TmnxDhcpsPoolStats6FoFreePct_Type()
)
tmnxDhcpsPoolStats6FoFreePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoFreePct.setStatus("current")


class _TmnxDhcpsPoolStats6FoFreePctP_Type(Integer32):
    """Custom type tmnxDhcpsPoolStats6FoFreePctP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDhcpsPoolStats6FoFreePctP_Type.__name__ = "Integer32"
_TmnxDhcpsPoolStats6FoFreePctP_Object = MibTableColumn
tmnxDhcpsPoolStats6FoFreePctP = _TmnxDhcpsPoolStats6FoFreePctP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 33),
    _TmnxDhcpsPoolStats6FoFreePctP_Type()
)
tmnxDhcpsPoolStats6FoFreePctP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoFreePctP.setStatus("current")
_TmnxDhcpsPoolStats6FoFreePctPT_Type = TimeStamp
_TmnxDhcpsPoolStats6FoFreePctPT_Object = MibTableColumn
tmnxDhcpsPoolStats6FoFreePctPT = _TmnxDhcpsPoolStats6FoFreePctPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 34),
    _TmnxDhcpsPoolStats6FoFreePctPT_Type()
)
tmnxDhcpsPoolStats6FoFreePctPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoFreePctPT.setStatus("current")
_TmnxDhcpsPoolStats6Advertise_Type = Counter32
_TmnxDhcpsPoolStats6Advertise_Object = MibTableColumn
tmnxDhcpsPoolStats6Advertise = _TmnxDhcpsPoolStats6Advertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 35),
    _TmnxDhcpsPoolStats6Advertise_Type()
)
tmnxDhcpsPoolStats6Advertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6Advertise.setStatus("current")
_TmnxDhcpsPoolStats6AdvertP_Type = Counter32
_TmnxDhcpsPoolStats6AdvertP_Object = MibTableColumn
tmnxDhcpsPoolStats6AdvertP = _TmnxDhcpsPoolStats6AdvertP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 36),
    _TmnxDhcpsPoolStats6AdvertP_Type()
)
tmnxDhcpsPoolStats6AdvertP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6AdvertP.setStatus("current")
_TmnxDhcpsPoolStats6AdvertPT_Type = TimeStamp
_TmnxDhcpsPoolStats6AdvertPT_Object = MibTableColumn
tmnxDhcpsPoolStats6AdvertPT = _TmnxDhcpsPoolStats6AdvertPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 37),
    _TmnxDhcpsPoolStats6AdvertPT_Type()
)
tmnxDhcpsPoolStats6AdvertPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6AdvertPT.setStatus("current")
_TmnxDhcpsPoolStats6FoAdvertise_Type = Counter32
_TmnxDhcpsPoolStats6FoAdvertise_Object = MibTableColumn
tmnxDhcpsPoolStats6FoAdvertise = _TmnxDhcpsPoolStats6FoAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 38),
    _TmnxDhcpsPoolStats6FoAdvertise_Type()
)
tmnxDhcpsPoolStats6FoAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoAdvertise.setStatus("current")
_TmnxDhcpsPoolStats6FoAdvertP_Type = Counter32
_TmnxDhcpsPoolStats6FoAdvertP_Object = MibTableColumn
tmnxDhcpsPoolStats6FoAdvertP = _TmnxDhcpsPoolStats6FoAdvertP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 39),
    _TmnxDhcpsPoolStats6FoAdvertP_Type()
)
tmnxDhcpsPoolStats6FoAdvertP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoAdvertP.setStatus("current")
_TmnxDhcpsPoolStats6FoAdvertPT_Type = TimeStamp
_TmnxDhcpsPoolStats6FoAdvertPT_Object = MibTableColumn
tmnxDhcpsPoolStats6FoAdvertPT = _TmnxDhcpsPoolStats6FoAdvertPT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 40),
    _TmnxDhcpsPoolStats6FoAdvertPT_Type()
)
tmnxDhcpsPoolStats6FoAdvertPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6FoAdvertPT.setStatus("current")
_TmnxDhcpsPoolStats6IntNoPfxWan_Type = Counter32
_TmnxDhcpsPoolStats6IntNoPfxWan_Object = MibTableColumn
tmnxDhcpsPoolStats6IntNoPfxWan = _TmnxDhcpsPoolStats6IntNoPfxWan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 41),
    _TmnxDhcpsPoolStats6IntNoPfxWan_Type()
)
tmnxDhcpsPoolStats6IntNoPfxWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6IntNoPfxWan.setStatus("current")
_TmnxDhcpsPoolStats6IntNoPfxSlaa_Type = Counter32
_TmnxDhcpsPoolStats6IntNoPfxSlaa_Object = MibTableColumn
tmnxDhcpsPoolStats6IntNoPfxSlaa = _TmnxDhcpsPoolStats6IntNoPfxSlaa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 28, 1, 42),
    _TmnxDhcpsPoolStats6IntNoPfxSlaa_Type()
)
tmnxDhcpsPoolStats6IntNoPfxSlaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpsPoolStats6IntNoPfxSlaa.setStatus("current")
_TmnxDhcpSvrSubnetBindingTable_Object = MibTable
tmnxDhcpSvrSubnetBindingTable = _TmnxDhcpSvrSubnetBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29)
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindingTable.setStatus("obsolete")
_TmnxDhcpSvrSubnetBindingEntry_Object = MibTableRow
tmnxDhcpSvrSubnetBindingEntry = _TmnxDhcpSvrSubnetBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29, 1)
)
tmnxDhcpSvrSubnetBindingEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgServerName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolName"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddrType"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetAddress"),
    (0, "TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindingEntry.setStatus("obsolete")


class _TmnxDhcpSvrSubnetBindSystemId_Type(OctetString):
    """Custom type tmnxDhcpSvrSubnetBindSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrSubnetBindSystemId_Type.__name__ = "OctetString"
_TmnxDhcpSvrSubnetBindSystemId_Object = MibTableColumn
tmnxDhcpSvrSubnetBindSystemId = _TmnxDhcpSvrSubnetBindSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29, 1, 1),
    _TmnxDhcpSvrSubnetBindSystemId_Type()
)
tmnxDhcpSvrSubnetBindSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindSystemId.setStatus("obsolete")


class _TmnxDhcpSvrSubnetBindServiceId_Type(OctetString):
    """Custom type tmnxDhcpSvrSubnetBindServiceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrSubnetBindServiceId_Type.__name__ = "OctetString"
_TmnxDhcpSvrSubnetBindServiceId_Object = MibTableColumn
tmnxDhcpSvrSubnetBindServiceId = _TmnxDhcpSvrSubnetBindServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29, 1, 2),
    _TmnxDhcpSvrSubnetBindServiceId_Type()
)
tmnxDhcpSvrSubnetBindServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindServiceId.setStatus("obsolete")


class _TmnxDhcpSvrSubnetBindString_Type(OctetString):
    """Custom type tmnxDhcpSvrSubnetBindString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrSubnetBindString_Type.__name__ = "OctetString"
_TmnxDhcpSvrSubnetBindString_Object = MibTableColumn
tmnxDhcpSvrSubnetBindString = _TmnxDhcpSvrSubnetBindString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29, 1, 3),
    _TmnxDhcpSvrSubnetBindString_Type()
)
tmnxDhcpSvrSubnetBindString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindString.setStatus("obsolete")
_TmnxDhcpSvrSubnetBindUnbindTime_Type = Unsigned32
_TmnxDhcpSvrSubnetBindUnbindTime_Object = MibTableColumn
tmnxDhcpSvrSubnetBindUnbindTime = _TmnxDhcpSvrSubnetBindUnbindTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29, 1, 4),
    _TmnxDhcpSvrSubnetBindUnbindTime_Type()
)
tmnxDhcpSvrSubnetBindUnbindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindUnbindTime.setStatus("obsolete")


class _TmnxDhcpSvrSubnetBindActive_Type(TruthValue):
    """Custom type tmnxDhcpSvrSubnetBindActive based on TruthValue"""
    defaultValue = 2


_TmnxDhcpSvrSubnetBindActive_Type.__name__ = "TruthValue"
_TmnxDhcpSvrSubnetBindActive_Object = MibTableColumn
tmnxDhcpSvrSubnetBindActive = _TmnxDhcpSvrSubnetBindActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29, 1, 5),
    _TmnxDhcpSvrSubnetBindActive_Type()
)
tmnxDhcpSvrSubnetBindActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindActive.setStatus("obsolete")


class _TmnxDhcpSvrSubnetBindState_Type(Integer32):
    """Custom type tmnxDhcpSvrSubnetBindState based on Integer32"""
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
        *(("notBound", 1),
          ("offered", 2),
          ("bound", 3),
          ("unbinding", 4))
    )


_TmnxDhcpSvrSubnetBindState_Type.__name__ = "Integer32"
_TmnxDhcpSvrSubnetBindState_Object = MibTableColumn
tmnxDhcpSvrSubnetBindState = _TmnxDhcpSvrSubnetBindState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 29, 1, 6),
    _TmnxDhcpSvrSubnetBindState_Type()
)
tmnxDhcpSvrSubnetBindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindState.setStatus("obsolete")
_TmnxDhcpSvrSubntBndngTbleLastCh_Type = TimeStamp
_TmnxDhcpSvrSubntBndngTbleLastCh_Object = MibScalar
tmnxDhcpSvrSubntBndngTbleLastCh = _TmnxDhcpSvrSubntBndngTbleLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 1, 30),
    _TmnxDhcpSvrSubntBndngTbleLastCh_Type()
)
tmnxDhcpSvrSubntBndngTbleLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubntBndngTbleLastCh.setStatus("obsolete")
_TmnxDhcpServerNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxDhcpServerNotificationObjs = _TmnxDhcpServerNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2)
)
_TmnxDhcpSvrNotifDescription_Type = DisplayString
_TmnxDhcpSvrNotifDescription_Object = MibScalar
tmnxDhcpSvrNotifDescription = _TmnxDhcpSvrNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 1),
    _TmnxDhcpSvrNotifDescription_Type()
)
tmnxDhcpSvrNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifDescription.setStatus("current")
_TmnxDhcpSvrNotifUnknownPoolName_Type = TNamedItem
_TmnxDhcpSvrNotifUnknownPoolName_Object = MibScalar
tmnxDhcpSvrNotifUnknownPoolName = _TmnxDhcpSvrNotifUnknownPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 2),
    _TmnxDhcpSvrNotifUnknownPoolName_Type()
)
tmnxDhcpSvrNotifUnknownPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifUnknownPoolName.setStatus("current")
_TmnxDhcpSvrNotifServerName_Type = TNamedItem
_TmnxDhcpSvrNotifServerName_Object = MibScalar
tmnxDhcpSvrNotifServerName = _TmnxDhcpSvrNotifServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 3),
    _TmnxDhcpSvrNotifServerName_Type()
)
tmnxDhcpSvrNotifServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifServerName.setStatus("current")
_TmnxDhcpSvrNotifLeaseClientAddrType_Type = InetAddressType
_TmnxDhcpSvrNotifLeaseClientAddrType_Object = MibScalar
tmnxDhcpSvrNotifLeaseClientAddrType = _TmnxDhcpSvrNotifLeaseClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 4),
    _TmnxDhcpSvrNotifLeaseClientAddrType_Type()
)
tmnxDhcpSvrNotifLeaseClientAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifLeaseClientAddrType.setStatus("current")


class _TmnxDhcpSvrNotifLeaseClientAddr_Type(InetAddress):
    """Custom type tmnxDhcpSvrNotifLeaseClientAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrNotifLeaseClientAddr_Type.__name__ = "InetAddress"
_TmnxDhcpSvrNotifLeaseClientAddr_Object = MibScalar
tmnxDhcpSvrNotifLeaseClientAddr = _TmnxDhcpSvrNotifLeaseClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 5),
    _TmnxDhcpSvrNotifLeaseClientAddr_Type()
)
tmnxDhcpSvrNotifLeaseClientAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifLeaseClientAddr.setStatus("current")
_TmnxDhcpSvrNotifUserDatabaseName_Type = TNamedItem
_TmnxDhcpSvrNotifUserDatabaseName_Object = MibScalar
tmnxDhcpSvrNotifUserDatabaseName = _TmnxDhcpSvrNotifUserDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 6),
    _TmnxDhcpSvrNotifUserDatabaseName_Type()
)
tmnxDhcpSvrNotifUserDatabaseName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifUserDatabaseName.setStatus("current")


class _TmnxDhcpSvrNotifHostName_Type(DisplayString):
    """Custom type tmnxDhcpSvrNotifHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxDhcpSvrNotifHostName_Type.__name__ = "DisplayString"
_TmnxDhcpSvrNotifHostName_Object = MibScalar
tmnxDhcpSvrNotifHostName = _TmnxDhcpSvrNotifHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 7),
    _TmnxDhcpSvrNotifHostName_Type()
)
tmnxDhcpSvrNotifHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifHostName.setStatus("current")


class _TmnxDhcpSvrNotifHostType_Type(Integer32):
    """Custom type tmnxDhcpSvrNotifHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dhcp", 1),
          ("pppoe", 2))
    )


_TmnxDhcpSvrNotifHostType_Type.__name__ = "Integer32"
_TmnxDhcpSvrNotifHostType_Object = MibScalar
tmnxDhcpSvrNotifHostType = _TmnxDhcpSvrNotifHostType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 8),
    _TmnxDhcpSvrNotifHostType_Type()
)
tmnxDhcpSvrNotifHostType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifHostType.setStatus("current")
_TmnxDhcpSvrNotifVRtrID_Type = TmnxVRtrID
_TmnxDhcpSvrNotifVRtrID_Object = MibScalar
tmnxDhcpSvrNotifVRtrID = _TmnxDhcpSvrNotifVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 9),
    _TmnxDhcpSvrNotifVRtrID_Type()
)
tmnxDhcpSvrNotifVRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifVRtrID.setStatus("current")
_TmnxDhcpSvrNotifMsgHwAddress_Type = MacAddress
_TmnxDhcpSvrNotifMsgHwAddress_Object = MibScalar
tmnxDhcpSvrNotifMsgHwAddress = _TmnxDhcpSvrNotifMsgHwAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 10),
    _TmnxDhcpSvrNotifMsgHwAddress_Type()
)
tmnxDhcpSvrNotifMsgHwAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifMsgHwAddress.setStatus("current")
_TmnxDhcpSvrNotifMsgOption82_Type = OctetString
_TmnxDhcpSvrNotifMsgOption82_Object = MibScalar
tmnxDhcpSvrNotifMsgOption82 = _TmnxDhcpSvrNotifMsgOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 11),
    _TmnxDhcpSvrNotifMsgOption82_Type()
)
tmnxDhcpSvrNotifMsgOption82.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifMsgOption82.setStatus("current")
_TmnxDhcpSvrNotifMsgSizeLimit_Type = Unsigned32
_TmnxDhcpSvrNotifMsgSizeLimit_Object = MibScalar
tmnxDhcpSvrNotifMsgSizeLimit = _TmnxDhcpSvrNotifMsgSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 12),
    _TmnxDhcpSvrNotifMsgSizeLimit_Type()
)
tmnxDhcpSvrNotifMsgSizeLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifMsgSizeLimit.setStatus("current")
_TmnxDhcpsFoLeaseFailureReason_Type = TmnxDhcpsFoLeaseFailureReason
_TmnxDhcpsFoLeaseFailureReason_Object = MibScalar
tmnxDhcpsFoLeaseFailureReason = _TmnxDhcpsFoLeaseFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 13),
    _TmnxDhcpsFoLeaseFailureReason_Type()
)
tmnxDhcpsFoLeaseFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpsFoLeaseFailureReason.setStatus("current")
_TmnxDhcpSvrNotifPoolFree_Type = Unsigned32
_TmnxDhcpSvrNotifPoolFree_Object = MibScalar
tmnxDhcpSvrNotifPoolFree = _TmnxDhcpSvrNotifPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 14),
    _TmnxDhcpSvrNotifPoolFree_Type()
)
tmnxDhcpSvrNotifPoolFree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifPoolFree.setStatus("current")
_TmnxDhcpSvrNotifLeaseClientAddrLen_Type = Unsigned32
_TmnxDhcpSvrNotifLeaseClientAddrLen_Object = MibScalar
tmnxDhcpSvrNotifLeaseClientAddrLen = _TmnxDhcpSvrNotifLeaseClientAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 15),
    _TmnxDhcpSvrNotifLeaseClientAddrLen_Type()
)
tmnxDhcpSvrNotifLeaseClientAddrLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifLeaseClientAddrLen.setStatus("current")
_TmnxDhcpSvrNotifClientDUID_Type = OctetString
_TmnxDhcpSvrNotifClientDUID_Object = MibScalar
tmnxDhcpSvrNotifClientDUID = _TmnxDhcpSvrNotifClientDUID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 16),
    _TmnxDhcpSvrNotifClientDUID_Type()
)
tmnxDhcpSvrNotifClientDUID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifClientDUID.setStatus("current")


class _TmnxDhcpSvrNotifLinkAddr_Type(InetAddress):
    """Custom type tmnxDhcpSvrNotifLinkAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrNotifLinkAddr_Type.__name__ = "InetAddress"
_TmnxDhcpSvrNotifLinkAddr_Object = MibScalar
tmnxDhcpSvrNotifLinkAddr = _TmnxDhcpSvrNotifLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 17),
    _TmnxDhcpSvrNotifLinkAddr_Type()
)
tmnxDhcpSvrNotifLinkAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifLinkAddr.setStatus("current")
_TmnxDhcpSvrNotifPrimaryPool_Type = TNamedItem
_TmnxDhcpSvrNotifPrimaryPool_Object = MibScalar
tmnxDhcpSvrNotifPrimaryPool = _TmnxDhcpSvrNotifPrimaryPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 18),
    _TmnxDhcpSvrNotifPrimaryPool_Type()
)
tmnxDhcpSvrNotifPrimaryPool.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifPrimaryPool.setStatus("current")
_TmnxDhcpSvrNotifSecondaryPool_Type = TNamedItem
_TmnxDhcpSvrNotifSecondaryPool_Object = MibScalar
tmnxDhcpSvrNotifSecondaryPool = _TmnxDhcpSvrNotifSecondaryPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 19),
    _TmnxDhcpSvrNotifSecondaryPool_Type()
)
tmnxDhcpSvrNotifSecondaryPool.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifSecondaryPool.setStatus("current")


class _TmnxDhcpSvrNotifSystemId_Type(OctetString):
    """Custom type tmnxDhcpSvrNotifSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrNotifSystemId_Type.__name__ = "OctetString"
_TmnxDhcpSvrNotifSystemId_Object = MibScalar
tmnxDhcpSvrNotifSystemId = _TmnxDhcpSvrNotifSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 20),
    _TmnxDhcpSvrNotifSystemId_Type()
)
tmnxDhcpSvrNotifSystemId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifSystemId.setStatus("current")


class _TmnxDhcpSvrNotifServiceId_Type(OctetString):
    """Custom type tmnxDhcpSvrNotifServiceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrNotifServiceId_Type.__name__ = "OctetString"
_TmnxDhcpSvrNotifServiceId_Object = MibScalar
tmnxDhcpSvrNotifServiceId = _TmnxDhcpSvrNotifServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 21),
    _TmnxDhcpSvrNotifServiceId_Type()
)
tmnxDhcpSvrNotifServiceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifServiceId.setStatus("current")


class _TmnxDhcpSvrNotifString_Type(OctetString):
    """Custom type tmnxDhcpSvrNotifString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDhcpSvrNotifString_Type.__name__ = "OctetString"
_TmnxDhcpSvrNotifString_Object = MibScalar
tmnxDhcpSvrNotifString = _TmnxDhcpSvrNotifString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 22),
    _TmnxDhcpSvrNotifString_Type()
)
tmnxDhcpSvrNotifString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifString.setStatus("current")
_TmnxDhcpSvrNotifPoolName_Type = TNamedItem
_TmnxDhcpSvrNotifPoolName_Object = MibScalar
tmnxDhcpSvrNotifPoolName = _TmnxDhcpSvrNotifPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 23),
    _TmnxDhcpSvrNotifPoolName_Type()
)
tmnxDhcpSvrNotifPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifPoolName.setStatus("current")
_TmnxDhcpSvrNotifSubnetAddrType_Type = InetAddressType
_TmnxDhcpSvrNotifSubnetAddrType_Object = MibScalar
tmnxDhcpSvrNotifSubnetAddrType = _TmnxDhcpSvrNotifSubnetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 24),
    _TmnxDhcpSvrNotifSubnetAddrType_Type()
)
tmnxDhcpSvrNotifSubnetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifSubnetAddrType.setStatus("current")


class _TmnxDhcpSvrNotifSubnetPfx_Type(InetAddress):
    """Custom type tmnxDhcpSvrNotifSubnetPfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDhcpSvrNotifSubnetPfx_Type.__name__ = "InetAddress"
_TmnxDhcpSvrNotifSubnetPfx_Object = MibScalar
tmnxDhcpSvrNotifSubnetPfx = _TmnxDhcpSvrNotifSubnetPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 25),
    _TmnxDhcpSvrNotifSubnetPfx_Type()
)
tmnxDhcpSvrNotifSubnetPfx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifSubnetPfx.setStatus("current")


class _TmnxDhcpSvrNotifSubnetPfxlen_Type(InetAddressPrefixLength):
    """Custom type tmnxDhcpSvrNotifSubnetPfxlen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxDhcpSvrNotifSubnetPfxlen_Type.__name__ = "InetAddressPrefixLength"
_TmnxDhcpSvrNotifSubnetPfxlen_Object = MibScalar
tmnxDhcpSvrNotifSubnetPfxlen = _TmnxDhcpSvrNotifSubnetPfxlen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 26),
    _TmnxDhcpSvrNotifSubnetPfxlen_Type()
)
tmnxDhcpSvrNotifSubnetPfxlen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifSubnetPfxlen.setStatus("current")
_TmnxDhcpSvrNotifUnbindTime_Type = Unsigned32
_TmnxDhcpSvrNotifUnbindTime_Object = MibScalar
tmnxDhcpSvrNotifUnbindTime = _TmnxDhcpSvrNotifUnbindTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 47, 2, 27),
    _TmnxDhcpSvrNotifUnbindTime_Type()
)
tmnxDhcpSvrNotifUnbindTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifUnbindTime.setStatus("current")
_TmnxDhcpServerNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDhcpServerNotifyPrefix = _TmnxDhcpServerNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47)
)
_TmnxDhcpServerNotifications_ObjectIdentity = ObjectIdentity
tmnxDhcpServerNotifications = _TmnxDhcpServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0)
)
tmnxDhcpServerConfigEntry.registerAugmentions(
    ("TIMETRA-DHCP-SERVER-MIB",
     "tmnxDhcpsFoEntry")
)
tmnxDhcpsFoEntry.setIndexNames(*tmnxDhcpServerConfigEntry.getIndexNames())
tmnxDhcpServerConfigEntry.registerAugmentions(
    ("TIMETRA-DHCP-SERVER-MIB",
     "tmnxDhcpsFoStatsEntry")
)
tmnxDhcpsFoStatsEntry.setIndexNames(*tmnxDhcpServerConfigEntry.getIndexNames())
tmnxDhcpServerPoolEntry.registerAugmentions(
    ("TIMETRA-DHCP-SERVER-MIB",
     "tmnxDhcpsPoolFoEntry")
)
tmnxDhcpsPoolFoEntry.setIndexNames(*tmnxDhcpServerPoolEntry.getIndexNames())
tmnxDhcpServerPoolEntry.registerAugmentions(
    ("TIMETRA-DHCP-SERVER-MIB",
     "tmnxDhcpsPoolFoStatsEntry")
)
tmnxDhcpsPoolFoStatsEntry.setIndexNames(*tmnxDhcpServerPoolEntry.getIndexNames())
tmnxDhcpServerConfigEntry.registerAugmentions(
    ("TIMETRA-DHCP-SERVER-MIB",
     "tmnxDhcpServerDuidEntry")
)
tmnxDhcpServerDuidEntry.setIndexNames(*tmnxDhcpServerConfigEntry.getIndexNames())

# Managed Objects groups

tmnxDhcpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 1)
)
tmnxDhcpServerGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerConfigTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgAdminState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUserDatabase"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseGiAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgSendForceRenews"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgOperState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMinLeaseTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMaxLeaseTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolOfferTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionValue"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerSubnetTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMinFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMaxDeclined"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesTblLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionTblLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionValue"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerGroup.setStatus("obsolete")

tmnxDhcpLeaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 2)
)
tmnxDhcpLeaseGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseStart"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseLastRenew"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseRemainLeaseTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseRemPotentExpTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseClientHwAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseXid"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseOption82"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseClientType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeasePPPoEUserName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseOpt82CircId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseOption60"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNumLeases"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrMaxLeases"))
)
if mibBuilder.loadTexts:
    tmnxDhcpLeaseGroup.setStatus("current")

tmnxDhcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 3)
)
tmnxDhcpStatsGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxDiscovers"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxRequests"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxReleases"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxDeclines"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxInforms"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxOffers"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxAcks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxNaks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxForceRenews"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropBadPackets"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropInvalidTypes"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoUsrDbFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropUnknownHosts"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropUserNotAllow"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropLseNotReady"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoLeaseFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNotSrvngPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropInvalidUsr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropPersOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsOffersIgnore"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropGenError"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropDestOther"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropAddrUnavail"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropMaxReached"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropSvrDown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoSubnet"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsLeasesExpired"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsOffered"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsStable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFRPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsRemPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsDeclined"))
)
if mibBuilder.loadTexts:
    tmnxDhcpStatsGroup.setStatus("obsolete")

tmnxDhcpAddrListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 4)
)
tmnxDhcpAddrListGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddrAddedTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddrHwAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddrOption82"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddrClientType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddrUserName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclinedAddrCircId"))
)
if mibBuilder.loadTexts:
    tmnxDhcpAddrListGroup.setStatus("current")

tmnxDhcpToolsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 5)
)
tmnxDhcpToolsGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrActForceRenewAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrActForceRenewAddr"))
)
if mibBuilder.loadTexts:
    tmnxDhcpToolsGroup.setStatus("current")

tmnxDhcpsFailoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 6)
)
tmnxDhcpsFailoverGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoTableLastChanged"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoLastChanged"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoAdminState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoMaxClientLeadTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoOperMaxClientLeadTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStartupWaitTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoPartnerDownDelay"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoTimeLeft"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangeFailCtrl"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseFailCtrl"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFreeAddrFailCtrl"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoOffered"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoStable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoFRPend"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoRemPend"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoDeclined"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsLeaseNotFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsDropInvalidPkts"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsFoShutdown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsExpired"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsMaxReached"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsSubnetNotFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsRangeNotFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsHostConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsAddressConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsPeerConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionVRtrId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionGo"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionSuccessful"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionErrorMsg"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionTime"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsFailoverGroup.setStatus("current")

tmnxDhcpsNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 7)
)
tmnxDhcpsNotifyObjsGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifUnknownPoolName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifUserDatabaseName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifHostName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifHostType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgHwAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgOption82"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgSizeLimit"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoLeaseFailureReason"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPoolFree"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsNotifyObjsGroup.setStatus("current")

tmnxDhcpServerV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 8)
)
tmnxDhcpServerV6v1Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerConfigTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgAdminState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUserDatabase"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseGiAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgSendForceRenews"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseClientPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgOperState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMinLeaseTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMaxLeaseTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolOfferTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionValue"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerSubnetTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMinFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMaxDeclined"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesTblLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionTblLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionValue"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV6v1Group.setStatus("obsolete")

tmnxDhcpStatsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 9)
)
tmnxDhcpStatsV6v1Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxDiscovers"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxRequests"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxReleases"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxDeclines"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxInforms"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxOffers"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxAcks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxNaks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxForceRenews"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropBadPackets"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropInvalidTypes"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoUsrDbFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropUnknownHosts"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropUserNotAllow"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropLseNotReady"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoLeaseFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNotSrvngPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropInvalidUsr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropPersOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsOffersIgnore"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropGenError"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropDestOther"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropAddrUnavail"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropMaxReached"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropSvrDown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoSubnet"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsLeasesExpired"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropDuplDiffGi"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsOffered"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsStable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFRPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsRemPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsDeclined"))
)
if mibBuilder.loadTexts:
    tmnxDhcpStatsV6v1Group.setStatus("obsolete")

tmnxDhcpServerV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 10)
)
tmnxDhcpServerV8v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerConfigTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgAdminState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUserDatabase"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseGiAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgSendForceRenews"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseClientPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgOperState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMinLeaseTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMaxLeaseTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolOfferTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolOptionValue"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerSubnetTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetLastChangeTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMinFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMaxDeclined"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesTblLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRangesLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionTblLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionRowStatus"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetOptionValue"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMinFreeType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMinFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMinFreeType"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV8v0Group.setStatus("current")

tmnxDhcpStatsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 11)
)
tmnxDhcpStatsV8v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxDiscovers"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxRequests"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxReleases"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxDeclines"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxInforms"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxOffers"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxAcks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxNaks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsTxForceRenews"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropBadPackets"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropInvalidTypes"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoUsrDbFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropUnknownHosts"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropUserNotAllow"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropLseNotReady"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoLeaseFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNotSrvngPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropInvalidUsr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropPersOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsOffersIgnore"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropGenError"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropDestOther"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropAddrUnavail"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropMaxReached"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropSvrDown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropNoSubnet"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsLeasesExpired"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropDuplDiffGi"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsOffered"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsStable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFRPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsRemPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsDeclined"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsProv"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoProv"))
)
if mibBuilder.loadTexts:
    tmnxDhcpStatsV8v0Group.setStatus("current")

tmnxDhcpServerV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 12)
)
tmnxDhcpServerV9v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgLeaseHoldTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseGiScope"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRenewTimer"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRebindTimer"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetValidLifetime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefLifetime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseClientPrefixLen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseIAOptionType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseIAID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseDUID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseRemainHoldTime"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV9v0Group.setStatus("current")

tmnxDhcpStatsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 13)
)
tmnxDhcpStatsV9v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxSolicits"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6TxAdvertises"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxRequests"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxConfirms"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxRenews"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxRebinds"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxDeclines"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxReleases"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6TxReplies"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6TxReconfigures"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxInfRequests"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropBadPackets"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropInvldTypes"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropLseNotReady"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropNoSrvngPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropPerOverload"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6OffersIgnore"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropGenError"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropDestOther"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropMaxReached"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropSvrDown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6LeasesExpired"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6Advertise"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6Stable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6RCPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6RmPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6Declined"))
)
if mibBuilder.loadTexts:
    tmnxDhcpStatsV9v0Group.setStatus("current")

tmnxDhcpsNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 14)
)
tmnxDhcpsNotifyObjsV9v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrLen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifClientDUID"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsNotifyObjsV9v0Group.setStatus("current")

tmnxDhcpServerV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 15)
)
tmnxDhcpServerV10v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolDepletedEvent"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetDepletedEvent"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetFailCtrl"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgIgnRapidCommit"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUserIdent"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgItfIdMapping"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseRelayInterfaceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseLDRAInterfaceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseLnkLclAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseLnkLclAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetPrefixType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropDuplDiffRly"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV10v0Group.setStatus("current")

tmnxDhcpServerV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 16)
)
tmnxDhcpServerV11v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetDrain"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseCPDelimiter"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolDlgatedPfxLen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgCreationOrigin"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolSubnetBindKey"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolSubnetBindDly"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindSystemId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindServiceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindString"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindUnbindTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubntBndngTbleLastCh"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV11v0Group.setStatus("obsolete")

tmnxDhcpStatsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 17)
)
tmnxDhcpStatsV11v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsOffered"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsStable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFRPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsRemPending"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsDeclined"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoOffered"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoStable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFRPend"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoRemPend"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoDeclined"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsProv"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoProv"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsHasExt"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsExtResetT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsStableP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsStablePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoStableP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoStablePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsUsed"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsUsedP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsUsedPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoUsed"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoUsedP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoUsedPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFreeP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFreePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFreeP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFreePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsUsedPct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsUsedPctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsUsedPctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoUsdPct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoUsdPctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoUsdPctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFreePct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFreePctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFreePctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFrePct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFrePctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoFrePctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsOfferP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsOfferPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoOfferP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolStatsFoOfferPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxIntRequests"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsRxIntReleases"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropIntWithLudb"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropIntWithFo"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropIntConflicts"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6HasExt"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6ExtResetT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6StableP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6StablePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6ProvBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6UsedBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6UsedBlkP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6UsedBlkPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6FreeBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6FreeBlkP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6FreeBlkPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6UsedPct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6UsedPctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6UsedPctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6FreePct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6FreePctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6FreePctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6AdvertP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStats6AdvertPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6Stable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoStable"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6HasExt"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6ExtResetT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6StableP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6StablePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoStableP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoStablePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6ProvBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoProvBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6UsedBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6UsedBlkP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6UsedBlkPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoUsedBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoUsedBlkP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoUsedBlkPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FreeBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FreeBlkP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FreeBlkPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoFreeBlk"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoFreeBlkP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoFreeBlkPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6UsedPct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6UsedPctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6UsedPctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoUsedPct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoUsedPctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoUsedPctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FreePct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FreePctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FreePctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoFreePct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoFreePctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoFreePctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6Advertise"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6AdvertP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6AdvertPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoAdvertise"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoAdvertP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6FoAdvertPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6IntNoPfxWan"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolStats6IntNoPfxSlaa"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsHasExt"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsExtResetT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsStableP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsStablePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoStableP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoStablePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsUsed"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsUsedP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsUsedPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoUsed"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoUsedP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoUsedPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFreeP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFreePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoFreeP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoFreePT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsUsedPct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsUsedPctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsUsedPctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoUsdPct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoUsdPctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoUsdPctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFreePct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFreePctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFreePctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoFrePct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoFrePctP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoFrePctPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsOfferP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsOfferPT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoOfferP"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFoOfferPT"))
)
if mibBuilder.loadTexts:
    tmnxDhcpStatsV11v0Group.setStatus("current")

tmnxDhcpsFailoverV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 18)
)
tmnxDhcpsFailoverV11v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoIgnoreMclt"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoTableLastChanged"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoLastChanged"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoAdminState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoMCLT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoOperMCLT"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStartupWaitTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoPartnerDownDelay"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoTimeLeft"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoIgnoreMclt"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsLeaseNFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsDropInvPkts"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsFoShutdown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsExpired"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsMaxReached"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsSubnetNFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsRangeNFound"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsHostConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsAddrConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsPeerConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStatsPersistCong"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoActionPoolName"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsFailoverV11v0Group.setStatus("current")

tmnxDhcpServerDuidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 19)
)
tmnxDhcpServerDuidGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidTableLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidLastChanged"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidTypeCode"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidEnNumber"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidEnIdData"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidEnIdDataType"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerDuidGroup.setStatus("current")

tmnxDhcpsNotifyObjsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 20)
)
tmnxDhcpsNotifyObjsV11v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLinkAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPrimaryPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSecondaryPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSystemId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServiceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifString"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPoolName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfx"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfxlen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifUnbindTime"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsNotifyObjsV11v0Group.setStatus("current")

tmnxDhcpServerV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 21)
)
tmnxDhcpServerV12v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetDrain"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseCPDelimiter"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolDlgatedPfxLen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgCreationOrigin"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxIntPppSlaac"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxIntReqIpoeWan"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxIntReleases"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropIntWFo"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropIntWConflct"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropIntWIfIdMap"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropIntWUserId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6RxIntIpoeSlaac"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStatsDropAudit"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrStats6DropAudit"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV12v0Group.setStatus("current")

tmnxDhcpsFailoverV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 22)
)
tmnxDhcpsFailoverV10v0Group.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStatsPersistCongest")
)
if mibBuilder.loadTexts:
    tmnxDhcpsFailoverV10v0Group.setStatus("current")

tmnxDhcpLeaseV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 23)
)
tmnxDhcpLeaseV12v0Group.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseIntClientType")
)
if mibBuilder.loadTexts:
    tmnxDhcpLeaseV12v0Group.setStatus("current")

tmnxDhcpsObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 100)
)
tmnxDhcpsObsoleteGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolSubnetBindDly"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolSubnetBindKey"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindSystemId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindServiceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindString"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindUnbindTime"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindState"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubntBndngTbleLastCh"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindActive"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsObsoleteGroup.setStatus("current")


# Notification objects

tmnxDhcpSvrSubnetMinFreeExc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 1)
)
tmnxDhcpSvrSubnetMinFreeExc.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetStatsFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMinFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMinFreeType"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetMinFreeExc.setStatus(
        "current"
    )

tmnxDhcpSvrHostConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 2)
)
tmnxDhcpSvrHostConflict.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifUserDatabaseName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifHostType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifHostName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifDescription"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrHostConflict.setStatus(
        "current"
    )

tmnxDhcpSvrPoolUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 3)
)
tmnxDhcpSvrPoolUnknown.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifUnknownPoolName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifDescription"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolUnknown.setStatus(
        "current"
    )

tmnxDhcpSvrLeaseNotOwner = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 4)
)
tmnxDhcpSvrLeaseNotOwner.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgHwAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgOption82"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrLen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifClientDUID"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseNotOwner.setStatus(
        "current"
    )

tmnxDhcpSvrDeclineStaticAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 5)
)
tmnxDhcpSvrDeclineStaticAddr.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgHwAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgOption82"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrDeclineStaticAddr.setStatus(
        "current"
    )

tmnxDhcpSvrMsgTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 6)
)
tmnxDhcpSvrMsgTooLong.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgHwAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgOption82"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifMsgSizeLimit"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifClientDUID"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrMsgTooLong.setStatus(
        "current"
    )

tmnxDhcpsFoStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 7)
)
tmnxDhcpsFoStateChange.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoState")
)
if mibBuilder.loadTexts:
    tmnxDhcpsFoStateChange.setStatus(
        "current"
    )

tmnxDhcpsFoLeaseUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 8)
)
tmnxDhcpsFoLeaseUpdateFailed.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoLeaseFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsFoLeaseUpdateFailed.setStatus(
        "current"
    )

tmnxDhcpSvrUserDbUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 9)
)
tmnxDhcpSvrUserDbUnknown.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUserDatabase")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrUserDbUnknown.setStatus(
        "current"
    )

tmnxDhcpSvrMaxLeasesReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 10)
)
tmnxDhcpSvrMaxLeasesReached.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrMaxLeases")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrMaxLeasesReached.setStatus(
        "current"
    )

tmnxDhcpSvrNoSubnetFixAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 11)
)
tmnxDhcpSvrNoSubnetFixAddr.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifUserDatabaseName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifHostType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifHostName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrNoSubnetFixAddr.setStatus(
        "current"
    )

tmnxDhcpSvrLeaseDefaultTimers = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 12)
)
tmnxDhcpSvrLeaseDefaultTimers.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifDescription"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrLen"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseDefaultTimers.setStatus(
        "current"
    )

tmnxDhcpSvrPoolMinFreeExc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 13)
)
tmnxDhcpSvrPoolMinFreeExc.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPoolFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMinFree"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolMinFreeType"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolMinFreeExc.setStatus(
        "current"
    )

tmnxDhcpSvrSubnetDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 14)
)
tmnxDhcpSvrSubnetDepleted.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRowStatus")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetDepleted.setStatus(
        "current"
    )

tmnxDhcpSvrPoolDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 15)
)
tmnxDhcpSvrPoolDepleted.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolRowStatus")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrPoolDepleted.setStatus(
        "current"
    )

tmnxDhcpSvrIntLseConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 16)
)
tmnxDhcpSvrIntLseConflict.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifDescription"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrIntLseConflict.setStatus(
        "current"
    )

tmnxDhcpSvrLeaseModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 17)
)
tmnxDhcpSvrLeaseModify.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseStart")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseModify.setStatus(
        "current"
    )

tmnxDhcpSvrLeaseCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 18)
)
tmnxDhcpSvrLeaseCreate.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseStart")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseCreate.setStatus(
        "current"
    )

tmnxDhcpSvrLeaseDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 19)
)
tmnxDhcpSvrLeaseDelete.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseStart")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrLeaseDelete.setStatus(
        "current"
    )

tmnxDhcpSvrNoContFreeBlocks = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 20)
)
tmnxDhcpSvrNoContFreeBlocks.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseGiAddress"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerCfgUseClientPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLinkAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPrimaryPool"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSecondaryPool"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrNoContFreeBlocks.setStatus(
        "current"
    )

tmnxDhcpSvrSubnetBindingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 23)
)
tmnxDhcpSvrSubnetBindingFailed.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerPoolSubnetBindKey"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSystemId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServiceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifString"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindingFailed.setStatus(
        "obsolete"
    )

tmnxDhcpsPoolFoStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 24)
)
tmnxDhcpsPoolFoStateChange.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoState")
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoStateChange.setStatus(
        "current"
    )

tmnxDhcpsPoolFoLeaseUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 25)
)
tmnxDhcpsPoolFoLeaseUpdateFailed.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoLastChanged"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifLeaseClientAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoLeaseFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsPoolFoLeaseUpdateFailed.setStatus(
        "current"
    )

tmnxDhcpSvrSubnetBindingCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 26)
)
tmnxDhcpSvrSubnetBindingCreate.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPoolName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfx"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfxlen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSystemId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServiceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifString"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindingCreate.setStatus(
        "obsolete"
    )

tmnxDhcpSvrSubnetBindingUnbind = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 27)
)
tmnxDhcpSvrSubnetBindingUnbind.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPoolName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfx"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfxlen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSystemId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServiceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifString"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifUnbindTime"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindingUnbind.setStatus(
        "obsolete"
    )

tmnxDhcpSvrSubnetBindingDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 28)
)
tmnxDhcpSvrSubnetBindingDelete.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifVRtrID"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServerName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifPoolName"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetAddrType"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfx"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSubnetPfxlen"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifSystemId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifServiceId"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifString"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetBindingDelete.setStatus(
        "obsolete"
    )

tmnxDhcpSvrSubnetFailCtrlError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 47, 0, 29)
)
tmnxDhcpSvrSubnetFailCtrlError.setObjects(
    ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetRowStatus")
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrSubnetFailCtrlError.setStatus(
        "obsolete"
    )


# Notifications groups

tmnxDhcpsObsoletedNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 2, 99)
)
tmnxDhcpsObsoletedNotifyGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingCreate"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingDelete"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingFailed"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingUnbind"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetFailCtrlError"))
)
if mibBuilder.loadTexts:
    tmnxDhcpsObsoletedNotifyGroup.setStatus(
        "current"
    )

tmnxDhcpSvrNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 3, 1)
)
tmnxDhcpSvrNotifGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetMinFreeExc"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrHostConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolUnknown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseNotOwner"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrDeclineStaticAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrMsgTooLong"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrUserDbUnknown"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrMaxLeasesReached"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNoSubnetFixAddr"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseDefaultTimers"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolMinFreeExc"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifGroup.setStatus(
        "current"
    )

tmnxDhcpSvrFoNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 3, 2)
)
tmnxDhcpSvrFoNotifGroup.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoStateChange"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFoLeaseUpdateFailed"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrFoNotifGroup.setStatus(
        "current"
    )

tmnxDhcpSvrNotifV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 3, 3)
)
tmnxDhcpSvrNotifV10v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetDepleted"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrPoolDepleted"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifV10v0Group.setStatus(
        "current"
    )

tmnxDhcpSvrNotifV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 3, 4)
)
tmnxDhcpSvrNotifV11v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrIntLseConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseModify"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseCreate"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseDelete"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNoContFreeBlocks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingFailed"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetFailCtrlError"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStateChange"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoLeaseUpdateFailed"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingCreate"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingUnbind"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrSubnetBindingDelete"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifV11v0Group.setStatus(
        "obsolete"
    )

tmnxDhcpSvrNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 3, 5)
)
tmnxDhcpSvrNotifV12v0Group.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrIntLseConflict"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseModify"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseCreate"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrLeaseDelete"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNoContFreeBlocks"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoStateChange"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsPoolFoLeaseUpdateFailed"))
)
if mibBuilder.loadTexts:
    tmnxDhcpSvrNotifV12v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDhcpServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1, 1)
)
tmnxDhcpServerCompliance.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpAddrListGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpToolsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFoNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerCompliance.setStatus(
        "obsolete"
    )

tmnxDhcpServerV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1, 2)
)
tmnxDhcpServerV6v1Compliance.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV6v1Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV6v1Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpAddrListGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpToolsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFoNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxDhcpServerV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1, 3)
)
tmnxDhcpServerV8v0Compliance.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpAddrListGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpToolsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFoNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxDhcpServerV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1, 4)
)
tmnxDhcpServerV9v0Compliance.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpAddrListGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpToolsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFoNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxDhcpServerV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1, 5)
)
tmnxDhcpServerV10v0Compliance.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV10v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpAddrListGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpToolsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifV10v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFoNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxDhcpServerV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1, 6)
)
tmnxDhcpServerV11v0Compliance.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV10v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV11v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpAddrListGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpToolsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifV10v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifV11v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverV11v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFoNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxDhcpServerV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 47, 1, 7)
)
tmnxDhcpServerV12v0Compliance.setObjects(
      *(("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV10v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerV12v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpServerDuidGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpLeaseV12v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV8v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV9v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpAddrListGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpToolsGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifV10v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrNotifV12v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverV10v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpsFailoverV11v0Group"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpSvrFoNotifGroup"),
        ("TIMETRA-DHCP-SERVER-MIB", "tmnxDhcpStatsV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDhcpServerV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DHCP-SERVER-MIB",
    **{"TmnxDhcpSvrOperState": TmnxDhcpSvrOperState,
       "TmnxDhcpSvrClientType": TmnxDhcpSvrClientType,
       "TmnxDhcpSvrFailCtrlType": TmnxDhcpSvrFailCtrlType,
       "TmnxDhcpsFoState": TmnxDhcpsFoState,
       "TmnxDhcpsFoLeaseFailureReason": TmnxDhcpsFoLeaseFailureReason,
       "TmnxDhcpsFoActionType": TmnxDhcpsFoActionType,
       "timetraDhcpServerMIBModule": timetraDhcpServerMIBModule,
       "tmnxDhcpServerConformance": tmnxDhcpServerConformance,
       "tmnxDhcpServerCompliances": tmnxDhcpServerCompliances,
       "tmnxDhcpServerCompliance": tmnxDhcpServerCompliance,
       "tmnxDhcpServerV6v1Compliance": tmnxDhcpServerV6v1Compliance,
       "tmnxDhcpServerV8v0Compliance": tmnxDhcpServerV8v0Compliance,
       "tmnxDhcpServerV9v0Compliance": tmnxDhcpServerV9v0Compliance,
       "tmnxDhcpServerV10v0Compliance": tmnxDhcpServerV10v0Compliance,
       "tmnxDhcpServerV11v0Compliance": tmnxDhcpServerV11v0Compliance,
       "tmnxDhcpServerV12v0Compliance": tmnxDhcpServerV12v0Compliance,
       "tmnxDhcpServerGroups": tmnxDhcpServerGroups,
       "tmnxDhcpServerGroup": tmnxDhcpServerGroup,
       "tmnxDhcpLeaseGroup": tmnxDhcpLeaseGroup,
       "tmnxDhcpStatsGroup": tmnxDhcpStatsGroup,
       "tmnxDhcpAddrListGroup": tmnxDhcpAddrListGroup,
       "tmnxDhcpToolsGroup": tmnxDhcpToolsGroup,
       "tmnxDhcpsFailoverGroup": tmnxDhcpsFailoverGroup,
       "tmnxDhcpsNotifyObjsGroup": tmnxDhcpsNotifyObjsGroup,
       "tmnxDhcpServerV6v1Group": tmnxDhcpServerV6v1Group,
       "tmnxDhcpStatsV6v1Group": tmnxDhcpStatsV6v1Group,
       "tmnxDhcpServerV8v0Group": tmnxDhcpServerV8v0Group,
       "tmnxDhcpStatsV8v0Group": tmnxDhcpStatsV8v0Group,
       "tmnxDhcpServerV9v0Group": tmnxDhcpServerV9v0Group,
       "tmnxDhcpStatsV9v0Group": tmnxDhcpStatsV9v0Group,
       "tmnxDhcpsNotifyObjsV9v0Group": tmnxDhcpsNotifyObjsV9v0Group,
       "tmnxDhcpServerV10v0Group": tmnxDhcpServerV10v0Group,
       "tmnxDhcpServerV11v0Group": tmnxDhcpServerV11v0Group,
       "tmnxDhcpStatsV11v0Group": tmnxDhcpStatsV11v0Group,
       "tmnxDhcpsFailoverV11v0Group": tmnxDhcpsFailoverV11v0Group,
       "tmnxDhcpServerDuidGroup": tmnxDhcpServerDuidGroup,
       "tmnxDhcpsNotifyObjsV11v0Group": tmnxDhcpsNotifyObjsV11v0Group,
       "tmnxDhcpServerV12v0Group": tmnxDhcpServerV12v0Group,
       "tmnxDhcpsFailoverV10v0Group": tmnxDhcpsFailoverV10v0Group,
       "tmnxDhcpLeaseV12v0Group": tmnxDhcpLeaseV12v0Group,
       "tmnxDhcpsObsoletedNotifyGroup": tmnxDhcpsObsoletedNotifyGroup,
       "tmnxDhcpsObsoleteGroup": tmnxDhcpsObsoleteGroup,
       "tmnxDhcpServerNotifGroups": tmnxDhcpServerNotifGroups,
       "tmnxDhcpSvrNotifGroup": tmnxDhcpSvrNotifGroup,
       "tmnxDhcpSvrFoNotifGroup": tmnxDhcpSvrFoNotifGroup,
       "tmnxDhcpSvrNotifV10v0Group": tmnxDhcpSvrNotifV10v0Group,
       "tmnxDhcpSvrNotifV11v0Group": tmnxDhcpSvrNotifV11v0Group,
       "tmnxDhcpSvrNotifV12v0Group": tmnxDhcpSvrNotifV12v0Group,
       "tmnxDhcpServer": tmnxDhcpServer,
       "tmnxDhcpServerObjs": tmnxDhcpServerObjs,
       "tmnxDhcpServerConfigTableLastCh": tmnxDhcpServerConfigTableLastCh,
       "tmnxDhcpServerConfigTable": tmnxDhcpServerConfigTable,
       "tmnxDhcpServerConfigEntry": tmnxDhcpServerConfigEntry,
       "tmnxDhcpServerCfgServerName": tmnxDhcpServerCfgServerName,
       "tmnxDhcpServerCfgRowStatus": tmnxDhcpServerCfgRowStatus,
       "tmnxDhcpServerCfgLastChangeTime": tmnxDhcpServerCfgLastChangeTime,
       "tmnxDhcpServerCfgAdminState": tmnxDhcpServerCfgAdminState,
       "tmnxDhcpServerCfgDescription": tmnxDhcpServerCfgDescription,
       "tmnxDhcpServerCfgUserDatabase": tmnxDhcpServerCfgUserDatabase,
       "tmnxDhcpServerCfgUseGiAddress": tmnxDhcpServerCfgUseGiAddress,
       "tmnxDhcpServerCfgSendForceRenews": tmnxDhcpServerCfgSendForceRenews,
       "tmnxDhcpServerCfgUseClientPool": tmnxDhcpServerCfgUseClientPool,
       "tmnxDhcpServerCfgOperState": tmnxDhcpServerCfgOperState,
       "tmnxDhcpServerCfgAddrType": tmnxDhcpServerCfgAddrType,
       "tmnxDhcpServerCfgLeaseHoldTime": tmnxDhcpServerCfgLeaseHoldTime,
       "tmnxDhcpServerCfgUseGiScope": tmnxDhcpServerCfgUseGiScope,
       "tmnxDhcpServerCfgIgnRapidCommit": tmnxDhcpServerCfgIgnRapidCommit,
       "tmnxDhcpServerCfgUserIdent": tmnxDhcpServerCfgUserIdent,
       "tmnxDhcpServerCfgItfIdMapping": tmnxDhcpServerCfgItfIdMapping,
       "tmnxDhcpServerCfgUseCPDelimiter": tmnxDhcpServerCfgUseCPDelimiter,
       "tmnxDhcpServerCfgCreationOrigin": tmnxDhcpServerCfgCreationOrigin,
       "tmnxDhcpServerPoolTableLastCh": tmnxDhcpServerPoolTableLastCh,
       "tmnxDhcpServerPoolTable": tmnxDhcpServerPoolTable,
       "tmnxDhcpServerPoolEntry": tmnxDhcpServerPoolEntry,
       "tmnxDhcpServerPoolName": tmnxDhcpServerPoolName,
       "tmnxDhcpServerPoolRowStatus": tmnxDhcpServerPoolRowStatus,
       "tmnxDhcpServerPoolLastChangeTime": tmnxDhcpServerPoolLastChangeTime,
       "tmnxDhcpServerPoolDescription": tmnxDhcpServerPoolDescription,
       "tmnxDhcpServerPoolMinLeaseTime": tmnxDhcpServerPoolMinLeaseTime,
       "tmnxDhcpServerPoolMaxLeaseTime": tmnxDhcpServerPoolMaxLeaseTime,
       "tmnxDhcpServerPoolOfferTime": tmnxDhcpServerPoolOfferTime,
       "tmnxDhcpServerPoolMinFree": tmnxDhcpServerPoolMinFree,
       "tmnxDhcpServerPoolMinFreeType": tmnxDhcpServerPoolMinFreeType,
       "tmnxDhcpServerPoolDepletedEvent": tmnxDhcpServerPoolDepletedEvent,
       "tmnxDhcpServerPoolDlgatedPfxLen": tmnxDhcpServerPoolDlgatedPfxLen,
       "tmnxDhcpServerPoolSubnetBindKey": tmnxDhcpServerPoolSubnetBindKey,
       "tmnxDhcpServerPoolSubnetBindDly": tmnxDhcpServerPoolSubnetBindDly,
       "tmnxDhcpSvrPoolOptionTableLastCh": tmnxDhcpSvrPoolOptionTableLastCh,
       "tmnxDhcpSvrPoolOptionTable": tmnxDhcpSvrPoolOptionTable,
       "tmnxDhcpSvrPoolOptionEntry": tmnxDhcpSvrPoolOptionEntry,
       "tmnxDhcpSvrPoolOptionNumber": tmnxDhcpSvrPoolOptionNumber,
       "tmnxDhcpSvrPoolOptionRowStatus": tmnxDhcpSvrPoolOptionRowStatus,
       "tmnxDhcpSvrPoolOptionLastCh": tmnxDhcpSvrPoolOptionLastCh,
       "tmnxDhcpSvrPoolOptionType": tmnxDhcpSvrPoolOptionType,
       "tmnxDhcpSvrPoolOptionValue": tmnxDhcpSvrPoolOptionValue,
       "tmnxDhcpServerSubnetTableLastCh": tmnxDhcpServerSubnetTableLastCh,
       "tmnxDhcpServerSubnetTable": tmnxDhcpServerSubnetTable,
       "tmnxDhcpServerSubnetEntry": tmnxDhcpServerSubnetEntry,
       "tmnxDhcpSvrSubnetAddrType": tmnxDhcpSvrSubnetAddrType,
       "tmnxDhcpSvrSubnetAddress": tmnxDhcpSvrSubnetAddress,
       "tmnxDhcpSvrSubnetPrefixLength": tmnxDhcpSvrSubnetPrefixLength,
       "tmnxDhcpSvrSubnetRowStatus": tmnxDhcpSvrSubnetRowStatus,
       "tmnxDhcpSvrSubnetLastChangeTime": tmnxDhcpSvrSubnetLastChangeTime,
       "tmnxDhcpSvrSubnetMinFree": tmnxDhcpSvrSubnetMinFree,
       "tmnxDhcpSvrSubnetMaxDeclined": tmnxDhcpSvrSubnetMaxDeclined,
       "tmnxDhcpSvrSubnetMinFreeType": tmnxDhcpSvrSubnetMinFreeType,
       "tmnxDhcpSvrSubnetRenewTimer": tmnxDhcpSvrSubnetRenewTimer,
       "tmnxDhcpSvrSubnetRebindTimer": tmnxDhcpSvrSubnetRebindTimer,
       "tmnxDhcpSvrSubnetValidLifetime": tmnxDhcpSvrSubnetValidLifetime,
       "tmnxDhcpSvrSubnetPrefLifetime": tmnxDhcpSvrSubnetPrefLifetime,
       "tmnxDhcpSvrSubnetFailCtrl": tmnxDhcpSvrSubnetFailCtrl,
       "tmnxDhcpSvrSubnetPrefixType": tmnxDhcpSvrSubnetPrefixType,
       "tmnxDhcpSvrSubnetDepletedEvent": tmnxDhcpSvrSubnetDepletedEvent,
       "tmnxDhcpSvrSubnetDrain": tmnxDhcpSvrSubnetDrain,
       "tmnxDhcpSvrSubnetRangesTblLastCh": tmnxDhcpSvrSubnetRangesTblLastCh,
       "tmnxDhcpSvrSubnetRangesTable": tmnxDhcpSvrSubnetRangesTable,
       "tmnxDhcpSvrSubnetRangesEntry": tmnxDhcpSvrSubnetRangesEntry,
       "tmnxDhcpSvrSubnetRangeType": tmnxDhcpSvrSubnetRangeType,
       "tmnxDhcpSvrSubnetStartAddrType": tmnxDhcpSvrSubnetStartAddrType,
       "tmnxDhcpSvrSubnetStartAddress": tmnxDhcpSvrSubnetStartAddress,
       "tmnxDhcpSvrSubnetEndAddrType": tmnxDhcpSvrSubnetEndAddrType,
       "tmnxDhcpSvrSubnetEndAddress": tmnxDhcpSvrSubnetEndAddress,
       "tmnxDhcpSvrSubnetRangesRowStatus": tmnxDhcpSvrSubnetRangesRowStatus,
       "tmnxDhcpSvrSubnetRangesLastCh": tmnxDhcpSvrSubnetRangesLastCh,
       "tmnxDhcpSvrSubnetRangeFailCtrl": tmnxDhcpSvrSubnetRangeFailCtrl,
       "tmnxDhcpSvrSubnetOptionTblLastCh": tmnxDhcpSvrSubnetOptionTblLastCh,
       "tmnxDhcpSvrSubnetOptionTable": tmnxDhcpSvrSubnetOptionTable,
       "tmnxDhcpSvrSubnetOptionEntry": tmnxDhcpSvrSubnetOptionEntry,
       "tmnxDhcpSvrSubnetOptionNumber": tmnxDhcpSvrSubnetOptionNumber,
       "tmnxDhcpSvrSubnetOptionRowStatus": tmnxDhcpSvrSubnetOptionRowStatus,
       "tmnxDhcpSvrSubnetOptionLastCh": tmnxDhcpSvrSubnetOptionLastCh,
       "tmnxDhcpSvrSubnetOptionType": tmnxDhcpSvrSubnetOptionType,
       "tmnxDhcpSvrSubnetOptionValue": tmnxDhcpSvrSubnetOptionValue,
       "tmnxDhcpSvrLeaseTable": tmnxDhcpSvrLeaseTable,
       "tmnxDhcpSvrLeaseEntry": tmnxDhcpSvrLeaseEntry,
       "tmnxDhcpSvrLeaseClientAddrType": tmnxDhcpSvrLeaseClientAddrType,
       "tmnxDhcpSvrLeaseClientAddress": tmnxDhcpSvrLeaseClientAddress,
       "tmnxDhcpSvrLeaseState": tmnxDhcpSvrLeaseState,
       "tmnxDhcpSvrLeaseStart": tmnxDhcpSvrLeaseStart,
       "tmnxDhcpSvrLeaseLastRenew": tmnxDhcpSvrLeaseLastRenew,
       "tmnxDhcpSvrLeaseRemainLeaseTime": tmnxDhcpSvrLeaseRemainLeaseTime,
       "tmnxDhcpSvrLeaseRemPotentExpTime": tmnxDhcpSvrLeaseRemPotentExpTime,
       "tmnxDhcpSvrLeaseClientHwAddress": tmnxDhcpSvrLeaseClientHwAddress,
       "tmnxDhcpSvrLeaseXid": tmnxDhcpSvrLeaseXid,
       "tmnxDhcpSvrLeaseOption82": tmnxDhcpSvrLeaseOption82,
       "tmnxDhcpSvrLeaseClientType": tmnxDhcpSvrLeaseClientType,
       "tmnxDhcpSvrLeasePPPoEUserName": tmnxDhcpSvrLeasePPPoEUserName,
       "tmnxDhcpSvrLeaseOpt82CircId": tmnxDhcpSvrLeaseOpt82CircId,
       "tmnxDhcpSvrLeaseFailCtrl": tmnxDhcpSvrLeaseFailCtrl,
       "tmnxDhcpSvrLeaseOption60": tmnxDhcpSvrLeaseOption60,
       "tmnxDhcpSvrLeaseClientPrefixLen": tmnxDhcpSvrLeaseClientPrefixLen,
       "tmnxDhcpSvrLeaseIAOptionType": tmnxDhcpSvrLeaseIAOptionType,
       "tmnxDhcpSvrLeaseIAID": tmnxDhcpSvrLeaseIAID,
       "tmnxDhcpSvrLeaseDUID": tmnxDhcpSvrLeaseDUID,
       "tmnxDhcpSvrLeaseRemainHoldTime": tmnxDhcpSvrLeaseRemainHoldTime,
       "tmnxDhcpSvrLeaseRelayInterfaceId": tmnxDhcpSvrLeaseRelayInterfaceId,
       "tmnxDhcpSvrLeaseLDRAInterfaceId": tmnxDhcpSvrLeaseLDRAInterfaceId,
       "tmnxDhcpSvrLeaseLnkLclAddrType": tmnxDhcpSvrLeaseLnkLclAddrType,
       "tmnxDhcpSvrLeaseLnkLclAddress": tmnxDhcpSvrLeaseLnkLclAddress,
       "tmnxDhcpSvrLeaseIntClientType": tmnxDhcpSvrLeaseIntClientType,
       "tmnxDhcpServerStatsTable": tmnxDhcpServerStatsTable,
       "tmnxDhcpServerStatsEntry": tmnxDhcpServerStatsEntry,
       "tmnxDhcpSvrStatsRxDiscovers": tmnxDhcpSvrStatsRxDiscovers,
       "tmnxDhcpSvrStatsRxRequests": tmnxDhcpSvrStatsRxRequests,
       "tmnxDhcpSvrStatsRxReleases": tmnxDhcpSvrStatsRxReleases,
       "tmnxDhcpSvrStatsRxDeclines": tmnxDhcpSvrStatsRxDeclines,
       "tmnxDhcpSvrStatsRxInforms": tmnxDhcpSvrStatsRxInforms,
       "tmnxDhcpSvrStatsTxOffers": tmnxDhcpSvrStatsTxOffers,
       "tmnxDhcpSvrStatsTxAcks": tmnxDhcpSvrStatsTxAcks,
       "tmnxDhcpSvrStatsTxNaks": tmnxDhcpSvrStatsTxNaks,
       "tmnxDhcpSvrStatsTxForceRenews": tmnxDhcpSvrStatsTxForceRenews,
       "tmnxDhcpSvrStatsDropBadPackets": tmnxDhcpSvrStatsDropBadPackets,
       "tmnxDhcpSvrStatsDropInvalidTypes": tmnxDhcpSvrStatsDropInvalidTypes,
       "tmnxDhcpSvrStatsDropNoUsrDbFound": tmnxDhcpSvrStatsDropNoUsrDbFound,
       "tmnxDhcpSvrStatsDropUnknownHosts": tmnxDhcpSvrStatsDropUnknownHosts,
       "tmnxDhcpSvrStatsDropUserNotAllow": tmnxDhcpSvrStatsDropUserNotAllow,
       "tmnxDhcpSvrStatsDropLseNotReady": tmnxDhcpSvrStatsDropLseNotReady,
       "tmnxDhcpSvrStatsDropNoLeaseFound": tmnxDhcpSvrStatsDropNoLeaseFound,
       "tmnxDhcpSvrStatsDropNotSrvngPool": tmnxDhcpSvrStatsDropNotSrvngPool,
       "tmnxDhcpSvrStatsDropInvalidUsr": tmnxDhcpSvrStatsDropInvalidUsr,
       "tmnxDhcpSvrStatsDropOverload": tmnxDhcpSvrStatsDropOverload,
       "tmnxDhcpSvrStatsDropPersOverload": tmnxDhcpSvrStatsDropPersOverload,
       "tmnxDhcpSvrStatsOffersIgnore": tmnxDhcpSvrStatsOffersIgnore,
       "tmnxDhcpSvrStatsDropGenError": tmnxDhcpSvrStatsDropGenError,
       "tmnxDhcpSvrStatsDropDestOther": tmnxDhcpSvrStatsDropDestOther,
       "tmnxDhcpSvrStatsDropAddrUnavail": tmnxDhcpSvrStatsDropAddrUnavail,
       "tmnxDhcpSvrStatsDropMaxReached": tmnxDhcpSvrStatsDropMaxReached,
       "tmnxDhcpSvrStatsDropSvrDown": tmnxDhcpSvrStatsDropSvrDown,
       "tmnxDhcpSvrStatsDropNoSubnet": tmnxDhcpSvrStatsDropNoSubnet,
       "tmnxDhcpSvrStatsLeasesExpired": tmnxDhcpSvrStatsLeasesExpired,
       "tmnxDhcpSvrStatsDropDuplDiffGi": tmnxDhcpSvrStatsDropDuplDiffGi,
       "tmnxDhcpSvrStatsRxIntRequests": tmnxDhcpSvrStatsRxIntRequests,
       "tmnxDhcpSvrStatsRxIntReleases": tmnxDhcpSvrStatsRxIntReleases,
       "tmnxDhcpSvrStatsDropIntWithLudb": tmnxDhcpSvrStatsDropIntWithLudb,
       "tmnxDhcpSvrStatsDropIntWithFo": tmnxDhcpSvrStatsDropIntWithFo,
       "tmnxDhcpSvrStatsDropIntConflicts": tmnxDhcpSvrStatsDropIntConflicts,
       "tmnxDhcpSvrStatsDropAudit": tmnxDhcpSvrStatsDropAudit,
       "tmnxDhcpSvrDeclinedAddrTable": tmnxDhcpSvrDeclinedAddrTable,
       "tmnxDhcpSvrDeclinedAddrEntry": tmnxDhcpSvrDeclinedAddrEntry,
       "tmnxDhcpSvrDeclinedAddrType": tmnxDhcpSvrDeclinedAddrType,
       "tmnxDhcpSvrDeclinedAddress": tmnxDhcpSvrDeclinedAddress,
       "tmnxDhcpSvrDeclinedAddrHwAddress": tmnxDhcpSvrDeclinedAddrHwAddress,
       "tmnxDhcpSvrDeclinedAddrAddedTime": tmnxDhcpSvrDeclinedAddrAddedTime,
       "tmnxDhcpSvrDeclinedAddrOption82": tmnxDhcpSvrDeclinedAddrOption82,
       "tmnxDhcpSvrDeclinedAddrClientType": tmnxDhcpSvrDeclinedAddrClientType,
       "tmnxDhcpSvrDeclinedAddrUserName": tmnxDhcpSvrDeclinedAddrUserName,
       "tmnxDhcpSvrDeclinedAddrCircId": tmnxDhcpSvrDeclinedAddrCircId,
       "tmnxDhcpSvrSubnetStatsTable": tmnxDhcpSvrSubnetStatsTable,
       "tmnxDhcpSvrSubnetStatsEntry": tmnxDhcpSvrSubnetStatsEntry,
       "tmnxDhcpSvrSubnetStatsFree": tmnxDhcpSvrSubnetStatsFree,
       "tmnxDhcpSvrSubnetStatsOffered": tmnxDhcpSvrSubnetStatsOffered,
       "tmnxDhcpSvrSubnetStatsStable": tmnxDhcpSvrSubnetStatsStable,
       "tmnxDhcpSvrSubnetStatsFRPending": tmnxDhcpSvrSubnetStatsFRPending,
       "tmnxDhcpSvrSubnetStatsRemPending": tmnxDhcpSvrSubnetStatsRemPending,
       "tmnxDhcpSvrSubnetStatsDeclined": tmnxDhcpSvrSubnetStatsDeclined,
       "tmnxDhcpSvrSubnetStatsFoFree": tmnxDhcpSvrSubnetStatsFoFree,
       "tmnxDhcpSvrSubnetStatsFoOffered": tmnxDhcpSvrSubnetStatsFoOffered,
       "tmnxDhcpSvrSubnetStatsFoStable": tmnxDhcpSvrSubnetStatsFoStable,
       "tmnxDhcpSvrSubnetStatsFoFRPend": tmnxDhcpSvrSubnetStatsFoFRPend,
       "tmnxDhcpSvrSubnetStatsFoRemPend": tmnxDhcpSvrSubnetStatsFoRemPend,
       "tmnxDhcpSvrSubnetStatsFoDeclined": tmnxDhcpSvrSubnetStatsFoDeclined,
       "tmnxDhcpSvrSubnetStatsProv": tmnxDhcpSvrSubnetStatsProv,
       "tmnxDhcpSvrSubnetStatsFoProv": tmnxDhcpSvrSubnetStatsFoProv,
       "tmnxDhcpSvrSubnetStatsHasExt": tmnxDhcpSvrSubnetStatsHasExt,
       "tmnxDhcpSvrSubnetStatsExtResetT": tmnxDhcpSvrSubnetStatsExtResetT,
       "tmnxDhcpSvrSubnetStatsStableP": tmnxDhcpSvrSubnetStatsStableP,
       "tmnxDhcpSvrSubnetStatsStablePT": tmnxDhcpSvrSubnetStatsStablePT,
       "tmnxDhcpSvrSubnetStatsFoStableP": tmnxDhcpSvrSubnetStatsFoStableP,
       "tmnxDhcpSvrSubnetStatsFoStablePT": tmnxDhcpSvrSubnetStatsFoStablePT,
       "tmnxDhcpSvrSubnetStatsUsed": tmnxDhcpSvrSubnetStatsUsed,
       "tmnxDhcpSvrSubnetStatsUsedP": tmnxDhcpSvrSubnetStatsUsedP,
       "tmnxDhcpSvrSubnetStatsUsedPT": tmnxDhcpSvrSubnetStatsUsedPT,
       "tmnxDhcpSvrSubnetStatsFoUsed": tmnxDhcpSvrSubnetStatsFoUsed,
       "tmnxDhcpSvrSubnetStatsFoUsedP": tmnxDhcpSvrSubnetStatsFoUsedP,
       "tmnxDhcpSvrSubnetStatsFoUsedPT": tmnxDhcpSvrSubnetStatsFoUsedPT,
       "tmnxDhcpSvrSubnetStatsFreeP": tmnxDhcpSvrSubnetStatsFreeP,
       "tmnxDhcpSvrSubnetStatsFreePT": tmnxDhcpSvrSubnetStatsFreePT,
       "tmnxDhcpSvrSubnetStatsFoFreeP": tmnxDhcpSvrSubnetStatsFoFreeP,
       "tmnxDhcpSvrSubnetStatsFoFreePT": tmnxDhcpSvrSubnetStatsFoFreePT,
       "tmnxDhcpSvrSubnetStatsUsedPct": tmnxDhcpSvrSubnetStatsUsedPct,
       "tmnxDhcpSvrSubnetStatsUsedPctP": tmnxDhcpSvrSubnetStatsUsedPctP,
       "tmnxDhcpSvrSubnetStatsUsedPctPT": tmnxDhcpSvrSubnetStatsUsedPctPT,
       "tmnxDhcpSvrSubnetStatsFoUsdPct": tmnxDhcpSvrSubnetStatsFoUsdPct,
       "tmnxDhcpSvrSubnetStatsFoUsdPctP": tmnxDhcpSvrSubnetStatsFoUsdPctP,
       "tmnxDhcpSvrSubnetStatsFoUsdPctPT": tmnxDhcpSvrSubnetStatsFoUsdPctPT,
       "tmnxDhcpSvrSubnetStatsFreePct": tmnxDhcpSvrSubnetStatsFreePct,
       "tmnxDhcpSvrSubnetStatsFreePctP": tmnxDhcpSvrSubnetStatsFreePctP,
       "tmnxDhcpSvrSubnetStatsFreePctPT": tmnxDhcpSvrSubnetStatsFreePctPT,
       "tmnxDhcpSvrSubnetStatsFoFrePct": tmnxDhcpSvrSubnetStatsFoFrePct,
       "tmnxDhcpSvrSubnetStatsFoFrePctP": tmnxDhcpSvrSubnetStatsFoFrePctP,
       "tmnxDhcpSvrSubnetStatsFoFrePctPT": tmnxDhcpSvrSubnetStatsFoFrePctPT,
       "tmnxDhcpSvrSubnetStatsOfferP": tmnxDhcpSvrSubnetStatsOfferP,
       "tmnxDhcpSvrSubnetStatsOfferPT": tmnxDhcpSvrSubnetStatsOfferPT,
       "tmnxDhcpSvrSubnetStatsFoOfferP": tmnxDhcpSvrSubnetStatsFoOfferP,
       "tmnxDhcpSvrSubnetStatsFoOfferPT": tmnxDhcpSvrSubnetStatsFoOfferPT,
       "tmnxDhcpsFailoverObjs": tmnxDhcpsFailoverObjs,
       "tmnxDhcpsFoTableLastChanged": tmnxDhcpsFoTableLastChanged,
       "tmnxDhcpsFoTable": tmnxDhcpsFoTable,
       "tmnxDhcpsFoEntry": tmnxDhcpsFoEntry,
       "tmnxDhcpsFoLastChanged": tmnxDhcpsFoLastChanged,
       "tmnxDhcpsFoAdminState": tmnxDhcpsFoAdminState,
       "tmnxDhcpsFoMaxClientLeadTime": tmnxDhcpsFoMaxClientLeadTime,
       "tmnxDhcpsFoOperMaxClientLeadTime": tmnxDhcpsFoOperMaxClientLeadTime,
       "tmnxDhcpsFoStartupWaitTime": tmnxDhcpsFoStartupWaitTime,
       "tmnxDhcpsFoPartnerDownDelay": tmnxDhcpsFoPartnerDownDelay,
       "tmnxDhcpsFoState": tmnxDhcpsFoState,
       "tmnxDhcpsFoTimeLeft": tmnxDhcpsFoTimeLeft,
       "tmnxDhcpsFoIgnoreMclt": tmnxDhcpsFoIgnoreMclt,
       "tmnxDhcpsFoStatsTable": tmnxDhcpsFoStatsTable,
       "tmnxDhcpsFoStatsEntry": tmnxDhcpsFoStatsEntry,
       "tmnxDhcpsFoStatsLeaseNotFound": tmnxDhcpsFoStatsLeaseNotFound,
       "tmnxDhcpsFoStatsDropInvalidPkts": tmnxDhcpsFoStatsDropInvalidPkts,
       "tmnxDhcpsFoStatsFoShutdown": tmnxDhcpsFoStatsFoShutdown,
       "tmnxDhcpsFoStatsExpired": tmnxDhcpsFoStatsExpired,
       "tmnxDhcpsFoStatsMaxReached": tmnxDhcpsFoStatsMaxReached,
       "tmnxDhcpsFoStatsSubnetNotFound": tmnxDhcpsFoStatsSubnetNotFound,
       "tmnxDhcpsFoStatsRangeNotFound": tmnxDhcpsFoStatsRangeNotFound,
       "tmnxDhcpsFoStatsHostConflict": tmnxDhcpsFoStatsHostConflict,
       "tmnxDhcpsFoStatsAddressConflict": tmnxDhcpsFoStatsAddressConflict,
       "tmnxDhcpsFoStatsPeerConflict": tmnxDhcpsFoStatsPeerConflict,
       "tmnxDhcpsFoStatsPersistCongest": tmnxDhcpsFoStatsPersistCongest,
       "tmnxDhcpsFoAction": tmnxDhcpsFoAction,
       "tmnxDhcpsFoActionVRtrId": tmnxDhcpsFoActionVRtrId,
       "tmnxDhcpsFoActionServerName": tmnxDhcpsFoActionServerName,
       "tmnxDhcpsFoActionType": tmnxDhcpsFoActionType,
       "tmnxDhcpsFoActionGo": tmnxDhcpsFoActionGo,
       "tmnxDhcpsFoActionSuccessful": tmnxDhcpsFoActionSuccessful,
       "tmnxDhcpsFoActionErrorMsg": tmnxDhcpsFoActionErrorMsg,
       "tmnxDhcpsFoActionTime": tmnxDhcpsFoActionTime,
       "tmnxDhcpsFoActionPoolName": tmnxDhcpsFoActionPoolName,
       "tmnxDhcpsPoolFoTableLastChanged": tmnxDhcpsPoolFoTableLastChanged,
       "tmnxDhcpsPoolFoTable": tmnxDhcpsPoolFoTable,
       "tmnxDhcpsPoolFoEntry": tmnxDhcpsPoolFoEntry,
       "tmnxDhcpsPoolFoLastChanged": tmnxDhcpsPoolFoLastChanged,
       "tmnxDhcpsPoolFoAdminState": tmnxDhcpsPoolFoAdminState,
       "tmnxDhcpsPoolFoMCLT": tmnxDhcpsPoolFoMCLT,
       "tmnxDhcpsPoolFoOperMCLT": tmnxDhcpsPoolFoOperMCLT,
       "tmnxDhcpsPoolFoStartupWaitTime": tmnxDhcpsPoolFoStartupWaitTime,
       "tmnxDhcpsPoolFoPartnerDownDelay": tmnxDhcpsPoolFoPartnerDownDelay,
       "tmnxDhcpsPoolFoState": tmnxDhcpsPoolFoState,
       "tmnxDhcpsPoolFoTimeLeft": tmnxDhcpsPoolFoTimeLeft,
       "tmnxDhcpsPoolFoIgnoreMclt": tmnxDhcpsPoolFoIgnoreMclt,
       "tmnxDhcpsPoolFoStatsTable": tmnxDhcpsPoolFoStatsTable,
       "tmnxDhcpsPoolFoStatsEntry": tmnxDhcpsPoolFoStatsEntry,
       "tmnxDhcpsPoolFoStatsLeaseNFound": tmnxDhcpsPoolFoStatsLeaseNFound,
       "tmnxDhcpsPoolFoStatsDropInvPkts": tmnxDhcpsPoolFoStatsDropInvPkts,
       "tmnxDhcpsPoolFoStatsFoShutdown": tmnxDhcpsPoolFoStatsFoShutdown,
       "tmnxDhcpsPoolFoStatsExpired": tmnxDhcpsPoolFoStatsExpired,
       "tmnxDhcpsPoolFoStatsMaxReached": tmnxDhcpsPoolFoStatsMaxReached,
       "tmnxDhcpsPoolFoStatsSubnetNFound": tmnxDhcpsPoolFoStatsSubnetNFound,
       "tmnxDhcpsPoolFoStatsRangeNFound": tmnxDhcpsPoolFoStatsRangeNFound,
       "tmnxDhcpsPoolFoStatsHostConflict": tmnxDhcpsPoolFoStatsHostConflict,
       "tmnxDhcpsPoolFoStatsAddrConflict": tmnxDhcpsPoolFoStatsAddrConflict,
       "tmnxDhcpsPoolFoStatsPeerConflict": tmnxDhcpsPoolFoStatsPeerConflict,
       "tmnxDhcpsPoolFoStatsPersistCong": tmnxDhcpsPoolFoStatsPersistCong,
       "tmnxDhcpSvrFreeAddrTable": tmnxDhcpSvrFreeAddrTable,
       "tmnxDhcpSvrFreeAddrEntry": tmnxDhcpSvrFreeAddrEntry,
       "tmnxDhcpSvrFreeAddrType": tmnxDhcpSvrFreeAddrType,
       "tmnxDhcpSvrFreeAddress": tmnxDhcpSvrFreeAddress,
       "tmnxDhcpSvrFreeAddrFailCtrl": tmnxDhcpSvrFreeAddrFailCtrl,
       "tmnxDhcpSvrActionTable": tmnxDhcpSvrActionTable,
       "tmnxDhcpSvrActionEntry": tmnxDhcpSvrActionEntry,
       "tmnxDhcpSvrActForceRenewAddrType": tmnxDhcpSvrActForceRenewAddrType,
       "tmnxDhcpSvrActForceRenewAddr": tmnxDhcpSvrActForceRenewAddr,
       "tmnxDhcpSvrNumLeases": tmnxDhcpSvrNumLeases,
       "tmnxDhcpSvrMaxLeases": tmnxDhcpSvrMaxLeases,
       "tmnxDhcpServerStats6Table": tmnxDhcpServerStats6Table,
       "tmnxDhcpServerStats6Entry": tmnxDhcpServerStats6Entry,
       "tmnxDhcpSvrStats6RxSolicits": tmnxDhcpSvrStats6RxSolicits,
       "tmnxDhcpSvrStats6TxAdvertises": tmnxDhcpSvrStats6TxAdvertises,
       "tmnxDhcpSvrStats6RxRequests": tmnxDhcpSvrStats6RxRequests,
       "tmnxDhcpSvrStats6RxConfirms": tmnxDhcpSvrStats6RxConfirms,
       "tmnxDhcpSvrStats6RxRenews": tmnxDhcpSvrStats6RxRenews,
       "tmnxDhcpSvrStats6RxRebinds": tmnxDhcpSvrStats6RxRebinds,
       "tmnxDhcpSvrStats6RxDeclines": tmnxDhcpSvrStats6RxDeclines,
       "tmnxDhcpSvrStats6RxReleases": tmnxDhcpSvrStats6RxReleases,
       "tmnxDhcpSvrStats6TxReplies": tmnxDhcpSvrStats6TxReplies,
       "tmnxDhcpSvrStats6TxReconfigures": tmnxDhcpSvrStats6TxReconfigures,
       "tmnxDhcpSvrStats6RxInfRequests": tmnxDhcpSvrStats6RxInfRequests,
       "tmnxDhcpSvrStats6DropBadPackets": tmnxDhcpSvrStats6DropBadPackets,
       "tmnxDhcpSvrStats6DropInvldTypes": tmnxDhcpSvrStats6DropInvldTypes,
       "tmnxDhcpSvrStats6DropLseNotReady": tmnxDhcpSvrStats6DropLseNotReady,
       "tmnxDhcpSvrStats6DropNoSrvngPool": tmnxDhcpSvrStats6DropNoSrvngPool,
       "tmnxDhcpSvrStats6DropOverload": tmnxDhcpSvrStats6DropOverload,
       "tmnxDhcpSvrStats6DropPerOverload": tmnxDhcpSvrStats6DropPerOverload,
       "tmnxDhcpSvrStats6OffersIgnore": tmnxDhcpSvrStats6OffersIgnore,
       "tmnxDhcpSvrStats6DropGenError": tmnxDhcpSvrStats6DropGenError,
       "tmnxDhcpSvrStats6DropDestOther": tmnxDhcpSvrStats6DropDestOther,
       "tmnxDhcpSvrStats6DropMaxReached": tmnxDhcpSvrStats6DropMaxReached,
       "tmnxDhcpSvrStats6DropSvrDown": tmnxDhcpSvrStats6DropSvrDown,
       "tmnxDhcpSvrStats6LeasesExpired": tmnxDhcpSvrStats6LeasesExpired,
       "tmnxDhcpSvrStats6DropDuplDiffRly": tmnxDhcpSvrStats6DropDuplDiffRly,
       "tmnxDhcpSvrStats6RxIntPppSlaac": tmnxDhcpSvrStats6RxIntPppSlaac,
       "tmnxDhcpSvrStats6RxIntReqIpoeWan": tmnxDhcpSvrStats6RxIntReqIpoeWan,
       "tmnxDhcpSvrStats6RxIntReleases": tmnxDhcpSvrStats6RxIntReleases,
       "tmnxDhcpSvrStats6DropIntWFo": tmnxDhcpSvrStats6DropIntWFo,
       "tmnxDhcpSvrStats6DropIntWConflct": tmnxDhcpSvrStats6DropIntWConflct,
       "tmnxDhcpSvrStats6DropIntWIfIdMap": tmnxDhcpSvrStats6DropIntWIfIdMap,
       "tmnxDhcpSvrStats6DropIntWUserId": tmnxDhcpSvrStats6DropIntWUserId,
       "tmnxDhcpSvrStats6RxIntIpoeSlaac": tmnxDhcpSvrStats6RxIntIpoeSlaac,
       "tmnxDhcpSvrStats6DropAudit": tmnxDhcpSvrStats6DropAudit,
       "tmnxDhcpSvrSubnetStats6Table": tmnxDhcpSvrSubnetStats6Table,
       "tmnxDhcpSvrSubnetStats6Entry": tmnxDhcpSvrSubnetStats6Entry,
       "tmnxDhcpSvrSubnetStats6Advertise": tmnxDhcpSvrSubnetStats6Advertise,
       "tmnxDhcpSvrSubnetStats6Stable": tmnxDhcpSvrSubnetStats6Stable,
       "tmnxDhcpSvrSubnetStats6RCPending": tmnxDhcpSvrSubnetStats6RCPending,
       "tmnxDhcpSvrSubnetStats6RmPending": tmnxDhcpSvrSubnetStats6RmPending,
       "tmnxDhcpSvrSubnetStats6Declined": tmnxDhcpSvrSubnetStats6Declined,
       "tmnxDhcpSvrSubnetStats6HasExt": tmnxDhcpSvrSubnetStats6HasExt,
       "tmnxDhcpSvrSubnetStats6ExtResetT": tmnxDhcpSvrSubnetStats6ExtResetT,
       "tmnxDhcpSvrSubnetStats6StableP": tmnxDhcpSvrSubnetStats6StableP,
       "tmnxDhcpSvrSubnetStats6StablePT": tmnxDhcpSvrSubnetStats6StablePT,
       "tmnxDhcpSvrSubnetStats6ProvBlk": tmnxDhcpSvrSubnetStats6ProvBlk,
       "tmnxDhcpSvrSubnetStats6UsedBlk": tmnxDhcpSvrSubnetStats6UsedBlk,
       "tmnxDhcpSvrSubnetStats6UsedBlkP": tmnxDhcpSvrSubnetStats6UsedBlkP,
       "tmnxDhcpSvrSubnetStats6UsedBlkPT": tmnxDhcpSvrSubnetStats6UsedBlkPT,
       "tmnxDhcpSvrSubnetStats6FreeBlk": tmnxDhcpSvrSubnetStats6FreeBlk,
       "tmnxDhcpSvrSubnetStats6FreeBlkP": tmnxDhcpSvrSubnetStats6FreeBlkP,
       "tmnxDhcpSvrSubnetStats6FreeBlkPT": tmnxDhcpSvrSubnetStats6FreeBlkPT,
       "tmnxDhcpSvrSubnetStats6UsedPct": tmnxDhcpSvrSubnetStats6UsedPct,
       "tmnxDhcpSvrSubnetStats6UsedPctP": tmnxDhcpSvrSubnetStats6UsedPctP,
       "tmnxDhcpSvrSubnetStats6UsedPctPT": tmnxDhcpSvrSubnetStats6UsedPctPT,
       "tmnxDhcpSvrSubnetStats6FreePct": tmnxDhcpSvrSubnetStats6FreePct,
       "tmnxDhcpSvrSubnetStats6FreePctP": tmnxDhcpSvrSubnetStats6FreePctP,
       "tmnxDhcpSvrSubnetStats6FreePctPT": tmnxDhcpSvrSubnetStats6FreePctPT,
       "tmnxDhcpSvrSubnetStats6AdvertP": tmnxDhcpSvrSubnetStats6AdvertP,
       "tmnxDhcpSvrSubnetStats6AdvertPT": tmnxDhcpSvrSubnetStats6AdvertPT,
       "tmnxDhcpSvrPoolStatsTable": tmnxDhcpSvrPoolStatsTable,
       "tmnxDhcpSvrPoolStatsEntry": tmnxDhcpSvrPoolStatsEntry,
       "tmnxDhcpSvrPoolStatsFree": tmnxDhcpSvrPoolStatsFree,
       "tmnxDhcpSvrPoolStatsOffered": tmnxDhcpSvrPoolStatsOffered,
       "tmnxDhcpSvrPoolStatsStable": tmnxDhcpSvrPoolStatsStable,
       "tmnxDhcpSvrPoolStatsFRPending": tmnxDhcpSvrPoolStatsFRPending,
       "tmnxDhcpSvrPoolStatsRemPending": tmnxDhcpSvrPoolStatsRemPending,
       "tmnxDhcpSvrPoolStatsDeclined": tmnxDhcpSvrPoolStatsDeclined,
       "tmnxDhcpSvrPoolStatsFoFree": tmnxDhcpSvrPoolStatsFoFree,
       "tmnxDhcpSvrPoolStatsFoOffered": tmnxDhcpSvrPoolStatsFoOffered,
       "tmnxDhcpSvrPoolStatsFoStable": tmnxDhcpSvrPoolStatsFoStable,
       "tmnxDhcpSvrPoolStatsFoFRPend": tmnxDhcpSvrPoolStatsFoFRPend,
       "tmnxDhcpSvrPoolStatsFoRemPend": tmnxDhcpSvrPoolStatsFoRemPend,
       "tmnxDhcpSvrPoolStatsFoDeclined": tmnxDhcpSvrPoolStatsFoDeclined,
       "tmnxDhcpSvrPoolStatsProv": tmnxDhcpSvrPoolStatsProv,
       "tmnxDhcpSvrPoolStatsFoProv": tmnxDhcpSvrPoolStatsFoProv,
       "tmnxDhcpSvrPoolStatsHasExt": tmnxDhcpSvrPoolStatsHasExt,
       "tmnxDhcpSvrPoolStatsExtResetT": tmnxDhcpSvrPoolStatsExtResetT,
       "tmnxDhcpSvrPoolStatsStableP": tmnxDhcpSvrPoolStatsStableP,
       "tmnxDhcpSvrPoolStatsStablePT": tmnxDhcpSvrPoolStatsStablePT,
       "tmnxDhcpSvrPoolStatsFoStableP": tmnxDhcpSvrPoolStatsFoStableP,
       "tmnxDhcpSvrPoolStatsFoStablePT": tmnxDhcpSvrPoolStatsFoStablePT,
       "tmnxDhcpSvrPoolStatsUsed": tmnxDhcpSvrPoolStatsUsed,
       "tmnxDhcpSvrPoolStatsUsedP": tmnxDhcpSvrPoolStatsUsedP,
       "tmnxDhcpSvrPoolStatsUsedPT": tmnxDhcpSvrPoolStatsUsedPT,
       "tmnxDhcpSvrPoolStatsFoUsed": tmnxDhcpSvrPoolStatsFoUsed,
       "tmnxDhcpSvrPoolStatsFoUsedP": tmnxDhcpSvrPoolStatsFoUsedP,
       "tmnxDhcpSvrPoolStatsFoUsedPT": tmnxDhcpSvrPoolStatsFoUsedPT,
       "tmnxDhcpSvrPoolStatsFreeP": tmnxDhcpSvrPoolStatsFreeP,
       "tmnxDhcpSvrPoolStatsFreePT": tmnxDhcpSvrPoolStatsFreePT,
       "tmnxDhcpSvrPoolStatsFoFreeP": tmnxDhcpSvrPoolStatsFoFreeP,
       "tmnxDhcpSvrPoolStatsFoFreePT": tmnxDhcpSvrPoolStatsFoFreePT,
       "tmnxDhcpSvrPoolStatsUsedPct": tmnxDhcpSvrPoolStatsUsedPct,
       "tmnxDhcpSvrPoolStatsUsedPctP": tmnxDhcpSvrPoolStatsUsedPctP,
       "tmnxDhcpSvrPoolStatsUsedPctPT": tmnxDhcpSvrPoolStatsUsedPctPT,
       "tmnxDhcpSvrPoolStatsFoUsdPct": tmnxDhcpSvrPoolStatsFoUsdPct,
       "tmnxDhcpSvrPoolStatsFoUsdPctP": tmnxDhcpSvrPoolStatsFoUsdPctP,
       "tmnxDhcpSvrPoolStatsFoUsdPctPT": tmnxDhcpSvrPoolStatsFoUsdPctPT,
       "tmnxDhcpSvrPoolStatsFreePct": tmnxDhcpSvrPoolStatsFreePct,
       "tmnxDhcpSvrPoolStatsFreePctP": tmnxDhcpSvrPoolStatsFreePctP,
       "tmnxDhcpSvrPoolStatsFreePctPT": tmnxDhcpSvrPoolStatsFreePctPT,
       "tmnxDhcpSvrPoolStatsFoFrePct": tmnxDhcpSvrPoolStatsFoFrePct,
       "tmnxDhcpSvrPoolStatsFoFrePctP": tmnxDhcpSvrPoolStatsFoFrePctP,
       "tmnxDhcpSvrPoolStatsFoFrePctPT": tmnxDhcpSvrPoolStatsFoFrePctPT,
       "tmnxDhcpSvrPoolStatsOfferP": tmnxDhcpSvrPoolStatsOfferP,
       "tmnxDhcpSvrPoolStatsOfferPT": tmnxDhcpSvrPoolStatsOfferPT,
       "tmnxDhcpSvrPoolStatsFoOfferP": tmnxDhcpSvrPoolStatsFoOfferP,
       "tmnxDhcpSvrPoolStatsFoOfferPT": tmnxDhcpSvrPoolStatsFoOfferPT,
       "tmnxDhcpServerDuidTableLastCh": tmnxDhcpServerDuidTableLastCh,
       "tmnxDhcpServerDuidTable": tmnxDhcpServerDuidTable,
       "tmnxDhcpServerDuidEntry": tmnxDhcpServerDuidEntry,
       "tmnxDhcpServerDuidLastChanged": tmnxDhcpServerDuidLastChanged,
       "tmnxDhcpServerDuidTypeCode": tmnxDhcpServerDuidTypeCode,
       "tmnxDhcpServerDuidEnNumber": tmnxDhcpServerDuidEnNumber,
       "tmnxDhcpServerDuidEnIdData": tmnxDhcpServerDuidEnIdData,
       "tmnxDhcpServerDuidEnIdDataType": tmnxDhcpServerDuidEnIdDataType,
       "tmnxDhcpsPoolStats6Table": tmnxDhcpsPoolStats6Table,
       "tmnxDhcpsPoolStats6Entry": tmnxDhcpsPoolStats6Entry,
       "tmnxDhcpsPoolStats6Stable": tmnxDhcpsPoolStats6Stable,
       "tmnxDhcpsPoolStats6FoStable": tmnxDhcpsPoolStats6FoStable,
       "tmnxDhcpsPoolStats6HasExt": tmnxDhcpsPoolStats6HasExt,
       "tmnxDhcpsPoolStats6ExtResetT": tmnxDhcpsPoolStats6ExtResetT,
       "tmnxDhcpsPoolStats6StableP": tmnxDhcpsPoolStats6StableP,
       "tmnxDhcpsPoolStats6StablePT": tmnxDhcpsPoolStats6StablePT,
       "tmnxDhcpsPoolStats6FoStableP": tmnxDhcpsPoolStats6FoStableP,
       "tmnxDhcpsPoolStats6FoStablePT": tmnxDhcpsPoolStats6FoStablePT,
       "tmnxDhcpsPoolStats6ProvBlk": tmnxDhcpsPoolStats6ProvBlk,
       "tmnxDhcpsPoolStats6FoProvBlk": tmnxDhcpsPoolStats6FoProvBlk,
       "tmnxDhcpsPoolStats6UsedBlk": tmnxDhcpsPoolStats6UsedBlk,
       "tmnxDhcpsPoolStats6UsedBlkP": tmnxDhcpsPoolStats6UsedBlkP,
       "tmnxDhcpsPoolStats6UsedBlkPT": tmnxDhcpsPoolStats6UsedBlkPT,
       "tmnxDhcpsPoolStats6FoUsedBlk": tmnxDhcpsPoolStats6FoUsedBlk,
       "tmnxDhcpsPoolStats6FoUsedBlkP": tmnxDhcpsPoolStats6FoUsedBlkP,
       "tmnxDhcpsPoolStats6FoUsedBlkPT": tmnxDhcpsPoolStats6FoUsedBlkPT,
       "tmnxDhcpsPoolStats6FreeBlk": tmnxDhcpsPoolStats6FreeBlk,
       "tmnxDhcpsPoolStats6FreeBlkP": tmnxDhcpsPoolStats6FreeBlkP,
       "tmnxDhcpsPoolStats6FreeBlkPT": tmnxDhcpsPoolStats6FreeBlkPT,
       "tmnxDhcpsPoolStats6FoFreeBlk": tmnxDhcpsPoolStats6FoFreeBlk,
       "tmnxDhcpsPoolStats6FoFreeBlkP": tmnxDhcpsPoolStats6FoFreeBlkP,
       "tmnxDhcpsPoolStats6FoFreeBlkPT": tmnxDhcpsPoolStats6FoFreeBlkPT,
       "tmnxDhcpsPoolStats6UsedPct": tmnxDhcpsPoolStats6UsedPct,
       "tmnxDhcpsPoolStats6UsedPctP": tmnxDhcpsPoolStats6UsedPctP,
       "tmnxDhcpsPoolStats6UsedPctPT": tmnxDhcpsPoolStats6UsedPctPT,
       "tmnxDhcpsPoolStats6FoUsedPct": tmnxDhcpsPoolStats6FoUsedPct,
       "tmnxDhcpsPoolStats6FoUsedPctP": tmnxDhcpsPoolStats6FoUsedPctP,
       "tmnxDhcpsPoolStats6FoUsedPctPT": tmnxDhcpsPoolStats6FoUsedPctPT,
       "tmnxDhcpsPoolStats6FreePct": tmnxDhcpsPoolStats6FreePct,
       "tmnxDhcpsPoolStats6FreePctP": tmnxDhcpsPoolStats6FreePctP,
       "tmnxDhcpsPoolStats6FreePctPT": tmnxDhcpsPoolStats6FreePctPT,
       "tmnxDhcpsPoolStats6FoFreePct": tmnxDhcpsPoolStats6FoFreePct,
       "tmnxDhcpsPoolStats6FoFreePctP": tmnxDhcpsPoolStats6FoFreePctP,
       "tmnxDhcpsPoolStats6FoFreePctPT": tmnxDhcpsPoolStats6FoFreePctPT,
       "tmnxDhcpsPoolStats6Advertise": tmnxDhcpsPoolStats6Advertise,
       "tmnxDhcpsPoolStats6AdvertP": tmnxDhcpsPoolStats6AdvertP,
       "tmnxDhcpsPoolStats6AdvertPT": tmnxDhcpsPoolStats6AdvertPT,
       "tmnxDhcpsPoolStats6FoAdvertise": tmnxDhcpsPoolStats6FoAdvertise,
       "tmnxDhcpsPoolStats6FoAdvertP": tmnxDhcpsPoolStats6FoAdvertP,
       "tmnxDhcpsPoolStats6FoAdvertPT": tmnxDhcpsPoolStats6FoAdvertPT,
       "tmnxDhcpsPoolStats6IntNoPfxWan": tmnxDhcpsPoolStats6IntNoPfxWan,
       "tmnxDhcpsPoolStats6IntNoPfxSlaa": tmnxDhcpsPoolStats6IntNoPfxSlaa,
       "tmnxDhcpSvrSubnetBindingTable": tmnxDhcpSvrSubnetBindingTable,
       "tmnxDhcpSvrSubnetBindingEntry": tmnxDhcpSvrSubnetBindingEntry,
       "tmnxDhcpSvrSubnetBindSystemId": tmnxDhcpSvrSubnetBindSystemId,
       "tmnxDhcpSvrSubnetBindServiceId": tmnxDhcpSvrSubnetBindServiceId,
       "tmnxDhcpSvrSubnetBindString": tmnxDhcpSvrSubnetBindString,
       "tmnxDhcpSvrSubnetBindUnbindTime": tmnxDhcpSvrSubnetBindUnbindTime,
       "tmnxDhcpSvrSubnetBindActive": tmnxDhcpSvrSubnetBindActive,
       "tmnxDhcpSvrSubnetBindState": tmnxDhcpSvrSubnetBindState,
       "tmnxDhcpSvrSubntBndngTbleLastCh": tmnxDhcpSvrSubntBndngTbleLastCh,
       "tmnxDhcpServerNotificationObjs": tmnxDhcpServerNotificationObjs,
       "tmnxDhcpSvrNotifDescription": tmnxDhcpSvrNotifDescription,
       "tmnxDhcpSvrNotifUnknownPoolName": tmnxDhcpSvrNotifUnknownPoolName,
       "tmnxDhcpSvrNotifServerName": tmnxDhcpSvrNotifServerName,
       "tmnxDhcpSvrNotifLeaseClientAddrType": tmnxDhcpSvrNotifLeaseClientAddrType,
       "tmnxDhcpSvrNotifLeaseClientAddr": tmnxDhcpSvrNotifLeaseClientAddr,
       "tmnxDhcpSvrNotifUserDatabaseName": tmnxDhcpSvrNotifUserDatabaseName,
       "tmnxDhcpSvrNotifHostName": tmnxDhcpSvrNotifHostName,
       "tmnxDhcpSvrNotifHostType": tmnxDhcpSvrNotifHostType,
       "tmnxDhcpSvrNotifVRtrID": tmnxDhcpSvrNotifVRtrID,
       "tmnxDhcpSvrNotifMsgHwAddress": tmnxDhcpSvrNotifMsgHwAddress,
       "tmnxDhcpSvrNotifMsgOption82": tmnxDhcpSvrNotifMsgOption82,
       "tmnxDhcpSvrNotifMsgSizeLimit": tmnxDhcpSvrNotifMsgSizeLimit,
       "tmnxDhcpsFoLeaseFailureReason": tmnxDhcpsFoLeaseFailureReason,
       "tmnxDhcpSvrNotifPoolFree": tmnxDhcpSvrNotifPoolFree,
       "tmnxDhcpSvrNotifLeaseClientAddrLen": tmnxDhcpSvrNotifLeaseClientAddrLen,
       "tmnxDhcpSvrNotifClientDUID": tmnxDhcpSvrNotifClientDUID,
       "tmnxDhcpSvrNotifLinkAddr": tmnxDhcpSvrNotifLinkAddr,
       "tmnxDhcpSvrNotifPrimaryPool": tmnxDhcpSvrNotifPrimaryPool,
       "tmnxDhcpSvrNotifSecondaryPool": tmnxDhcpSvrNotifSecondaryPool,
       "tmnxDhcpSvrNotifSystemId": tmnxDhcpSvrNotifSystemId,
       "tmnxDhcpSvrNotifServiceId": tmnxDhcpSvrNotifServiceId,
       "tmnxDhcpSvrNotifString": tmnxDhcpSvrNotifString,
       "tmnxDhcpSvrNotifPoolName": tmnxDhcpSvrNotifPoolName,
       "tmnxDhcpSvrNotifSubnetAddrType": tmnxDhcpSvrNotifSubnetAddrType,
       "tmnxDhcpSvrNotifSubnetPfx": tmnxDhcpSvrNotifSubnetPfx,
       "tmnxDhcpSvrNotifSubnetPfxlen": tmnxDhcpSvrNotifSubnetPfxlen,
       "tmnxDhcpSvrNotifUnbindTime": tmnxDhcpSvrNotifUnbindTime,
       "tmnxDhcpServerNotifyPrefix": tmnxDhcpServerNotifyPrefix,
       "tmnxDhcpServerNotifications": tmnxDhcpServerNotifications,
       "tmnxDhcpSvrSubnetMinFreeExc": tmnxDhcpSvrSubnetMinFreeExc,
       "tmnxDhcpSvrHostConflict": tmnxDhcpSvrHostConflict,
       "tmnxDhcpSvrPoolUnknown": tmnxDhcpSvrPoolUnknown,
       "tmnxDhcpSvrLeaseNotOwner": tmnxDhcpSvrLeaseNotOwner,
       "tmnxDhcpSvrDeclineStaticAddr": tmnxDhcpSvrDeclineStaticAddr,
       "tmnxDhcpSvrMsgTooLong": tmnxDhcpSvrMsgTooLong,
       "tmnxDhcpsFoStateChange": tmnxDhcpsFoStateChange,
       "tmnxDhcpsFoLeaseUpdateFailed": tmnxDhcpsFoLeaseUpdateFailed,
       "tmnxDhcpSvrUserDbUnknown": tmnxDhcpSvrUserDbUnknown,
       "tmnxDhcpSvrMaxLeasesReached": tmnxDhcpSvrMaxLeasesReached,
       "tmnxDhcpSvrNoSubnetFixAddr": tmnxDhcpSvrNoSubnetFixAddr,
       "tmnxDhcpSvrLeaseDefaultTimers": tmnxDhcpSvrLeaseDefaultTimers,
       "tmnxDhcpSvrPoolMinFreeExc": tmnxDhcpSvrPoolMinFreeExc,
       "tmnxDhcpSvrSubnetDepleted": tmnxDhcpSvrSubnetDepleted,
       "tmnxDhcpSvrPoolDepleted": tmnxDhcpSvrPoolDepleted,
       "tmnxDhcpSvrIntLseConflict": tmnxDhcpSvrIntLseConflict,
       "tmnxDhcpSvrLeaseModify": tmnxDhcpSvrLeaseModify,
       "tmnxDhcpSvrLeaseCreate": tmnxDhcpSvrLeaseCreate,
       "tmnxDhcpSvrLeaseDelete": tmnxDhcpSvrLeaseDelete,
       "tmnxDhcpSvrNoContFreeBlocks": tmnxDhcpSvrNoContFreeBlocks,
       "tmnxDhcpSvrSubnetBindingFailed": tmnxDhcpSvrSubnetBindingFailed,
       "tmnxDhcpsPoolFoStateChange": tmnxDhcpsPoolFoStateChange,
       "tmnxDhcpsPoolFoLeaseUpdateFailed": tmnxDhcpsPoolFoLeaseUpdateFailed,
       "tmnxDhcpSvrSubnetBindingCreate": tmnxDhcpSvrSubnetBindingCreate,
       "tmnxDhcpSvrSubnetBindingUnbind": tmnxDhcpSvrSubnetBindingUnbind,
       "tmnxDhcpSvrSubnetBindingDelete": tmnxDhcpSvrSubnetBindingDelete,
       "tmnxDhcpSvrSubnetFailCtrlError": tmnxDhcpSvrSubnetFailCtrlError}
)
