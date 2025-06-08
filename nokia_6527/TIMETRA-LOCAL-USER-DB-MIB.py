# SNMP MIB module (TIMETRA-LOCAL-USER-DB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-LOCAL-USER-DB-MIB.mib
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

(TIPFilterIdOrEmpty,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TIPFilterIdOrEmpty")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxL2tpTunnelGroupNameOrEmpty,) = mibBuilder.importSymbols(
    "TIMETRA-L2TP-MIB",
    "TmnxL2tpTunnelGroupNameOrEmpty")

(TmnxPortEncapType,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxPortEncapType")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxAncpStringOrZero,
 TmnxDhcpOptionType,
 TmnxEncapVal,
 TmnxFilterProfileStringOrEmpty,
 TmnxMacSpecification,
 TmnxPppoePadoDelay,
 TmnxPppoeUserNameOrEmpty,
 TmnxServId,
 TmnxSlaProfileStringOrEmpty,
 TmnxSubAleOffset,
 TmnxSubAleOffsetMode,
 TmnxSubIdentStringOrEmpty,
 TmnxSubProfileStringOrEmpty,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxAncpStringOrZero",
    "TmnxDhcpOptionType",
    "TmnxEncapVal",
    "TmnxFilterProfileStringOrEmpty",
    "TmnxMacSpecification",
    "TmnxPppoePadoDelay",
    "TmnxPppoeUserNameOrEmpty",
    "TmnxServId",
    "TmnxSlaProfileStringOrEmpty",
    "TmnxSubAleOffset",
    "TmnxSubAleOffsetMode",
    "TmnxSubIdentStringOrEmpty",
    "TmnxSubProfileStringOrEmpty",
    "TmnxVRtrIDOrZero")


# MODULE-IDENTITY

timetraLocalUserDbMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 51)
)
if mibBuilder.loadTexts:
    timetraLocalUserDbMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxLocUsrDbUserNameFormat(TextualConvention, Integer32):
    status = "current"
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
          ("full", 1),
          ("hostOnly", 2),
          ("domainOnly", 3))
    )



class TmnxLocUsrDbPasswordType(TextualConvention, Integer32):
    status = "current"
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
          ("ignore", 1),
          ("pap", 2),
          ("chap", 3))
    )



class TmnxLocUsrDbMatchTypePppoe(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("circuitId", 1),
          ("macAddr", 2),
          ("remoteId", 3),
          ("userName", 4),
          ("serviceName", 5),
          ("sapId", 6),
          ("encTagRange", 7))
    )



class TmnxLocUsrDbMatchTypeDhcp(TextualConvention, Integer32):
    status = "current"
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("circuitId", 1),
          ("macAddr", 2),
          ("remoteId", 3),
          ("sapId", 4),
          ("serviceId", 5),
          ("string", 6),
          ("systemId", 7),
          ("option60", 8),
          ("encTagRange", 9),
          ("dualStackRemoteId", 10),
          ("derivedId", 11))
    )



class TmnxLocUsrDbHostType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("dhcp", 1),
          ("ppp", 2))
    )



class TmnxLocUsrDbHostApplications(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bitDHCP", 0),
          ("bitPPP", 1))
    )


class TmnxLocUsrDbUnmatchedReason(TextualConvention, Integer32):
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
        *(("noMatchTypes", 1),
          ("duplicate", 2),
          ("genError", 3))
    )



class TmnxLocUsrDbDataFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 3))
    )



class TmnxLocUsrDbMaskString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class TmnxLudbDataFormat(TextualConvention, Integer32):
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
        *(("none", 1),
          ("ascii", 2),
          ("hex", 3))
    )



class TmnxLudbMsapGrpIfPfxSfxType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("portId", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxLocalUserDbConformance_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbConformance = _TmnxLocalUserDbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51)
)
_TmnxLocalUserDbCompliances_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbCompliances = _TmnxLocalUserDbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1)
)
_TmnxLocalUserDbGroups_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbGroups = _TmnxLocalUserDbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2)
)
_TmnxLocalUserDbNotifGroups_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbNotifGroups = _TmnxLocalUserDbNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 3)
)
_TmnxLocalUserDb_ObjectIdentity = ObjectIdentity
tmnxLocalUserDb = _TmnxLocalUserDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51)
)
_TmnxLocalUserDbObjs_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbObjs = _TmnxLocalUserDbObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1)
)
_TmnxLocalUserDbTableLastChange_Type = TimeStamp
_TmnxLocalUserDbTableLastChange_Object = MibScalar
tmnxLocalUserDbTableLastChange = _TmnxLocalUserDbTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 1),
    _TmnxLocalUserDbTableLastChange_Type()
)
tmnxLocalUserDbTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocalUserDbTableLastChange.setStatus("current")
_TmnxLocalUserDbTable_Object = MibTable
tmnxLocalUserDbTable = _TmnxLocalUserDbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbTable.setStatus("current")
_TmnxLocalUserDbEntry_Object = MibTableRow
tmnxLocalUserDbEntry = _TmnxLocalUserDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1)
)
tmnxLocalUserDbEntry.setIndexNames(
    (1, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbEntry.setStatus("current")
_TmnxLocUsrDbUserDatabaseName_Type = TNamedItem
_TmnxLocUsrDbUserDatabaseName_Object = MibTableColumn
tmnxLocUsrDbUserDatabaseName = _TmnxLocUsrDbUserDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 1),
    _TmnxLocUsrDbUserDatabaseName_Type()
)
tmnxLocUsrDbUserDatabaseName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbUserDatabaseName.setStatus("current")
_TmnxLocUsrDbRowStatus_Type = RowStatus
_TmnxLocUsrDbRowStatus_Object = MibTableColumn
tmnxLocUsrDbRowStatus = _TmnxLocUsrDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 2),
    _TmnxLocUsrDbRowStatus_Type()
)
tmnxLocUsrDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbRowStatus.setStatus("current")
_TmnxLocUsrDbLastChangeTime_Type = TimeStamp
_TmnxLocUsrDbLastChangeTime_Object = MibTableColumn
tmnxLocUsrDbLastChangeTime = _TmnxLocUsrDbLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 3),
    _TmnxLocUsrDbLastChangeTime_Type()
)
tmnxLocUsrDbLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbLastChangeTime.setStatus("current")


class _TmnxLocUsrDbAdminState_Type(TmnxAdminState):
    """Custom type tmnxLocUsrDbAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLocUsrDbAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLocUsrDbAdminState_Object = MibTableColumn
tmnxLocUsrDbAdminState = _TmnxLocUsrDbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 4),
    _TmnxLocUsrDbAdminState_Type()
)
tmnxLocUsrDbAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbAdminState.setStatus("current")


class _TmnxLocUsrDbDescription_Type(TItemDescription):
    """Custom type tmnxLocUsrDbDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDescription_Type.__name__ = "TItemDescription"
_TmnxLocUsrDbDescription_Object = MibTableColumn
tmnxLocUsrDbDescription = _TmnxLocUsrDbDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 5),
    _TmnxLocUsrDbDescription_Type()
)
tmnxLocUsrDbDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDescription.setStatus("current")


class _TmnxLocUsrDbMatchTypeDhcp1_Type(TmnxLocUsrDbMatchTypeDhcp):
    """Custom type tmnxLocUsrDbMatchTypeDhcp1 based on TmnxLocUsrDbMatchTypeDhcp"""
    defaultValue = 0


_TmnxLocUsrDbMatchTypeDhcp1_Type.__name__ = "TmnxLocUsrDbMatchTypeDhcp"
_TmnxLocUsrDbMatchTypeDhcp1_Object = MibTableColumn
tmnxLocUsrDbMatchTypeDhcp1 = _TmnxLocUsrDbMatchTypeDhcp1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 6),
    _TmnxLocUsrDbMatchTypeDhcp1_Type()
)
tmnxLocUsrDbMatchTypeDhcp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbMatchTypeDhcp1.setStatus("current")


class _TmnxLocUsrDbMatchTypeDhcp2_Type(TmnxLocUsrDbMatchTypeDhcp):
    """Custom type tmnxLocUsrDbMatchTypeDhcp2 based on TmnxLocUsrDbMatchTypeDhcp"""
    defaultValue = 0


_TmnxLocUsrDbMatchTypeDhcp2_Type.__name__ = "TmnxLocUsrDbMatchTypeDhcp"
_TmnxLocUsrDbMatchTypeDhcp2_Object = MibTableColumn
tmnxLocUsrDbMatchTypeDhcp2 = _TmnxLocUsrDbMatchTypeDhcp2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 7),
    _TmnxLocUsrDbMatchTypeDhcp2_Type()
)
tmnxLocUsrDbMatchTypeDhcp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbMatchTypeDhcp2.setStatus("current")


class _TmnxLocUsrDbMatchTypeDhcp3_Type(TmnxLocUsrDbMatchTypeDhcp):
    """Custom type tmnxLocUsrDbMatchTypeDhcp3 based on TmnxLocUsrDbMatchTypeDhcp"""
    defaultValue = 0


_TmnxLocUsrDbMatchTypeDhcp3_Type.__name__ = "TmnxLocUsrDbMatchTypeDhcp"
_TmnxLocUsrDbMatchTypeDhcp3_Object = MibTableColumn
tmnxLocUsrDbMatchTypeDhcp3 = _TmnxLocUsrDbMatchTypeDhcp3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 8),
    _TmnxLocUsrDbMatchTypeDhcp3_Type()
)
tmnxLocUsrDbMatchTypeDhcp3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbMatchTypeDhcp3.setStatus("current")


class _TmnxLocUsrDbMatchTypeDhcp4_Type(TmnxLocUsrDbMatchTypeDhcp):
    """Custom type tmnxLocUsrDbMatchTypeDhcp4 based on TmnxLocUsrDbMatchTypeDhcp"""
    defaultValue = 0


_TmnxLocUsrDbMatchTypeDhcp4_Type.__name__ = "TmnxLocUsrDbMatchTypeDhcp"
_TmnxLocUsrDbMatchTypeDhcp4_Object = MibTableColumn
tmnxLocUsrDbMatchTypeDhcp4 = _TmnxLocUsrDbMatchTypeDhcp4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 9),
    _TmnxLocUsrDbMatchTypeDhcp4_Type()
)
tmnxLocUsrDbMatchTypeDhcp4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbMatchTypeDhcp4.setStatus("current")


class _TmnxLocUsrDbMatchTypePppoe1_Type(TmnxLocUsrDbMatchTypePppoe):
    """Custom type tmnxLocUsrDbMatchTypePppoe1 based on TmnxLocUsrDbMatchTypePppoe"""
    defaultValue = 0


_TmnxLocUsrDbMatchTypePppoe1_Type.__name__ = "TmnxLocUsrDbMatchTypePppoe"
_TmnxLocUsrDbMatchTypePppoe1_Object = MibTableColumn
tmnxLocUsrDbMatchTypePppoe1 = _TmnxLocUsrDbMatchTypePppoe1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 10),
    _TmnxLocUsrDbMatchTypePppoe1_Type()
)
tmnxLocUsrDbMatchTypePppoe1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbMatchTypePppoe1.setStatus("current")


class _TmnxLocUsrDbMatchTypePppoe2_Type(TmnxLocUsrDbMatchTypePppoe):
    """Custom type tmnxLocUsrDbMatchTypePppoe2 based on TmnxLocUsrDbMatchTypePppoe"""
    defaultValue = 0


_TmnxLocUsrDbMatchTypePppoe2_Type.__name__ = "TmnxLocUsrDbMatchTypePppoe"
_TmnxLocUsrDbMatchTypePppoe2_Object = MibTableColumn
tmnxLocUsrDbMatchTypePppoe2 = _TmnxLocUsrDbMatchTypePppoe2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 11),
    _TmnxLocUsrDbMatchTypePppoe2_Type()
)
tmnxLocUsrDbMatchTypePppoe2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbMatchTypePppoe2.setStatus("current")


class _TmnxLocUsrDbMatchTypePppoe3_Type(TmnxLocUsrDbMatchTypePppoe):
    """Custom type tmnxLocUsrDbMatchTypePppoe3 based on TmnxLocUsrDbMatchTypePppoe"""
    defaultValue = 0


_TmnxLocUsrDbMatchTypePppoe3_Type.__name__ = "TmnxLocUsrDbMatchTypePppoe"
_TmnxLocUsrDbMatchTypePppoe3_Object = MibTableColumn
tmnxLocUsrDbMatchTypePppoe3 = _TmnxLocUsrDbMatchTypePppoe3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 12),
    _TmnxLocUsrDbMatchTypePppoe3_Type()
)
tmnxLocUsrDbMatchTypePppoe3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbMatchTypePppoe3.setStatus("current")


class _TmnxLocUsrDbPppoeCIdMaskPreStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbPppoeCIdMaskPreStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeCIdMaskPreStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbPppoeCIdMaskPreStr_Object = MibTableColumn
tmnxLocUsrDbPppoeCIdMaskPreStr = _TmnxLocUsrDbPppoeCIdMaskPreStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 13),
    _TmnxLocUsrDbPppoeCIdMaskPreStr_Type()
)
tmnxLocUsrDbPppoeCIdMaskPreStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeCIdMaskPreStr.setStatus("obsolete")


class _TmnxLocUsrDbPppoeCIdMaskPreNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbPppoeCIdMaskPreNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeCIdMaskPreNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbPppoeCIdMaskPreNum_Object = MibTableColumn
tmnxLocUsrDbPppoeCIdMaskPreNum = _TmnxLocUsrDbPppoeCIdMaskPreNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 14),
    _TmnxLocUsrDbPppoeCIdMaskPreNum_Type()
)
tmnxLocUsrDbPppoeCIdMaskPreNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeCIdMaskPreNum.setStatus("obsolete")


class _TmnxLocUsrDbPppoeCIdMaskSufStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbPppoeCIdMaskSufStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeCIdMaskSufStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbPppoeCIdMaskSufStr_Object = MibTableColumn
tmnxLocUsrDbPppoeCIdMaskSufStr = _TmnxLocUsrDbPppoeCIdMaskSufStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 15),
    _TmnxLocUsrDbPppoeCIdMaskSufStr_Type()
)
tmnxLocUsrDbPppoeCIdMaskSufStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeCIdMaskSufStr.setStatus("obsolete")


class _TmnxLocUsrDbPppoeCIdMaskSufNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbPppoeCIdMaskSufNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeCIdMaskSufNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbPppoeCIdMaskSufNum_Object = MibTableColumn
tmnxLocUsrDbPppoeCIdMaskSufNum = _TmnxLocUsrDbPppoeCIdMaskSufNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 16),
    _TmnxLocUsrDbPppoeCIdMaskSufNum_Type()
)
tmnxLocUsrDbPppoeCIdMaskSufNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeCIdMaskSufNum.setStatus("obsolete")


class _TmnxLocUsrDbDhcpCIdMaskPreStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbDhcpCIdMaskPreStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpCIdMaskPreStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbDhcpCIdMaskPreStr_Object = MibTableColumn
tmnxLocUsrDbDhcpCIdMaskPreStr = _TmnxLocUsrDbDhcpCIdMaskPreStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 17),
    _TmnxLocUsrDbDhcpCIdMaskPreStr_Type()
)
tmnxLocUsrDbDhcpCIdMaskPreStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpCIdMaskPreStr.setStatus("obsolete")


class _TmnxLocUsrDbDhcpCIdMaskPreNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpCIdMaskPreNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpCIdMaskPreNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpCIdMaskPreNum_Object = MibTableColumn
tmnxLocUsrDbDhcpCIdMaskPreNum = _TmnxLocUsrDbDhcpCIdMaskPreNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 18),
    _TmnxLocUsrDbDhcpCIdMaskPreNum_Type()
)
tmnxLocUsrDbDhcpCIdMaskPreNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpCIdMaskPreNum.setStatus("obsolete")


class _TmnxLocUsrDbDhcpCIdMaskSufStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbDhcpCIdMaskSufStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpCIdMaskSufStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbDhcpCIdMaskSufStr_Object = MibTableColumn
tmnxLocUsrDbDhcpCIdMaskSufStr = _TmnxLocUsrDbDhcpCIdMaskSufStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 19),
    _TmnxLocUsrDbDhcpCIdMaskSufStr_Type()
)
tmnxLocUsrDbDhcpCIdMaskSufStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpCIdMaskSufStr.setStatus("obsolete")


class _TmnxLocUsrDbDhcpCIdMaskSufNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpCIdMaskSufNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpCIdMaskSufNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpCIdMaskSufNum_Object = MibTableColumn
tmnxLocUsrDbDhcpCIdMaskSufNum = _TmnxLocUsrDbDhcpCIdMaskSufNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 20),
    _TmnxLocUsrDbDhcpCIdMaskSufNum_Type()
)
tmnxLocUsrDbDhcpCIdMaskSufNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpCIdMaskSufNum.setStatus("obsolete")
_TmnxLocUsrDbHostCount_Type = Unsigned32
_TmnxLocUsrDbHostCount_Object = MibTableColumn
tmnxLocUsrDbHostCount = _TmnxLocUsrDbHostCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 2, 1, 21),
    _TmnxLocUsrDbHostCount_Type()
)
tmnxLocUsrDbHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbHostCount.setStatus("current")
_TmnxLocUsrDbPppoeTableLastChange_Type = TimeStamp
_TmnxLocUsrDbPppoeTableLastChange_Object = MibScalar
tmnxLocUsrDbPppoeTableLastChange = _TmnxLocUsrDbPppoeTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 3),
    _TmnxLocUsrDbPppoeTableLastChange_Type()
)
tmnxLocUsrDbPppoeTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeTableLastChange.setStatus("current")
_TmnxLocUsrDbPppoeTable_Object = MibTable
tmnxLocUsrDbPppoeTable = _TmnxLocUsrDbPppoeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeTable.setStatus("current")
_TmnxLocUsrDbPppoeEntry_Object = MibTableRow
tmnxLocUsrDbPppoeEntry = _TmnxLocUsrDbPppoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1)
)
tmnxLocUsrDbPppoeEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeHostName"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeEntry.setStatus("current")


class _TmnxLocUsrDbPppoeHostName_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxLocUsrDbPppoeHostName_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeHostName_Object = MibTableColumn
tmnxLocUsrDbPppoeHostName = _TmnxLocUsrDbPppoeHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 1),
    _TmnxLocUsrDbPppoeHostName_Type()
)
tmnxLocUsrDbPppoeHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeHostName.setStatus("current")
_TmnxLocUsrDbPppoeRowStatus_Type = RowStatus
_TmnxLocUsrDbPppoeRowStatus_Object = MibTableColumn
tmnxLocUsrDbPppoeRowStatus = _TmnxLocUsrDbPppoeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 2),
    _TmnxLocUsrDbPppoeRowStatus_Type()
)
tmnxLocUsrDbPppoeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeRowStatus.setStatus("current")
_TmnxLocUsrDbPppoeLastChangeTime_Type = TimeStamp
_TmnxLocUsrDbPppoeLastChangeTime_Object = MibTableColumn
tmnxLocUsrDbPppoeLastChangeTime = _TmnxLocUsrDbPppoeLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 3),
    _TmnxLocUsrDbPppoeLastChangeTime_Type()
)
tmnxLocUsrDbPppoeLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeLastChangeTime.setStatus("current")


class _TmnxLocUsrDbPppoeAdminState_Type(TmnxAdminState):
    """Custom type tmnxLocUsrDbPppoeAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLocUsrDbPppoeAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLocUsrDbPppoeAdminState_Object = MibTableColumn
tmnxLocUsrDbPppoeAdminState = _TmnxLocUsrDbPppoeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 4),
    _TmnxLocUsrDbPppoeAdminState_Type()
)
tmnxLocUsrDbPppoeAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAdminState.setStatus("current")


class _TmnxLocUsrDbPppoeMacAddress_Type(MacAddress):
    """Custom type tmnxLocUsrDbPppoeMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxLocUsrDbPppoeMacAddress_Type.__name__ = "MacAddress"
_TmnxLocUsrDbPppoeMacAddress_Object = MibTableColumn
tmnxLocUsrDbPppoeMacAddress = _TmnxLocUsrDbPppoeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 5),
    _TmnxLocUsrDbPppoeMacAddress_Type()
)
tmnxLocUsrDbPppoeMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMacAddress.setStatus("current")


class _TmnxLocUsrDbPppoeCircuitIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLocUsrDbPppoeCircuitIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLocUsrDbPppoeCircuitIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLocUsrDbPppoeCircuitIdFmt_Object = MibTableColumn
tmnxLocUsrDbPppoeCircuitIdFmt = _TmnxLocUsrDbPppoeCircuitIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 6),
    _TmnxLocUsrDbPppoeCircuitIdFmt_Type()
)
tmnxLocUsrDbPppoeCircuitIdFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeCircuitIdFmt.setStatus("current")


class _TmnxLocUsrDbPppoeCircuitId_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeCircuitId based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeCircuitId_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeCircuitId_Object = MibTableColumn
tmnxLocUsrDbPppoeCircuitId = _TmnxLocUsrDbPppoeCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 7),
    _TmnxLocUsrDbPppoeCircuitId_Type()
)
tmnxLocUsrDbPppoeCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeCircuitId.setStatus("current")


class _TmnxLocUsrDbPppoeRemoteId_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeRemoteId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeRemoteId_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeRemoteId_Object = MibTableColumn
tmnxLocUsrDbPppoeRemoteId = _TmnxLocUsrDbPppoeRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 8),
    _TmnxLocUsrDbPppoeRemoteId_Type()
)
tmnxLocUsrDbPppoeRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeRemoteId.setStatus("current")


class _TmnxLocUsrDbPppoeUserNameFormat_Type(TmnxLocUsrDbUserNameFormat):
    """Custom type tmnxLocUsrDbPppoeUserNameFormat based on TmnxLocUsrDbUserNameFormat"""
    defaultValue = 0


_TmnxLocUsrDbPppoeUserNameFormat_Type.__name__ = "TmnxLocUsrDbUserNameFormat"
_TmnxLocUsrDbPppoeUserNameFormat_Object = MibTableColumn
tmnxLocUsrDbPppoeUserNameFormat = _TmnxLocUsrDbPppoeUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 9),
    _TmnxLocUsrDbPppoeUserNameFormat_Type()
)
tmnxLocUsrDbPppoeUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUserNameFormat.setStatus("current")


class _TmnxLocUsrDbPppoeUserName_Type(TmnxPppoeUserNameOrEmpty):
    """Custom type tmnxLocUsrDbPppoeUserName based on TmnxPppoeUserNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeUserName_Type.__name__ = "TmnxPppoeUserNameOrEmpty"
_TmnxLocUsrDbPppoeUserName_Object = MibTableColumn
tmnxLocUsrDbPppoeUserName = _TmnxLocUsrDbPppoeUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 10),
    _TmnxLocUsrDbPppoeUserName_Type()
)
tmnxLocUsrDbPppoeUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUserName.setStatus("current")


class _TmnxLocUsrDbPppoePasswordType_Type(TmnxLocUsrDbPasswordType):
    """Custom type tmnxLocUsrDbPppoePasswordType based on TmnxLocUsrDbPasswordType"""
    defaultValue = 0


_TmnxLocUsrDbPppoePasswordType_Type.__name__ = "TmnxLocUsrDbPasswordType"
_TmnxLocUsrDbPppoePasswordType_Object = MibTableColumn
tmnxLocUsrDbPppoePasswordType = _TmnxLocUsrDbPppoePasswordType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 11),
    _TmnxLocUsrDbPppoePasswordType_Type()
)
tmnxLocUsrDbPppoePasswordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoePasswordType.setStatus("current")


class _TmnxLocUsrDbPppoePassword_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoePassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxLocUsrDbPppoePassword_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoePassword_Object = MibTableColumn
tmnxLocUsrDbPppoePassword = _TmnxLocUsrDbPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 12),
    _TmnxLocUsrDbPppoePassword_Type()
)
tmnxLocUsrDbPppoePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoePassword.setStatus("current")


class _TmnxLocUsrDbPppoeAddrType_Type(InetAddressType):
    """Custom type tmnxLocUsrDbPppoeAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLocUsrDbPppoeAddrType_Type.__name__ = "InetAddressType"
_TmnxLocUsrDbPppoeAddrType_Object = MibTableColumn
tmnxLocUsrDbPppoeAddrType = _TmnxLocUsrDbPppoeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 13),
    _TmnxLocUsrDbPppoeAddrType_Type()
)
tmnxLocUsrDbPppoeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAddrType.setStatus("current")


class _TmnxLocUsrDbPppoeAddress_Type(InetAddress):
    """Custom type tmnxLocUsrDbPppoeAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLocUsrDbPppoeAddress_Type.__name__ = "InetAddress"
_TmnxLocUsrDbPppoeAddress_Object = MibTableColumn
tmnxLocUsrDbPppoeAddress = _TmnxLocUsrDbPppoeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 14),
    _TmnxLocUsrDbPppoeAddress_Type()
)
tmnxLocUsrDbPppoeAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAddress.setStatus("current")


class _TmnxLocUsrDbPppoePool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoePool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoePool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoePool_Object = MibTableColumn
tmnxLocUsrDbPppoePool = _TmnxLocUsrDbPppoePool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 15),
    _TmnxLocUsrDbPppoePool_Type()
)
tmnxLocUsrDbPppoePool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoePool.setStatus("current")


class _TmnxLocUsrDbPppoeUseGiAddress_Type(TruthValue):
    """Custom type tmnxLocUsrDbPppoeUseGiAddress based on TruthValue"""
    defaultValue = 2


_TmnxLocUsrDbPppoeUseGiAddress_Type.__name__ = "TruthValue"
_TmnxLocUsrDbPppoeUseGiAddress_Object = MibTableColumn
tmnxLocUsrDbPppoeUseGiAddress = _TmnxLocUsrDbPppoeUseGiAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 16),
    _TmnxLocUsrDbPppoeUseGiAddress_Type()
)
tmnxLocUsrDbPppoeUseGiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUseGiAddress.setStatus("current")


class _TmnxLocUsrDbPppoeIdStringOptNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbPppoeIdStringOptNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxLocUsrDbPppoeIdStringOptNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbPppoeIdStringOptNum_Object = MibTableColumn
tmnxLocUsrDbPppoeIdStringOptNum = _TmnxLocUsrDbPppoeIdStringOptNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 17),
    _TmnxLocUsrDbPppoeIdStringOptNum_Type()
)
tmnxLocUsrDbPppoeIdStringOptNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIdStringOptNum.setStatus("current")


class _TmnxLocUsrDbPppoeSubscriberId_Type(TmnxSubIdentStringOrEmpty):
    """Custom type tmnxLocUsrDbPppoeSubscriberId based on TmnxSubIdentStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeSubscriberId_Type.__name__ = "TmnxSubIdentStringOrEmpty"
_TmnxLocUsrDbPppoeSubscriberId_Object = MibTableColumn
tmnxLocUsrDbPppoeSubscriberId = _TmnxLocUsrDbPppoeSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 18),
    _TmnxLocUsrDbPppoeSubscriberId_Type()
)
tmnxLocUsrDbPppoeSubscriberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeSubscriberId.setStatus("current")


class _TmnxLocUsrDbPppoeSlaProfString_Type(TmnxSlaProfileStringOrEmpty):
    """Custom type tmnxLocUsrDbPppoeSlaProfString based on TmnxSlaProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeSlaProfString_Type.__name__ = "TmnxSlaProfileStringOrEmpty"
_TmnxLocUsrDbPppoeSlaProfString_Object = MibTableColumn
tmnxLocUsrDbPppoeSlaProfString = _TmnxLocUsrDbPppoeSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 19),
    _TmnxLocUsrDbPppoeSlaProfString_Type()
)
tmnxLocUsrDbPppoeSlaProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeSlaProfString.setStatus("current")


class _TmnxLocUsrDbPppoeSubProfString_Type(TmnxSubProfileStringOrEmpty):
    """Custom type tmnxLocUsrDbPppoeSubProfString based on TmnxSubProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeSubProfString_Type.__name__ = "TmnxSubProfileStringOrEmpty"
_TmnxLocUsrDbPppoeSubProfString_Object = MibTableColumn
tmnxLocUsrDbPppoeSubProfString = _TmnxLocUsrDbPppoeSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 20),
    _TmnxLocUsrDbPppoeSubProfString_Type()
)
tmnxLocUsrDbPppoeSubProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeSubProfString.setStatus("current")


class _TmnxLocUsrDbPppoeAppProfString_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeAppProfString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxLocUsrDbPppoeAppProfString_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeAppProfString_Object = MibTableColumn
tmnxLocUsrDbPppoeAppProfString = _TmnxLocUsrDbPppoeAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 21),
    _TmnxLocUsrDbPppoeAppProfString_Type()
)
tmnxLocUsrDbPppoeAppProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAppProfString.setStatus("current")


class _TmnxLocUsrDbPppoeAncpString_Type(TmnxAncpStringOrZero):
    """Custom type tmnxLocUsrDbPppoeAncpString based on TmnxAncpStringOrZero"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeAncpString_Type.__name__ = "TmnxAncpStringOrZero"
_TmnxLocUsrDbPppoeAncpString_Object = MibTableColumn
tmnxLocUsrDbPppoeAncpString = _TmnxLocUsrDbPppoeAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 22),
    _TmnxLocUsrDbPppoeAncpString_Type()
)
tmnxLocUsrDbPppoeAncpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAncpString.setStatus("current")


class _TmnxLocUsrDbPppoeInterDestId_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeInterDestId based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeInterDestId_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeInterDestId_Object = MibTableColumn
tmnxLocUsrDbPppoeInterDestId = _TmnxLocUsrDbPppoeInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 23),
    _TmnxLocUsrDbPppoeInterDestId_Type()
)
tmnxLocUsrDbPppoeInterDestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeInterDestId.setStatus("current")


class _TmnxLocUsrDbPppoeUseClientPool_Type(TruthValue):
    """Custom type tmnxLocUsrDbPppoeUseClientPool based on TruthValue"""
    defaultValue = 2


_TmnxLocUsrDbPppoeUseClientPool_Type.__name__ = "TruthValue"
_TmnxLocUsrDbPppoeUseClientPool_Object = MibTableColumn
tmnxLocUsrDbPppoeUseClientPool = _TmnxLocUsrDbPppoeUseClientPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 24),
    _TmnxLocUsrDbPppoeUseClientPool_Type()
)
tmnxLocUsrDbPppoeUseClientPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUseClientPool.setStatus("current")


class _TmnxLocUsrDbPppoePadoDelay_Type(TmnxPppoePadoDelay):
    """Custom type tmnxLocUsrDbPppoePadoDelay based on TmnxPppoePadoDelay"""
    defaultValue = 0


_TmnxLocUsrDbPppoePadoDelay_Type.__name__ = "TmnxPppoePadoDelay"
_TmnxLocUsrDbPppoePadoDelay_Object = MibTableColumn
tmnxLocUsrDbPppoePadoDelay = _TmnxLocUsrDbPppoePadoDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 25),
    _TmnxLocUsrDbPppoePadoDelay_Type()
)
tmnxLocUsrDbPppoePadoDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoePadoDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoePadoDelay.setUnits("deci-seconds")


class _TmnxLocUsrDbPppoeServiceName_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeServiceName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeServiceName_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeServiceName_Object = MibTableColumn
tmnxLocUsrDbPppoeServiceName = _TmnxLocUsrDbPppoeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 26),
    _TmnxLocUsrDbPppoeServiceName_Type()
)
tmnxLocUsrDbPppoeServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeServiceName.setStatus("current")


class _TmnxLocUsrDbPppoeL2tpTunnelGroup_Type(TmnxL2tpTunnelGroupNameOrEmpty):
    """Custom type tmnxLocUsrDbPppoeL2tpTunnelGroup based on TmnxL2tpTunnelGroupNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeL2tpTunnelGroup_Type.__name__ = "TmnxL2tpTunnelGroupNameOrEmpty"
_TmnxLocUsrDbPppoeL2tpTunnelGroup_Object = MibTableColumn
tmnxLocUsrDbPppoeL2tpTunnelGroup = _TmnxLocUsrDbPppoeL2tpTunnelGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 27),
    _TmnxLocUsrDbPppoeL2tpTunnelGroup_Type()
)
tmnxLocUsrDbPppoeL2tpTunnelGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeL2tpTunnelGroup.setStatus("current")


class _TmnxLocUsrDbPppoeAuthPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeAuthPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeAuthPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeAuthPolicy_Object = MibTableColumn
tmnxLocUsrDbPppoeAuthPolicy = _TmnxLocUsrDbPppoeAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 28),
    _TmnxLocUsrDbPppoeAuthPolicy_Type()
)
tmnxLocUsrDbPppoeAuthPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthPolicy.setStatus("current")


class _TmnxLocUsrDbPppoeRetailerSvcId_Type(TmnxServId):
    """Custom type tmnxLocUsrDbPppoeRetailerSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxLocUsrDbPppoeRetailerSvcId_Type.__name__ = "TmnxServId"
_TmnxLocUsrDbPppoeRetailerSvcId_Object = MibTableColumn
tmnxLocUsrDbPppoeRetailerSvcId = _TmnxLocUsrDbPppoeRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 29),
    _TmnxLocUsrDbPppoeRetailerSvcId_Type()
)
tmnxLocUsrDbPppoeRetailerSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeRetailerSvcId.setStatus("current")


class _TmnxLocUsrDbPppoeCategoryMapName_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeCategoryMapName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeCategoryMapName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeCategoryMapName_Object = MibTableColumn
tmnxLocUsrDbPppoeCategoryMapName = _TmnxLocUsrDbPppoeCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 30),
    _TmnxLocUsrDbPppoeCategoryMapName_Type()
)
tmnxLocUsrDbPppoeCategoryMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeCategoryMapName.setStatus("current")


class _TmnxLocUsrDbPppoeDefMsapPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxLocUsrDbPppoeDefMsapPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeDefMsapPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxLocUsrDbPppoeDefMsapPolicy_Object = MibTableColumn
tmnxLocUsrDbPppoeDefMsapPolicy = _TmnxLocUsrDbPppoeDefMsapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 31),
    _TmnxLocUsrDbPppoeDefMsapPolicy_Type()
)
tmnxLocUsrDbPppoeDefMsapPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeDefMsapPolicy.setStatus("current")


class _TmnxLocUsrDbPppoeDefMsapService_Type(TmnxServId):
    """Custom type tmnxLocUsrDbPppoeDefMsapService based on TmnxServId"""
    defaultValue = 0


_TmnxLocUsrDbPppoeDefMsapService_Type.__name__ = "TmnxServId"
_TmnxLocUsrDbPppoeDefMsapService_Object = MibTableColumn
tmnxLocUsrDbPppoeDefMsapService = _TmnxLocUsrDbPppoeDefMsapService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 32),
    _TmnxLocUsrDbPppoeDefMsapService_Type()
)
tmnxLocUsrDbPppoeDefMsapService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeDefMsapService.setStatus("current")


class _TmnxLocUsrDbPppoeDefMsapGroupIf_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeDefMsapGroupIf based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeDefMsapGroupIf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeDefMsapGroupIf_Object = MibTableColumn
tmnxLocUsrDbPppoeDefMsapGroupIf = _TmnxLocUsrDbPppoeDefMsapGroupIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 33),
    _TmnxLocUsrDbPppoeDefMsapGroupIf_Type()
)
tmnxLocUsrDbPppoeDefMsapGroupIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeDefMsapGroupIf.setStatus("current")


class _TmnxLocUsrDbPppoeRemoteIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLocUsrDbPppoeRemoteIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLocUsrDbPppoeRemoteIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLocUsrDbPppoeRemoteIdFmt_Object = MibTableColumn
tmnxLocUsrDbPppoeRemoteIdFmt = _TmnxLocUsrDbPppoeRemoteIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 34),
    _TmnxLocUsrDbPppoeRemoteIdFmt_Type()
)
tmnxLocUsrDbPppoeRemoteIdFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeRemoteIdFmt.setStatus("current")


class _TmnxLocUsrDbPppoeL2tpSvcId_Type(TmnxServId):
    """Custom type tmnxLocUsrDbPppoeL2tpSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxLocUsrDbPppoeL2tpSvcId_Type.__name__ = "TmnxServId"
_TmnxLocUsrDbPppoeL2tpSvcId_Object = MibTableColumn
tmnxLocUsrDbPppoeL2tpSvcId = _TmnxLocUsrDbPppoeL2tpSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 35),
    _TmnxLocUsrDbPppoeL2tpSvcId_Type()
)
tmnxLocUsrDbPppoeL2tpSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeL2tpSvcId.setStatus("current")


class _TmnxLocUsrDbPppoeService_Type(TmnxServId):
    """Custom type tmnxLocUsrDbPppoeService based on TmnxServId"""
    defaultValue = 0


_TmnxLocUsrDbPppoeService_Type.__name__ = "TmnxServId"
_TmnxLocUsrDbPppoeService_Object = MibTableColumn
tmnxLocUsrDbPppoeService = _TmnxLocUsrDbPppoeService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 36),
    _TmnxLocUsrDbPppoeService_Type()
)
tmnxLocUsrDbPppoeService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeService.setStatus("current")


class _TmnxLocUsrDbPppoeInterface_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeInterface based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeInterface_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeInterface_Object = MibTableColumn
tmnxLocUsrDbPppoeInterface = _TmnxLocUsrDbPppoeInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 37),
    _TmnxLocUsrDbPppoeInterface_Type()
)
tmnxLocUsrDbPppoeInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeInterface.setStatus("current")


class _TmnxLocUsrDbPppoePrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxLocUsrDbPppoePrefixLength based on InetAddressPrefixLength"""
    defaultValue = 32


_TmnxLocUsrDbPppoePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxLocUsrDbPppoePrefixLength_Object = MibTableColumn
tmnxLocUsrDbPppoePrefixLength = _TmnxLocUsrDbPppoePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 38),
    _TmnxLocUsrDbPppoePrefixLength_Type()
)
tmnxLocUsrDbPppoePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoePrefixLength.setStatus("current")


class _TmnxLocUsrDbPppoeFltrProfString_Type(TmnxFilterProfileStringOrEmpty):
    """Custom type tmnxLocUsrDbPppoeFltrProfString based on TmnxFilterProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeFltrProfString_Type.__name__ = "TmnxFilterProfileStringOrEmpty"
_TmnxLocUsrDbPppoeFltrProfString_Object = MibTableColumn
tmnxLocUsrDbPppoeFltrProfString = _TmnxLocUsrDbPppoeFltrProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 39),
    _TmnxLocUsrDbPppoeFltrProfString_Type()
)
tmnxLocUsrDbPppoeFltrProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeFltrProfString.setStatus("current")


class _TmnxLocUsrDbPppoeSapId_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeSapId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeSapId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeSapId_Object = MibTableColumn
tmnxLocUsrDbPppoeSapId = _TmnxLocUsrDbPppoeSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 40),
    _TmnxLocUsrDbPppoeSapId_Type()
)
tmnxLocUsrDbPppoeSapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeSapId.setStatus("current")


class _TmnxLocUsrDbPppoeIngIpv4FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbPppoeIngIpv4FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbPppoeIngIpv4FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbPppoeIngIpv4FltrId_Object = MibTableColumn
tmnxLocUsrDbPppoeIngIpv4FltrId = _TmnxLocUsrDbPppoeIngIpv4FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 41),
    _TmnxLocUsrDbPppoeIngIpv4FltrId_Type()
)
tmnxLocUsrDbPppoeIngIpv4FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIngIpv4FltrId.setStatus("current")


class _TmnxLocUsrDbPppoeEgrIpv4FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbPppoeEgrIpv4FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbPppoeEgrIpv4FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbPppoeEgrIpv4FltrId_Object = MibTableColumn
tmnxLocUsrDbPppoeEgrIpv4FltrId = _TmnxLocUsrDbPppoeEgrIpv4FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 42),
    _TmnxLocUsrDbPppoeEgrIpv4FltrId_Type()
)
tmnxLocUsrDbPppoeEgrIpv4FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeEgrIpv4FltrId.setStatus("current")


class _TmnxLocUsrDbPppoeIngIpv6FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbPppoeIngIpv6FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbPppoeIngIpv6FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbPppoeIngIpv6FltrId_Object = MibTableColumn
tmnxLocUsrDbPppoeIngIpv6FltrId = _TmnxLocUsrDbPppoeIngIpv6FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 43),
    _TmnxLocUsrDbPppoeIngIpv6FltrId_Type()
)
tmnxLocUsrDbPppoeIngIpv6FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIngIpv6FltrId.setStatus("current")


class _TmnxLocUsrDbPppoeEgrIpv6FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbPppoeEgrIpv6FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbPppoeEgrIpv6FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbPppoeEgrIpv6FltrId_Object = MibTableColumn
tmnxLocUsrDbPppoeEgrIpv6FltrId = _TmnxLocUsrDbPppoeEgrIpv6FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 44),
    _TmnxLocUsrDbPppoeEgrIpv6FltrId_Type()
)
tmnxLocUsrDbPppoeEgrIpv6FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeEgrIpv6FltrId.setStatus("current")


class _TmnxLocUsrDbPppoeUseGiAddrScope_Type(Integer32):
    """Custom type tmnxLocUsrDbPppoeUseGiAddrScope based on Integer32"""
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


_TmnxLocUsrDbPppoeUseGiAddrScope_Type.__name__ = "Integer32"
_TmnxLocUsrDbPppoeUseGiAddrScope_Object = MibTableColumn
tmnxLocUsrDbPppoeUseGiAddrScope = _TmnxLocUsrDbPppoeUseGiAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 45),
    _TmnxLocUsrDbPppoeUseGiAddrScope_Type()
)
tmnxLocUsrDbPppoeUseGiAddrScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUseGiAddrScope.setStatus("current")


class _TmnxLocUsrDbPppoeSecPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeSecPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeSecPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeSecPool_Object = MibTableColumn
tmnxLocUsrDbPppoeSecPool = _TmnxLocUsrDbPppoeSecPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 46),
    _TmnxLocUsrDbPppoeSecPool_Type()
)
tmnxLocUsrDbPppoeSecPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeSecPool.setStatus("current")


class _TmnxLocUsrDbPppoePreAuthPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoePreAuthPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoePreAuthPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoePreAuthPolicy_Object = MibTableColumn
tmnxLocUsrDbPppoePreAuthPolicy = _TmnxLocUsrDbPppoePreAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 47),
    _TmnxLocUsrDbPppoePreAuthPolicy_Type()
)
tmnxLocUsrDbPppoePreAuthPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoePreAuthPolicy.setStatus("current")


class _TmnxLocUsrDbPppoeUseCPDelimiter_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeUseCPDelimiter based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_TmnxLocUsrDbPppoeUseCPDelimiter_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeUseCPDelimiter_Object = MibTableColumn
tmnxLocUsrDbPppoeUseCPDelimiter = _TmnxLocUsrDbPppoeUseCPDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 48),
    _TmnxLocUsrDbPppoeUseCPDelimiter_Type()
)
tmnxLocUsrDbPppoeUseCPDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUseCPDelimiter.setStatus("current")
_TmnxLocUsrDbPppoeEncTagRangeType_Type = TmnxPortEncapType
_TmnxLocUsrDbPppoeEncTagRangeType_Object = MibTableColumn
tmnxLocUsrDbPppoeEncTagRangeType = _TmnxLocUsrDbPppoeEncTagRangeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 49),
    _TmnxLocUsrDbPppoeEncTagRangeType_Type()
)
tmnxLocUsrDbPppoeEncTagRangeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeEncTagRangeType.setStatus("current")
_TmnxLocUsrDbPppoeEncTagRangeStrt_Type = TmnxEncapVal
_TmnxLocUsrDbPppoeEncTagRangeStrt_Object = MibTableColumn
tmnxLocUsrDbPppoeEncTagRangeStrt = _TmnxLocUsrDbPppoeEncTagRangeStrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 50),
    _TmnxLocUsrDbPppoeEncTagRangeStrt_Type()
)
tmnxLocUsrDbPppoeEncTagRangeStrt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeEncTagRangeStrt.setStatus("current")
_TmnxLocUsrDbPppoeEncTagRangeEnd_Type = TmnxEncapVal
_TmnxLocUsrDbPppoeEncTagRangeEnd_Object = MibTableColumn
tmnxLocUsrDbPppoeEncTagRangeEnd = _TmnxLocUsrDbPppoeEncTagRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 51),
    _TmnxLocUsrDbPppoeEncTagRangeEnd_Type()
)
tmnxLocUsrDbPppoeEncTagRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeEncTagRangeEnd.setStatus("current")


class _TmnxLocUsrDbPppoeMsapGroupIfPfx_Type(TmnxLudbMsapGrpIfPfxSfxType):
    """Custom type tmnxLocUsrDbPppoeMsapGroupIfPfx based on TmnxLudbMsapGrpIfPfxSfxType"""
    defaultValue = 1


_TmnxLocUsrDbPppoeMsapGroupIfPfx_Type.__name__ = "TmnxLudbMsapGrpIfPfxSfxType"
_TmnxLocUsrDbPppoeMsapGroupIfPfx_Object = MibTableColumn
tmnxLocUsrDbPppoeMsapGroupIfPfx = _TmnxLocUsrDbPppoeMsapGroupIfPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 52),
    _TmnxLocUsrDbPppoeMsapGroupIfPfx_Type()
)
tmnxLocUsrDbPppoeMsapGroupIfPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMsapGroupIfPfx.setStatus("current")


class _TmnxLocUsrDbPppoeMsapGroupIfSfx_Type(TmnxLudbMsapGrpIfPfxSfxType):
    """Custom type tmnxLocUsrDbPppoeMsapGroupIfSfx based on TmnxLudbMsapGrpIfPfxSfxType"""
    defaultValue = 1


_TmnxLocUsrDbPppoeMsapGroupIfSfx_Type.__name__ = "TmnxLudbMsapGrpIfPfxSfxType"
_TmnxLocUsrDbPppoeMsapGroupIfSfx_Object = MibTableColumn
tmnxLocUsrDbPppoeMsapGroupIfSfx = _TmnxLocUsrDbPppoeMsapGroupIfSfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 53),
    _TmnxLocUsrDbPppoeMsapGroupIfSfx_Type()
)
tmnxLocUsrDbPppoeMsapGroupIfSfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMsapGroupIfSfx.setStatus("current")


class _TmnxLocUsrDbPppoeAcctPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeAcctPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeAcctPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeAcctPolicy_Object = MibTableColumn
tmnxLocUsrDbPppoeAcctPolicy = _TmnxLocUsrDbPppoeAcctPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 54),
    _TmnxLocUsrDbPppoeAcctPolicy_Type()
)
tmnxLocUsrDbPppoeAcctPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAcctPolicy.setStatus("current")


class _TmnxLocUsrDbPppoeDuplAcctPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeDuplAcctPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeDuplAcctPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeDuplAcctPolicy_Object = MibTableColumn
tmnxLocUsrDbPppoeDuplAcctPolicy = _TmnxLocUsrDbPppoeDuplAcctPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 55),
    _TmnxLocUsrDbPppoeDuplAcctPolicy_Type()
)
tmnxLocUsrDbPppoeDuplAcctPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeDuplAcctPolicy.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6Addr_Type(InetAddress):
    """Custom type tmnxLocUsrDbPppoeIpv6Addr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxLocUsrDbPppoeIpv6Addr_Type.__name__ = "InetAddress"
_TmnxLocUsrDbPppoeIpv6Addr_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6Addr = _TmnxLocUsrDbPppoeIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 56),
    _TmnxLocUsrDbPppoeIpv6Addr_Type()
)
tmnxLocUsrDbPppoeIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6Addr.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6DelPfx_Type(InetAddress):
    """Custom type tmnxLocUsrDbPppoeIpv6DelPfx based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxLocUsrDbPppoeIpv6DelPfx_Type.__name__ = "InetAddress"
_TmnxLocUsrDbPppoeIpv6DelPfx_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6DelPfx = _TmnxLocUsrDbPppoeIpv6DelPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 57),
    _TmnxLocUsrDbPppoeIpv6DelPfx_Type()
)
tmnxLocUsrDbPppoeIpv6DelPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6DelPfx.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6DelPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxLocUsrDbPppoeIpv6DelPfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(48, 64),
    )


_TmnxLocUsrDbPppoeIpv6DelPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxLocUsrDbPppoeIpv6DelPfxLen_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6DelPfxLen = _TmnxLocUsrDbPppoeIpv6DelPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 58),
    _TmnxLocUsrDbPppoeIpv6DelPfxLen_Type()
)
tmnxLocUsrDbPppoeIpv6DelPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6DelPfxLen.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6ReqDelPfxLn_Type(InetAddressPrefixLength):
    """Custom type tmnxLocUsrDbPppoeIpv6ReqDelPfxLn based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(48, 64),
    )


_TmnxLocUsrDbPppoeIpv6ReqDelPfxLn_Type.__name__ = "InetAddressPrefixLength"
_TmnxLocUsrDbPppoeIpv6ReqDelPfxLn_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6ReqDelPfxLn = _TmnxLocUsrDbPppoeIpv6ReqDelPfxLn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 59),
    _TmnxLocUsrDbPppoeIpv6ReqDelPfxLn_Type()
)
tmnxLocUsrDbPppoeIpv6ReqDelPfxLn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6ReqDelPfxLn.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6SlaacPfx_Type(InetAddress):
    """Custom type tmnxLocUsrDbPppoeIpv6SlaacPfx based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxLocUsrDbPppoeIpv6SlaacPfx_Type.__name__ = "InetAddress"
_TmnxLocUsrDbPppoeIpv6SlaacPfx_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6SlaacPfx = _TmnxLocUsrDbPppoeIpv6SlaacPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 60),
    _TmnxLocUsrDbPppoeIpv6SlaacPfx_Type()
)
tmnxLocUsrDbPppoeIpv6SlaacPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6SlaacPfx.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6SlaacPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxLocUsrDbPppoeIpv6SlaacPfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 64),
    )


_TmnxLocUsrDbPppoeIpv6SlaacPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxLocUsrDbPppoeIpv6SlaacPfxLen_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6SlaacPfxLen = _TmnxLocUsrDbPppoeIpv6SlaacPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 61),
    _TmnxLocUsrDbPppoeIpv6SlaacPfxLen_Type()
)
tmnxLocUsrDbPppoeIpv6SlaacPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6SlaacPfxLen.setStatus("current")


class _TmnxLocUsrDbPppoeForceIpv6cp_Type(TruthValue):
    """Custom type tmnxLocUsrDbPppoeForceIpv6cp based on TruthValue"""
    defaultValue = 2


_TmnxLocUsrDbPppoeForceIpv6cp_Type.__name__ = "TruthValue"
_TmnxLocUsrDbPppoeForceIpv6cp_Object = MibTableColumn
tmnxLocUsrDbPppoeForceIpv6cp = _TmnxLocUsrDbPppoeForceIpv6cp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 62),
    _TmnxLocUsrDbPppoeForceIpv6cp_Type()
)
tmnxLocUsrDbPppoeForceIpv6cp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeForceIpv6cp.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6DelPfxPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeIpv6DelPfxPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeIpv6DelPfxPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeIpv6DelPfxPool_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6DelPfxPool = _TmnxLocUsrDbPppoeIpv6DelPfxPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 63),
    _TmnxLocUsrDbPppoeIpv6DelPfxPool_Type()
)
tmnxLocUsrDbPppoeIpv6DelPfxPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6DelPfxPool.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6WanAddrPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeIpv6WanAddrPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeIpv6WanAddrPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeIpv6WanAddrPool_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6WanAddrPool = _TmnxLocUsrDbPppoeIpv6WanAddrPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 64),
    _TmnxLocUsrDbPppoeIpv6WanAddrPool_Type()
)
tmnxLocUsrDbPppoeIpv6WanAddrPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6WanAddrPool.setStatus("current")


class _TmnxLocUsrDbPppoeIpv6SlaacPfxPl_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeIpv6SlaacPfxPl based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeIpv6SlaacPfxPl_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeIpv6SlaacPfxPl_Object = MibTableColumn
tmnxLocUsrDbPppoeIpv6SlaacPfxPl = _TmnxLocUsrDbPppoeIpv6SlaacPfxPl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 4, 1, 65),
    _TmnxLocUsrDbPppoeIpv6SlaacPfxPl_Type()
)
tmnxLocUsrDbPppoeIpv6SlaacPfxPl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeIpv6SlaacPfxPl.setStatus("current")
_TmnxLocUsrDbPppoeUnmatchedTable_Object = MibTable
tmnxLocUsrDbPppoeUnmatchedTable = _TmnxLocUsrDbPppoeUnmatchedTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnmatchedTable.setStatus("current")
_TmnxLocUsrDbPppoeUnmatchedEntry_Object = MibTableRow
tmnxLocUsrDbPppoeUnmatchedEntry = _TmnxLocUsrDbPppoeUnmatchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1)
)
tmnxLocUsrDbPppoeUnmatchedEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeHostName"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnmatchedEntry.setStatus("current")
_TmnxLocUsrDbPppoeUnMacAddress_Type = MacAddress
_TmnxLocUsrDbPppoeUnMacAddress_Object = MibTableColumn
tmnxLocUsrDbPppoeUnMacAddress = _TmnxLocUsrDbPppoeUnMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 1),
    _TmnxLocUsrDbPppoeUnMacAddress_Type()
)
tmnxLocUsrDbPppoeUnMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnMacAddress.setStatus("current")


class _TmnxLocUsrDbPppoeUnCircuitId_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeUnCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeUnCircuitId_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeUnCircuitId_Object = MibTableColumn
tmnxLocUsrDbPppoeUnCircuitId = _TmnxLocUsrDbPppoeUnCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 2),
    _TmnxLocUsrDbPppoeUnCircuitId_Type()
)
tmnxLocUsrDbPppoeUnCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnCircuitId.setStatus("current")


class _TmnxLocUsrDbPppoeUnRemoteId_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeUnRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeUnRemoteId_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeUnRemoteId_Object = MibTableColumn
tmnxLocUsrDbPppoeUnRemoteId = _TmnxLocUsrDbPppoeUnRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 3),
    _TmnxLocUsrDbPppoeUnRemoteId_Type()
)
tmnxLocUsrDbPppoeUnRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnRemoteId.setStatus("current")
_TmnxLocUsrDbPppoeUnUserNameFmt_Type = TmnxLocUsrDbUserNameFormat
_TmnxLocUsrDbPppoeUnUserNameFmt_Object = MibTableColumn
tmnxLocUsrDbPppoeUnUserNameFmt = _TmnxLocUsrDbPppoeUnUserNameFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 4),
    _TmnxLocUsrDbPppoeUnUserNameFmt_Type()
)
tmnxLocUsrDbPppoeUnUserNameFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnUserNameFmt.setStatus("current")
_TmnxLocUsrDbPppoeUnUserName_Type = TmnxPppoeUserNameOrEmpty
_TmnxLocUsrDbPppoeUnUserName_Object = MibTableColumn
tmnxLocUsrDbPppoeUnUserName = _TmnxLocUsrDbPppoeUnUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 5),
    _TmnxLocUsrDbPppoeUnUserName_Type()
)
tmnxLocUsrDbPppoeUnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnUserName.setStatus("current")
_TmnxLocUsrDbPppoeUnmatchedReason_Type = TmnxLocUsrDbUnmatchedReason
_TmnxLocUsrDbPppoeUnmatchedReason_Object = MibTableColumn
tmnxLocUsrDbPppoeUnmatchedReason = _TmnxLocUsrDbPppoeUnmatchedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 6),
    _TmnxLocUsrDbPppoeUnmatchedReason_Type()
)
tmnxLocUsrDbPppoeUnmatchedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnmatchedReason.setStatus("current")


class _TmnxLocUsrDbPppoeUnDuplicateHost_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeUnDuplicateHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLocUsrDbPppoeUnDuplicateHost_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeUnDuplicateHost_Object = MibTableColumn
tmnxLocUsrDbPppoeUnDuplicateHost = _TmnxLocUsrDbPppoeUnDuplicateHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 7),
    _TmnxLocUsrDbPppoeUnDuplicateHost_Type()
)
tmnxLocUsrDbPppoeUnDuplicateHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnDuplicateHost.setStatus("current")


class _TmnxLocUsrDbPppoeUnServiceName_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeUnServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeUnServiceName_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeUnServiceName_Object = MibTableColumn
tmnxLocUsrDbPppoeUnServiceName = _TmnxLocUsrDbPppoeUnServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 8),
    _TmnxLocUsrDbPppoeUnServiceName_Type()
)
tmnxLocUsrDbPppoeUnServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnServiceName.setStatus("current")


class _TmnxLocUsrDbPppoeUnSapId_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeUnSapId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeUnSapId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeUnSapId_Object = MibTableColumn
tmnxLocUsrDbPppoeUnSapId = _TmnxLocUsrDbPppoeUnSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 5, 1, 9),
    _TmnxLocUsrDbPppoeUnSapId_Type()
)
tmnxLocUsrDbPppoeUnSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeUnSapId.setStatus("current")
_TmnxLocUsrDbPppoeOptionTbleLstCh_Type = TimeStamp
_TmnxLocUsrDbPppoeOptionTbleLstCh_Object = MibScalar
tmnxLocUsrDbPppoeOptionTbleLstCh = _TmnxLocUsrDbPppoeOptionTbleLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 6),
    _TmnxLocUsrDbPppoeOptionTbleLstCh_Type()
)
tmnxLocUsrDbPppoeOptionTbleLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionTbleLstCh.setStatus("current")
_TmnxLocUsrDbPppoeOptionTable_Object = MibTable
tmnxLocUsrDbPppoeOptionTable = _TmnxLocUsrDbPppoeOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionTable.setStatus("current")
_TmnxLocUsrDbPppoeOptionEntry_Object = MibTableRow
tmnxLocUsrDbPppoeOptionEntry = _TmnxLocUsrDbPppoeOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 7, 1)
)
tmnxLocUsrDbPppoeOptionEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeHostName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionNumber"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionEntry.setStatus("current")


class _TmnxLocUsrDbPppoeOptionNumber_Type(Unsigned32):
    """Custom type tmnxLocUsrDbPppoeOptionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_TmnxLocUsrDbPppoeOptionNumber_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbPppoeOptionNumber_Object = MibTableColumn
tmnxLocUsrDbPppoeOptionNumber = _TmnxLocUsrDbPppoeOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 7, 1, 1),
    _TmnxLocUsrDbPppoeOptionNumber_Type()
)
tmnxLocUsrDbPppoeOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionNumber.setStatus("current")
_TmnxLocUsrDbPppoeOptionRowStatus_Type = RowStatus
_TmnxLocUsrDbPppoeOptionRowStatus_Object = MibTableColumn
tmnxLocUsrDbPppoeOptionRowStatus = _TmnxLocUsrDbPppoeOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 7, 1, 2),
    _TmnxLocUsrDbPppoeOptionRowStatus_Type()
)
tmnxLocUsrDbPppoeOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionRowStatus.setStatus("current")
_TmnxLocUsrDbPppoeOptionLstChngTm_Type = TimeStamp
_TmnxLocUsrDbPppoeOptionLstChngTm_Object = MibTableColumn
tmnxLocUsrDbPppoeOptionLstChngTm = _TmnxLocUsrDbPppoeOptionLstChngTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 7, 1, 3),
    _TmnxLocUsrDbPppoeOptionLstChngTm_Type()
)
tmnxLocUsrDbPppoeOptionLstChngTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionLstChngTm.setStatus("current")
_TmnxLocUsrDbPppoeOptionType_Type = TmnxDhcpOptionType
_TmnxLocUsrDbPppoeOptionType_Object = MibTableColumn
tmnxLocUsrDbPppoeOptionType = _TmnxLocUsrDbPppoeOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 7, 1, 4),
    _TmnxLocUsrDbPppoeOptionType_Type()
)
tmnxLocUsrDbPppoeOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionType.setStatus("current")


class _TmnxLocUsrDbPppoeOptionValue_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeOptionValue_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeOptionValue_Object = MibTableColumn
tmnxLocUsrDbPppoeOptionValue = _TmnxLocUsrDbPppoeOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 7, 1, 5),
    _TmnxLocUsrDbPppoeOptionValue_Type()
)
tmnxLocUsrDbPppoeOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeOptionValue.setStatus("current")
_TmnxLocUsrDbDhcpTableLastChange_Type = TimeStamp
_TmnxLocUsrDbDhcpTableLastChange_Object = MibScalar
tmnxLocUsrDbDhcpTableLastChange = _TmnxLocUsrDbDhcpTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 8),
    _TmnxLocUsrDbDhcpTableLastChange_Type()
)
tmnxLocUsrDbDhcpTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpTableLastChange.setStatus("current")
_TmnxLocUsrDbDhcpTable_Object = MibTable
tmnxLocUsrDbDhcpTable = _TmnxLocUsrDbDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpTable.setStatus("current")
_TmnxLocUsrDbDhcpEntry_Object = MibTableRow
tmnxLocUsrDbDhcpEntry = _TmnxLocUsrDbDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1)
)
tmnxLocUsrDbDhcpEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpHostName"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpEntry.setStatus("current")


class _TmnxLocUsrDbDhcpHostName_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxLocUsrDbDhcpHostName_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpHostName_Object = MibTableColumn
tmnxLocUsrDbDhcpHostName = _TmnxLocUsrDbDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 1),
    _TmnxLocUsrDbDhcpHostName_Type()
)
tmnxLocUsrDbDhcpHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpHostName.setStatus("current")
_TmnxLocUsrDbDhcpRowStatus_Type = RowStatus
_TmnxLocUsrDbDhcpRowStatus_Object = MibTableColumn
tmnxLocUsrDbDhcpRowStatus = _TmnxLocUsrDbDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 2),
    _TmnxLocUsrDbDhcpRowStatus_Type()
)
tmnxLocUsrDbDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpRowStatus.setStatus("current")
_TmnxLocUsrDbDhcpLastChangeTime_Type = TimeStamp
_TmnxLocUsrDbDhcpLastChangeTime_Object = MibTableColumn
tmnxLocUsrDbDhcpLastChangeTime = _TmnxLocUsrDbDhcpLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 3),
    _TmnxLocUsrDbDhcpLastChangeTime_Type()
)
tmnxLocUsrDbDhcpLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpLastChangeTime.setStatus("current")


class _TmnxLocUsrDbDhcpAdminState_Type(TmnxAdminState):
    """Custom type tmnxLocUsrDbDhcpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLocUsrDbDhcpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLocUsrDbDhcpAdminState_Object = MibTableColumn
tmnxLocUsrDbDhcpAdminState = _TmnxLocUsrDbDhcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 4),
    _TmnxLocUsrDbDhcpAdminState_Type()
)
tmnxLocUsrDbDhcpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAdminState.setStatus("current")


class _TmnxLocUsrDbDhcpMacAddress_Type(MacAddress):
    """Custom type tmnxLocUsrDbDhcpMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxLocUsrDbDhcpMacAddress_Type.__name__ = "MacAddress"
_TmnxLocUsrDbDhcpMacAddress_Object = MibTableColumn
tmnxLocUsrDbDhcpMacAddress = _TmnxLocUsrDbDhcpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 5),
    _TmnxLocUsrDbDhcpMacAddress_Type()
)
tmnxLocUsrDbDhcpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMacAddress.setStatus("current")


class _TmnxLocUsrDbDhcpCircuitIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLocUsrDbDhcpCircuitIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLocUsrDbDhcpCircuitIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLocUsrDbDhcpCircuitIdFmt_Object = MibTableColumn
tmnxLocUsrDbDhcpCircuitIdFmt = _TmnxLocUsrDbDhcpCircuitIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 6),
    _TmnxLocUsrDbDhcpCircuitIdFmt_Type()
)
tmnxLocUsrDbDhcpCircuitIdFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpCircuitIdFmt.setStatus("current")


class _TmnxLocUsrDbDhcpCircuitId_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpCircuitId based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpCircuitId_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpCircuitId_Object = MibTableColumn
tmnxLocUsrDbDhcpCircuitId = _TmnxLocUsrDbDhcpCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 7),
    _TmnxLocUsrDbDhcpCircuitId_Type()
)
tmnxLocUsrDbDhcpCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpCircuitId.setStatus("current")


class _TmnxLocUsrDbDhcpRemoteId_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpRemoteId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpRemoteId_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpRemoteId_Object = MibTableColumn
tmnxLocUsrDbDhcpRemoteId = _TmnxLocUsrDbDhcpRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 8),
    _TmnxLocUsrDbDhcpRemoteId_Type()
)
tmnxLocUsrDbDhcpRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpRemoteId.setStatus("current")


class _TmnxLocUsrDbDhcpSystemId_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpSystemId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpSystemId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpSystemId_Object = MibTableColumn
tmnxLocUsrDbDhcpSystemId = _TmnxLocUsrDbDhcpSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 9),
    _TmnxLocUsrDbDhcpSystemId_Type()
)
tmnxLocUsrDbDhcpSystemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpSystemId.setStatus("current")


class _TmnxLocUsrDbDhcpServiceId_Type(TmnxServId):
    """Custom type tmnxLocUsrDbDhcpServiceId based on TmnxServId"""
    defaultValue = 0


_TmnxLocUsrDbDhcpServiceId_Type.__name__ = "TmnxServId"
_TmnxLocUsrDbDhcpServiceId_Object = MibTableColumn
tmnxLocUsrDbDhcpServiceId = _TmnxLocUsrDbDhcpServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 10),
    _TmnxLocUsrDbDhcpServiceId_Type()
)
tmnxLocUsrDbDhcpServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpServiceId.setStatus("current")


class _TmnxLocUsrDbDhcpSapId_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpSapId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpSapId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpSapId_Object = MibTableColumn
tmnxLocUsrDbDhcpSapId = _TmnxLocUsrDbDhcpSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 11),
    _TmnxLocUsrDbDhcpSapId_Type()
)
tmnxLocUsrDbDhcpSapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpSapId.setStatus("current")


class _TmnxLocUsrDbDhcpString_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpString_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpString_Object = MibTableColumn
tmnxLocUsrDbDhcpString = _TmnxLocUsrDbDhcpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 12),
    _TmnxLocUsrDbDhcpString_Type()
)
tmnxLocUsrDbDhcpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpString.setStatus("current")


class _TmnxLocUsrDbDhcpOption60_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpOption60 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLocUsrDbDhcpOption60_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpOption60_Object = MibTableColumn
tmnxLocUsrDbDhcpOption60 = _TmnxLocUsrDbDhcpOption60_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 13),
    _TmnxLocUsrDbDhcpOption60_Type()
)
tmnxLocUsrDbDhcpOption60.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption60.setStatus("current")


class _TmnxLocUsrDbDhcpAddrType_Type(InetAddressType):
    """Custom type tmnxLocUsrDbDhcpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLocUsrDbDhcpAddrType_Type.__name__ = "InetAddressType"
_TmnxLocUsrDbDhcpAddrType_Object = MibTableColumn
tmnxLocUsrDbDhcpAddrType = _TmnxLocUsrDbDhcpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 14),
    _TmnxLocUsrDbDhcpAddrType_Type()
)
tmnxLocUsrDbDhcpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAddrType.setStatus("current")


class _TmnxLocUsrDbDhcpAddress_Type(InetAddress):
    """Custom type tmnxLocUsrDbDhcpAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLocUsrDbDhcpAddress_Type.__name__ = "InetAddress"
_TmnxLocUsrDbDhcpAddress_Object = MibTableColumn
tmnxLocUsrDbDhcpAddress = _TmnxLocUsrDbDhcpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 15),
    _TmnxLocUsrDbDhcpAddress_Type()
)
tmnxLocUsrDbDhcpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAddress.setStatus("current")


class _TmnxLocUsrDbDhcpPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpPool_Object = MibTableColumn
tmnxLocUsrDbDhcpPool = _TmnxLocUsrDbDhcpPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 16),
    _TmnxLocUsrDbDhcpPool_Type()
)
tmnxLocUsrDbDhcpPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpPool.setStatus("current")


class _TmnxLocUsrDbDhcpUseGiAddress_Type(TruthValue):
    """Custom type tmnxLocUsrDbDhcpUseGiAddress based on TruthValue"""
    defaultValue = 2


_TmnxLocUsrDbDhcpUseGiAddress_Type.__name__ = "TruthValue"
_TmnxLocUsrDbDhcpUseGiAddress_Object = MibTableColumn
tmnxLocUsrDbDhcpUseGiAddress = _TmnxLocUsrDbDhcpUseGiAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 17),
    _TmnxLocUsrDbDhcpUseGiAddress_Type()
)
tmnxLocUsrDbDhcpUseGiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUseGiAddress.setStatus("current")


class _TmnxLocUsrDbDhcpIdStringOptNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpIdStringOptNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxLocUsrDbDhcpIdStringOptNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpIdStringOptNum_Object = MibTableColumn
tmnxLocUsrDbDhcpIdStringOptNum = _TmnxLocUsrDbDhcpIdStringOptNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 18),
    _TmnxLocUsrDbDhcpIdStringOptNum_Type()
)
tmnxLocUsrDbDhcpIdStringOptNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIdStringOptNum.setStatus("current")


class _TmnxLocUsrDbDhcpSubscriberId_Type(TmnxSubIdentStringOrEmpty):
    """Custom type tmnxLocUsrDbDhcpSubscriberId based on TmnxSubIdentStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpSubscriberId_Type.__name__ = "TmnxSubIdentStringOrEmpty"
_TmnxLocUsrDbDhcpSubscriberId_Object = MibTableColumn
tmnxLocUsrDbDhcpSubscriberId = _TmnxLocUsrDbDhcpSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 19),
    _TmnxLocUsrDbDhcpSubscriberId_Type()
)
tmnxLocUsrDbDhcpSubscriberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpSubscriberId.setStatus("current")


class _TmnxLocUsrDbDhcpSlaProfString_Type(TmnxSlaProfileStringOrEmpty):
    """Custom type tmnxLocUsrDbDhcpSlaProfString based on TmnxSlaProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpSlaProfString_Type.__name__ = "TmnxSlaProfileStringOrEmpty"
_TmnxLocUsrDbDhcpSlaProfString_Object = MibTableColumn
tmnxLocUsrDbDhcpSlaProfString = _TmnxLocUsrDbDhcpSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 20),
    _TmnxLocUsrDbDhcpSlaProfString_Type()
)
tmnxLocUsrDbDhcpSlaProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpSlaProfString.setStatus("current")


class _TmnxLocUsrDbDhcpSubProfString_Type(TmnxSubProfileStringOrEmpty):
    """Custom type tmnxLocUsrDbDhcpSubProfString based on TmnxSubProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpSubProfString_Type.__name__ = "TmnxSubProfileStringOrEmpty"
_TmnxLocUsrDbDhcpSubProfString_Object = MibTableColumn
tmnxLocUsrDbDhcpSubProfString = _TmnxLocUsrDbDhcpSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 21),
    _TmnxLocUsrDbDhcpSubProfString_Type()
)
tmnxLocUsrDbDhcpSubProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpSubProfString.setStatus("current")


class _TmnxLocUsrDbDhcpAppProfString_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpAppProfString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxLocUsrDbDhcpAppProfString_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpAppProfString_Object = MibTableColumn
tmnxLocUsrDbDhcpAppProfString = _TmnxLocUsrDbDhcpAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 22),
    _TmnxLocUsrDbDhcpAppProfString_Type()
)
tmnxLocUsrDbDhcpAppProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAppProfString.setStatus("current")


class _TmnxLocUsrDbDhcpAncpString_Type(TmnxAncpStringOrZero):
    """Custom type tmnxLocUsrDbDhcpAncpString based on TmnxAncpStringOrZero"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpAncpString_Type.__name__ = "TmnxAncpStringOrZero"
_TmnxLocUsrDbDhcpAncpString_Object = MibTableColumn
tmnxLocUsrDbDhcpAncpString = _TmnxLocUsrDbDhcpAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 23),
    _TmnxLocUsrDbDhcpAncpString_Type()
)
tmnxLocUsrDbDhcpAncpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAncpString.setStatus("current")


class _TmnxLocUsrDbDhcpInterDestId_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpInterDestId based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpInterDestId_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpInterDestId_Object = MibTableColumn
tmnxLocUsrDbDhcpInterDestId = _TmnxLocUsrDbDhcpInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 24),
    _TmnxLocUsrDbDhcpInterDestId_Type()
)
tmnxLocUsrDbDhcpInterDestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpInterDestId.setStatus("current")


class _TmnxLocUsrDbDhcpAuthPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpAuthPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpAuthPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpAuthPolicy_Object = MibTableColumn
tmnxLocUsrDbDhcpAuthPolicy = _TmnxLocUsrDbDhcpAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 25),
    _TmnxLocUsrDbDhcpAuthPolicy_Type()
)
tmnxLocUsrDbDhcpAuthPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAuthPolicy.setStatus("current")


class _TmnxLocUsrDbDhcpServerAddrType_Type(InetAddressType):
    """Custom type tmnxLocUsrDbDhcpServerAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLocUsrDbDhcpServerAddrType_Type.__name__ = "InetAddressType"
_TmnxLocUsrDbDhcpServerAddrType_Object = MibTableColumn
tmnxLocUsrDbDhcpServerAddrType = _TmnxLocUsrDbDhcpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 26),
    _TmnxLocUsrDbDhcpServerAddrType_Type()
)
tmnxLocUsrDbDhcpServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpServerAddrType.setStatus("current")


class _TmnxLocUsrDbDhcpServerAddress_Type(InetAddress):
    """Custom type tmnxLocUsrDbDhcpServerAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLocUsrDbDhcpServerAddress_Type.__name__ = "InetAddress"
_TmnxLocUsrDbDhcpServerAddress_Object = MibTableColumn
tmnxLocUsrDbDhcpServerAddress = _TmnxLocUsrDbDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 27),
    _TmnxLocUsrDbDhcpServerAddress_Type()
)
tmnxLocUsrDbDhcpServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpServerAddress.setStatus("current")


class _TmnxLocUsrDbDhcpAuthDomainName_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpAuthDomainName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLocUsrDbDhcpAuthDomainName_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpAuthDomainName_Object = MibTableColumn
tmnxLocUsrDbDhcpAuthDomainName = _TmnxLocUsrDbDhcpAuthDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 28),
    _TmnxLocUsrDbDhcpAuthDomainName_Type()
)
tmnxLocUsrDbDhcpAuthDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAuthDomainName.setStatus("current")


class _TmnxLocUsrDbDhcpCategoryMapName_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpCategoryMapName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpCategoryMapName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpCategoryMapName_Object = MibTableColumn
tmnxLocUsrDbDhcpCategoryMapName = _TmnxLocUsrDbDhcpCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 29),
    _TmnxLocUsrDbDhcpCategoryMapName_Type()
)
tmnxLocUsrDbDhcpCategoryMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpCategoryMapName.setStatus("current")


class _TmnxLocUsrDbDhcpOption60Fmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLocUsrDbDhcpOption60Fmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 3


_TmnxLocUsrDbDhcpOption60Fmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLocUsrDbDhcpOption60Fmt_Object = MibTableColumn
tmnxLocUsrDbDhcpOption60Fmt = _TmnxLocUsrDbDhcpOption60Fmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 30),
    _TmnxLocUsrDbDhcpOption60Fmt_Type()
)
tmnxLocUsrDbDhcpOption60Fmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption60Fmt.setStatus("current")


class _TmnxLocUsrDbDhcpUseClientPool_Type(TruthValue):
    """Custom type tmnxLocUsrDbDhcpUseClientPool based on TruthValue"""
    defaultValue = 2


_TmnxLocUsrDbDhcpUseClientPool_Type.__name__ = "TruthValue"
_TmnxLocUsrDbDhcpUseClientPool_Object = MibTableColumn
tmnxLocUsrDbDhcpUseClientPool = _TmnxLocUsrDbDhcpUseClientPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 31),
    _TmnxLocUsrDbDhcpUseClientPool_Type()
)
tmnxLocUsrDbDhcpUseClientPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUseClientPool.setStatus("current")


class _TmnxLocUsrDbDhcpDefMsapPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxLocUsrDbDhcpDefMsapPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpDefMsapPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxLocUsrDbDhcpDefMsapPolicy_Object = MibTableColumn
tmnxLocUsrDbDhcpDefMsapPolicy = _TmnxLocUsrDbDhcpDefMsapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 32),
    _TmnxLocUsrDbDhcpDefMsapPolicy_Type()
)
tmnxLocUsrDbDhcpDefMsapPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpDefMsapPolicy.setStatus("current")


class _TmnxLocUsrDbDhcpDefMsapService_Type(TmnxServId):
    """Custom type tmnxLocUsrDbDhcpDefMsapService based on TmnxServId"""
    defaultValue = 0


_TmnxLocUsrDbDhcpDefMsapService_Type.__name__ = "TmnxServId"
_TmnxLocUsrDbDhcpDefMsapService_Object = MibTableColumn
tmnxLocUsrDbDhcpDefMsapService = _TmnxLocUsrDbDhcpDefMsapService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 33),
    _TmnxLocUsrDbDhcpDefMsapService_Type()
)
tmnxLocUsrDbDhcpDefMsapService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpDefMsapService.setStatus("current")


class _TmnxLocUsrDbDhcpDefMsapGroupIf_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpDefMsapGroupIf based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpDefMsapGroupIf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpDefMsapGroupIf_Object = MibTableColumn
tmnxLocUsrDbDhcpDefMsapGroupIf = _TmnxLocUsrDbDhcpDefMsapGroupIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 34),
    _TmnxLocUsrDbDhcpDefMsapGroupIf_Type()
)
tmnxLocUsrDbDhcpDefMsapGroupIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpDefMsapGroupIf.setStatus("current")


class _TmnxLocUsrDbDhcpRetailerSvcId_Type(TmnxServId):
    """Custom type tmnxLocUsrDbDhcpRetailerSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxLocUsrDbDhcpRetailerSvcId_Type.__name__ = "TmnxServId"
_TmnxLocUsrDbDhcpRetailerSvcId_Object = MibTableColumn
tmnxLocUsrDbDhcpRetailerSvcId = _TmnxLocUsrDbDhcpRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 35),
    _TmnxLocUsrDbDhcpRetailerSvcId_Type()
)
tmnxLocUsrDbDhcpRetailerSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpRetailerSvcId.setStatus("current")


class _TmnxLocUsrDbDhcpRemoteIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLocUsrDbDhcpRemoteIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLocUsrDbDhcpRemoteIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLocUsrDbDhcpRemoteIdFmt_Object = MibTableColumn
tmnxLocUsrDbDhcpRemoteIdFmt = _TmnxLocUsrDbDhcpRemoteIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 36),
    _TmnxLocUsrDbDhcpRemoteIdFmt_Type()
)
tmnxLocUsrDbDhcpRemoteIdFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpRemoteIdFmt.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6Addr_Type(InetAddress):
    """Custom type tmnxLocUsrDbDhcpIpv6Addr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxLocUsrDbDhcpIpv6Addr_Type.__name__ = "InetAddress"
_TmnxLocUsrDbDhcpIpv6Addr_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6Addr = _TmnxLocUsrDbDhcpIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 37),
    _TmnxLocUsrDbDhcpIpv6Addr_Type()
)
tmnxLocUsrDbDhcpIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6Addr.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6Pfx_Type(InetAddress):
    """Custom type tmnxLocUsrDbDhcpIpv6Pfx based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxLocUsrDbDhcpIpv6Pfx_Type.__name__ = "InetAddress"
_TmnxLocUsrDbDhcpIpv6Pfx_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6Pfx = _TmnxLocUsrDbDhcpIpv6Pfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 38),
    _TmnxLocUsrDbDhcpIpv6Pfx_Type()
)
tmnxLocUsrDbDhcpIpv6Pfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6Pfx.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxLocUsrDbDhcpIpv6PfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(48, 64),
    )


_TmnxLocUsrDbDhcpIpv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxLocUsrDbDhcpIpv6PfxLen_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6PfxLen = _TmnxLocUsrDbDhcpIpv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 39),
    _TmnxLocUsrDbDhcpIpv6PfxLen_Type()
)
tmnxLocUsrDbDhcpIpv6PfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6PfxLen.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6WanAddrPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpIpv6WanAddrPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpIpv6WanAddrPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpIpv6WanAddrPool_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6WanAddrPool = _TmnxLocUsrDbDhcpIpv6WanAddrPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 40),
    _TmnxLocUsrDbDhcpIpv6WanAddrPool_Type()
)
tmnxLocUsrDbDhcpIpv6WanAddrPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6WanAddrPool.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6DelPfxPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpIpv6DelPfxPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpIpv6DelPfxPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpIpv6DelPfxPool_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6DelPfxPool = _TmnxLocUsrDbDhcpIpv6DelPfxPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 41),
    _TmnxLocUsrDbDhcpIpv6DelPfxPool_Type()
)
tmnxLocUsrDbDhcpIpv6DelPfxPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6DelPfxPool.setStatus("current")


class _TmnxLocUsrDbDhcpFltrProfString_Type(TmnxFilterProfileStringOrEmpty):
    """Custom type tmnxLocUsrDbDhcpFltrProfString based on TmnxFilterProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpFltrProfString_Type.__name__ = "TmnxFilterProfileStringOrEmpty"
_TmnxLocUsrDbDhcpFltrProfString_Object = MibTableColumn
tmnxLocUsrDbDhcpFltrProfString = _TmnxLocUsrDbDhcpFltrProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 42),
    _TmnxLocUsrDbDhcpFltrProfString_Type()
)
tmnxLocUsrDbDhcpFltrProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpFltrProfString.setStatus("current")


class _TmnxLocUsrDbDhcpIngIpv4FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbDhcpIngIpv4FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbDhcpIngIpv4FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbDhcpIngIpv4FltrId_Object = MibTableColumn
tmnxLocUsrDbDhcpIngIpv4FltrId = _TmnxLocUsrDbDhcpIngIpv4FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 43),
    _TmnxLocUsrDbDhcpIngIpv4FltrId_Type()
)
tmnxLocUsrDbDhcpIngIpv4FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIngIpv4FltrId.setStatus("current")


class _TmnxLocUsrDbDhcpEgrIpv4FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbDhcpEgrIpv4FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbDhcpEgrIpv4FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbDhcpEgrIpv4FltrId_Object = MibTableColumn
tmnxLocUsrDbDhcpEgrIpv4FltrId = _TmnxLocUsrDbDhcpEgrIpv4FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 44),
    _TmnxLocUsrDbDhcpEgrIpv4FltrId_Type()
)
tmnxLocUsrDbDhcpEgrIpv4FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpEgrIpv4FltrId.setStatus("current")


class _TmnxLocUsrDbDhcpIngIpv6FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbDhcpIngIpv6FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbDhcpIngIpv6FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbDhcpIngIpv6FltrId_Object = MibTableColumn
tmnxLocUsrDbDhcpIngIpv6FltrId = _TmnxLocUsrDbDhcpIngIpv6FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 45),
    _TmnxLocUsrDbDhcpIngIpv6FltrId_Type()
)
tmnxLocUsrDbDhcpIngIpv6FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIngIpv6FltrId.setStatus("current")


class _TmnxLocUsrDbDhcpEgrIpv6FltrId_Type(TIPFilterIdOrEmpty):
    """Custom type tmnxLocUsrDbDhcpEgrIpv6FltrId based on TIPFilterIdOrEmpty"""
    defaultValue = 0


_TmnxLocUsrDbDhcpEgrIpv6FltrId_Type.__name__ = "TIPFilterIdOrEmpty"
_TmnxLocUsrDbDhcpEgrIpv6FltrId_Object = MibTableColumn
tmnxLocUsrDbDhcpEgrIpv6FltrId = _TmnxLocUsrDbDhcpEgrIpv6FltrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 46),
    _TmnxLocUsrDbDhcpEgrIpv6FltrId_Type()
)
tmnxLocUsrDbDhcpEgrIpv6FltrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpEgrIpv6FltrId.setStatus("current")


class _TmnxLocUsrDbDhcpUseGiAddrScope_Type(Integer32):
    """Custom type tmnxLocUsrDbDhcpUseGiAddrScope based on Integer32"""
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


_TmnxLocUsrDbDhcpUseGiAddrScope_Type.__name__ = "Integer32"
_TmnxLocUsrDbDhcpUseGiAddrScope_Object = MibTableColumn
tmnxLocUsrDbDhcpUseGiAddrScope = _TmnxLocUsrDbDhcpUseGiAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 47),
    _TmnxLocUsrDbDhcpUseGiAddrScope_Type()
)
tmnxLocUsrDbDhcpUseGiAddrScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUseGiAddrScope.setStatus("current")


class _TmnxLocUsrDbDhcpSecPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpSecPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpSecPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpSecPool_Object = MibTableColumn
tmnxLocUsrDbDhcpSecPool = _TmnxLocUsrDbDhcpSecPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 48),
    _TmnxLocUsrDbDhcpSecPool_Type()
)
tmnxLocUsrDbDhcpSecPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpSecPool.setStatus("current")


class _TmnxLocUsrDbDhcpUseCPDelimiter_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpUseCPDelimiter based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_TmnxLocUsrDbDhcpUseCPDelimiter_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpUseCPDelimiter_Object = MibTableColumn
tmnxLocUsrDbDhcpUseCPDelimiter = _TmnxLocUsrDbDhcpUseCPDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 49),
    _TmnxLocUsrDbDhcpUseCPDelimiter_Type()
)
tmnxLocUsrDbDhcpUseCPDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUseCPDelimiter.setStatus("current")
_TmnxLocUsrDbDhcpEncTagRangeType_Type = TmnxPortEncapType
_TmnxLocUsrDbDhcpEncTagRangeType_Object = MibTableColumn
tmnxLocUsrDbDhcpEncTagRangeType = _TmnxLocUsrDbDhcpEncTagRangeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 50),
    _TmnxLocUsrDbDhcpEncTagRangeType_Type()
)
tmnxLocUsrDbDhcpEncTagRangeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpEncTagRangeType.setStatus("current")
_TmnxLocUsrDbDhcpEncTagRangeStrt_Type = TmnxEncapVal
_TmnxLocUsrDbDhcpEncTagRangeStrt_Object = MibTableColumn
tmnxLocUsrDbDhcpEncTagRangeStrt = _TmnxLocUsrDbDhcpEncTagRangeStrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 51),
    _TmnxLocUsrDbDhcpEncTagRangeStrt_Type()
)
tmnxLocUsrDbDhcpEncTagRangeStrt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpEncTagRangeStrt.setStatus("current")
_TmnxLocUsrDbDhcpEncTagRangeEnd_Type = TmnxEncapVal
_TmnxLocUsrDbDhcpEncTagRangeEnd_Object = MibTableColumn
tmnxLocUsrDbDhcpEncTagRangeEnd = _TmnxLocUsrDbDhcpEncTagRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 52),
    _TmnxLocUsrDbDhcpEncTagRangeEnd_Type()
)
tmnxLocUsrDbDhcpEncTagRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpEncTagRangeEnd.setStatus("current")


class _TmnxLocUsrDbDhcpMsapGroupIfPfx_Type(TmnxLudbMsapGrpIfPfxSfxType):
    """Custom type tmnxLocUsrDbDhcpMsapGroupIfPfx based on TmnxLudbMsapGrpIfPfxSfxType"""
    defaultValue = 1


_TmnxLocUsrDbDhcpMsapGroupIfPfx_Type.__name__ = "TmnxLudbMsapGrpIfPfxSfxType"
_TmnxLocUsrDbDhcpMsapGroupIfPfx_Object = MibTableColumn
tmnxLocUsrDbDhcpMsapGroupIfPfx = _TmnxLocUsrDbDhcpMsapGroupIfPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 53),
    _TmnxLocUsrDbDhcpMsapGroupIfPfx_Type()
)
tmnxLocUsrDbDhcpMsapGroupIfPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMsapGroupIfPfx.setStatus("current")


class _TmnxLocUsrDbDhcpMsapGroupIfSfx_Type(TmnxLudbMsapGrpIfPfxSfxType):
    """Custom type tmnxLocUsrDbDhcpMsapGroupIfSfx based on TmnxLudbMsapGrpIfPfxSfxType"""
    defaultValue = 1


_TmnxLocUsrDbDhcpMsapGroupIfSfx_Type.__name__ = "TmnxLudbMsapGrpIfPfxSfxType"
_TmnxLocUsrDbDhcpMsapGroupIfSfx_Object = MibTableColumn
tmnxLocUsrDbDhcpMsapGroupIfSfx = _TmnxLocUsrDbDhcpMsapGroupIfSfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 54),
    _TmnxLocUsrDbDhcpMsapGroupIfSfx_Type()
)
tmnxLocUsrDbDhcpMsapGroupIfSfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMsapGroupIfSfx.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6ReqDelPfxLn_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpIpv6ReqDelPfxLn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(48, 64),
    )


_TmnxLocUsrDbDhcpIpv6ReqDelPfxLn_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpIpv6ReqDelPfxLn_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6ReqDelPfxLn = _TmnxLocUsrDbDhcpIpv6ReqDelPfxLn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 55),
    _TmnxLocUsrDbDhcpIpv6ReqDelPfxLn_Type()
)
tmnxLocUsrDbDhcpIpv6ReqDelPfxLn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6ReqDelPfxLn.setStatus("current")


class _TmnxLocUsrDbDhcpAcctPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpAcctPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpAcctPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpAcctPolicy_Object = MibTableColumn
tmnxLocUsrDbDhcpAcctPolicy = _TmnxLocUsrDbDhcpAcctPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 56),
    _TmnxLocUsrDbDhcpAcctPolicy_Type()
)
tmnxLocUsrDbDhcpAcctPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpAcctPolicy.setStatus("current")


class _TmnxLocUsrDbDhcpDuplAcctPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpDuplAcctPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpDuplAcctPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpDuplAcctPolicy_Object = MibTableColumn
tmnxLocUsrDbDhcpDuplAcctPolicy = _TmnxLocUsrDbDhcpDuplAcctPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 57),
    _TmnxLocUsrDbDhcpDuplAcctPolicy_Type()
)
tmnxLocUsrDbDhcpDuplAcctPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpDuplAcctPolicy.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6SlaacPfx_Type(InetAddress):
    """Custom type tmnxLocUsrDbDhcpIpv6SlaacPfx based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxLocUsrDbDhcpIpv6SlaacPfx_Type.__name__ = "InetAddress"
_TmnxLocUsrDbDhcpIpv6SlaacPfx_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6SlaacPfx = _TmnxLocUsrDbDhcpIpv6SlaacPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 58),
    _TmnxLocUsrDbDhcpIpv6SlaacPfx_Type()
)
tmnxLocUsrDbDhcpIpv6SlaacPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6SlaacPfx.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6SlaacPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxLocUsrDbDhcpIpv6SlaacPfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 64),
    )


_TmnxLocUsrDbDhcpIpv6SlaacPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxLocUsrDbDhcpIpv6SlaacPfxLen_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6SlaacPfxLen = _TmnxLocUsrDbDhcpIpv6SlaacPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 59),
    _TmnxLocUsrDbDhcpIpv6SlaacPfxLen_Type()
)
tmnxLocUsrDbDhcpIpv6SlaacPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6SlaacPfxLen.setStatus("current")


class _TmnxLocUsrDbDhcpDerivedId_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpDerivedId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpDerivedId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpDerivedId_Object = MibTableColumn
tmnxLocUsrDbDhcpDerivedId = _TmnxLocUsrDbDhcpDerivedId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 60),
    _TmnxLocUsrDbDhcpDerivedId_Type()
)
tmnxLocUsrDbDhcpDerivedId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpDerivedId.setStatus("current")


class _TmnxLocUsrDbDhcpIpv6SlaacPfxPl_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbDhcpIpv6SlaacPfxPl based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpIpv6SlaacPfxPl_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbDhcpIpv6SlaacPfxPl_Object = MibTableColumn
tmnxLocUsrDbDhcpIpv6SlaacPfxPl = _TmnxLocUsrDbDhcpIpv6SlaacPfxPl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 9, 1, 61),
    _TmnxLocUsrDbDhcpIpv6SlaacPfxPl_Type()
)
tmnxLocUsrDbDhcpIpv6SlaacPfxPl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpIpv6SlaacPfxPl.setStatus("current")
_TmnxLocUsrDbDhcpUnmatchedTable_Object = MibTable
tmnxLocUsrDbDhcpUnmatchedTable = _TmnxLocUsrDbDhcpUnmatchedTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnmatchedTable.setStatus("current")
_TmnxLocUsrDbDhcpUnmatchedEntry_Object = MibTableRow
tmnxLocUsrDbDhcpUnmatchedEntry = _TmnxLocUsrDbDhcpUnmatchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1)
)
tmnxLocUsrDbDhcpUnmatchedEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpHostName"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnmatchedEntry.setStatus("current")
_TmnxLocUsrDbDhcpUnMacAddress_Type = MacAddress
_TmnxLocUsrDbDhcpUnMacAddress_Object = MibTableColumn
tmnxLocUsrDbDhcpUnMacAddress = _TmnxLocUsrDbDhcpUnMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 1),
    _TmnxLocUsrDbDhcpUnMacAddress_Type()
)
tmnxLocUsrDbDhcpUnMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnMacAddress.setStatus("current")


class _TmnxLocUsrDbDhcpUnCircuitId_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpUnCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpUnCircuitId_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpUnCircuitId_Object = MibTableColumn
tmnxLocUsrDbDhcpUnCircuitId = _TmnxLocUsrDbDhcpUnCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 2),
    _TmnxLocUsrDbDhcpUnCircuitId_Type()
)
tmnxLocUsrDbDhcpUnCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnCircuitId.setStatus("current")


class _TmnxLocUsrDbDhcpUnRemoteId_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpUnRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpUnRemoteId_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpUnRemoteId_Object = MibTableColumn
tmnxLocUsrDbDhcpUnRemoteId = _TmnxLocUsrDbDhcpUnRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 3),
    _TmnxLocUsrDbDhcpUnRemoteId_Type()
)
tmnxLocUsrDbDhcpUnRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnRemoteId.setStatus("current")


class _TmnxLocUsrDbDhcpUnSystemId_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpUnSystemId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpUnSystemId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpUnSystemId_Object = MibTableColumn
tmnxLocUsrDbDhcpUnSystemId = _TmnxLocUsrDbDhcpUnSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 4),
    _TmnxLocUsrDbDhcpUnSystemId_Type()
)
tmnxLocUsrDbDhcpUnSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnSystemId.setStatus("current")
_TmnxLocUsrDbDhcpUnServiceId_Type = TmnxServId
_TmnxLocUsrDbDhcpUnServiceId_Object = MibTableColumn
tmnxLocUsrDbDhcpUnServiceId = _TmnxLocUsrDbDhcpUnServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 5),
    _TmnxLocUsrDbDhcpUnServiceId_Type()
)
tmnxLocUsrDbDhcpUnServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnServiceId.setStatus("current")


class _TmnxLocUsrDbDhcpUnSapId_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpUnSapId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpUnSapId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpUnSapId_Object = MibTableColumn
tmnxLocUsrDbDhcpUnSapId = _TmnxLocUsrDbDhcpUnSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 6),
    _TmnxLocUsrDbDhcpUnSapId_Type()
)
tmnxLocUsrDbDhcpUnSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnSapId.setStatus("current")


class _TmnxLocUsrDbDhcpUnString_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpUnString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbDhcpUnString_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpUnString_Object = MibTableColumn
tmnxLocUsrDbDhcpUnString = _TmnxLocUsrDbDhcpUnString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 7),
    _TmnxLocUsrDbDhcpUnString_Type()
)
tmnxLocUsrDbDhcpUnString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnString.setStatus("current")


class _TmnxLocUsrDbDhcpUnOption60_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpUnOption60 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLocUsrDbDhcpUnOption60_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpUnOption60_Object = MibTableColumn
tmnxLocUsrDbDhcpUnOption60 = _TmnxLocUsrDbDhcpUnOption60_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 8),
    _TmnxLocUsrDbDhcpUnOption60_Type()
)
tmnxLocUsrDbDhcpUnOption60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnOption60.setStatus("current")
_TmnxLocUsrDbDhcpUnmatchedReason_Type = TmnxLocUsrDbUnmatchedReason
_TmnxLocUsrDbDhcpUnmatchedReason_Object = MibTableColumn
tmnxLocUsrDbDhcpUnmatchedReason = _TmnxLocUsrDbDhcpUnmatchedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 9),
    _TmnxLocUsrDbDhcpUnmatchedReason_Type()
)
tmnxLocUsrDbDhcpUnmatchedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnmatchedReason.setStatus("current")


class _TmnxLocUsrDbDhcpUnDuplicateHost_Type(DisplayString):
    """Custom type tmnxLocUsrDbDhcpUnDuplicateHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLocUsrDbDhcpUnDuplicateHost_Type.__name__ = "DisplayString"
_TmnxLocUsrDbDhcpUnDuplicateHost_Object = MibTableColumn
tmnxLocUsrDbDhcpUnDuplicateHost = _TmnxLocUsrDbDhcpUnDuplicateHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 10, 1, 10),
    _TmnxLocUsrDbDhcpUnDuplicateHost_Type()
)
tmnxLocUsrDbDhcpUnDuplicateHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpUnDuplicateHost.setStatus("current")
_TmnxLocUsrDbDhcpOptionTableLstCh_Type = TimeStamp
_TmnxLocUsrDbDhcpOptionTableLstCh_Object = MibScalar
tmnxLocUsrDbDhcpOptionTableLstCh = _TmnxLocUsrDbDhcpOptionTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 11),
    _TmnxLocUsrDbDhcpOptionTableLstCh_Type()
)
tmnxLocUsrDbDhcpOptionTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionTableLstCh.setStatus("current")
_TmnxLocUsrDbDhcpOptionTable_Object = MibTable
tmnxLocUsrDbDhcpOptionTable = _TmnxLocUsrDbDhcpOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionTable.setStatus("current")
_TmnxLocUsrDbDhcpOptionEntry_Object = MibTableRow
tmnxLocUsrDbDhcpOptionEntry = _TmnxLocUsrDbDhcpOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 12, 1)
)
tmnxLocUsrDbDhcpOptionEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpHostName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionNumber"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionEntry.setStatus("current")


class _TmnxLocUsrDbDhcpOptionNumber_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpOptionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_TmnxLocUsrDbDhcpOptionNumber_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpOptionNumber_Object = MibTableColumn
tmnxLocUsrDbDhcpOptionNumber = _TmnxLocUsrDbDhcpOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 12, 1, 1),
    _TmnxLocUsrDbDhcpOptionNumber_Type()
)
tmnxLocUsrDbDhcpOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionNumber.setStatus("current")
_TmnxLocUsrDbDhcpOptionRowStatus_Type = RowStatus
_TmnxLocUsrDbDhcpOptionRowStatus_Object = MibTableColumn
tmnxLocUsrDbDhcpOptionRowStatus = _TmnxLocUsrDbDhcpOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 12, 1, 2),
    _TmnxLocUsrDbDhcpOptionRowStatus_Type()
)
tmnxLocUsrDbDhcpOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionRowStatus.setStatus("current")
_TmnxLocUsrDbDhcpOptionLastChngTm_Type = TimeStamp
_TmnxLocUsrDbDhcpOptionLastChngTm_Object = MibTableColumn
tmnxLocUsrDbDhcpOptionLastChngTm = _TmnxLocUsrDbDhcpOptionLastChngTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 12, 1, 3),
    _TmnxLocUsrDbDhcpOptionLastChngTm_Type()
)
tmnxLocUsrDbDhcpOptionLastChngTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionLastChngTm.setStatus("current")
_TmnxLocUsrDbDhcpOptionType_Type = TmnxDhcpOptionType
_TmnxLocUsrDbDhcpOptionType_Object = MibTableColumn
tmnxLocUsrDbDhcpOptionType = _TmnxLocUsrDbDhcpOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 12, 1, 4),
    _TmnxLocUsrDbDhcpOptionType_Type()
)
tmnxLocUsrDbDhcpOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionType.setStatus("current")


class _TmnxLocUsrDbDhcpOptionValue_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpOptionValue_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpOptionValue_Object = MibTableColumn
tmnxLocUsrDbDhcpOptionValue = _TmnxLocUsrDbDhcpOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 12, 1, 5),
    _TmnxLocUsrDbDhcpOptionValue_Type()
)
tmnxLocUsrDbDhcpOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOptionValue.setStatus("current")
_TmnxLocUsrDbPppoeAuthTool_ObjectIdentity = ObjectIdentity
tmnxLocUsrDbPppoeAuthTool = _TmnxLocUsrDbPppoeAuthTool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13)
)


class _TmnxLocUsrDbPppoeAuthDbName_Type(TNamedItemOrEmpty):
    """Custom type tmnxLocUsrDbPppoeAuthDbName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeAuthDbName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLocUsrDbPppoeAuthDbName_Object = MibScalar
tmnxLocUsrDbPppoeAuthDbName = _TmnxLocUsrDbPppoeAuthDbName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 1),
    _TmnxLocUsrDbPppoeAuthDbName_Type()
)
tmnxLocUsrDbPppoeAuthDbName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthDbName.setStatus("current")


class _TmnxLocUsrDbPppoeAuthUsrName_Type(TmnxPppoeUserNameOrEmpty):
    """Custom type tmnxLocUsrDbPppoeAuthUsrName based on TmnxPppoeUserNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeAuthUsrName_Type.__name__ = "TmnxPppoeUserNameOrEmpty"
_TmnxLocUsrDbPppoeAuthUsrName_Object = MibScalar
tmnxLocUsrDbPppoeAuthUsrName = _TmnxLocUsrDbPppoeAuthUsrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 2),
    _TmnxLocUsrDbPppoeAuthUsrName_Type()
)
tmnxLocUsrDbPppoeAuthUsrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthUsrName.setStatus("current")


class _TmnxLocUsrDbPppoeAuthPwd_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeAuthPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLocUsrDbPppoeAuthPwd_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeAuthPwd_Object = MibScalar
tmnxLocUsrDbPppoeAuthPwd = _TmnxLocUsrDbPppoeAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 3),
    _TmnxLocUsrDbPppoeAuthPwd_Type()
)
tmnxLocUsrDbPppoeAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthPwd.setStatus("current")


class _TmnxLocUsrDbPppoeAuthenticate_Type(TmnxActionType):
    """Custom type tmnxLocUsrDbPppoeAuthenticate based on TmnxActionType"""
    defaultValue = 2


_TmnxLocUsrDbPppoeAuthenticate_Type.__name__ = "TmnxActionType"
_TmnxLocUsrDbPppoeAuthenticate_Object = MibScalar
tmnxLocUsrDbPppoeAuthenticate = _TmnxLocUsrDbPppoeAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 4),
    _TmnxLocUsrDbPppoeAuthenticate_Type()
)
tmnxLocUsrDbPppoeAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthenticate.setStatus("current")
_TmnxLocUsrDbPppoeAuthSuccessful_Type = TruthValue
_TmnxLocUsrDbPppoeAuthSuccessful_Object = MibScalar
tmnxLocUsrDbPppoeAuthSuccessful = _TmnxLocUsrDbPppoeAuthSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 5),
    _TmnxLocUsrDbPppoeAuthSuccessful_Type()
)
tmnxLocUsrDbPppoeAuthSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthSuccessful.setStatus("current")


class _TmnxLocUsrDbPppoeAuthErrorMsg_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeAuthErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeAuthErrorMsg_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeAuthErrorMsg_Object = MibScalar
tmnxLocUsrDbPppoeAuthErrorMsg = _TmnxLocUsrDbPppoeAuthErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 6),
    _TmnxLocUsrDbPppoeAuthErrorMsg_Type()
)
tmnxLocUsrDbPppoeAuthErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthErrorMsg.setStatus("current")
_TmnxLocUsrDbPppoeAuthTime_Type = TimeStamp
_TmnxLocUsrDbPppoeAuthTime_Object = MibScalar
tmnxLocUsrDbPppoeAuthTime = _TmnxLocUsrDbPppoeAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 7),
    _TmnxLocUsrDbPppoeAuthTime_Type()
)
tmnxLocUsrDbPppoeAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthTime.setStatus("current")


class _TmnxLocUsrDbPppoeAuthHostName_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeAuthHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLocUsrDbPppoeAuthHostName_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeAuthHostName_Object = MibScalar
tmnxLocUsrDbPppoeAuthHostName = _TmnxLocUsrDbPppoeAuthHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 8),
    _TmnxLocUsrDbPppoeAuthHostName_Type()
)
tmnxLocUsrDbPppoeAuthHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthHostName.setStatus("current")


class _TmnxLocUsrDbPppoeAuthMacAddress_Type(MacAddress):
    """Custom type tmnxLocUsrDbPppoeAuthMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxLocUsrDbPppoeAuthMacAddress_Type.__name__ = "MacAddress"
_TmnxLocUsrDbPppoeAuthMacAddress_Object = MibScalar
tmnxLocUsrDbPppoeAuthMacAddress = _TmnxLocUsrDbPppoeAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 9),
    _TmnxLocUsrDbPppoeAuthMacAddress_Type()
)
tmnxLocUsrDbPppoeAuthMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthMacAddress.setStatus("current")


class _TmnxLocUsrDbPppoeAuthRemoteId_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeAuthRemoteId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeAuthRemoteId_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeAuthRemoteId_Object = MibScalar
tmnxLocUsrDbPppoeAuthRemoteId = _TmnxLocUsrDbPppoeAuthRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 10),
    _TmnxLocUsrDbPppoeAuthRemoteId_Type()
)
tmnxLocUsrDbPppoeAuthRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthRemoteId.setStatus("current")


class _TmnxLocUsrDbPppoeAuthCircuitIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLocUsrDbPppoeAuthCircuitIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLocUsrDbPppoeAuthCircuitIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLocUsrDbPppoeAuthCircuitIdFmt_Object = MibScalar
tmnxLocUsrDbPppoeAuthCircuitIdFmt = _TmnxLocUsrDbPppoeAuthCircuitIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 11),
    _TmnxLocUsrDbPppoeAuthCircuitIdFmt_Type()
)
tmnxLocUsrDbPppoeAuthCircuitIdFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthCircuitIdFmt.setStatus("current")


class _TmnxLocUsrDbPppoeAuthCircuitId_Type(OctetString):
    """Custom type tmnxLocUsrDbPppoeAuthCircuitId based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeAuthCircuitId_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppoeAuthCircuitId_Object = MibScalar
tmnxLocUsrDbPppoeAuthCircuitId = _TmnxLocUsrDbPppoeAuthCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 12),
    _TmnxLocUsrDbPppoeAuthCircuitId_Type()
)
tmnxLocUsrDbPppoeAuthCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthCircuitId.setStatus("current")


class _TmnxLocUsrDbPppoeAuthServiceName_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeAuthServiceName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeAuthServiceName_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeAuthServiceName_Object = MibScalar
tmnxLocUsrDbPppoeAuthServiceName = _TmnxLocUsrDbPppoeAuthServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 13),
    _TmnxLocUsrDbPppoeAuthServiceName_Type()
)
tmnxLocUsrDbPppoeAuthServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthServiceName.setStatus("current")


class _TmnxLocUsrDbPppoeAuthRemoteIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLocUsrDbPppoeAuthRemoteIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLocUsrDbPppoeAuthRemoteIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLocUsrDbPppoeAuthRemoteIdFmt_Object = MibScalar
tmnxLocUsrDbPppoeAuthRemoteIdFmt = _TmnxLocUsrDbPppoeAuthRemoteIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 14),
    _TmnxLocUsrDbPppoeAuthRemoteIdFmt_Type()
)
tmnxLocUsrDbPppoeAuthRemoteIdFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthRemoteIdFmt.setStatus("current")


class _TmnxLocUsrDbPppoeAuthSapId_Type(DisplayString):
    """Custom type tmnxLocUsrDbPppoeAuthSapId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLocUsrDbPppoeAuthSapId_Type.__name__ = "DisplayString"
_TmnxLocUsrDbPppoeAuthSapId_Object = MibScalar
tmnxLocUsrDbPppoeAuthSapId = _TmnxLocUsrDbPppoeAuthSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 13, 15),
    _TmnxLocUsrDbPppoeAuthSapId_Type()
)
tmnxLocUsrDbPppoeAuthSapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeAuthSapId.setStatus("current")
_TmnxLocUsrDbDhcpMaskTableLstCh_Type = TimeStamp
_TmnxLocUsrDbDhcpMaskTableLstCh_Object = MibScalar
tmnxLocUsrDbDhcpMaskTableLstCh = _TmnxLocUsrDbDhcpMaskTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 14),
    _TmnxLocUsrDbDhcpMaskTableLstCh_Type()
)
tmnxLocUsrDbDhcpMaskTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskTableLstCh.setStatus("current")
_TmnxLocUsrDbDhcpMaskTable_Object = MibTable
tmnxLocUsrDbDhcpMaskTable = _TmnxLocUsrDbDhcpMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskTable.setStatus("current")
_TmnxLocUsrDbDhcpMaskEntry_Object = MibTableRow
tmnxLocUsrDbDhcpMaskEntry = _TmnxLocUsrDbDhcpMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15, 1)
)
tmnxLocUsrDbDhcpMaskEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskMatchType"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskEntry.setStatus("current")
_TmnxLocUsrDbDhcpMaskMatchType_Type = TmnxLocUsrDbMatchTypeDhcp
_TmnxLocUsrDbDhcpMaskMatchType_Object = MibTableColumn
tmnxLocUsrDbDhcpMaskMatchType = _TmnxLocUsrDbDhcpMaskMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15, 1, 1),
    _TmnxLocUsrDbDhcpMaskMatchType_Type()
)
tmnxLocUsrDbDhcpMaskMatchType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskMatchType.setStatus("current")
_TmnxLocUsrDbDhcpMaskRowStatus_Type = RowStatus
_TmnxLocUsrDbDhcpMaskRowStatus_Object = MibTableColumn
tmnxLocUsrDbDhcpMaskRowStatus = _TmnxLocUsrDbDhcpMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15, 1, 2),
    _TmnxLocUsrDbDhcpMaskRowStatus_Type()
)
tmnxLocUsrDbDhcpMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskRowStatus.setStatus("current")


class _TmnxLocUsrDbDhcpMaskPreStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbDhcpMaskPreStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpMaskPreStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbDhcpMaskPreStr_Object = MibTableColumn
tmnxLocUsrDbDhcpMaskPreStr = _TmnxLocUsrDbDhcpMaskPreStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15, 1, 3),
    _TmnxLocUsrDbDhcpMaskPreStr_Type()
)
tmnxLocUsrDbDhcpMaskPreStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskPreStr.setStatus("current")


class _TmnxLocUsrDbDhcpMaskPreNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpMaskPreNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpMaskPreNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpMaskPreNum_Object = MibTableColumn
tmnxLocUsrDbDhcpMaskPreNum = _TmnxLocUsrDbDhcpMaskPreNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15, 1, 4),
    _TmnxLocUsrDbDhcpMaskPreNum_Type()
)
tmnxLocUsrDbDhcpMaskPreNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskPreNum.setStatus("current")


class _TmnxLocUsrDbDhcpMaskSufStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbDhcpMaskSufStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbDhcpMaskSufStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbDhcpMaskSufStr_Object = MibTableColumn
tmnxLocUsrDbDhcpMaskSufStr = _TmnxLocUsrDbDhcpMaskSufStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15, 1, 5),
    _TmnxLocUsrDbDhcpMaskSufStr_Type()
)
tmnxLocUsrDbDhcpMaskSufStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskSufStr.setStatus("current")


class _TmnxLocUsrDbDhcpMaskSufNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpMaskSufNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpMaskSufNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpMaskSufNum_Object = MibTableColumn
tmnxLocUsrDbDhcpMaskSufNum = _TmnxLocUsrDbDhcpMaskSufNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 15, 1, 6),
    _TmnxLocUsrDbDhcpMaskSufNum_Type()
)
tmnxLocUsrDbDhcpMaskSufNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpMaskSufNum.setStatus("current")
_TmnxLocUsrDbPppoeMaskTableLstCh_Type = TimeStamp
_TmnxLocUsrDbPppoeMaskTableLstCh_Object = MibScalar
tmnxLocUsrDbPppoeMaskTableLstCh = _TmnxLocUsrDbPppoeMaskTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 16),
    _TmnxLocUsrDbPppoeMaskTableLstCh_Type()
)
tmnxLocUsrDbPppoeMaskTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskTableLstCh.setStatus("current")
_TmnxLocUsrDbPppoeMaskTable_Object = MibTable
tmnxLocUsrDbPppoeMaskTable = _TmnxLocUsrDbPppoeMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskTable.setStatus("current")
_TmnxLocUsrDbPppoeMaskEntry_Object = MibTableRow
tmnxLocUsrDbPppoeMaskEntry = _TmnxLocUsrDbPppoeMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17, 1)
)
tmnxLocUsrDbPppoeMaskEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskMatchType"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskEntry.setStatus("current")
_TmnxLocUsrDbPppoeMaskMatchType_Type = TmnxLocUsrDbMatchTypePppoe
_TmnxLocUsrDbPppoeMaskMatchType_Object = MibTableColumn
tmnxLocUsrDbPppoeMaskMatchType = _TmnxLocUsrDbPppoeMaskMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17, 1, 1),
    _TmnxLocUsrDbPppoeMaskMatchType_Type()
)
tmnxLocUsrDbPppoeMaskMatchType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskMatchType.setStatus("current")
_TmnxLocUsrDbPppoeMaskRowStatus_Type = RowStatus
_TmnxLocUsrDbPppoeMaskRowStatus_Object = MibTableColumn
tmnxLocUsrDbPppoeMaskRowStatus = _TmnxLocUsrDbPppoeMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17, 1, 2),
    _TmnxLocUsrDbPppoeMaskRowStatus_Type()
)
tmnxLocUsrDbPppoeMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskRowStatus.setStatus("current")


class _TmnxLocUsrDbPppoeMaskPreStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbPppoeMaskPreStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeMaskPreStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbPppoeMaskPreStr_Object = MibTableColumn
tmnxLocUsrDbPppoeMaskPreStr = _TmnxLocUsrDbPppoeMaskPreStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17, 1, 3),
    _TmnxLocUsrDbPppoeMaskPreStr_Type()
)
tmnxLocUsrDbPppoeMaskPreStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskPreStr.setStatus("current")


class _TmnxLocUsrDbPppoeMaskPreNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbPppoeMaskPreNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeMaskPreNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbPppoeMaskPreNum_Object = MibTableColumn
tmnxLocUsrDbPppoeMaskPreNum = _TmnxLocUsrDbPppoeMaskPreNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17, 1, 4),
    _TmnxLocUsrDbPppoeMaskPreNum_Type()
)
tmnxLocUsrDbPppoeMaskPreNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskPreNum.setStatus("current")


class _TmnxLocUsrDbPppoeMaskSufStr_Type(TmnxLocUsrDbMaskString):
    """Custom type tmnxLocUsrDbPppoeMaskSufStr based on TmnxLocUsrDbMaskString"""
    defaultValue = OctetString("")


_TmnxLocUsrDbPppoeMaskSufStr_Type.__name__ = "TmnxLocUsrDbMaskString"
_TmnxLocUsrDbPppoeMaskSufStr_Object = MibTableColumn
tmnxLocUsrDbPppoeMaskSufStr = _TmnxLocUsrDbPppoeMaskSufStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17, 1, 5),
    _TmnxLocUsrDbPppoeMaskSufStr_Type()
)
tmnxLocUsrDbPppoeMaskSufStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskSufStr.setStatus("current")


class _TmnxLocUsrDbPppoeMaskSufNum_Type(Unsigned32):
    """Custom type tmnxLocUsrDbPppoeMaskSufNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxLocUsrDbPppoeMaskSufNum_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbPppoeMaskSufNum_Object = MibTableColumn
tmnxLocUsrDbPppoeMaskSufNum = _TmnxLocUsrDbPppoeMaskSufNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 17, 1, 6),
    _TmnxLocUsrDbPppoeMaskSufNum_Type()
)
tmnxLocUsrDbPppoeMaskSufNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppoeMaskSufNum.setStatus("current")
_TmnxLudbHostTableLastChange_Type = TimeStamp
_TmnxLudbHostTableLastChange_Object = MibScalar
tmnxLudbHostTableLastChange = _TmnxLudbHostTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 20),
    _TmnxLudbHostTableLastChange_Type()
)
tmnxLudbHostTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbHostTableLastChange.setStatus("current")
_TmnxLudbHostTable_Object = MibTable
tmnxLudbHostTable = _TmnxLudbHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21)
)
if mibBuilder.loadTexts:
    tmnxLudbHostTable.setStatus("current")
_TmnxLudbHostEntry_Object = MibTableRow
tmnxLudbHostEntry = _TmnxLudbHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1)
)
tmnxLudbHostEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostType"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostName"),
)
if mibBuilder.loadTexts:
    tmnxLudbHostEntry.setStatus("current")
_TmnxLudbHostType_Type = TmnxLocUsrDbHostType
_TmnxLudbHostType_Object = MibTableColumn
tmnxLudbHostType = _TmnxLudbHostType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 1),
    _TmnxLudbHostType_Type()
)
tmnxLudbHostType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLudbHostType.setStatus("current")


class _TmnxLudbHostName_Type(DisplayString):
    """Custom type tmnxLudbHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxLudbHostName_Type.__name__ = "DisplayString"
_TmnxLudbHostName_Object = MibTableColumn
tmnxLudbHostName = _TmnxLudbHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 2),
    _TmnxLudbHostName_Type()
)
tmnxLudbHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLudbHostName.setStatus("current")
_TmnxLudbHostRowStatus_Type = RowStatus
_TmnxLudbHostRowStatus_Object = MibTableColumn
tmnxLudbHostRowStatus = _TmnxLudbHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 3),
    _TmnxLudbHostRowStatus_Type()
)
tmnxLudbHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostRowStatus.setStatus("current")
_TmnxLudbHostLastChangeTime_Type = TimeStamp
_TmnxLudbHostLastChangeTime_Object = MibTableColumn
tmnxLudbHostLastChangeTime = _TmnxLudbHostLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 4),
    _TmnxLudbHostLastChangeTime_Type()
)
tmnxLudbHostLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbHostLastChangeTime.setStatus("current")
_TmnxLudbHostApplications_Type = TmnxLocUsrDbHostApplications
_TmnxLudbHostApplications_Object = MibTableColumn
tmnxLudbHostApplications = _TmnxLudbHostApplications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 5),
    _TmnxLudbHostApplications_Type()
)
tmnxLudbHostApplications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostApplications.setStatus("current")


class _TmnxLudbHostAdminState_Type(TmnxAdminState):
    """Custom type tmnxLudbHostAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLudbHostAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLudbHostAdminState_Object = MibTableColumn
tmnxLudbHostAdminState = _TmnxLudbHostAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 10),
    _TmnxLudbHostAdminState_Type()
)
tmnxLudbHostAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostAdminState.setStatus("current")


class _TmnxLudbHostMacAddress_Type(MacAddress):
    """Custom type tmnxLudbHostMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxLudbHostMacAddress_Type.__name__ = "MacAddress"
_TmnxLudbHostMacAddress_Object = MibTableColumn
tmnxLudbHostMacAddress = _TmnxLudbHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 11),
    _TmnxLudbHostMacAddress_Type()
)
tmnxLudbHostMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostMacAddress.setStatus("current")


class _TmnxLudbHostCircuitIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLudbHostCircuitIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLudbHostCircuitIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLudbHostCircuitIdFmt_Object = MibTableColumn
tmnxLudbHostCircuitIdFmt = _TmnxLudbHostCircuitIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 12),
    _TmnxLudbHostCircuitIdFmt_Type()
)
tmnxLudbHostCircuitIdFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostCircuitIdFmt.setStatus("current")


class _TmnxLudbHostCircuitId_Type(OctetString):
    """Custom type tmnxLudbHostCircuitId based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLudbHostCircuitId_Type.__name__ = "OctetString"
_TmnxLudbHostCircuitId_Object = MibTableColumn
tmnxLudbHostCircuitId = _TmnxLudbHostCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 13),
    _TmnxLudbHostCircuitId_Type()
)
tmnxLudbHostCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostCircuitId.setStatus("current")


class _TmnxLudbHostRemoteIdFmt_Type(TmnxLocUsrDbDataFormat):
    """Custom type tmnxLudbHostRemoteIdFmt based on TmnxLocUsrDbDataFormat"""
    defaultValue = 2


_TmnxLudbHostRemoteIdFmt_Type.__name__ = "TmnxLocUsrDbDataFormat"
_TmnxLudbHostRemoteIdFmt_Object = MibTableColumn
tmnxLudbHostRemoteIdFmt = _TmnxLudbHostRemoteIdFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 14),
    _TmnxLudbHostRemoteIdFmt_Type()
)
tmnxLudbHostRemoteIdFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostRemoteIdFmt.setStatus("current")


class _TmnxLudbHostRemoteId_Type(OctetString):
    """Custom type tmnxLudbHostRemoteId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLudbHostRemoteId_Type.__name__ = "OctetString"
_TmnxLudbHostRemoteId_Object = MibTableColumn
tmnxLudbHostRemoteId = _TmnxLudbHostRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 15),
    _TmnxLudbHostRemoteId_Type()
)
tmnxLudbHostRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostRemoteId.setStatus("current")


class _TmnxLudbHostAddrType_Type(InetAddressType):
    """Custom type tmnxLudbHostAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLudbHostAddrType_Type.__name__ = "InetAddressType"
_TmnxLudbHostAddrType_Object = MibTableColumn
tmnxLudbHostAddrType = _TmnxLudbHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 16),
    _TmnxLudbHostAddrType_Type()
)
tmnxLudbHostAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostAddrType.setStatus("current")


class _TmnxLudbHostAddress_Type(InetAddress):
    """Custom type tmnxLudbHostAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLudbHostAddress_Type.__name__ = "InetAddress"
_TmnxLudbHostAddress_Object = MibTableColumn
tmnxLudbHostAddress = _TmnxLudbHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 17),
    _TmnxLudbHostAddress_Type()
)
tmnxLudbHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostAddress.setStatus("current")


class _TmnxLudbHostPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbHostPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbHostPool_Object = MibTableColumn
tmnxLudbHostPool = _TmnxLudbHostPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 18),
    _TmnxLudbHostPool_Type()
)
tmnxLudbHostPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPool.setStatus("current")


class _TmnxLudbHostUseGiAddress_Type(TruthValue):
    """Custom type tmnxLudbHostUseGiAddress based on TruthValue"""
    defaultValue = 2


_TmnxLudbHostUseGiAddress_Type.__name__ = "TruthValue"
_TmnxLudbHostUseGiAddress_Object = MibTableColumn
tmnxLudbHostUseGiAddress = _TmnxLudbHostUseGiAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 19),
    _TmnxLudbHostUseGiAddress_Type()
)
tmnxLudbHostUseGiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostUseGiAddress.setStatus("current")


class _TmnxLudbHostIdStringOptNum_Type(Unsigned32):
    """Custom type tmnxLudbHostIdStringOptNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxLudbHostIdStringOptNum_Type.__name__ = "Unsigned32"
_TmnxLudbHostIdStringOptNum_Object = MibTableColumn
tmnxLudbHostIdStringOptNum = _TmnxLudbHostIdStringOptNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 20),
    _TmnxLudbHostIdStringOptNum_Type()
)
tmnxLudbHostIdStringOptNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostIdStringOptNum.setStatus("current")


class _TmnxLudbHostSubscriberId_Type(TmnxSubIdentStringOrEmpty):
    """Custom type tmnxLudbHostSubscriberId based on TmnxSubIdentStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostSubscriberId_Type.__name__ = "TmnxSubIdentStringOrEmpty"
_TmnxLudbHostSubscriberId_Object = MibTableColumn
tmnxLudbHostSubscriberId = _TmnxLudbHostSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 21),
    _TmnxLudbHostSubscriberId_Type()
)
tmnxLudbHostSubscriberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostSubscriberId.setStatus("current")


class _TmnxLudbHostSlaProfString_Type(TmnxSlaProfileStringOrEmpty):
    """Custom type tmnxLudbHostSlaProfString based on TmnxSlaProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostSlaProfString_Type.__name__ = "TmnxSlaProfileStringOrEmpty"
_TmnxLudbHostSlaProfString_Object = MibTableColumn
tmnxLudbHostSlaProfString = _TmnxLudbHostSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 22),
    _TmnxLudbHostSlaProfString_Type()
)
tmnxLudbHostSlaProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostSlaProfString.setStatus("current")


class _TmnxLudbHostFltrProfString_Type(TmnxFilterProfileStringOrEmpty):
    """Custom type tmnxLudbHostFltrProfString based on TmnxFilterProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostFltrProfString_Type.__name__ = "TmnxFilterProfileStringOrEmpty"
_TmnxLudbHostFltrProfString_Object = MibTableColumn
tmnxLudbHostFltrProfString = _TmnxLudbHostFltrProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 23),
    _TmnxLudbHostFltrProfString_Type()
)
tmnxLudbHostFltrProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostFltrProfString.setStatus("current")


class _TmnxLudbHostSubProfString_Type(TmnxSubProfileStringOrEmpty):
    """Custom type tmnxLudbHostSubProfString based on TmnxSubProfileStringOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostSubProfString_Type.__name__ = "TmnxSubProfileStringOrEmpty"
_TmnxLudbHostSubProfString_Object = MibTableColumn
tmnxLudbHostSubProfString = _TmnxLudbHostSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 24),
    _TmnxLudbHostSubProfString_Type()
)
tmnxLudbHostSubProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostSubProfString.setStatus("current")


class _TmnxLudbHostAppProfString_Type(DisplayString):
    """Custom type tmnxLudbHostAppProfString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxLudbHostAppProfString_Type.__name__ = "DisplayString"
_TmnxLudbHostAppProfString_Object = MibTableColumn
tmnxLudbHostAppProfString = _TmnxLudbHostAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 25),
    _TmnxLudbHostAppProfString_Type()
)
tmnxLudbHostAppProfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostAppProfString.setStatus("current")


class _TmnxLudbHostAncpString_Type(TmnxAncpStringOrZero):
    """Custom type tmnxLudbHostAncpString based on TmnxAncpStringOrZero"""
    defaultValue = OctetString("")


_TmnxLudbHostAncpString_Type.__name__ = "TmnxAncpStringOrZero"
_TmnxLudbHostAncpString_Object = MibTableColumn
tmnxLudbHostAncpString = _TmnxLudbHostAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 26),
    _TmnxLudbHostAncpString_Type()
)
tmnxLudbHostAncpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostAncpString.setStatus("current")


class _TmnxLudbHostInterDestId_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbHostInterDestId based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostInterDestId_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbHostInterDestId_Object = MibTableColumn
tmnxLudbHostInterDestId = _TmnxLudbHostInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 27),
    _TmnxLudbHostInterDestId_Type()
)
tmnxLudbHostInterDestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostInterDestId.setStatus("current")


class _TmnxLudbHostUseClientPool_Type(TruthValue):
    """Custom type tmnxLudbHostUseClientPool based on TruthValue"""
    defaultValue = 2


_TmnxLudbHostUseClientPool_Type.__name__ = "TruthValue"
_TmnxLudbHostUseClientPool_Object = MibTableColumn
tmnxLudbHostUseClientPool = _TmnxLudbHostUseClientPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 28),
    _TmnxLudbHostUseClientPool_Type()
)
tmnxLudbHostUseClientPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostUseClientPool.setStatus("current")


class _TmnxLudbHostAuthPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbHostAuthPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostAuthPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbHostAuthPolicy_Object = MibTableColumn
tmnxLudbHostAuthPolicy = _TmnxLudbHostAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 29),
    _TmnxLudbHostAuthPolicy_Type()
)
tmnxLudbHostAuthPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostAuthPolicy.setStatus("current")


class _TmnxLudbHostRetailerSvcId_Type(TmnxServId):
    """Custom type tmnxLudbHostRetailerSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxLudbHostRetailerSvcId_Type.__name__ = "TmnxServId"
_TmnxLudbHostRetailerSvcId_Object = MibTableColumn
tmnxLudbHostRetailerSvcId = _TmnxLudbHostRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 30),
    _TmnxLudbHostRetailerSvcId_Type()
)
tmnxLudbHostRetailerSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostRetailerSvcId.setStatus("current")


class _TmnxLudbHostCategoryMapName_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbHostCategoryMapName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostCategoryMapName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbHostCategoryMapName_Object = MibTableColumn
tmnxLudbHostCategoryMapName = _TmnxLudbHostCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 31),
    _TmnxLudbHostCategoryMapName_Type()
)
tmnxLudbHostCategoryMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostCategoryMapName.setStatus("current")


class _TmnxLudbHostDefMsapPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxLudbHostDefMsapPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostDefMsapPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TmnxLudbHostDefMsapPolicy_Object = MibTableColumn
tmnxLudbHostDefMsapPolicy = _TmnxLudbHostDefMsapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 32),
    _TmnxLudbHostDefMsapPolicy_Type()
)
tmnxLudbHostDefMsapPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostDefMsapPolicy.setStatus("current")


class _TmnxLudbHostDefMsapService_Type(TmnxServId):
    """Custom type tmnxLudbHostDefMsapService based on TmnxServId"""
    defaultValue = 0


_TmnxLudbHostDefMsapService_Type.__name__ = "TmnxServId"
_TmnxLudbHostDefMsapService_Object = MibTableColumn
tmnxLudbHostDefMsapService = _TmnxLudbHostDefMsapService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 33),
    _TmnxLudbHostDefMsapService_Type()
)
tmnxLudbHostDefMsapService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostDefMsapService.setStatus("current")


class _TmnxLudbHostDefMsapGroupIf_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbHostDefMsapGroupIf based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostDefMsapGroupIf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbHostDefMsapGroupIf_Object = MibTableColumn
tmnxLudbHostDefMsapGroupIf = _TmnxLudbHostDefMsapGroupIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 34),
    _TmnxLudbHostDefMsapGroupIf_Type()
)
tmnxLudbHostDefMsapGroupIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostDefMsapGroupIf.setStatus("current")


class _TmnxLudbHostSystemId_Type(DisplayString):
    """Custom type tmnxLudbHostSystemId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLudbHostSystemId_Type.__name__ = "DisplayString"
_TmnxLudbHostSystemId_Object = MibTableColumn
tmnxLudbHostSystemId = _TmnxLudbHostSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 35),
    _TmnxLudbHostSystemId_Type()
)
tmnxLudbHostSystemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostSystemId.setStatus("current")


class _TmnxLudbHostServiceId_Type(TmnxServId):
    """Custom type tmnxLudbHostServiceId based on TmnxServId"""
    defaultValue = 0


_TmnxLudbHostServiceId_Type.__name__ = "TmnxServId"
_TmnxLudbHostServiceId_Object = MibTableColumn
tmnxLudbHostServiceId = _TmnxLudbHostServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 36),
    _TmnxLudbHostServiceId_Type()
)
tmnxLudbHostServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostServiceId.setStatus("current")


class _TmnxLudbHostSapId_Type(DisplayString):
    """Custom type tmnxLudbHostSapId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLudbHostSapId_Type.__name__ = "DisplayString"
_TmnxLudbHostSapId_Object = MibTableColumn
tmnxLudbHostSapId = _TmnxLudbHostSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 37),
    _TmnxLudbHostSapId_Type()
)
tmnxLudbHostSapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostSapId.setStatus("current")


class _TmnxLudbHostString_Type(DisplayString):
    """Custom type tmnxLudbHostString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLudbHostString_Type.__name__ = "DisplayString"
_TmnxLudbHostString_Object = MibTableColumn
tmnxLudbHostString = _TmnxLudbHostString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 38),
    _TmnxLudbHostString_Type()
)
tmnxLudbHostString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostString.setStatus("current")


class _TmnxLudbHostIpv6Addr_Type(InetAddress):
    """Custom type tmnxLudbHostIpv6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxLudbHostIpv6Addr_Type.__name__ = "InetAddress"
_TmnxLudbHostIpv6Addr_Object = MibTableColumn
tmnxLudbHostIpv6Addr = _TmnxLudbHostIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 39),
    _TmnxLudbHostIpv6Addr_Type()
)
tmnxLudbHostIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostIpv6Addr.setStatus("current")


class _TmnxLudbHostIpv6Pfx_Type(InetAddress):
    """Custom type tmnxLudbHostIpv6Pfx based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxLudbHostIpv6Pfx_Type.__name__ = "InetAddress"
_TmnxLudbHostIpv6Pfx_Object = MibTableColumn
tmnxLudbHostIpv6Pfx = _TmnxLudbHostIpv6Pfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 40),
    _TmnxLudbHostIpv6Pfx_Type()
)
tmnxLudbHostIpv6Pfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostIpv6Pfx.setStatus("current")


class _TmnxLudbHostIpv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxLudbHostIpv6PfxLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(48, 64),
    )


_TmnxLudbHostIpv6PfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxLudbHostIpv6PfxLen_Object = MibTableColumn
tmnxLudbHostIpv6PfxLen = _TmnxLudbHostIpv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 41),
    _TmnxLudbHostIpv6PfxLen_Type()
)
tmnxLudbHostIpv6PfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostIpv6PfxLen.setStatus("current")


class _TmnxLudbHostAuthDomainName_Type(DisplayString):
    """Custom type tmnxLudbHostAuthDomainName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLudbHostAuthDomainName_Type.__name__ = "DisplayString"
_TmnxLudbHostAuthDomainName_Object = MibTableColumn
tmnxLudbHostAuthDomainName = _TmnxLudbHostAuthDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 42),
    _TmnxLudbHostAuthDomainName_Type()
)
tmnxLudbHostAuthDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostAuthDomainName.setStatus("current")


class _TmnxLudbHostDhcpOption60Fmt_Type(TmnxLudbDataFormat):
    """Custom type tmnxLudbHostDhcpOption60Fmt based on TmnxLudbDataFormat"""
    defaultValue = 3


_TmnxLudbHostDhcpOption60Fmt_Type.__name__ = "TmnxLudbDataFormat"
_TmnxLudbHostDhcpOption60Fmt_Object = MibTableColumn
tmnxLudbHostDhcpOption60Fmt = _TmnxLudbHostDhcpOption60Fmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 100),
    _TmnxLudbHostDhcpOption60Fmt_Type()
)
tmnxLudbHostDhcpOption60Fmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostDhcpOption60Fmt.setStatus("current")


class _TmnxLudbHostDhcpOption60_Type(OctetString):
    """Custom type tmnxLudbHostDhcpOption60 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxLudbHostDhcpOption60_Type.__name__ = "OctetString"
_TmnxLudbHostDhcpOption60_Object = MibTableColumn
tmnxLudbHostDhcpOption60 = _TmnxLudbHostDhcpOption60_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 101),
    _TmnxLudbHostDhcpOption60_Type()
)
tmnxLudbHostDhcpOption60.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostDhcpOption60.setStatus("current")


class _TmnxLudbHostDhcpRelayAddrType_Type(InetAddressType):
    """Custom type tmnxLudbHostDhcpRelayAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLudbHostDhcpRelayAddrType_Type.__name__ = "InetAddressType"
_TmnxLudbHostDhcpRelayAddrType_Object = MibTableColumn
tmnxLudbHostDhcpRelayAddrType = _TmnxLudbHostDhcpRelayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 102),
    _TmnxLudbHostDhcpRelayAddrType_Type()
)
tmnxLudbHostDhcpRelayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostDhcpRelayAddrType.setStatus("current")


class _TmnxLudbHostDhcpRelayAddress_Type(InetAddress):
    """Custom type tmnxLudbHostDhcpRelayAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLudbHostDhcpRelayAddress_Type.__name__ = "InetAddress"
_TmnxLudbHostDhcpRelayAddress_Object = MibTableColumn
tmnxLudbHostDhcpRelayAddress = _TmnxLudbHostDhcpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 103),
    _TmnxLudbHostDhcpRelayAddress_Type()
)
tmnxLudbHostDhcpRelayAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostDhcpRelayAddress.setStatus("current")


class _TmnxLudbHostPppUserNameFormat_Type(TmnxLocUsrDbUserNameFormat):
    """Custom type tmnxLudbHostPppUserNameFormat based on TmnxLocUsrDbUserNameFormat"""
    defaultValue = 0


_TmnxLudbHostPppUserNameFormat_Type.__name__ = "TmnxLocUsrDbUserNameFormat"
_TmnxLudbHostPppUserNameFormat_Object = MibTableColumn
tmnxLudbHostPppUserNameFormat = _TmnxLudbHostPppUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 200),
    _TmnxLudbHostPppUserNameFormat_Type()
)
tmnxLudbHostPppUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppUserNameFormat.setStatus("current")


class _TmnxLudbHostPppUserName_Type(TmnxPppoeUserNameOrEmpty):
    """Custom type tmnxLudbHostPppUserName based on TmnxPppoeUserNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostPppUserName_Type.__name__ = "TmnxPppoeUserNameOrEmpty"
_TmnxLudbHostPppUserName_Object = MibTableColumn
tmnxLudbHostPppUserName = _TmnxLudbHostPppUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 201),
    _TmnxLudbHostPppUserName_Type()
)
tmnxLudbHostPppUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppUserName.setStatus("current")


class _TmnxLudbHostPppPasswordType_Type(TmnxLocUsrDbPasswordType):
    """Custom type tmnxLudbHostPppPasswordType based on TmnxLocUsrDbPasswordType"""
    defaultValue = 0


_TmnxLudbHostPppPasswordType_Type.__name__ = "TmnxLocUsrDbPasswordType"
_TmnxLudbHostPppPasswordType_Object = MibTableColumn
tmnxLudbHostPppPasswordType = _TmnxLudbHostPppPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 202),
    _TmnxLudbHostPppPasswordType_Type()
)
tmnxLudbHostPppPasswordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppPasswordType.setStatus("current")


class _TmnxLudbHostPppPassword_Type(OctetString):
    """Custom type tmnxLudbHostPppPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxLudbHostPppPassword_Type.__name__ = "OctetString"
_TmnxLudbHostPppPassword_Object = MibTableColumn
tmnxLudbHostPppPassword = _TmnxLudbHostPppPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 203),
    _TmnxLudbHostPppPassword_Type()
)
tmnxLudbHostPppPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppPassword.setStatus("current")


class _TmnxLudbHostPppServiceName_Type(DisplayString):
    """Custom type tmnxLudbHostPppServiceName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxLudbHostPppServiceName_Type.__name__ = "DisplayString"
_TmnxLudbHostPppServiceName_Object = MibTableColumn
tmnxLudbHostPppServiceName = _TmnxLudbHostPppServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 204),
    _TmnxLudbHostPppServiceName_Type()
)
tmnxLudbHostPppServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppServiceName.setStatus("current")


class _TmnxLudbHostPppL2tpTunnelGroup_Type(TmnxL2tpTunnelGroupNameOrEmpty):
    """Custom type tmnxLudbHostPppL2tpTunnelGroup based on TmnxL2tpTunnelGroupNameOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostPppL2tpTunnelGroup_Type.__name__ = "TmnxL2tpTunnelGroupNameOrEmpty"
_TmnxLudbHostPppL2tpTunnelGroup_Object = MibTableColumn
tmnxLudbHostPppL2tpTunnelGroup = _TmnxLudbHostPppL2tpTunnelGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 205),
    _TmnxLudbHostPppL2tpTunnelGroup_Type()
)
tmnxLudbHostPppL2tpTunnelGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppL2tpTunnelGroup.setStatus("current")


class _TmnxLudbHostPppL2tpSvcId_Type(TmnxServId):
    """Custom type tmnxLudbHostPppL2tpSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxLudbHostPppL2tpSvcId_Type.__name__ = "TmnxServId"
_TmnxLudbHostPppL2tpSvcId_Object = MibTableColumn
tmnxLudbHostPppL2tpSvcId = _TmnxLudbHostPppL2tpSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 206),
    _TmnxLudbHostPppL2tpSvcId_Type()
)
tmnxLudbHostPppL2tpSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppL2tpSvcId.setStatus("current")


class _TmnxLudbHostPppService_Type(TmnxServId):
    """Custom type tmnxLudbHostPppService based on TmnxServId"""
    defaultValue = 0


_TmnxLudbHostPppService_Type.__name__ = "TmnxServId"
_TmnxLudbHostPppService_Object = MibTableColumn
tmnxLudbHostPppService = _TmnxLudbHostPppService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 207),
    _TmnxLudbHostPppService_Type()
)
tmnxLudbHostPppService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppService.setStatus("current")


class _TmnxLudbHostPppInterface_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbHostPppInterface based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbHostPppInterface_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbHostPppInterface_Object = MibTableColumn
tmnxLudbHostPppInterface = _TmnxLudbHostPppInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 208),
    _TmnxLudbHostPppInterface_Type()
)
tmnxLudbHostPppInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppInterface.setStatus("current")


class _TmnxLudbHostPppoePadoDelay_Type(TmnxPppoePadoDelay):
    """Custom type tmnxLudbHostPppoePadoDelay based on TmnxPppoePadoDelay"""
    defaultValue = 0


_TmnxLudbHostPppoePadoDelay_Type.__name__ = "TmnxPppoePadoDelay"
_TmnxLudbHostPppoePadoDelay_Object = MibTableColumn
tmnxLudbHostPppoePadoDelay = _TmnxLudbHostPppoePadoDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 21, 1, 290),
    _TmnxLudbHostPppoePadoDelay_Type()
)
tmnxLudbHostPppoePadoDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbHostPppoePadoDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLudbHostPppoePadoDelay.setUnits("deci-seconds")
_TmnxLudbPppAleTableLastChange_Type = TimeStamp
_TmnxLudbPppAleTableLastChange_Object = MibScalar
tmnxLudbPppAleTableLastChange = _TmnxLudbPppAleTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 22),
    _TmnxLudbPppAleTableLastChange_Type()
)
tmnxLudbPppAleTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbPppAleTableLastChange.setStatus("current")
_TmnxLudbPppAleTable_Object = MibTable
tmnxLudbPppAleTable = _TmnxLudbPppAleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 23)
)
if mibBuilder.loadTexts:
    tmnxLudbPppAleTable.setStatus("current")
_TmnxLudbPppAleEntry_Object = MibTableRow
tmnxLudbPppAleEntry = _TmnxLudbPppAleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 23, 1)
)
tmnxLudbPppAleEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeHostName"),
)
if mibBuilder.loadTexts:
    tmnxLudbPppAleEntry.setStatus("current")
_TmnxLudbPppAleRowStatus_Type = RowStatus
_TmnxLudbPppAleRowStatus_Object = MibTableColumn
tmnxLudbPppAleRowStatus = _TmnxLudbPppAleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 23, 1, 1),
    _TmnxLudbPppAleRowStatus_Type()
)
tmnxLudbPppAleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAleRowStatus.setStatus("current")
_TmnxLudbPppAleLastChangeTime_Type = TimeStamp
_TmnxLudbPppAleLastChangeTime_Object = MibTableColumn
tmnxLudbPppAleLastChangeTime = _TmnxLudbPppAleLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 23, 1, 2),
    _TmnxLudbPppAleLastChangeTime_Type()
)
tmnxLudbPppAleLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbPppAleLastChangeTime.setStatus("current")


class _TmnxLudbPppAleEncapOffsetMode_Type(TmnxSubAleOffsetMode):
    """Custom type tmnxLudbPppAleEncapOffsetMode based on TmnxSubAleOffsetMode"""
    defaultValue = 0


_TmnxLudbPppAleEncapOffsetMode_Type.__name__ = "TmnxSubAleOffsetMode"
_TmnxLudbPppAleEncapOffsetMode_Object = MibTableColumn
tmnxLudbPppAleEncapOffsetMode = _TmnxLudbPppAleEncapOffsetMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 23, 1, 3),
    _TmnxLudbPppAleEncapOffsetMode_Type()
)
tmnxLudbPppAleEncapOffsetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAleEncapOffsetMode.setStatus("current")


class _TmnxLudbPppAleEncapOffset_Type(TmnxSubAleOffset):
    """Custom type tmnxLudbPppAleEncapOffset based on TmnxSubAleOffset"""
    defaultValue = 0


_TmnxLudbPppAleEncapOffset_Type.__name__ = "TmnxSubAleOffset"
_TmnxLudbPppAleEncapOffset_Object = MibTableColumn
tmnxLudbPppAleEncapOffset = _TmnxLudbPppAleEncapOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 23, 1, 4),
    _TmnxLudbPppAleEncapOffset_Type()
)
tmnxLudbPppAleEncapOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAleEncapOffset.setStatus("current")


class _TmnxLudbPppAleRateDown_Type(Unsigned32):
    """Custom type tmnxLudbPppAleRateDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxLudbPppAleRateDown_Type.__name__ = "Unsigned32"
_TmnxLudbPppAleRateDown_Object = MibTableColumn
tmnxLudbPppAleRateDown = _TmnxLudbPppAleRateDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 23, 1, 6),
    _TmnxLudbPppAleRateDown_Type()
)
tmnxLudbPppAleRateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAleRateDown.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLudbPppAleRateDown.setUnits("kbps")
_TmnxLudbRadproxCacheTableLastCh_Type = TimeStamp
_TmnxLudbRadproxCacheTableLastCh_Object = MibScalar
tmnxLudbRadproxCacheTableLastCh = _TmnxLudbRadproxCacheTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 24),
    _TmnxLudbRadproxCacheTableLastCh_Type()
)
tmnxLudbRadproxCacheTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheTableLastCh.setStatus("current")
_TmnxLudbRadproxCacheTable_Object = MibTable
tmnxLudbRadproxCacheTable = _TmnxLudbRadproxCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25)
)
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheTable.setStatus("current")
_TmnxLudbRadproxCacheEntry_Object = MibTableRow
tmnxLudbRadproxCacheEntry = _TmnxLudbRadproxCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1)
)
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheEntry.setStatus("current")
_TmnxLudbRadproxCacheLastCh_Type = TimeStamp
_TmnxLudbRadproxCacheLastCh_Object = MibTableColumn
tmnxLudbRadproxCacheLastCh = _TmnxLudbRadproxCacheLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 1),
    _TmnxLudbRadproxCacheLastCh_Type()
)
tmnxLudbRadproxCacheLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheLastCh.setStatus("current")


class _TmnxLudbRadproxCacheService_Type(TmnxServId):
    """Custom type tmnxLudbRadproxCacheService based on TmnxServId"""
    defaultValue = 0


_TmnxLudbRadproxCacheService_Type.__name__ = "TmnxServId"
_TmnxLudbRadproxCacheService_Object = MibTableColumn
tmnxLudbRadproxCacheService = _TmnxLudbRadproxCacheService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 2),
    _TmnxLudbRadproxCacheService_Type()
)
tmnxLudbRadproxCacheService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheService.setStatus("current")


class _TmnxLudbRadproxCacheServer_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbRadproxCacheServer based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxLudbRadproxCacheServer_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbRadproxCacheServer_Object = MibTableColumn
tmnxLudbRadproxCacheServer = _TmnxLudbRadproxCacheServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 3),
    _TmnxLudbRadproxCacheServer_Type()
)
tmnxLudbRadproxCacheServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheServer.setStatus("current")


class _TmnxLudbRadproxCacheMatchType_Type(Integer32):
    """Custom type tmnxLudbRadproxCacheMatchType based on Integer32"""
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
        *(("mac", 1),
          ("circuitId", 2),
          ("remoteId", 3),
          ("option", 4))
    )


_TmnxLudbRadproxCacheMatchType_Type.__name__ = "Integer32"
_TmnxLudbRadproxCacheMatchType_Object = MibTableColumn
tmnxLudbRadproxCacheMatchType = _TmnxLudbRadproxCacheMatchType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 4),
    _TmnxLudbRadproxCacheMatchType_Type()
)
tmnxLudbRadproxCacheMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheMatchType.setStatus("current")


class _TmnxLudbRadproxCacheMatchOption_Type(Unsigned32):
    """Custom type tmnxLudbRadproxCacheMatchOption based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 254),
    )


_TmnxLudbRadproxCacheMatchOption_Type.__name__ = "Unsigned32"
_TmnxLudbRadproxCacheMatchOption_Object = MibTableColumn
tmnxLudbRadproxCacheMatchOption = _TmnxLudbRadproxCacheMatchOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 5),
    _TmnxLudbRadproxCacheMatchOption_Type()
)
tmnxLudbRadproxCacheMatchOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheMatchOption.setStatus("current")


class _TmnxLudbRadproxCacheFailAction_Type(Integer32):
    """Custom type tmnxLudbRadproxCacheFailAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2))
    )


_TmnxLudbRadproxCacheFailAction_Type.__name__ = "Integer32"
_TmnxLudbRadproxCacheFailAction_Object = MibTableColumn
tmnxLudbRadproxCacheFailAction = _TmnxLudbRadproxCacheFailAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 6),
    _TmnxLudbRadproxCacheFailAction_Type()
)
tmnxLudbRadproxCacheFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheFailAction.setStatus("current")


class _TmnxLudbRadproxCacheMacFormat_Type(TmnxMacSpecification):
    """Custom type tmnxLudbRadproxCacheMacFormat based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxLudbRadproxCacheMacFormat_Type.__name__ = "TmnxMacSpecification"
_TmnxLudbRadproxCacheMacFormat_Object = MibTableColumn
tmnxLudbRadproxCacheMacFormat = _TmnxLudbRadproxCacheMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 7),
    _TmnxLudbRadproxCacheMacFormat_Type()
)
tmnxLudbRadproxCacheMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheMacFormat.setStatus("current")


class _TmnxLudbRadproxCacheMatchOption6_Type(Unsigned32):
    """Custom type tmnxLudbRadproxCacheMatchOption6 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxLudbRadproxCacheMatchOption6_Type.__name__ = "Unsigned32"
_TmnxLudbRadproxCacheMatchOption6_Object = MibTableColumn
tmnxLudbRadproxCacheMatchOption6 = _TmnxLudbRadproxCacheMatchOption6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 25, 1, 9),
    _TmnxLudbRadproxCacheMatchOption6_Type()
)
tmnxLudbRadproxCacheMatchOption6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbRadproxCacheMatchOption6.setStatus("current")
_TmnxLocUsrDbDhcpOption6TblLstCh_Type = TimeStamp
_TmnxLocUsrDbDhcpOption6TblLstCh_Object = MibScalar
tmnxLocUsrDbDhcpOption6TblLstCh = _TmnxLocUsrDbDhcpOption6TblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 26),
    _TmnxLocUsrDbDhcpOption6TblLstCh_Type()
)
tmnxLocUsrDbDhcpOption6TblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6TblLstCh.setStatus("current")
_TmnxLocUsrDbDhcpOption6Table_Object = MibTable
tmnxLocUsrDbDhcpOption6Table = _TmnxLocUsrDbDhcpOption6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 27)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6Table.setStatus("current")
_TmnxLocUsrDbDhcpOption6Entry_Object = MibTableRow
tmnxLocUsrDbDhcpOption6Entry = _TmnxLocUsrDbDhcpOption6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 27, 1)
)
tmnxLocUsrDbDhcpOption6Entry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpHostName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption6Number"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6Entry.setStatus("current")


class _TmnxLocUsrDbDhcpOption6Number_Type(Unsigned32):
    """Custom type tmnxLocUsrDbDhcpOption6Number based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_TmnxLocUsrDbDhcpOption6Number_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbDhcpOption6Number_Object = MibTableColumn
tmnxLocUsrDbDhcpOption6Number = _TmnxLocUsrDbDhcpOption6Number_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 27, 1, 1),
    _TmnxLocUsrDbDhcpOption6Number_Type()
)
tmnxLocUsrDbDhcpOption6Number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6Number.setStatus("current")
_TmnxLocUsrDbDhcpOption6RowStatus_Type = RowStatus
_TmnxLocUsrDbDhcpOption6RowStatus_Object = MibTableColumn
tmnxLocUsrDbDhcpOption6RowStatus = _TmnxLocUsrDbDhcpOption6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 27, 1, 2),
    _TmnxLocUsrDbDhcpOption6RowStatus_Type()
)
tmnxLocUsrDbDhcpOption6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6RowStatus.setStatus("current")
_TmnxLocUsrDbDhcpOption6LstChngTm_Type = TimeStamp
_TmnxLocUsrDbDhcpOption6LstChngTm_Object = MibTableColumn
tmnxLocUsrDbDhcpOption6LstChngTm = _TmnxLocUsrDbDhcpOption6LstChngTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 27, 1, 3),
    _TmnxLocUsrDbDhcpOption6LstChngTm_Type()
)
tmnxLocUsrDbDhcpOption6LstChngTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6LstChngTm.setStatus("current")
_TmnxLocUsrDbDhcpOption6Type_Type = TmnxDhcpOptionType
_TmnxLocUsrDbDhcpOption6Type_Object = MibTableColumn
tmnxLocUsrDbDhcpOption6Type = _TmnxLocUsrDbDhcpOption6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 27, 1, 4),
    _TmnxLocUsrDbDhcpOption6Type_Type()
)
tmnxLocUsrDbDhcpOption6Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6Type.setStatus("current")


class _TmnxLocUsrDbDhcpOption6Value_Type(OctetString):
    """Custom type tmnxLocUsrDbDhcpOption6Value based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbDhcpOption6Value_Type.__name__ = "OctetString"
_TmnxLocUsrDbDhcpOption6Value_Object = MibTableColumn
tmnxLocUsrDbDhcpOption6Value = _TmnxLocUsrDbDhcpOption6Value_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 27, 1, 5),
    _TmnxLocUsrDbDhcpOption6Value_Type()
)
tmnxLocUsrDbDhcpOption6Value.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbDhcpOption6Value.setStatus("current")
_TmnxLocUsrDbPppOption6TblLstCh_Type = TimeStamp
_TmnxLocUsrDbPppOption6TblLstCh_Object = MibScalar
tmnxLocUsrDbPppOption6TblLstCh = _TmnxLocUsrDbPppOption6TblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 28),
    _TmnxLocUsrDbPppOption6TblLstCh_Type()
)
tmnxLocUsrDbPppOption6TblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6TblLstCh.setStatus("current")
_TmnxLocUsrDbPppOption6Table_Object = MibTable
tmnxLocUsrDbPppOption6Table = _TmnxLocUsrDbPppOption6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 29)
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6Table.setStatus("current")
_TmnxLocUsrDbPppOption6Entry_Object = MibTableRow
tmnxLocUsrDbPppOption6Entry = _TmnxLocUsrDbPppOption6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 29, 1)
)
tmnxLocUsrDbPppOption6Entry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeHostName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppOption6Number"),
)
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6Entry.setStatus("current")


class _TmnxLocUsrDbPppOption6Number_Type(Unsigned32):
    """Custom type tmnxLocUsrDbPppOption6Number based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_TmnxLocUsrDbPppOption6Number_Type.__name__ = "Unsigned32"
_TmnxLocUsrDbPppOption6Number_Object = MibTableColumn
tmnxLocUsrDbPppOption6Number = _TmnxLocUsrDbPppOption6Number_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 29, 1, 1),
    _TmnxLocUsrDbPppOption6Number_Type()
)
tmnxLocUsrDbPppOption6Number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6Number.setStatus("current")
_TmnxLocUsrDbPppOption6RowSts_Type = RowStatus
_TmnxLocUsrDbPppOption6RowSts_Object = MibTableColumn
tmnxLocUsrDbPppOption6RowSts = _TmnxLocUsrDbPppOption6RowSts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 29, 1, 2),
    _TmnxLocUsrDbPppOption6RowSts_Type()
)
tmnxLocUsrDbPppOption6RowSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6RowSts.setStatus("current")
_TmnxLocUsrDbPppOption6LstChgTm_Type = TimeStamp
_TmnxLocUsrDbPppOption6LstChgTm_Object = MibTableColumn
tmnxLocUsrDbPppOption6LstChgTm = _TmnxLocUsrDbPppOption6LstChgTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 29, 1, 3),
    _TmnxLocUsrDbPppOption6LstChgTm_Type()
)
tmnxLocUsrDbPppOption6LstChgTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6LstChgTm.setStatus("current")
_TmnxLocUsrDbPppOption6Type_Type = TmnxDhcpOptionType
_TmnxLocUsrDbPppOption6Type_Object = MibTableColumn
tmnxLocUsrDbPppOption6Type = _TmnxLocUsrDbPppOption6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 29, 1, 4),
    _TmnxLocUsrDbPppOption6Type_Type()
)
tmnxLocUsrDbPppOption6Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6Type.setStatus("current")


class _TmnxLocUsrDbPppOption6Value_Type(OctetString):
    """Custom type tmnxLocUsrDbPppOption6Value based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLocUsrDbPppOption6Value_Type.__name__ = "OctetString"
_TmnxLocUsrDbPppOption6Value_Object = MibTableColumn
tmnxLocUsrDbPppOption6Value = _TmnxLocUsrDbPppOption6Value_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 29, 1, 5),
    _TmnxLocUsrDbPppOption6Value_Type()
)
tmnxLocUsrDbPppOption6Value.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLocUsrDbPppOption6Value.setStatus("current")
_TmnxLudbPppAliTableLastChange_Type = TimeStamp
_TmnxLudbPppAliTableLastChange_Object = MibScalar
tmnxLudbPppAliTableLastChange = _TmnxLudbPppAliTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 30),
    _TmnxLudbPppAliTableLastChange_Type()
)
tmnxLudbPppAliTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbPppAliTableLastChange.setStatus("current")
_TmnxLudbPppAliTable_Object = MibTable
tmnxLudbPppAliTable = _TmnxLudbPppAliTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 31)
)
if mibBuilder.loadTexts:
    tmnxLudbPppAliTable.setStatus("current")
_TmnxLudbPppAliEntry_Object = MibTableRow
tmnxLudbPppAliEntry = _TmnxLudbPppAliEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 31, 1)
)
if mibBuilder.loadTexts:
    tmnxLudbPppAliEntry.setStatus("current")
_TmnxLudbPppAliLastChangeTime_Type = TimeStamp
_TmnxLudbPppAliLastChangeTime_Object = MibTableColumn
tmnxLudbPppAliLastChangeTime = _TmnxLudbPppAliLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 31, 1, 1),
    _TmnxLudbPppAliLastChangeTime_Type()
)
tmnxLudbPppAliLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbPppAliLastChangeTime.setStatus("current")


class _TmnxLudbPppAliCircuitIdType_Type(Integer32):
    """Custom type tmnxLudbPppAliCircuitIdType based on Integer32"""
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
          ("ascii", 1),
          ("sapId", 2))
    )


_TmnxLudbPppAliCircuitIdType_Type.__name__ = "Integer32"
_TmnxLudbPppAliCircuitIdType_Object = MibTableColumn
tmnxLudbPppAliCircuitIdType = _TmnxLudbPppAliCircuitIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 31, 1, 2),
    _TmnxLudbPppAliCircuitIdType_Type()
)
tmnxLudbPppAliCircuitIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAliCircuitIdType.setStatus("current")


class _TmnxLudbPppAliCircuitId_Type(OctetString):
    """Custom type tmnxLudbPppAliCircuitId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxLudbPppAliCircuitId_Type.__name__ = "OctetString"
_TmnxLudbPppAliCircuitId_Object = MibTableColumn
tmnxLudbPppAliCircuitId = _TmnxLudbPppAliCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 31, 1, 3),
    _TmnxLudbPppAliCircuitId_Type()
)
tmnxLudbPppAliCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAliCircuitId.setStatus("current")


class _TmnxLudbPppAliRemoteIdType_Type(Integer32):
    """Custom type tmnxLudbPppAliRemoteIdType based on Integer32"""
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
          ("ascii", 1),
          ("mac", 2))
    )


_TmnxLudbPppAliRemoteIdType_Type.__name__ = "Integer32"
_TmnxLudbPppAliRemoteIdType_Object = MibTableColumn
tmnxLudbPppAliRemoteIdType = _TmnxLudbPppAliRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 31, 1, 4),
    _TmnxLudbPppAliRemoteIdType_Type()
)
tmnxLudbPppAliRemoteIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAliRemoteIdType.setStatus("current")


class _TmnxLudbPppAliRemoteId_Type(OctetString):
    """Custom type tmnxLudbPppAliRemoteId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxLudbPppAliRemoteId_Type.__name__ = "OctetString"
_TmnxLudbPppAliRemoteId_Object = MibTableColumn
tmnxLudbPppAliRemoteId = _TmnxLudbPppAliRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 31, 1, 5),
    _TmnxLudbPppAliRemoteId_Type()
)
tmnxLudbPppAliRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPppAliRemoteId.setStatus("current")
_TmnxLudbDhcp2TableLastChange_Type = TimeStamp
_TmnxLudbDhcp2TableLastChange_Object = MibScalar
tmnxLudbDhcp2TableLastChange = _TmnxLudbDhcp2TableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 32),
    _TmnxLudbDhcp2TableLastChange_Type()
)
tmnxLudbDhcp2TableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2TableLastChange.setStatus("current")
_TmnxLudbDhcp2Table_Object = MibTable
tmnxLudbDhcp2Table = _TmnxLudbDhcp2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33)
)
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Table.setStatus("current")
_TmnxLudbDhcp2Entry_Object = MibTableRow
tmnxLudbDhcp2Entry = _TmnxLudbDhcp2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1)
)
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Entry.setStatus("current")
_TmnxLudbDhcp2LastChangeTime_Type = TimeStamp
_TmnxLudbDhcp2LastChangeTime_Object = MibTableColumn
tmnxLudbDhcp2LastChangeTime = _TmnxLudbDhcp2LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 1),
    _TmnxLudbDhcp2LastChangeTime_Type()
)
tmnxLudbDhcp2LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2LastChangeTime.setStatus("current")


class _TmnxLudbDhcp2WppPortalSvcId_Type(TmnxServId):
    """Custom type tmnxLudbDhcp2WppPortalSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxLudbDhcp2WppPortalSvcId_Type.__name__ = "TmnxServId"
_TmnxLudbDhcp2WppPortalSvcId_Object = MibTableColumn
tmnxLudbDhcp2WppPortalSvcId = _TmnxLudbDhcp2WppPortalSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 2),
    _TmnxLudbDhcp2WppPortalSvcId_Type()
)
tmnxLudbDhcp2WppPortalSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2WppPortalSvcId.setStatus("current")


class _TmnxLudbDhcp2WppPortalName_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbDhcp2WppPortalName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLudbDhcp2WppPortalName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbDhcp2WppPortalName_Object = MibTableColumn
tmnxLudbDhcp2WppPortalName = _TmnxLudbDhcp2WppPortalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 3),
    _TmnxLudbDhcp2WppPortalName_Type()
)
tmnxLudbDhcp2WppPortalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2WppPortalName.setStatus("current")


class _TmnxLudbDhcp2WppSubProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbDhcp2WppSubProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLudbDhcp2WppSubProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbDhcp2WppSubProfile_Object = MibTableColumn
tmnxLudbDhcp2WppSubProfile = _TmnxLudbDhcp2WppSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 4),
    _TmnxLudbDhcp2WppSubProfile_Type()
)
tmnxLudbDhcp2WppSubProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2WppSubProfile.setStatus("current")


class _TmnxLudbDhcp2WppSLAProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbDhcp2WppSLAProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLudbDhcp2WppSLAProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbDhcp2WppSLAProfile_Object = MibTableColumn
tmnxLudbDhcp2WppSLAProfile = _TmnxLudbDhcp2WppSLAProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 5),
    _TmnxLudbDhcp2WppSLAProfile_Type()
)
tmnxLudbDhcp2WppSLAProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2WppSLAProfile.setStatus("current")


class _TmnxLudbDhcp2WppAppProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbDhcp2WppAppProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLudbDhcp2WppAppProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbDhcp2WppAppProfile_Object = MibTableColumn
tmnxLudbDhcp2WppAppProfile = _TmnxLudbDhcp2WppAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 6),
    _TmnxLudbDhcp2WppAppProfile_Type()
)
tmnxLudbDhcp2WppAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2WppAppProfile.setStatus("current")


class _TmnxLudbDhcp2WppRestDiscon_Type(Integer32):
    """Custom type tmnxLudbDhcp2WppRestDiscon based on Integer32"""
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
          ("restore", 1),
          ("noRestore", 2))
    )


_TmnxLudbDhcp2WppRestDiscon_Type.__name__ = "Integer32"
_TmnxLudbDhcp2WppRestDiscon_Object = MibTableColumn
tmnxLudbDhcp2WppRestDiscon = _TmnxLudbDhcp2WppRestDiscon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 7),
    _TmnxLudbDhcp2WppRestDiscon_Type()
)
tmnxLudbDhcp2WppRestDiscon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2WppRestDiscon.setStatus("current")


class _TmnxLudbDhcp2GiAddrType_Type(InetAddressType):
    """Custom type tmnxLudbDhcp2GiAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLudbDhcp2GiAddrType_Type.__name__ = "InetAddressType"
_TmnxLudbDhcp2GiAddrType_Object = MibTableColumn
tmnxLudbDhcp2GiAddrType = _TmnxLudbDhcp2GiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 10),
    _TmnxLudbDhcp2GiAddrType_Type()
)
tmnxLudbDhcp2GiAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2GiAddrType.setStatus("current")


class _TmnxLudbDhcp2GiAddr_Type(InetAddress):
    """Custom type tmnxLudbDhcp2GiAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxLudbDhcp2GiAddr_Type.__name__ = "InetAddress"
_TmnxLudbDhcp2GiAddr_Object = MibTableColumn
tmnxLudbDhcp2GiAddr = _TmnxLudbDhcp2GiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 11),
    _TmnxLudbDhcp2GiAddr_Type()
)
tmnxLudbDhcp2GiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2GiAddr.setStatus("current")


class _TmnxLudbDhcp2LinkAddrType_Type(InetAddressType):
    """Custom type tmnxLudbDhcp2LinkAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLudbDhcp2LinkAddrType_Type.__name__ = "InetAddressType"
_TmnxLudbDhcp2LinkAddrType_Object = MibTableColumn
tmnxLudbDhcp2LinkAddrType = _TmnxLudbDhcp2LinkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 12),
    _TmnxLudbDhcp2LinkAddrType_Type()
)
tmnxLudbDhcp2LinkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2LinkAddrType.setStatus("current")


class _TmnxLudbDhcp2LinkAddr_Type(InetAddress):
    """Custom type tmnxLudbDhcp2LinkAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxLudbDhcp2LinkAddr_Type.__name__ = "InetAddress"
_TmnxLudbDhcp2LinkAddr_Object = MibTableColumn
tmnxLudbDhcp2LinkAddr = _TmnxLudbDhcp2LinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 13),
    _TmnxLudbDhcp2LinkAddr_Type()
)
tmnxLudbDhcp2LinkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2LinkAddr.setStatus("current")


class _TmnxLudbDhcp2Server6AddrType_Type(InetAddressType):
    """Custom type tmnxLudbDhcp2Server6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLudbDhcp2Server6AddrType_Type.__name__ = "InetAddressType"
_TmnxLudbDhcp2Server6AddrType_Object = MibTableColumn
tmnxLudbDhcp2Server6AddrType = _TmnxLudbDhcp2Server6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 14),
    _TmnxLudbDhcp2Server6AddrType_Type()
)
tmnxLudbDhcp2Server6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Server6AddrType.setStatus("current")


class _TmnxLudbDhcp2Server6Addr_Type(InetAddress):
    """Custom type tmnxLudbDhcp2Server6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxLudbDhcp2Server6Addr_Type.__name__ = "InetAddress"
_TmnxLudbDhcp2Server6Addr_Object = MibTableColumn
tmnxLudbDhcp2Server6Addr = _TmnxLudbDhcp2Server6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 15),
    _TmnxLudbDhcp2Server6Addr_Type()
)
tmnxLudbDhcp2Server6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Server6Addr.setStatus("current")


class _TmnxLudbDhcp2DiamAppPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbDhcp2DiamAppPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLudbDhcp2DiamAppPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbDhcp2DiamAppPlcy_Object = MibTableColumn
tmnxLudbDhcp2DiamAppPlcy = _TmnxLudbDhcp2DiamAppPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 16),
    _TmnxLudbDhcp2DiamAppPlcy_Type()
)
tmnxLudbDhcp2DiamAppPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2DiamAppPlcy.setStatus("current")


class _TmnxLudbDhcp2Ipv6LeaseRenew_Type(Unsigned32):
    """Custom type tmnxLudbDhcp2Ipv6LeaseRenew based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbDhcp2Ipv6LeaseRenew_Type.__name__ = "Unsigned32"
_TmnxLudbDhcp2Ipv6LeaseRenew_Object = MibTableColumn
tmnxLudbDhcp2Ipv6LeaseRenew = _TmnxLudbDhcp2Ipv6LeaseRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 17),
    _TmnxLudbDhcp2Ipv6LeaseRenew_Type()
)
tmnxLudbDhcp2Ipv6LeaseRenew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Ipv6LeaseRenew.setStatus("current")


class _TmnxLudbDhcp2Ipv6LeaseRebind_Type(Unsigned32):
    """Custom type tmnxLudbDhcp2Ipv6LeaseRebind based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbDhcp2Ipv6LeaseRebind_Type.__name__ = "Unsigned32"
_TmnxLudbDhcp2Ipv6LeaseRebind_Object = MibTableColumn
tmnxLudbDhcp2Ipv6LeaseRebind = _TmnxLudbDhcp2Ipv6LeaseRebind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 18),
    _TmnxLudbDhcp2Ipv6LeaseRebind_Type()
)
tmnxLudbDhcp2Ipv6LeaseRebind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Ipv6LeaseRebind.setStatus("current")


class _TmnxLudbDhcp2Ipv6LeaseValidLife_Type(Unsigned32):
    """Custom type tmnxLudbDhcp2Ipv6LeaseValidLife based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 315446399),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbDhcp2Ipv6LeaseValidLife_Type.__name__ = "Unsigned32"
_TmnxLudbDhcp2Ipv6LeaseValidLife_Object = MibTableColumn
tmnxLudbDhcp2Ipv6LeaseValidLife = _TmnxLudbDhcp2Ipv6LeaseValidLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 19),
    _TmnxLudbDhcp2Ipv6LeaseValidLife_Type()
)
tmnxLudbDhcp2Ipv6LeaseValidLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Ipv6LeaseValidLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Ipv6LeaseValidLife.setUnits("seconds")


class _TmnxLudbDhcp2Ipv6LeasePrefLife_Type(Unsigned32):
    """Custom type tmnxLudbDhcp2Ipv6LeasePrefLife based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 315446399),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbDhcp2Ipv6LeasePrefLife_Type.__name__ = "Unsigned32"
_TmnxLudbDhcp2Ipv6LeasePrefLife_Object = MibTableColumn
tmnxLudbDhcp2Ipv6LeasePrefLife = _TmnxLudbDhcp2Ipv6LeasePrefLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 33, 1, 20),
    _TmnxLudbDhcp2Ipv6LeasePrefLife_Type()
)
tmnxLudbDhcp2Ipv6LeasePrefLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Ipv6LeasePrefLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLudbDhcp2Ipv6LeasePrefLife.setUnits("seconds")
_TmnxLudbPpp2TableLastChange_Type = TimeStamp
_TmnxLudbPpp2TableLastChange_Object = MibScalar
tmnxLudbPpp2TableLastChange = _TmnxLudbPpp2TableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 34),
    _TmnxLudbPpp2TableLastChange_Type()
)
tmnxLudbPpp2TableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbPpp2TableLastChange.setStatus("current")
_TmnxLudbPpp2Table_Object = MibTable
tmnxLudbPpp2Table = _TmnxLudbPpp2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35)
)
if mibBuilder.loadTexts:
    tmnxLudbPpp2Table.setStatus("current")
_TmnxLudbPpp2Entry_Object = MibTableRow
tmnxLudbPpp2Entry = _TmnxLudbPpp2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35, 1)
)
if mibBuilder.loadTexts:
    tmnxLudbPpp2Entry.setStatus("current")
_TmnxLudbPpp2LastChangeTime_Type = TimeStamp
_TmnxLudbPpp2LastChangeTime_Object = MibTableColumn
tmnxLudbPpp2LastChangeTime = _TmnxLudbPpp2LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35, 1, 1),
    _TmnxLudbPpp2LastChangeTime_Type()
)
tmnxLudbPpp2LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbPpp2LastChangeTime.setStatus("current")


class _TmnxLudbPpp2DiamAppPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxLudbPpp2DiamAppPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLudbPpp2DiamAppPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLudbPpp2DiamAppPlcy_Object = MibTableColumn
tmnxLudbPpp2DiamAppPlcy = _TmnxLudbPpp2DiamAppPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35, 1, 2),
    _TmnxLudbPpp2DiamAppPlcy_Type()
)
tmnxLudbPpp2DiamAppPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPpp2DiamAppPlcy.setStatus("current")


class _TmnxLudbPpp2Ipv6LeaseRenew_Type(Unsigned32):
    """Custom type tmnxLudbPpp2Ipv6LeaseRenew based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbPpp2Ipv6LeaseRenew_Type.__name__ = "Unsigned32"
_TmnxLudbPpp2Ipv6LeaseRenew_Object = MibTableColumn
tmnxLudbPpp2Ipv6LeaseRenew = _TmnxLudbPpp2Ipv6LeaseRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35, 1, 3),
    _TmnxLudbPpp2Ipv6LeaseRenew_Type()
)
tmnxLudbPpp2Ipv6LeaseRenew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPpp2Ipv6LeaseRenew.setStatus("current")


class _TmnxLudbPpp2Ipv6LeaseRebind_Type(Unsigned32):
    """Custom type tmnxLudbPpp2Ipv6LeaseRebind based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbPpp2Ipv6LeaseRebind_Type.__name__ = "Unsigned32"
_TmnxLudbPpp2Ipv6LeaseRebind_Object = MibTableColumn
tmnxLudbPpp2Ipv6LeaseRebind = _TmnxLudbPpp2Ipv6LeaseRebind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35, 1, 4),
    _TmnxLudbPpp2Ipv6LeaseRebind_Type()
)
tmnxLudbPpp2Ipv6LeaseRebind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPpp2Ipv6LeaseRebind.setStatus("current")


class _TmnxLudbPpp2Ipv6LeaseValidLife_Type(Unsigned32):
    """Custom type tmnxLudbPpp2Ipv6LeaseValidLife based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 315446399),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbPpp2Ipv6LeaseValidLife_Type.__name__ = "Unsigned32"
_TmnxLudbPpp2Ipv6LeaseValidLife_Object = MibTableColumn
tmnxLudbPpp2Ipv6LeaseValidLife = _TmnxLudbPpp2Ipv6LeaseValidLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35, 1, 5),
    _TmnxLudbPpp2Ipv6LeaseValidLife_Type()
)
tmnxLudbPpp2Ipv6LeaseValidLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPpp2Ipv6LeaseValidLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLudbPpp2Ipv6LeaseValidLife.setUnits("seconds")


class _TmnxLudbPpp2Ipv6LeasePrefLife_Type(Unsigned32):
    """Custom type tmnxLudbPpp2Ipv6LeasePrefLife based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 315446399),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxLudbPpp2Ipv6LeasePrefLife_Type.__name__ = "Unsigned32"
_TmnxLudbPpp2Ipv6LeasePrefLife_Object = MibTableColumn
tmnxLudbPpp2Ipv6LeasePrefLife = _TmnxLudbPpp2Ipv6LeasePrefLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 35, 1, 6),
    _TmnxLudbPpp2Ipv6LeasePrefLife_Type()
)
tmnxLudbPpp2Ipv6LeasePrefLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbPpp2Ipv6LeasePrefLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLudbPpp2Ipv6LeasePrefLife.setUnits("seconds")
_TmnxLudbToClntOptTableLstCh_Type = TimeStamp
_TmnxLudbToClntOptTableLstCh_Object = MibScalar
tmnxLudbToClntOptTableLstCh = _TmnxLudbToClntOptTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 36),
    _TmnxLudbToClntOptTableLstCh_Type()
)
tmnxLudbToClntOptTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbToClntOptTableLstCh.setStatus("current")
_TmnxLudbToClntOptTable_Object = MibTable
tmnxLudbToClntOptTable = _TmnxLudbToClntOptTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37)
)
if mibBuilder.loadTexts:
    tmnxLudbToClntOptTable.setStatus("current")
_TmnxLudbToClntOptEntry_Object = MibTableRow
tmnxLudbToClntOptEntry = _TmnxLudbToClntOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37, 1)
)
tmnxLudbToClntOptEntry.setIndexNames(
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbUserDatabaseName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostType"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostName"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptAddrType"),
    (0, "TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptNumber"),
)
if mibBuilder.loadTexts:
    tmnxLudbToClntOptEntry.setStatus("current")
_TmnxLudbToClntOptAddrType_Type = InetAddressType
_TmnxLudbToClntOptAddrType_Object = MibTableColumn
tmnxLudbToClntOptAddrType = _TmnxLudbToClntOptAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37, 1, 1),
    _TmnxLudbToClntOptAddrType_Type()
)
tmnxLudbToClntOptAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLudbToClntOptAddrType.setStatus("current")


class _TmnxLudbToClntOptNumber_Type(Unsigned32):
    """Custom type tmnxLudbToClntOptNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
        ValueRangeConstraint(255, 65535),
    )


_TmnxLudbToClntOptNumber_Type.__name__ = "Unsigned32"
_TmnxLudbToClntOptNumber_Object = MibTableColumn
tmnxLudbToClntOptNumber = _TmnxLudbToClntOptNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37, 1, 2),
    _TmnxLudbToClntOptNumber_Type()
)
tmnxLudbToClntOptNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLudbToClntOptNumber.setStatus("current")
_TmnxLudbToClntOptRowStatus_Type = RowStatus
_TmnxLudbToClntOptRowStatus_Object = MibTableColumn
tmnxLudbToClntOptRowStatus = _TmnxLudbToClntOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37, 1, 3),
    _TmnxLudbToClntOptRowStatus_Type()
)
tmnxLudbToClntOptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbToClntOptRowStatus.setStatus("current")
_TmnxLudbToClntOptLastCh_Type = TimeStamp
_TmnxLudbToClntOptLastCh_Object = MibTableColumn
tmnxLudbToClntOptLastCh = _TmnxLudbToClntOptLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37, 1, 4),
    _TmnxLudbToClntOptLastCh_Type()
)
tmnxLudbToClntOptLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLudbToClntOptLastCh.setStatus("current")
_TmnxLudbToClntOptType_Type = TmnxDhcpOptionType
_TmnxLudbToClntOptType_Object = MibTableColumn
tmnxLudbToClntOptType = _TmnxLudbToClntOptType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37, 1, 5),
    _TmnxLudbToClntOptType_Type()
)
tmnxLudbToClntOptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbToClntOptType.setStatus("current")


class _TmnxLudbToClntOptValue_Type(OctetString):
    """Custom type tmnxLudbToClntOptValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TmnxLudbToClntOptValue_Type.__name__ = "OctetString"
_TmnxLudbToClntOptValue_Object = MibTableColumn
tmnxLudbToClntOptValue = _TmnxLudbToClntOptValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 1, 37, 1, 6),
    _TmnxLudbToClntOptValue_Type()
)
tmnxLudbToClntOptValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLudbToClntOptValue.setStatus("current")
_TmnxLocalUserDbNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbNotificationObjs = _TmnxLocalUserDbNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 2)
)
_TmnxLudbNotifyPortId_Type = TNamedItem
_TmnxLudbNotifyPortId_Object = MibScalar
tmnxLudbNotifyPortId = _TmnxLudbNotifyPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 51, 2, 1),
    _TmnxLudbNotifyPortId_Type()
)
tmnxLudbNotifyPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxLudbNotifyPortId.setStatus("current")
_TmnxLocalUserDbNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbNotifyPrefix = _TmnxLocalUserDbNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 51)
)
_TmnxLocalUserDbNotifications_ObjectIdentity = ObjectIdentity
tmnxLocalUserDbNotifications = _TmnxLocalUserDbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 51, 0)
)
tmnxLocUsrDbDhcpEntry.registerAugmentions(
    ("TIMETRA-LOCAL-USER-DB-MIB",
     "tmnxLudbRadproxCacheEntry")
)
tmnxLudbRadproxCacheEntry.setIndexNames(*tmnxLocUsrDbDhcpEntry.getIndexNames())
tmnxLocUsrDbPppoeEntry.registerAugmentions(
    ("TIMETRA-LOCAL-USER-DB-MIB",
     "tmnxLudbPppAliEntry")
)
tmnxLudbPppAliEntry.setIndexNames(*tmnxLocUsrDbPppoeEntry.getIndexNames())
tmnxLocUsrDbDhcpEntry.registerAugmentions(
    ("TIMETRA-LOCAL-USER-DB-MIB",
     "tmnxLudbDhcp2Entry")
)
tmnxLudbDhcp2Entry.setIndexNames(*tmnxLocUsrDbDhcpEntry.getIndexNames())
tmnxLocUsrDbPppoeEntry.registerAugmentions(
    ("TIMETRA-LOCAL-USER-DB-MIB",
     "tmnxLudbPpp2Entry")
)
tmnxLudbPpp2Entry.setIndexNames(*tmnxLocUsrDbPppoeEntry.getIndexNames())

# Managed Objects groups

tmnxLocalUserDbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 1)
)
tmnxLocalUserDbGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDescription"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp1"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp2"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp3"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp4"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypePppoe1"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypePppoe2"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypePppoe3"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskSufNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskSufNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbHostCount"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbGroup.setStatus("obsolete")

tmnxLocalUserDbPppoeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 2)
)
tmnxLocalUserDbPppoeGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserNameFormat"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePasswordType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePassword"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserNameFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnmatchedReason"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionTbleLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionLstChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionValue"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbPppoeGroup.setStatus("obsolete")

tmnxLocalUserDbDhcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 3)
)
tmnxLocalUserDbDhcpGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSystemId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpServiceId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption60"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnSystemId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnServiceId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnOption60"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnmatchedReason"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionLastChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionValue"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbDhcpGroup.setStatus("obsolete")

tmnxLocalUserDbToolsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 4)
)
tmnxLocalUserDbToolsGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthDbName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthUsrName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthPwd"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthenticate"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthSuccessful"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthErrorMsg"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthHostName"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbToolsGroup.setStatus("obsolete")

tmnxLocalUserDbPppoeV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 5)
)
tmnxLocalUserDbPppoeV6v1Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserNameFormat"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePasswordType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePassword"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseClientPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserNameFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnmatchedReason"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionTbleLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionLstChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionValue"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbPppoeV6v1Group.setStatus("obsolete")

tmnxLocalUserDbPppoeV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 6)
)
tmnxLocalUserDbPppoeV7v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserNameFormat"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePasswordType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePassword"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseClientPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePadoDelay"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeServiceName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeL2tpTunnelGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRetailerSvcId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCategoryMapName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserNameFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnmatchedReason"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnServiceName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionTbleLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionLstChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionValue"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskSufNum"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbPppoeV7v0Group.setStatus("obsolete")

tmnxLocalUserDbDhcpV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 7)
)
tmnxLocalUserDbDhcpV7v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSystemId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpServiceId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption60"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAuthPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpServerAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpServerAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAuthDomainName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCategoryMapName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption60Fmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUseClientPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnSystemId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnServiceId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnOption60"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnmatchedReason"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionLastChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionValue"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskSufNum"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbDhcpV7v0Group.setStatus("obsolete")

tmnxLocalUserDbV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 8)
)
tmnxLocalUserDbV7v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDescription"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp1"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp2"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp3"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypeDhcp4"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypePppoe1"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypePppoe2"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbMatchTypePppoe3"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbHostCount"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV7v0Group.setStatus("current")

tmnxLocalUserDbObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 9)
)
tmnxLocalUserDbObsoleteGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCIdMaskSufNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCIdMaskSufNum"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbObsoleteGroup.setStatus("current")

tmnxLocalUserDbToolsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 10)
)
tmnxLocalUserDbToolsV7v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthDbName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthUsrName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthPwd"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthenticate"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthSuccessful"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthErrorMsg"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthHostName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthServiceName"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbToolsV7v0Group.setStatus("obsolete")

tmnxLocalUserDbRadiusFllbckGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 11)
)
tmnxLocalUserDbRadiusFllbckGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeDefMsapPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeDefMsapService"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeDefMsapGroupIf"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpDefMsapPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpDefMsapService"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpDefMsapGroupIf"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRetailerSvcId"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbRadiusFllbckGroup.setStatus("current")

tmnxLocalUserDbDhcpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 12)
)
tmnxLocalUserDbDhcpV8v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSystemId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpServiceId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption60"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAuthPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpServerAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpServerAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAuthDomainName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpCategoryMapName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption60Fmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUseClientPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnSystemId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnServiceId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnOption60"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnmatchedReason"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionLastChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOptionValue"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMaskSufNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpRemoteIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6Addr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6Pfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6PfxLen"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbDhcpV8v0Group.setStatus("current")

tmnxLocalUserDbPppoeV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 13)
)
tmnxLocalUserDbPppoeV8v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserNameFormat"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePasswordType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePassword"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseClientPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePadoDelay"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeServiceName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeL2tpTunnelGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRetailerSvcId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeCategoryMapName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserNameFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnmatchedReason"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnDuplicateHost"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnServiceName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionTbleLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionLstChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeOptionValue"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskPreStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskPreNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskSufStr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMaskSufNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeRemoteIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeL2tpSvcId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeService"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeInterface"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbPppoeV8v0Group.setStatus("current")

tmnxLocalUserDbToolsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 14)
)
tmnxLocalUserDbToolsV8v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthDbName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthUsrName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthPwd"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthenticate"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthSuccessful"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthErrorMsg"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthHostName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthServiceName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthRemoteIdFmt"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbToolsV8v0Group.setStatus("current")

tmnxLocalUserDbHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 20)
)
tmnxLocalUserDbHostGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostAdminState"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostApplications"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostMacAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostCircuitIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostRemoteIdFmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostRemoteId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostUseGiAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostIdStringOptNum"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostSubscriberId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostSlaProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostSubProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostAppProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostAncpString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostInterDestId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostUseClientPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostAuthPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostRetailerSvcId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostCategoryMapName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostDefMsapPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostDefMsapService"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostDefMsapGroupIf"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostSystemId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostServiceId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostIpv6Addr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostIpv6Pfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostIpv6PfxLen"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostAuthDomainName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostDhcpOption60Fmt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostDhcpOption60"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostDhcpRelayAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostDhcpRelayAddress"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppUserNameFormat"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppUserName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppPasswordType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppPassword"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppServiceName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppL2tpTunnelGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppL2tpSvcId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppService"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppInterface"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostPppoePadoDelay"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbHostGroup.setStatus("current")

tmnxLocalUserDbPppoeV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 21)
)
tmnxLocalUserDbPppoeV9v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePrefixLength"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeFltrProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUnSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAuthSapId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIngIpv4FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeEgrIpv4FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIngIpv6FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeEgrIpv6FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseGiAddrScope"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbPppoeV9v0Group.setStatus("current")

tmnxLocalUserDbDhcpV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 22)
)
tmnxLocalUserDbDhcpV9v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6WanAddrPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6DelPfxPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpFltrProfString"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIngIpv4FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpEgrIpv4FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIngIpv6FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpEgrIpv6FltrId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUseGiAddrScope"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbDhcpV9v0Group.setStatus("current")

tmnxLocalUserDbFltrProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 23)
)
tmnxLocalUserDbFltrProfGroup.setObjects(
    ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbHostFltrProfString")
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbFltrProfGroup.setStatus("current")

tmnxLudbPppHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 24)
)
tmnxLudbPppHostGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAleTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAleRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAleLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAleEncapOffsetMode"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAleEncapOffset"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAleRateDown"))
)
if mibBuilder.loadTexts:
    tmnxLudbPppHostGroup.setStatus("current")

tmnxLudbRadproxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 25)
)
tmnxLudbRadproxGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheTableLastCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheLastCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheService"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheServer"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheMatchType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheMatchOption"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheMacFormat"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheFailAction"))
)
if mibBuilder.loadTexts:
    tmnxLudbRadproxGroup.setStatus("current")

tmnxLocalUserDbDhcpV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 26)
)
tmnxLocalUserDbDhcpV11v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpSecPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpUseCPDelimiter"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeSecPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoePreAuthPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeUseCPDelimiter"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpEncTagRangeType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpEncTagRangeStrt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpEncTagRangeEnd"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeEncTagRangeType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeEncTagRangeStrt"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeEncTagRangeEnd"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMsapGroupIfPfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpMsapGroupIfSfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMsapGroupIfPfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeMsapGroupIfSfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeAcctPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeDuplAcctPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6ReqDelPfxLn"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpAcctPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpDuplAcctPolicy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption6TblLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption6RowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption6LstChngTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption6Type"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpOption6Value"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6SlaacPfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6SlaacPfxLen"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6Addr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6DelPfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6DelPfxLen"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6ReqDelPfxLn"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6SlaacPfx"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6SlaacPfxLen"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeForceIpv6cp"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6DelPfxPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6WanAddrPool"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppOption6TblLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppOption6RowSts"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppOption6LstChgTm"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppOption6Type"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppOption6Value"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbDhcpV11v0Group.setStatus("current")

tmnxLudbPppAliGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 27)
)
tmnxLudbPppAliGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliTableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliLastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliCircuitIdType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliCircuitId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliRemoteIdType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliRemoteId"))
)
if mibBuilder.loadTexts:
    tmnxLudbPppAliGroup.setStatus("current")

tmnxLudbNotifyObjsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 28)
)
tmnxLudbNotifyObjsV11v0Group.setObjects(
    ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxLudbNotifyObjsV11v0Group.setStatus("current")

tmnxLocalUserDbDhcpV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 29)
)
tmnxLocalUserDbDhcpV12v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpDerivedId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2WppPortalSvcId"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2WppPortalName"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2WppSubProfile"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2WppSLAProfile"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2WppAppProfile"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2WppRestDiscon"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2TableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2LastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2GiAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2GiAddr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2LinkAddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2LinkAddr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2Server6AddrType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2Server6Addr"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2Ipv6LeaseRenew"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2Ipv6LeaseRebind"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2Ipv6LeaseValidLife"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2Ipv6LeasePrefLife"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPpp2TableLastChange"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPpp2LastChangeTime"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPpp2Ipv6LeaseRenew"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPpp2Ipv6LeaseRebind"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPpp2Ipv6LeaseValidLife"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPpp2Ipv6LeasePrefLife"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpIpv6SlaacPfxPl"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcp2DiamAppPlcy"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPpp2DiamAppPlcy"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbDhcpV12v0Group.setStatus("current")

tmnxLudbRadproxV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 30)
)
tmnxLudbRadproxV12v0Group.setObjects(
    ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxCacheMatchOption6")
)
if mibBuilder.loadTexts:
    tmnxLudbRadproxV12v0Group.setStatus("current")

tmnxLocalUserDbPppoeV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 31)
)
tmnxLocalUserDbPppoeV12v0Group.setObjects(
    ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeIpv6SlaacPfxPl")
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbPppoeV12v0Group.setStatus("current")

tmnxLudbToClntOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 2, 32)
)
tmnxLudbToClntOptGroup.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptTableLstCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptRowStatus"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptLastCh"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptType"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptValue"))
)
if mibBuilder.loadTexts:
    tmnxLudbToClntOptGroup.setStatus("current")


# Notification objects

tmnxLudbDhcpGroupIfTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 51, 0, 1)
)
tmnxLudbDhcpGroupIfTooLong.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbDhcpDefMsapGroupIf"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxLudbDhcpGroupIfTooLong.setStatus(
        "current"
    )

tmnxLudbPppoeGroupIfTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 51, 0, 2)
)
tmnxLudbPppoeGroupIfTooLong.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocUsrDbPppoeDefMsapGroupIf"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxLudbPppoeGroupIfTooLong.setStatus(
        "current"
    )


# Notifications groups

tmnxLudbNotifV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 3, 1)
)
tmnxLudbNotifV11v0Group.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbDhcpGroupIfTooLong"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppoeGroupIfTooLong"))
)
if mibBuilder.loadTexts:
    tmnxLudbNotifV11v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLocalUserDbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 1)
)
tmnxLocalUserDbCompliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsGroup"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbCompliance.setStatus(
        "obsolete"
    )

tmnxLocalUserDbV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 2)
)
tmnxLocalUserDbV6v1Compliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV6v1Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsGroup"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxLocalUserDbV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 3)
)
tmnxLocalUserDbV7v0Compliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbObsoleteGroup"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxLocalUserDbV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 4)
)
tmnxLocalUserDbV8v0Compliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbRadiusFllbckGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbObsoleteGroup"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV8v0Compliance.setStatus(
        "current"
    )

tmnxLocalUserDbV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 5)
)
tmnxLocalUserDbV9v0Compliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbHostGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbRadiusFllbckGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbObsoleteGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbFltrProfGroup"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxLocalUserDbV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 6)
)
tmnxLocalUserDbV10v0Compliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbHostGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbRadiusFllbckGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbObsoleteGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbFltrProfGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppHostGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxGroup"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxLocalUserDbV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 7)
)
tmnxLocalUserDbV11v0Compliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV11v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbHostGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbRadiusFllbckGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbObsoleteGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbFltrProfGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppHostGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbNotifV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxLocalUserDbV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 51, 1, 8)
)
tmnxLocalUserDbV12v0Compliance.setObjects(
      *(("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbV7v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV9v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV11v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbDhcpV12v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbHostGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbToolsV8v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbRadiusFllbckGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbObsoleteGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbFltrProfGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppHostGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbPppAliGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxGroup"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbNotifV11v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbRadproxV12v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLocalUserDbPppoeV12v0Group"),
        ("TIMETRA-LOCAL-USER-DB-MIB", "tmnxLudbToClntOptGroup"))
)
if mibBuilder.loadTexts:
    tmnxLocalUserDbV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LOCAL-USER-DB-MIB",
    **{"TmnxLocUsrDbUserNameFormat": TmnxLocUsrDbUserNameFormat,
       "TmnxLocUsrDbPasswordType": TmnxLocUsrDbPasswordType,
       "TmnxLocUsrDbMatchTypePppoe": TmnxLocUsrDbMatchTypePppoe,
       "TmnxLocUsrDbMatchTypeDhcp": TmnxLocUsrDbMatchTypeDhcp,
       "TmnxLocUsrDbHostType": TmnxLocUsrDbHostType,
       "TmnxLocUsrDbHostApplications": TmnxLocUsrDbHostApplications,
       "TmnxLocUsrDbUnmatchedReason": TmnxLocUsrDbUnmatchedReason,
       "TmnxLocUsrDbDataFormat": TmnxLocUsrDbDataFormat,
       "TmnxLocUsrDbMaskString": TmnxLocUsrDbMaskString,
       "TmnxLudbDataFormat": TmnxLudbDataFormat,
       "TmnxLudbMsapGrpIfPfxSfxType": TmnxLudbMsapGrpIfPfxSfxType,
       "timetraLocalUserDbMIBModule": timetraLocalUserDbMIBModule,
       "tmnxLocalUserDbConformance": tmnxLocalUserDbConformance,
       "tmnxLocalUserDbCompliances": tmnxLocalUserDbCompliances,
       "tmnxLocalUserDbCompliance": tmnxLocalUserDbCompliance,
       "tmnxLocalUserDbV6v1Compliance": tmnxLocalUserDbV6v1Compliance,
       "tmnxLocalUserDbV7v0Compliance": tmnxLocalUserDbV7v0Compliance,
       "tmnxLocalUserDbV8v0Compliance": tmnxLocalUserDbV8v0Compliance,
       "tmnxLocalUserDbV9v0Compliance": tmnxLocalUserDbV9v0Compliance,
       "tmnxLocalUserDbV10v0Compliance": tmnxLocalUserDbV10v0Compliance,
       "tmnxLocalUserDbV11v0Compliance": tmnxLocalUserDbV11v0Compliance,
       "tmnxLocalUserDbV12v0Compliance": tmnxLocalUserDbV12v0Compliance,
       "tmnxLocalUserDbGroups": tmnxLocalUserDbGroups,
       "tmnxLocalUserDbGroup": tmnxLocalUserDbGroup,
       "tmnxLocalUserDbPppoeGroup": tmnxLocalUserDbPppoeGroup,
       "tmnxLocalUserDbDhcpGroup": tmnxLocalUserDbDhcpGroup,
       "tmnxLocalUserDbToolsGroup": tmnxLocalUserDbToolsGroup,
       "tmnxLocalUserDbPppoeV6v1Group": tmnxLocalUserDbPppoeV6v1Group,
       "tmnxLocalUserDbPppoeV7v0Group": tmnxLocalUserDbPppoeV7v0Group,
       "tmnxLocalUserDbDhcpV7v0Group": tmnxLocalUserDbDhcpV7v0Group,
       "tmnxLocalUserDbV7v0Group": tmnxLocalUserDbV7v0Group,
       "tmnxLocalUserDbObsoleteGroup": tmnxLocalUserDbObsoleteGroup,
       "tmnxLocalUserDbToolsV7v0Group": tmnxLocalUserDbToolsV7v0Group,
       "tmnxLocalUserDbRadiusFllbckGroup": tmnxLocalUserDbRadiusFllbckGroup,
       "tmnxLocalUserDbDhcpV8v0Group": tmnxLocalUserDbDhcpV8v0Group,
       "tmnxLocalUserDbPppoeV8v0Group": tmnxLocalUserDbPppoeV8v0Group,
       "tmnxLocalUserDbToolsV8v0Group": tmnxLocalUserDbToolsV8v0Group,
       "tmnxLocalUserDbHostGroup": tmnxLocalUserDbHostGroup,
       "tmnxLocalUserDbPppoeV9v0Group": tmnxLocalUserDbPppoeV9v0Group,
       "tmnxLocalUserDbDhcpV9v0Group": tmnxLocalUserDbDhcpV9v0Group,
       "tmnxLocalUserDbFltrProfGroup": tmnxLocalUserDbFltrProfGroup,
       "tmnxLudbPppHostGroup": tmnxLudbPppHostGroup,
       "tmnxLudbRadproxGroup": tmnxLudbRadproxGroup,
       "tmnxLocalUserDbDhcpV11v0Group": tmnxLocalUserDbDhcpV11v0Group,
       "tmnxLudbPppAliGroup": tmnxLudbPppAliGroup,
       "tmnxLudbNotifyObjsV11v0Group": tmnxLudbNotifyObjsV11v0Group,
       "tmnxLocalUserDbDhcpV12v0Group": tmnxLocalUserDbDhcpV12v0Group,
       "tmnxLudbRadproxV12v0Group": tmnxLudbRadproxV12v0Group,
       "tmnxLocalUserDbPppoeV12v0Group": tmnxLocalUserDbPppoeV12v0Group,
       "tmnxLudbToClntOptGroup": tmnxLudbToClntOptGroup,
       "tmnxLocalUserDbNotifGroups": tmnxLocalUserDbNotifGroups,
       "tmnxLudbNotifV11v0Group": tmnxLudbNotifV11v0Group,
       "tmnxLocalUserDb": tmnxLocalUserDb,
       "tmnxLocalUserDbObjs": tmnxLocalUserDbObjs,
       "tmnxLocalUserDbTableLastChange": tmnxLocalUserDbTableLastChange,
       "tmnxLocalUserDbTable": tmnxLocalUserDbTable,
       "tmnxLocalUserDbEntry": tmnxLocalUserDbEntry,
       "tmnxLocUsrDbUserDatabaseName": tmnxLocUsrDbUserDatabaseName,
       "tmnxLocUsrDbRowStatus": tmnxLocUsrDbRowStatus,
       "tmnxLocUsrDbLastChangeTime": tmnxLocUsrDbLastChangeTime,
       "tmnxLocUsrDbAdminState": tmnxLocUsrDbAdminState,
       "tmnxLocUsrDbDescription": tmnxLocUsrDbDescription,
       "tmnxLocUsrDbMatchTypeDhcp1": tmnxLocUsrDbMatchTypeDhcp1,
       "tmnxLocUsrDbMatchTypeDhcp2": tmnxLocUsrDbMatchTypeDhcp2,
       "tmnxLocUsrDbMatchTypeDhcp3": tmnxLocUsrDbMatchTypeDhcp3,
       "tmnxLocUsrDbMatchTypeDhcp4": tmnxLocUsrDbMatchTypeDhcp4,
       "tmnxLocUsrDbMatchTypePppoe1": tmnxLocUsrDbMatchTypePppoe1,
       "tmnxLocUsrDbMatchTypePppoe2": tmnxLocUsrDbMatchTypePppoe2,
       "tmnxLocUsrDbMatchTypePppoe3": tmnxLocUsrDbMatchTypePppoe3,
       "tmnxLocUsrDbPppoeCIdMaskPreStr": tmnxLocUsrDbPppoeCIdMaskPreStr,
       "tmnxLocUsrDbPppoeCIdMaskPreNum": tmnxLocUsrDbPppoeCIdMaskPreNum,
       "tmnxLocUsrDbPppoeCIdMaskSufStr": tmnxLocUsrDbPppoeCIdMaskSufStr,
       "tmnxLocUsrDbPppoeCIdMaskSufNum": tmnxLocUsrDbPppoeCIdMaskSufNum,
       "tmnxLocUsrDbDhcpCIdMaskPreStr": tmnxLocUsrDbDhcpCIdMaskPreStr,
       "tmnxLocUsrDbDhcpCIdMaskPreNum": tmnxLocUsrDbDhcpCIdMaskPreNum,
       "tmnxLocUsrDbDhcpCIdMaskSufStr": tmnxLocUsrDbDhcpCIdMaskSufStr,
       "tmnxLocUsrDbDhcpCIdMaskSufNum": tmnxLocUsrDbDhcpCIdMaskSufNum,
       "tmnxLocUsrDbHostCount": tmnxLocUsrDbHostCount,
       "tmnxLocUsrDbPppoeTableLastChange": tmnxLocUsrDbPppoeTableLastChange,
       "tmnxLocUsrDbPppoeTable": tmnxLocUsrDbPppoeTable,
       "tmnxLocUsrDbPppoeEntry": tmnxLocUsrDbPppoeEntry,
       "tmnxLocUsrDbPppoeHostName": tmnxLocUsrDbPppoeHostName,
       "tmnxLocUsrDbPppoeRowStatus": tmnxLocUsrDbPppoeRowStatus,
       "tmnxLocUsrDbPppoeLastChangeTime": tmnxLocUsrDbPppoeLastChangeTime,
       "tmnxLocUsrDbPppoeAdminState": tmnxLocUsrDbPppoeAdminState,
       "tmnxLocUsrDbPppoeMacAddress": tmnxLocUsrDbPppoeMacAddress,
       "tmnxLocUsrDbPppoeCircuitIdFmt": tmnxLocUsrDbPppoeCircuitIdFmt,
       "tmnxLocUsrDbPppoeCircuitId": tmnxLocUsrDbPppoeCircuitId,
       "tmnxLocUsrDbPppoeRemoteId": tmnxLocUsrDbPppoeRemoteId,
       "tmnxLocUsrDbPppoeUserNameFormat": tmnxLocUsrDbPppoeUserNameFormat,
       "tmnxLocUsrDbPppoeUserName": tmnxLocUsrDbPppoeUserName,
       "tmnxLocUsrDbPppoePasswordType": tmnxLocUsrDbPppoePasswordType,
       "tmnxLocUsrDbPppoePassword": tmnxLocUsrDbPppoePassword,
       "tmnxLocUsrDbPppoeAddrType": tmnxLocUsrDbPppoeAddrType,
       "tmnxLocUsrDbPppoeAddress": tmnxLocUsrDbPppoeAddress,
       "tmnxLocUsrDbPppoePool": tmnxLocUsrDbPppoePool,
       "tmnxLocUsrDbPppoeUseGiAddress": tmnxLocUsrDbPppoeUseGiAddress,
       "tmnxLocUsrDbPppoeIdStringOptNum": tmnxLocUsrDbPppoeIdStringOptNum,
       "tmnxLocUsrDbPppoeSubscriberId": tmnxLocUsrDbPppoeSubscriberId,
       "tmnxLocUsrDbPppoeSlaProfString": tmnxLocUsrDbPppoeSlaProfString,
       "tmnxLocUsrDbPppoeSubProfString": tmnxLocUsrDbPppoeSubProfString,
       "tmnxLocUsrDbPppoeAppProfString": tmnxLocUsrDbPppoeAppProfString,
       "tmnxLocUsrDbPppoeAncpString": tmnxLocUsrDbPppoeAncpString,
       "tmnxLocUsrDbPppoeInterDestId": tmnxLocUsrDbPppoeInterDestId,
       "tmnxLocUsrDbPppoeUseClientPool": tmnxLocUsrDbPppoeUseClientPool,
       "tmnxLocUsrDbPppoePadoDelay": tmnxLocUsrDbPppoePadoDelay,
       "tmnxLocUsrDbPppoeServiceName": tmnxLocUsrDbPppoeServiceName,
       "tmnxLocUsrDbPppoeL2tpTunnelGroup": tmnxLocUsrDbPppoeL2tpTunnelGroup,
       "tmnxLocUsrDbPppoeAuthPolicy": tmnxLocUsrDbPppoeAuthPolicy,
       "tmnxLocUsrDbPppoeRetailerSvcId": tmnxLocUsrDbPppoeRetailerSvcId,
       "tmnxLocUsrDbPppoeCategoryMapName": tmnxLocUsrDbPppoeCategoryMapName,
       "tmnxLocUsrDbPppoeDefMsapPolicy": tmnxLocUsrDbPppoeDefMsapPolicy,
       "tmnxLocUsrDbPppoeDefMsapService": tmnxLocUsrDbPppoeDefMsapService,
       "tmnxLocUsrDbPppoeDefMsapGroupIf": tmnxLocUsrDbPppoeDefMsapGroupIf,
       "tmnxLocUsrDbPppoeRemoteIdFmt": tmnxLocUsrDbPppoeRemoteIdFmt,
       "tmnxLocUsrDbPppoeL2tpSvcId": tmnxLocUsrDbPppoeL2tpSvcId,
       "tmnxLocUsrDbPppoeService": tmnxLocUsrDbPppoeService,
       "tmnxLocUsrDbPppoeInterface": tmnxLocUsrDbPppoeInterface,
       "tmnxLocUsrDbPppoePrefixLength": tmnxLocUsrDbPppoePrefixLength,
       "tmnxLocUsrDbPppoeFltrProfString": tmnxLocUsrDbPppoeFltrProfString,
       "tmnxLocUsrDbPppoeSapId": tmnxLocUsrDbPppoeSapId,
       "tmnxLocUsrDbPppoeIngIpv4FltrId": tmnxLocUsrDbPppoeIngIpv4FltrId,
       "tmnxLocUsrDbPppoeEgrIpv4FltrId": tmnxLocUsrDbPppoeEgrIpv4FltrId,
       "tmnxLocUsrDbPppoeIngIpv6FltrId": tmnxLocUsrDbPppoeIngIpv6FltrId,
       "tmnxLocUsrDbPppoeEgrIpv6FltrId": tmnxLocUsrDbPppoeEgrIpv6FltrId,
       "tmnxLocUsrDbPppoeUseGiAddrScope": tmnxLocUsrDbPppoeUseGiAddrScope,
       "tmnxLocUsrDbPppoeSecPool": tmnxLocUsrDbPppoeSecPool,
       "tmnxLocUsrDbPppoePreAuthPolicy": tmnxLocUsrDbPppoePreAuthPolicy,
       "tmnxLocUsrDbPppoeUseCPDelimiter": tmnxLocUsrDbPppoeUseCPDelimiter,
       "tmnxLocUsrDbPppoeEncTagRangeType": tmnxLocUsrDbPppoeEncTagRangeType,
       "tmnxLocUsrDbPppoeEncTagRangeStrt": tmnxLocUsrDbPppoeEncTagRangeStrt,
       "tmnxLocUsrDbPppoeEncTagRangeEnd": tmnxLocUsrDbPppoeEncTagRangeEnd,
       "tmnxLocUsrDbPppoeMsapGroupIfPfx": tmnxLocUsrDbPppoeMsapGroupIfPfx,
       "tmnxLocUsrDbPppoeMsapGroupIfSfx": tmnxLocUsrDbPppoeMsapGroupIfSfx,
       "tmnxLocUsrDbPppoeAcctPolicy": tmnxLocUsrDbPppoeAcctPolicy,
       "tmnxLocUsrDbPppoeDuplAcctPolicy": tmnxLocUsrDbPppoeDuplAcctPolicy,
       "tmnxLocUsrDbPppoeIpv6Addr": tmnxLocUsrDbPppoeIpv6Addr,
       "tmnxLocUsrDbPppoeIpv6DelPfx": tmnxLocUsrDbPppoeIpv6DelPfx,
       "tmnxLocUsrDbPppoeIpv6DelPfxLen": tmnxLocUsrDbPppoeIpv6DelPfxLen,
       "tmnxLocUsrDbPppoeIpv6ReqDelPfxLn": tmnxLocUsrDbPppoeIpv6ReqDelPfxLn,
       "tmnxLocUsrDbPppoeIpv6SlaacPfx": tmnxLocUsrDbPppoeIpv6SlaacPfx,
       "tmnxLocUsrDbPppoeIpv6SlaacPfxLen": tmnxLocUsrDbPppoeIpv6SlaacPfxLen,
       "tmnxLocUsrDbPppoeForceIpv6cp": tmnxLocUsrDbPppoeForceIpv6cp,
       "tmnxLocUsrDbPppoeIpv6DelPfxPool": tmnxLocUsrDbPppoeIpv6DelPfxPool,
       "tmnxLocUsrDbPppoeIpv6WanAddrPool": tmnxLocUsrDbPppoeIpv6WanAddrPool,
       "tmnxLocUsrDbPppoeIpv6SlaacPfxPl": tmnxLocUsrDbPppoeIpv6SlaacPfxPl,
       "tmnxLocUsrDbPppoeUnmatchedTable": tmnxLocUsrDbPppoeUnmatchedTable,
       "tmnxLocUsrDbPppoeUnmatchedEntry": tmnxLocUsrDbPppoeUnmatchedEntry,
       "tmnxLocUsrDbPppoeUnMacAddress": tmnxLocUsrDbPppoeUnMacAddress,
       "tmnxLocUsrDbPppoeUnCircuitId": tmnxLocUsrDbPppoeUnCircuitId,
       "tmnxLocUsrDbPppoeUnRemoteId": tmnxLocUsrDbPppoeUnRemoteId,
       "tmnxLocUsrDbPppoeUnUserNameFmt": tmnxLocUsrDbPppoeUnUserNameFmt,
       "tmnxLocUsrDbPppoeUnUserName": tmnxLocUsrDbPppoeUnUserName,
       "tmnxLocUsrDbPppoeUnmatchedReason": tmnxLocUsrDbPppoeUnmatchedReason,
       "tmnxLocUsrDbPppoeUnDuplicateHost": tmnxLocUsrDbPppoeUnDuplicateHost,
       "tmnxLocUsrDbPppoeUnServiceName": tmnxLocUsrDbPppoeUnServiceName,
       "tmnxLocUsrDbPppoeUnSapId": tmnxLocUsrDbPppoeUnSapId,
       "tmnxLocUsrDbPppoeOptionTbleLstCh": tmnxLocUsrDbPppoeOptionTbleLstCh,
       "tmnxLocUsrDbPppoeOptionTable": tmnxLocUsrDbPppoeOptionTable,
       "tmnxLocUsrDbPppoeOptionEntry": tmnxLocUsrDbPppoeOptionEntry,
       "tmnxLocUsrDbPppoeOptionNumber": tmnxLocUsrDbPppoeOptionNumber,
       "tmnxLocUsrDbPppoeOptionRowStatus": tmnxLocUsrDbPppoeOptionRowStatus,
       "tmnxLocUsrDbPppoeOptionLstChngTm": tmnxLocUsrDbPppoeOptionLstChngTm,
       "tmnxLocUsrDbPppoeOptionType": tmnxLocUsrDbPppoeOptionType,
       "tmnxLocUsrDbPppoeOptionValue": tmnxLocUsrDbPppoeOptionValue,
       "tmnxLocUsrDbDhcpTableLastChange": tmnxLocUsrDbDhcpTableLastChange,
       "tmnxLocUsrDbDhcpTable": tmnxLocUsrDbDhcpTable,
       "tmnxLocUsrDbDhcpEntry": tmnxLocUsrDbDhcpEntry,
       "tmnxLocUsrDbDhcpHostName": tmnxLocUsrDbDhcpHostName,
       "tmnxLocUsrDbDhcpRowStatus": tmnxLocUsrDbDhcpRowStatus,
       "tmnxLocUsrDbDhcpLastChangeTime": tmnxLocUsrDbDhcpLastChangeTime,
       "tmnxLocUsrDbDhcpAdminState": tmnxLocUsrDbDhcpAdminState,
       "tmnxLocUsrDbDhcpMacAddress": tmnxLocUsrDbDhcpMacAddress,
       "tmnxLocUsrDbDhcpCircuitIdFmt": tmnxLocUsrDbDhcpCircuitIdFmt,
       "tmnxLocUsrDbDhcpCircuitId": tmnxLocUsrDbDhcpCircuitId,
       "tmnxLocUsrDbDhcpRemoteId": tmnxLocUsrDbDhcpRemoteId,
       "tmnxLocUsrDbDhcpSystemId": tmnxLocUsrDbDhcpSystemId,
       "tmnxLocUsrDbDhcpServiceId": tmnxLocUsrDbDhcpServiceId,
       "tmnxLocUsrDbDhcpSapId": tmnxLocUsrDbDhcpSapId,
       "tmnxLocUsrDbDhcpString": tmnxLocUsrDbDhcpString,
       "tmnxLocUsrDbDhcpOption60": tmnxLocUsrDbDhcpOption60,
       "tmnxLocUsrDbDhcpAddrType": tmnxLocUsrDbDhcpAddrType,
       "tmnxLocUsrDbDhcpAddress": tmnxLocUsrDbDhcpAddress,
       "tmnxLocUsrDbDhcpPool": tmnxLocUsrDbDhcpPool,
       "tmnxLocUsrDbDhcpUseGiAddress": tmnxLocUsrDbDhcpUseGiAddress,
       "tmnxLocUsrDbDhcpIdStringOptNum": tmnxLocUsrDbDhcpIdStringOptNum,
       "tmnxLocUsrDbDhcpSubscriberId": tmnxLocUsrDbDhcpSubscriberId,
       "tmnxLocUsrDbDhcpSlaProfString": tmnxLocUsrDbDhcpSlaProfString,
       "tmnxLocUsrDbDhcpSubProfString": tmnxLocUsrDbDhcpSubProfString,
       "tmnxLocUsrDbDhcpAppProfString": tmnxLocUsrDbDhcpAppProfString,
       "tmnxLocUsrDbDhcpAncpString": tmnxLocUsrDbDhcpAncpString,
       "tmnxLocUsrDbDhcpInterDestId": tmnxLocUsrDbDhcpInterDestId,
       "tmnxLocUsrDbDhcpAuthPolicy": tmnxLocUsrDbDhcpAuthPolicy,
       "tmnxLocUsrDbDhcpServerAddrType": tmnxLocUsrDbDhcpServerAddrType,
       "tmnxLocUsrDbDhcpServerAddress": tmnxLocUsrDbDhcpServerAddress,
       "tmnxLocUsrDbDhcpAuthDomainName": tmnxLocUsrDbDhcpAuthDomainName,
       "tmnxLocUsrDbDhcpCategoryMapName": tmnxLocUsrDbDhcpCategoryMapName,
       "tmnxLocUsrDbDhcpOption60Fmt": tmnxLocUsrDbDhcpOption60Fmt,
       "tmnxLocUsrDbDhcpUseClientPool": tmnxLocUsrDbDhcpUseClientPool,
       "tmnxLocUsrDbDhcpDefMsapPolicy": tmnxLocUsrDbDhcpDefMsapPolicy,
       "tmnxLocUsrDbDhcpDefMsapService": tmnxLocUsrDbDhcpDefMsapService,
       "tmnxLocUsrDbDhcpDefMsapGroupIf": tmnxLocUsrDbDhcpDefMsapGroupIf,
       "tmnxLocUsrDbDhcpRetailerSvcId": tmnxLocUsrDbDhcpRetailerSvcId,
       "tmnxLocUsrDbDhcpRemoteIdFmt": tmnxLocUsrDbDhcpRemoteIdFmt,
       "tmnxLocUsrDbDhcpIpv6Addr": tmnxLocUsrDbDhcpIpv6Addr,
       "tmnxLocUsrDbDhcpIpv6Pfx": tmnxLocUsrDbDhcpIpv6Pfx,
       "tmnxLocUsrDbDhcpIpv6PfxLen": tmnxLocUsrDbDhcpIpv6PfxLen,
       "tmnxLocUsrDbDhcpIpv6WanAddrPool": tmnxLocUsrDbDhcpIpv6WanAddrPool,
       "tmnxLocUsrDbDhcpIpv6DelPfxPool": tmnxLocUsrDbDhcpIpv6DelPfxPool,
       "tmnxLocUsrDbDhcpFltrProfString": tmnxLocUsrDbDhcpFltrProfString,
       "tmnxLocUsrDbDhcpIngIpv4FltrId": tmnxLocUsrDbDhcpIngIpv4FltrId,
       "tmnxLocUsrDbDhcpEgrIpv4FltrId": tmnxLocUsrDbDhcpEgrIpv4FltrId,
       "tmnxLocUsrDbDhcpIngIpv6FltrId": tmnxLocUsrDbDhcpIngIpv6FltrId,
       "tmnxLocUsrDbDhcpEgrIpv6FltrId": tmnxLocUsrDbDhcpEgrIpv6FltrId,
       "tmnxLocUsrDbDhcpUseGiAddrScope": tmnxLocUsrDbDhcpUseGiAddrScope,
       "tmnxLocUsrDbDhcpSecPool": tmnxLocUsrDbDhcpSecPool,
       "tmnxLocUsrDbDhcpUseCPDelimiter": tmnxLocUsrDbDhcpUseCPDelimiter,
       "tmnxLocUsrDbDhcpEncTagRangeType": tmnxLocUsrDbDhcpEncTagRangeType,
       "tmnxLocUsrDbDhcpEncTagRangeStrt": tmnxLocUsrDbDhcpEncTagRangeStrt,
       "tmnxLocUsrDbDhcpEncTagRangeEnd": tmnxLocUsrDbDhcpEncTagRangeEnd,
       "tmnxLocUsrDbDhcpMsapGroupIfPfx": tmnxLocUsrDbDhcpMsapGroupIfPfx,
       "tmnxLocUsrDbDhcpMsapGroupIfSfx": tmnxLocUsrDbDhcpMsapGroupIfSfx,
       "tmnxLocUsrDbDhcpIpv6ReqDelPfxLn": tmnxLocUsrDbDhcpIpv6ReqDelPfxLn,
       "tmnxLocUsrDbDhcpAcctPolicy": tmnxLocUsrDbDhcpAcctPolicy,
       "tmnxLocUsrDbDhcpDuplAcctPolicy": tmnxLocUsrDbDhcpDuplAcctPolicy,
       "tmnxLocUsrDbDhcpIpv6SlaacPfx": tmnxLocUsrDbDhcpIpv6SlaacPfx,
       "tmnxLocUsrDbDhcpIpv6SlaacPfxLen": tmnxLocUsrDbDhcpIpv6SlaacPfxLen,
       "tmnxLocUsrDbDhcpDerivedId": tmnxLocUsrDbDhcpDerivedId,
       "tmnxLocUsrDbDhcpIpv6SlaacPfxPl": tmnxLocUsrDbDhcpIpv6SlaacPfxPl,
       "tmnxLocUsrDbDhcpUnmatchedTable": tmnxLocUsrDbDhcpUnmatchedTable,
       "tmnxLocUsrDbDhcpUnmatchedEntry": tmnxLocUsrDbDhcpUnmatchedEntry,
       "tmnxLocUsrDbDhcpUnMacAddress": tmnxLocUsrDbDhcpUnMacAddress,
       "tmnxLocUsrDbDhcpUnCircuitId": tmnxLocUsrDbDhcpUnCircuitId,
       "tmnxLocUsrDbDhcpUnRemoteId": tmnxLocUsrDbDhcpUnRemoteId,
       "tmnxLocUsrDbDhcpUnSystemId": tmnxLocUsrDbDhcpUnSystemId,
       "tmnxLocUsrDbDhcpUnServiceId": tmnxLocUsrDbDhcpUnServiceId,
       "tmnxLocUsrDbDhcpUnSapId": tmnxLocUsrDbDhcpUnSapId,
       "tmnxLocUsrDbDhcpUnString": tmnxLocUsrDbDhcpUnString,
       "tmnxLocUsrDbDhcpUnOption60": tmnxLocUsrDbDhcpUnOption60,
       "tmnxLocUsrDbDhcpUnmatchedReason": tmnxLocUsrDbDhcpUnmatchedReason,
       "tmnxLocUsrDbDhcpUnDuplicateHost": tmnxLocUsrDbDhcpUnDuplicateHost,
       "tmnxLocUsrDbDhcpOptionTableLstCh": tmnxLocUsrDbDhcpOptionTableLstCh,
       "tmnxLocUsrDbDhcpOptionTable": tmnxLocUsrDbDhcpOptionTable,
       "tmnxLocUsrDbDhcpOptionEntry": tmnxLocUsrDbDhcpOptionEntry,
       "tmnxLocUsrDbDhcpOptionNumber": tmnxLocUsrDbDhcpOptionNumber,
       "tmnxLocUsrDbDhcpOptionRowStatus": tmnxLocUsrDbDhcpOptionRowStatus,
       "tmnxLocUsrDbDhcpOptionLastChngTm": tmnxLocUsrDbDhcpOptionLastChngTm,
       "tmnxLocUsrDbDhcpOptionType": tmnxLocUsrDbDhcpOptionType,
       "tmnxLocUsrDbDhcpOptionValue": tmnxLocUsrDbDhcpOptionValue,
       "tmnxLocUsrDbPppoeAuthTool": tmnxLocUsrDbPppoeAuthTool,
       "tmnxLocUsrDbPppoeAuthDbName": tmnxLocUsrDbPppoeAuthDbName,
       "tmnxLocUsrDbPppoeAuthUsrName": tmnxLocUsrDbPppoeAuthUsrName,
       "tmnxLocUsrDbPppoeAuthPwd": tmnxLocUsrDbPppoeAuthPwd,
       "tmnxLocUsrDbPppoeAuthenticate": tmnxLocUsrDbPppoeAuthenticate,
       "tmnxLocUsrDbPppoeAuthSuccessful": tmnxLocUsrDbPppoeAuthSuccessful,
       "tmnxLocUsrDbPppoeAuthErrorMsg": tmnxLocUsrDbPppoeAuthErrorMsg,
       "tmnxLocUsrDbPppoeAuthTime": tmnxLocUsrDbPppoeAuthTime,
       "tmnxLocUsrDbPppoeAuthHostName": tmnxLocUsrDbPppoeAuthHostName,
       "tmnxLocUsrDbPppoeAuthMacAddress": tmnxLocUsrDbPppoeAuthMacAddress,
       "tmnxLocUsrDbPppoeAuthRemoteId": tmnxLocUsrDbPppoeAuthRemoteId,
       "tmnxLocUsrDbPppoeAuthCircuitIdFmt": tmnxLocUsrDbPppoeAuthCircuitIdFmt,
       "tmnxLocUsrDbPppoeAuthCircuitId": tmnxLocUsrDbPppoeAuthCircuitId,
       "tmnxLocUsrDbPppoeAuthServiceName": tmnxLocUsrDbPppoeAuthServiceName,
       "tmnxLocUsrDbPppoeAuthRemoteIdFmt": tmnxLocUsrDbPppoeAuthRemoteIdFmt,
       "tmnxLocUsrDbPppoeAuthSapId": tmnxLocUsrDbPppoeAuthSapId,
       "tmnxLocUsrDbDhcpMaskTableLstCh": tmnxLocUsrDbDhcpMaskTableLstCh,
       "tmnxLocUsrDbDhcpMaskTable": tmnxLocUsrDbDhcpMaskTable,
       "tmnxLocUsrDbDhcpMaskEntry": tmnxLocUsrDbDhcpMaskEntry,
       "tmnxLocUsrDbDhcpMaskMatchType": tmnxLocUsrDbDhcpMaskMatchType,
       "tmnxLocUsrDbDhcpMaskRowStatus": tmnxLocUsrDbDhcpMaskRowStatus,
       "tmnxLocUsrDbDhcpMaskPreStr": tmnxLocUsrDbDhcpMaskPreStr,
       "tmnxLocUsrDbDhcpMaskPreNum": tmnxLocUsrDbDhcpMaskPreNum,
       "tmnxLocUsrDbDhcpMaskSufStr": tmnxLocUsrDbDhcpMaskSufStr,
       "tmnxLocUsrDbDhcpMaskSufNum": tmnxLocUsrDbDhcpMaskSufNum,
       "tmnxLocUsrDbPppoeMaskTableLstCh": tmnxLocUsrDbPppoeMaskTableLstCh,
       "tmnxLocUsrDbPppoeMaskTable": tmnxLocUsrDbPppoeMaskTable,
       "tmnxLocUsrDbPppoeMaskEntry": tmnxLocUsrDbPppoeMaskEntry,
       "tmnxLocUsrDbPppoeMaskMatchType": tmnxLocUsrDbPppoeMaskMatchType,
       "tmnxLocUsrDbPppoeMaskRowStatus": tmnxLocUsrDbPppoeMaskRowStatus,
       "tmnxLocUsrDbPppoeMaskPreStr": tmnxLocUsrDbPppoeMaskPreStr,
       "tmnxLocUsrDbPppoeMaskPreNum": tmnxLocUsrDbPppoeMaskPreNum,
       "tmnxLocUsrDbPppoeMaskSufStr": tmnxLocUsrDbPppoeMaskSufStr,
       "tmnxLocUsrDbPppoeMaskSufNum": tmnxLocUsrDbPppoeMaskSufNum,
       "tmnxLudbHostTableLastChange": tmnxLudbHostTableLastChange,
       "tmnxLudbHostTable": tmnxLudbHostTable,
       "tmnxLudbHostEntry": tmnxLudbHostEntry,
       "tmnxLudbHostType": tmnxLudbHostType,
       "tmnxLudbHostName": tmnxLudbHostName,
       "tmnxLudbHostRowStatus": tmnxLudbHostRowStatus,
       "tmnxLudbHostLastChangeTime": tmnxLudbHostLastChangeTime,
       "tmnxLudbHostApplications": tmnxLudbHostApplications,
       "tmnxLudbHostAdminState": tmnxLudbHostAdminState,
       "tmnxLudbHostMacAddress": tmnxLudbHostMacAddress,
       "tmnxLudbHostCircuitIdFmt": tmnxLudbHostCircuitIdFmt,
       "tmnxLudbHostCircuitId": tmnxLudbHostCircuitId,
       "tmnxLudbHostRemoteIdFmt": tmnxLudbHostRemoteIdFmt,
       "tmnxLudbHostRemoteId": tmnxLudbHostRemoteId,
       "tmnxLudbHostAddrType": tmnxLudbHostAddrType,
       "tmnxLudbHostAddress": tmnxLudbHostAddress,
       "tmnxLudbHostPool": tmnxLudbHostPool,
       "tmnxLudbHostUseGiAddress": tmnxLudbHostUseGiAddress,
       "tmnxLudbHostIdStringOptNum": tmnxLudbHostIdStringOptNum,
       "tmnxLudbHostSubscriberId": tmnxLudbHostSubscriberId,
       "tmnxLudbHostSlaProfString": tmnxLudbHostSlaProfString,
       "tmnxLudbHostFltrProfString": tmnxLudbHostFltrProfString,
       "tmnxLudbHostSubProfString": tmnxLudbHostSubProfString,
       "tmnxLudbHostAppProfString": tmnxLudbHostAppProfString,
       "tmnxLudbHostAncpString": tmnxLudbHostAncpString,
       "tmnxLudbHostInterDestId": tmnxLudbHostInterDestId,
       "tmnxLudbHostUseClientPool": tmnxLudbHostUseClientPool,
       "tmnxLudbHostAuthPolicy": tmnxLudbHostAuthPolicy,
       "tmnxLudbHostRetailerSvcId": tmnxLudbHostRetailerSvcId,
       "tmnxLudbHostCategoryMapName": tmnxLudbHostCategoryMapName,
       "tmnxLudbHostDefMsapPolicy": tmnxLudbHostDefMsapPolicy,
       "tmnxLudbHostDefMsapService": tmnxLudbHostDefMsapService,
       "tmnxLudbHostDefMsapGroupIf": tmnxLudbHostDefMsapGroupIf,
       "tmnxLudbHostSystemId": tmnxLudbHostSystemId,
       "tmnxLudbHostServiceId": tmnxLudbHostServiceId,
       "tmnxLudbHostSapId": tmnxLudbHostSapId,
       "tmnxLudbHostString": tmnxLudbHostString,
       "tmnxLudbHostIpv6Addr": tmnxLudbHostIpv6Addr,
       "tmnxLudbHostIpv6Pfx": tmnxLudbHostIpv6Pfx,
       "tmnxLudbHostIpv6PfxLen": tmnxLudbHostIpv6PfxLen,
       "tmnxLudbHostAuthDomainName": tmnxLudbHostAuthDomainName,
       "tmnxLudbHostDhcpOption60Fmt": tmnxLudbHostDhcpOption60Fmt,
       "tmnxLudbHostDhcpOption60": tmnxLudbHostDhcpOption60,
       "tmnxLudbHostDhcpRelayAddrType": tmnxLudbHostDhcpRelayAddrType,
       "tmnxLudbHostDhcpRelayAddress": tmnxLudbHostDhcpRelayAddress,
       "tmnxLudbHostPppUserNameFormat": tmnxLudbHostPppUserNameFormat,
       "tmnxLudbHostPppUserName": tmnxLudbHostPppUserName,
       "tmnxLudbHostPppPasswordType": tmnxLudbHostPppPasswordType,
       "tmnxLudbHostPppPassword": tmnxLudbHostPppPassword,
       "tmnxLudbHostPppServiceName": tmnxLudbHostPppServiceName,
       "tmnxLudbHostPppL2tpTunnelGroup": tmnxLudbHostPppL2tpTunnelGroup,
       "tmnxLudbHostPppL2tpSvcId": tmnxLudbHostPppL2tpSvcId,
       "tmnxLudbHostPppService": tmnxLudbHostPppService,
       "tmnxLudbHostPppInterface": tmnxLudbHostPppInterface,
       "tmnxLudbHostPppoePadoDelay": tmnxLudbHostPppoePadoDelay,
       "tmnxLudbPppAleTableLastChange": tmnxLudbPppAleTableLastChange,
       "tmnxLudbPppAleTable": tmnxLudbPppAleTable,
       "tmnxLudbPppAleEntry": tmnxLudbPppAleEntry,
       "tmnxLudbPppAleRowStatus": tmnxLudbPppAleRowStatus,
       "tmnxLudbPppAleLastChangeTime": tmnxLudbPppAleLastChangeTime,
       "tmnxLudbPppAleEncapOffsetMode": tmnxLudbPppAleEncapOffsetMode,
       "tmnxLudbPppAleEncapOffset": tmnxLudbPppAleEncapOffset,
       "tmnxLudbPppAleRateDown": tmnxLudbPppAleRateDown,
       "tmnxLudbRadproxCacheTableLastCh": tmnxLudbRadproxCacheTableLastCh,
       "tmnxLudbRadproxCacheTable": tmnxLudbRadproxCacheTable,
       "tmnxLudbRadproxCacheEntry": tmnxLudbRadproxCacheEntry,
       "tmnxLudbRadproxCacheLastCh": tmnxLudbRadproxCacheLastCh,
       "tmnxLudbRadproxCacheService": tmnxLudbRadproxCacheService,
       "tmnxLudbRadproxCacheServer": tmnxLudbRadproxCacheServer,
       "tmnxLudbRadproxCacheMatchType": tmnxLudbRadproxCacheMatchType,
       "tmnxLudbRadproxCacheMatchOption": tmnxLudbRadproxCacheMatchOption,
       "tmnxLudbRadproxCacheFailAction": tmnxLudbRadproxCacheFailAction,
       "tmnxLudbRadproxCacheMacFormat": tmnxLudbRadproxCacheMacFormat,
       "tmnxLudbRadproxCacheMatchOption6": tmnxLudbRadproxCacheMatchOption6,
       "tmnxLocUsrDbDhcpOption6TblLstCh": tmnxLocUsrDbDhcpOption6TblLstCh,
       "tmnxLocUsrDbDhcpOption6Table": tmnxLocUsrDbDhcpOption6Table,
       "tmnxLocUsrDbDhcpOption6Entry": tmnxLocUsrDbDhcpOption6Entry,
       "tmnxLocUsrDbDhcpOption6Number": tmnxLocUsrDbDhcpOption6Number,
       "tmnxLocUsrDbDhcpOption6RowStatus": tmnxLocUsrDbDhcpOption6RowStatus,
       "tmnxLocUsrDbDhcpOption6LstChngTm": tmnxLocUsrDbDhcpOption6LstChngTm,
       "tmnxLocUsrDbDhcpOption6Type": tmnxLocUsrDbDhcpOption6Type,
       "tmnxLocUsrDbDhcpOption6Value": tmnxLocUsrDbDhcpOption6Value,
       "tmnxLocUsrDbPppOption6TblLstCh": tmnxLocUsrDbPppOption6TblLstCh,
       "tmnxLocUsrDbPppOption6Table": tmnxLocUsrDbPppOption6Table,
       "tmnxLocUsrDbPppOption6Entry": tmnxLocUsrDbPppOption6Entry,
       "tmnxLocUsrDbPppOption6Number": tmnxLocUsrDbPppOption6Number,
       "tmnxLocUsrDbPppOption6RowSts": tmnxLocUsrDbPppOption6RowSts,
       "tmnxLocUsrDbPppOption6LstChgTm": tmnxLocUsrDbPppOption6LstChgTm,
       "tmnxLocUsrDbPppOption6Type": tmnxLocUsrDbPppOption6Type,
       "tmnxLocUsrDbPppOption6Value": tmnxLocUsrDbPppOption6Value,
       "tmnxLudbPppAliTableLastChange": tmnxLudbPppAliTableLastChange,
       "tmnxLudbPppAliTable": tmnxLudbPppAliTable,
       "tmnxLudbPppAliEntry": tmnxLudbPppAliEntry,
       "tmnxLudbPppAliLastChangeTime": tmnxLudbPppAliLastChangeTime,
       "tmnxLudbPppAliCircuitIdType": tmnxLudbPppAliCircuitIdType,
       "tmnxLudbPppAliCircuitId": tmnxLudbPppAliCircuitId,
       "tmnxLudbPppAliRemoteIdType": tmnxLudbPppAliRemoteIdType,
       "tmnxLudbPppAliRemoteId": tmnxLudbPppAliRemoteId,
       "tmnxLudbDhcp2TableLastChange": tmnxLudbDhcp2TableLastChange,
       "tmnxLudbDhcp2Table": tmnxLudbDhcp2Table,
       "tmnxLudbDhcp2Entry": tmnxLudbDhcp2Entry,
       "tmnxLudbDhcp2LastChangeTime": tmnxLudbDhcp2LastChangeTime,
       "tmnxLudbDhcp2WppPortalSvcId": tmnxLudbDhcp2WppPortalSvcId,
       "tmnxLudbDhcp2WppPortalName": tmnxLudbDhcp2WppPortalName,
       "tmnxLudbDhcp2WppSubProfile": tmnxLudbDhcp2WppSubProfile,
       "tmnxLudbDhcp2WppSLAProfile": tmnxLudbDhcp2WppSLAProfile,
       "tmnxLudbDhcp2WppAppProfile": tmnxLudbDhcp2WppAppProfile,
       "tmnxLudbDhcp2WppRestDiscon": tmnxLudbDhcp2WppRestDiscon,
       "tmnxLudbDhcp2GiAddrType": tmnxLudbDhcp2GiAddrType,
       "tmnxLudbDhcp2GiAddr": tmnxLudbDhcp2GiAddr,
       "tmnxLudbDhcp2LinkAddrType": tmnxLudbDhcp2LinkAddrType,
       "tmnxLudbDhcp2LinkAddr": tmnxLudbDhcp2LinkAddr,
       "tmnxLudbDhcp2Server6AddrType": tmnxLudbDhcp2Server6AddrType,
       "tmnxLudbDhcp2Server6Addr": tmnxLudbDhcp2Server6Addr,
       "tmnxLudbDhcp2DiamAppPlcy": tmnxLudbDhcp2DiamAppPlcy,
       "tmnxLudbDhcp2Ipv6LeaseRenew": tmnxLudbDhcp2Ipv6LeaseRenew,
       "tmnxLudbDhcp2Ipv6LeaseRebind": tmnxLudbDhcp2Ipv6LeaseRebind,
       "tmnxLudbDhcp2Ipv6LeaseValidLife": tmnxLudbDhcp2Ipv6LeaseValidLife,
       "tmnxLudbDhcp2Ipv6LeasePrefLife": tmnxLudbDhcp2Ipv6LeasePrefLife,
       "tmnxLudbPpp2TableLastChange": tmnxLudbPpp2TableLastChange,
       "tmnxLudbPpp2Table": tmnxLudbPpp2Table,
       "tmnxLudbPpp2Entry": tmnxLudbPpp2Entry,
       "tmnxLudbPpp2LastChangeTime": tmnxLudbPpp2LastChangeTime,
       "tmnxLudbPpp2DiamAppPlcy": tmnxLudbPpp2DiamAppPlcy,
       "tmnxLudbPpp2Ipv6LeaseRenew": tmnxLudbPpp2Ipv6LeaseRenew,
       "tmnxLudbPpp2Ipv6LeaseRebind": tmnxLudbPpp2Ipv6LeaseRebind,
       "tmnxLudbPpp2Ipv6LeaseValidLife": tmnxLudbPpp2Ipv6LeaseValidLife,
       "tmnxLudbPpp2Ipv6LeasePrefLife": tmnxLudbPpp2Ipv6LeasePrefLife,
       "tmnxLudbToClntOptTableLstCh": tmnxLudbToClntOptTableLstCh,
       "tmnxLudbToClntOptTable": tmnxLudbToClntOptTable,
       "tmnxLudbToClntOptEntry": tmnxLudbToClntOptEntry,
       "tmnxLudbToClntOptAddrType": tmnxLudbToClntOptAddrType,
       "tmnxLudbToClntOptNumber": tmnxLudbToClntOptNumber,
       "tmnxLudbToClntOptRowStatus": tmnxLudbToClntOptRowStatus,
       "tmnxLudbToClntOptLastCh": tmnxLudbToClntOptLastCh,
       "tmnxLudbToClntOptType": tmnxLudbToClntOptType,
       "tmnxLudbToClntOptValue": tmnxLudbToClntOptValue,
       "tmnxLocalUserDbNotificationObjs": tmnxLocalUserDbNotificationObjs,
       "tmnxLudbNotifyPortId": tmnxLudbNotifyPortId,
       "tmnxLocalUserDbNotifyPrefix": tmnxLocalUserDbNotifyPrefix,
       "tmnxLocalUserDbNotifications": tmnxLocalUserDbNotifications,
       "tmnxLudbDhcpGroupIfTooLong": tmnxLudbDhcpGroupIfTooLong,
       "tmnxLudbPppoeGroupIfTooLong": tmnxLudbPppoeGroupIfTooLong}
)
