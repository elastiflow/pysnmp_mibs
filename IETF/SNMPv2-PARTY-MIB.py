# SNMP MIB module (SNMPv2-PARTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMPv2-PARTY-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:06:23 2025
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

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

partyMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Party(TextualConvention, ObjectIdentifier):
    status = "current"


class TAddress(TextualConvention, OctetString):
    status = "current"


class Clock(TextualConvention, Unsigned32):
    status = "current"


class Context(TextualConvention, ObjectIdentifier):
    status = "current"


class StorageType(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("volatile", 2),
          ("nonVolatile", 3),
          ("permanent", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PartyAdmin_ObjectIdentity = ObjectIdentity
partyAdmin = _PartyAdmin_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1)
)
_PartyProtocols_ObjectIdentity = ObjectIdentity
partyProtocols = _PartyProtocols_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 1)
)
_NoAuth_ObjectIdentity = ObjectIdentity
noAuth = _NoAuth_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 1, 1)
)
_NoPriv_ObjectIdentity = ObjectIdentity
noPriv = _NoPriv_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 1, 2)
)
_DesPrivProtocol_ObjectIdentity = ObjectIdentity
desPrivProtocol = _DesPrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 1, 3)
)
_V2md5AuthProtocol_ObjectIdentity = ObjectIdentity
v2md5AuthProtocol = _V2md5AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 1, 4)
)
_TemporalDomains_ObjectIdentity = ObjectIdentity
temporalDomains = _TemporalDomains_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 2)
)
_CurrentTime_ObjectIdentity = ObjectIdentity
currentTime = _CurrentTime_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 2, 1)
)
_RestartTime_ObjectIdentity = ObjectIdentity
restartTime = _RestartTime_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 2, 2)
)
_CacheTime_ObjectIdentity = ObjectIdentity
cacheTime = _CacheTime_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 2, 3)
)
_InitialPartyId_ObjectIdentity = ObjectIdentity
initialPartyId = _InitialPartyId_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 3)
)
_InitialContextId_ObjectIdentity = ObjectIdentity
initialContextId = _InitialContextId_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 1, 4)
)
_PartyMIBObjects_ObjectIdentity = ObjectIdentity
partyMIBObjects = _PartyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 2)
)
_SnmpParties_ObjectIdentity = ObjectIdentity
snmpParties = _SnmpParties_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 2, 1)
)
_PartyTable_Object = MibTable
partyTable = _PartyTable_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    partyTable.setStatus("current")
_PartyEntry_Object = MibTableRow
partyEntry = _PartyEntry_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1)
)
partyEntry.setIndexNames(
    (1, "SNMPv2-PARTY-MIB", "partyIdentity"),
)
if mibBuilder.loadTexts:
    partyEntry.setStatus("current")
_PartyIdentity_Type = Party
_PartyIdentity_Object = MibTableColumn
partyIdentity = _PartyIdentity_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 1),
    _PartyIdentity_Type()
)
partyIdentity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    partyIdentity.setStatus("current")


class _PartyIndex_Type(Integer32):
    """Custom type partyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PartyIndex_Type.__name__ = "Integer32"
_PartyIndex_Object = MibTableColumn
partyIndex = _PartyIndex_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 2),
    _PartyIndex_Type()
)
partyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partyIndex.setStatus("current")
_PartyTDomain_Type = ObjectIdentifier
_PartyTDomain_Object = MibTableColumn
partyTDomain = _PartyTDomain_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 3),
    _PartyTDomain_Type()
)
partyTDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyTDomain.setStatus("current")


class _PartyTAddress_Type(TAddress):
    """Custom type partyTAddress based on TAddress"""
    defaultHexValue = "000000000000"


_PartyTAddress_Type.__name__ = "TAddress"
_PartyTAddress_Object = MibTableColumn
partyTAddress = _PartyTAddress_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 4),
    _PartyTAddress_Type()
)
partyTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyTAddress.setStatus("current")


class _PartyMaxMessageSize_Type(Integer32):
    """Custom type partyMaxMessageSize based on Integer32"""
    defaultValue = 484

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 65507),
    )


_PartyMaxMessageSize_Type.__name__ = "Integer32"
_PartyMaxMessageSize_Object = MibTableColumn
partyMaxMessageSize = _PartyMaxMessageSize_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 5),
    _PartyMaxMessageSize_Type()
)
partyMaxMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyMaxMessageSize.setStatus("current")


class _PartyLocal_Type(TruthValue):
    """Custom type partyLocal based on TruthValue"""
    defaultValue = 2


_PartyLocal_Type.__name__ = "TruthValue"
_PartyLocal_Object = MibTableColumn
partyLocal = _PartyLocal_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 6),
    _PartyLocal_Type()
)
partyLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyLocal.setStatus("current")


class _PartyAuthProtocol_Type(ObjectIdentifier):
    """Custom type partyAuthProtocol based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 6, 3, 3, 1, 1, 4)


_PartyAuthProtocol_Type.__name__ = "ObjectIdentifier"
_PartyAuthProtocol_Object = MibTableColumn
partyAuthProtocol = _PartyAuthProtocol_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 7),
    _PartyAuthProtocol_Type()
)
partyAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyAuthProtocol.setStatus("current")


class _PartyAuthClock_Type(Clock):
    """Custom type partyAuthClock based on Clock"""
    defaultValue = 0


_PartyAuthClock_Type.__name__ = "Clock"
_PartyAuthClock_Object = MibTableColumn
partyAuthClock = _PartyAuthClock_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 8),
    _PartyAuthClock_Type()
)
partyAuthClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyAuthClock.setStatus("current")


class _PartyAuthPrivate_Type(OctetString):
    """Custom type partyAuthPrivate based on OctetString"""
    defaultHexValue = ""


_PartyAuthPrivate_Type.__name__ = "OctetString"
_PartyAuthPrivate_Object = MibTableColumn
partyAuthPrivate = _PartyAuthPrivate_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 9),
    _PartyAuthPrivate_Type()
)
partyAuthPrivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyAuthPrivate.setStatus("current")


class _PartyAuthPublic_Type(OctetString):
    """Custom type partyAuthPublic based on OctetString"""
    defaultHexValue = ""


_PartyAuthPublic_Type.__name__ = "OctetString"
_PartyAuthPublic_Object = MibTableColumn
partyAuthPublic = _PartyAuthPublic_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 10),
    _PartyAuthPublic_Type()
)
partyAuthPublic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyAuthPublic.setStatus("current")


class _PartyAuthLifetime_Type(Integer32):
    """Custom type partyAuthLifetime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PartyAuthLifetime_Type.__name__ = "Integer32"
_PartyAuthLifetime_Object = MibTableColumn
partyAuthLifetime = _PartyAuthLifetime_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 11),
    _PartyAuthLifetime_Type()
)
partyAuthLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyAuthLifetime.setStatus("current")
if mibBuilder.loadTexts:
    partyAuthLifetime.setUnits("seconds")


class _PartyPrivProtocol_Type(ObjectIdentifier):
    """Custom type partyPrivProtocol based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 6, 3, 3, 1, 1, 2)


_PartyPrivProtocol_Type.__name__ = "ObjectIdentifier"
_PartyPrivProtocol_Object = MibTableColumn
partyPrivProtocol = _PartyPrivProtocol_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 12),
    _PartyPrivProtocol_Type()
)
partyPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyPrivProtocol.setStatus("current")


class _PartyPrivPrivate_Type(OctetString):
    """Custom type partyPrivPrivate based on OctetString"""
    defaultHexValue = ""


_PartyPrivPrivate_Type.__name__ = "OctetString"
_PartyPrivPrivate_Object = MibTableColumn
partyPrivPrivate = _PartyPrivPrivate_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 13),
    _PartyPrivPrivate_Type()
)
partyPrivPrivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyPrivPrivate.setStatus("current")


class _PartyPrivPublic_Type(OctetString):
    """Custom type partyPrivPublic based on OctetString"""
    defaultHexValue = ""


_PartyPrivPublic_Type.__name__ = "OctetString"
_PartyPrivPublic_Object = MibTableColumn
partyPrivPublic = _PartyPrivPublic_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 14),
    _PartyPrivPublic_Type()
)
partyPrivPublic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyPrivPublic.setStatus("current")
_PartyCloneFrom_Type = Party
_PartyCloneFrom_Object = MibTableColumn
partyCloneFrom = _PartyCloneFrom_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 15),
    _PartyCloneFrom_Type()
)
partyCloneFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyCloneFrom.setStatus("current")


class _PartyStorageType_Type(StorageType):
    """Custom type partyStorageType based on StorageType"""
    defaultValue = 3


_PartyStorageType_Type.__name__ = "StorageType"
_PartyStorageType_Object = MibTableColumn
partyStorageType = _PartyStorageType_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 16),
    _PartyStorageType_Type()
)
partyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyStorageType.setStatus("current")
_PartyStatus_Type = RowStatus
_PartyStatus_Object = MibTableColumn
partyStatus = _PartyStatus_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 1, 1, 1, 17),
    _PartyStatus_Type()
)
partyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    partyStatus.setStatus("current")
_SnmpContexts_ObjectIdentity = ObjectIdentity
snmpContexts = _SnmpContexts_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 2, 2)
)
_ContextTable_Object = MibTable
contextTable = _ContextTable_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    contextTable.setStatus("current")
_ContextEntry_Object = MibTableRow
contextEntry = _ContextEntry_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1)
)
contextEntry.setIndexNames(
    (1, "SNMPv2-PARTY-MIB", "contextIdentity"),
)
if mibBuilder.loadTexts:
    contextEntry.setStatus("current")
_ContextIdentity_Type = Context
_ContextIdentity_Object = MibTableColumn
contextIdentity = _ContextIdentity_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 1),
    _ContextIdentity_Type()
)
contextIdentity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    contextIdentity.setStatus("current")


class _ContextIndex_Type(Integer32):
    """Custom type contextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ContextIndex_Type.__name__ = "Integer32"
_ContextIndex_Object = MibTableColumn
contextIndex = _ContextIndex_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 2),
    _ContextIndex_Type()
)
contextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contextIndex.setStatus("current")


class _ContextLocal_Type(TruthValue):
    """Custom type contextLocal based on TruthValue"""
    defaultValue = 1


_ContextLocal_Type.__name__ = "TruthValue"
_ContextLocal_Object = MibTableColumn
contextLocal = _ContextLocal_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 3),
    _ContextLocal_Type()
)
contextLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextLocal.setStatus("current")


class _ContextViewIndex_Type(Integer32):
    """Custom type contextViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ContextViewIndex_Type.__name__ = "Integer32"
_ContextViewIndex_Object = MibTableColumn
contextViewIndex = _ContextViewIndex_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 4),
    _ContextViewIndex_Type()
)
contextViewIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextViewIndex.setStatus("current")


class _ContextLocalEntity_Type(OctetString):
    """Custom type contextLocalEntity based on OctetString"""
    defaultHexValue = ""


_ContextLocalEntity_Type.__name__ = "OctetString"
_ContextLocalEntity_Object = MibTableColumn
contextLocalEntity = _ContextLocalEntity_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 5),
    _ContextLocalEntity_Type()
)
contextLocalEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextLocalEntity.setStatus("current")


class _ContextLocalTime_Type(ObjectIdentifier):
    """Custom type contextLocalTime based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 6, 3, 3, 1, 2, 1)


_ContextLocalTime_Type.__name__ = "ObjectIdentifier"
_ContextLocalTime_Object = MibTableColumn
contextLocalTime = _ContextLocalTime_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 6),
    _ContextLocalTime_Type()
)
contextLocalTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextLocalTime.setStatus("current")
_ContextProxyDstParty_Type = Party
_ContextProxyDstParty_Object = MibTableColumn
contextProxyDstParty = _ContextProxyDstParty_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 7),
    _ContextProxyDstParty_Type()
)
contextProxyDstParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextProxyDstParty.setStatus("current")
_ContextProxySrcParty_Type = Party
_ContextProxySrcParty_Object = MibTableColumn
contextProxySrcParty = _ContextProxySrcParty_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 8),
    _ContextProxySrcParty_Type()
)
contextProxySrcParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextProxySrcParty.setStatus("current")
_ContextProxyContext_Type = ObjectIdentifier
_ContextProxyContext_Object = MibTableColumn
contextProxyContext = _ContextProxyContext_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 9),
    _ContextProxyContext_Type()
)
contextProxyContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextProxyContext.setStatus("current")


class _ContextStorageType_Type(StorageType):
    """Custom type contextStorageType based on StorageType"""
    defaultValue = 3


_ContextStorageType_Type.__name__ = "StorageType"
_ContextStorageType_Object = MibTableColumn
contextStorageType = _ContextStorageType_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 10),
    _ContextStorageType_Type()
)
contextStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextStorageType.setStatus("current")
_ContextStatus_Type = RowStatus
_ContextStatus_Object = MibTableColumn
contextStatus = _ContextStatus_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 2, 1, 1, 11),
    _ContextStatus_Type()
)
contextStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    contextStatus.setStatus("current")
_SnmpAccess_ObjectIdentity = ObjectIdentity
snmpAccess = _SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 2, 3)
)
_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("current")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1, 1)
)
aclEntry.setIndexNames(
    (0, "SNMPv2-PARTY-MIB", "aclTarget"),
    (0, "SNMPv2-PARTY-MIB", "aclSubject"),
    (0, "SNMPv2-PARTY-MIB", "aclResources"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("current")


class _AclTarget_Type(Integer32):
    """Custom type aclTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclTarget_Type.__name__ = "Integer32"
_AclTarget_Object = MibTableColumn
aclTarget = _AclTarget_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1, 1, 1),
    _AclTarget_Type()
)
aclTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclTarget.setStatus("current")


class _AclSubject_Type(Integer32):
    """Custom type aclSubject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclSubject_Type.__name__ = "Integer32"
_AclSubject_Object = MibTableColumn
aclSubject = _AclSubject_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1, 1, 2),
    _AclSubject_Type()
)
aclSubject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclSubject.setStatus("current")


class _AclResources_Type(Integer32):
    """Custom type aclResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclResources_Type.__name__ = "Integer32"
_AclResources_Object = MibTableColumn
aclResources = _AclResources_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1, 1, 3),
    _AclResources_Type()
)
aclResources.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclResources.setStatus("current")


class _AclPrivileges_Type(Integer32):
    """Custom type aclPrivileges based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclPrivileges_Type.__name__ = "Integer32"
_AclPrivileges_Object = MibTableColumn
aclPrivileges = _AclPrivileges_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1, 1, 4),
    _AclPrivileges_Type()
)
aclPrivileges.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclPrivileges.setStatus("current")


class _AclStorageType_Type(StorageType):
    """Custom type aclStorageType based on StorageType"""
    defaultValue = 3


_AclStorageType_Type.__name__ = "StorageType"
_AclStorageType_Object = MibTableColumn
aclStorageType = _AclStorageType_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1, 1, 5),
    _AclStorageType_Type()
)
aclStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStorageType.setStatus("current")
_AclStatus_Type = RowStatus
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 3, 1, 1, 6),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStatus.setStatus("current")
_SnmpViews_ObjectIdentity = ObjectIdentity
snmpViews = _SnmpViews_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 2, 4)
)
_ViewTable_Object = MibTable
viewTable = _ViewTable_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    viewTable.setStatus("current")
_ViewEntry_Object = MibTableRow
viewEntry = _ViewEntry_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1, 1)
)
viewEntry.setIndexNames(
    (0, "SNMPv2-PARTY-MIB", "viewIndex"),
    (1, "SNMPv2-PARTY-MIB", "viewSubtree"),
)
if mibBuilder.loadTexts:
    viewEntry.setStatus("current")


class _ViewIndex_Type(Integer32):
    """Custom type viewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ViewIndex_Type.__name__ = "Integer32"
_ViewIndex_Object = MibTableColumn
viewIndex = _ViewIndex_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1, 1, 1),
    _ViewIndex_Type()
)
viewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    viewIndex.setStatus("current")
_ViewSubtree_Type = ObjectIdentifier
_ViewSubtree_Object = MibTableColumn
viewSubtree = _ViewSubtree_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1, 1, 2),
    _ViewSubtree_Type()
)
viewSubtree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    viewSubtree.setStatus("current")


class _ViewMask_Type(OctetString):
    """Custom type viewMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ViewMask_Type.__name__ = "OctetString"
_ViewMask_Object = MibTableColumn
viewMask = _ViewMask_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1, 1, 3),
    _ViewMask_Type()
)
viewMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    viewMask.setStatus("current")


class _ViewType_Type(Integer32):
    """Custom type viewType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_ViewType_Type.__name__ = "Integer32"
_ViewType_Object = MibTableColumn
viewType = _ViewType_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1, 1, 4),
    _ViewType_Type()
)
viewType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    viewType.setStatus("current")


class _ViewStorageType_Type(StorageType):
    """Custom type viewStorageType based on StorageType"""
    defaultValue = 3


_ViewStorageType_Type.__name__ = "StorageType"
_ViewStorageType_Object = MibTableColumn
viewStorageType = _ViewStorageType_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1, 1, 5),
    _ViewStorageType_Type()
)
viewStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    viewStorageType.setStatus("current")
_ViewStatus_Type = RowStatus
_ViewStatus_Object = MibTableColumn
viewStatus = _ViewStatus_Object(
    (1, 3, 6, 1, 6, 3, 3, 2, 4, 1, 1, 6),
    _ViewStatus_Type()
)
viewStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    viewStatus.setStatus("current")
_PartyMIBConformance_ObjectIdentity = ObjectIdentity
partyMIBConformance = _PartyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 3)
)
_PartyMIBCompliances_ObjectIdentity = ObjectIdentity
partyMIBCompliances = _PartyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 3, 1)
)
_PartyMIBGroups_ObjectIdentity = ObjectIdentity
partyMIBGroups = _PartyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 3, 3, 2)
)

# Managed Objects groups

partyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 3, 3, 2, 1)
)
partyMIBGroup.setObjects(
      *(("SNMPv2-PARTY-MIB", "partyIndex"),
        ("SNMPv2-PARTY-MIB", "partyTDomain"),
        ("SNMPv2-PARTY-MIB", "partyTAddress"),
        ("SNMPv2-PARTY-MIB", "partyMaxMessageSize"),
        ("SNMPv2-PARTY-MIB", "partyLocal"),
        ("SNMPv2-PARTY-MIB", "partyAuthProtocol"),
        ("SNMPv2-PARTY-MIB", "partyAuthClock"),
        ("SNMPv2-PARTY-MIB", "partyAuthPrivate"),
        ("SNMPv2-PARTY-MIB", "partyAuthPublic"),
        ("SNMPv2-PARTY-MIB", "partyAuthLifetime"),
        ("SNMPv2-PARTY-MIB", "partyPrivProtocol"),
        ("SNMPv2-PARTY-MIB", "partyPrivPrivate"),
        ("SNMPv2-PARTY-MIB", "partyPrivPublic"),
        ("SNMPv2-PARTY-MIB", "partyStorageType"),
        ("SNMPv2-PARTY-MIB", "partyStatus"),
        ("SNMPv2-PARTY-MIB", "partyCloneFrom"),
        ("SNMPv2-PARTY-MIB", "contextIndex"),
        ("SNMPv2-PARTY-MIB", "contextLocal"),
        ("SNMPv2-PARTY-MIB", "contextViewIndex"),
        ("SNMPv2-PARTY-MIB", "contextLocalEntity"),
        ("SNMPv2-PARTY-MIB", "contextLocalTime"),
        ("SNMPv2-PARTY-MIB", "contextStorageType"),
        ("SNMPv2-PARTY-MIB", "contextStatus"),
        ("SNMPv2-PARTY-MIB", "aclTarget"),
        ("SNMPv2-PARTY-MIB", "aclSubject"),
        ("SNMPv2-PARTY-MIB", "aclPrivileges"),
        ("SNMPv2-PARTY-MIB", "aclStorageType"),
        ("SNMPv2-PARTY-MIB", "aclStatus"),
        ("SNMPv2-PARTY-MIB", "viewMask"),
        ("SNMPv2-PARTY-MIB", "viewType"),
        ("SNMPv2-PARTY-MIB", "viewStorageType"),
        ("SNMPv2-PARTY-MIB", "viewStatus"))
)
if mibBuilder.loadTexts:
    partyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

unSecurableCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 3, 3, 1, 1)
)
unSecurableCompliance.setObjects(
    ("SNMPv2-PARTY-MIB", "partyMIBGroup")
)
if mibBuilder.loadTexts:
    unSecurableCompliance.setStatus(
        "current"
    )

partyNoPrivacyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 3, 3, 1, 2)
)
partyNoPrivacyCompliance.setObjects(
    ("SNMPv2-PARTY-MIB", "partyMIBGroup")
)
if mibBuilder.loadTexts:
    partyNoPrivacyCompliance.setStatus(
        "current"
    )

partyPrivacyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 3, 3, 1, 3)
)
partyPrivacyCompliance.setObjects(
    ("SNMPv2-PARTY-MIB", "partyMIBGroup")
)
if mibBuilder.loadTexts:
    partyPrivacyCompliance.setStatus(
        "current"
    )

fullPrivacyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 3, 3, 1, 4)
)
fullPrivacyCompliance.setObjects(
    ("SNMPv2-PARTY-MIB", "partyMIBGroup")
)
if mibBuilder.loadTexts:
    fullPrivacyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMPv2-PARTY-MIB",
    **{"Party": Party,
       "TAddress": TAddress,
       "Clock": Clock,
       "Context": Context,
       "StorageType": StorageType,
       "partyMIB": partyMIB,
       "partyAdmin": partyAdmin,
       "partyProtocols": partyProtocols,
       "noAuth": noAuth,
       "noPriv": noPriv,
       "desPrivProtocol": desPrivProtocol,
       "v2md5AuthProtocol": v2md5AuthProtocol,
       "temporalDomains": temporalDomains,
       "currentTime": currentTime,
       "restartTime": restartTime,
       "cacheTime": cacheTime,
       "initialPartyId": initialPartyId,
       "initialContextId": initialContextId,
       "partyMIBObjects": partyMIBObjects,
       "snmpParties": snmpParties,
       "partyTable": partyTable,
       "partyEntry": partyEntry,
       "partyIdentity": partyIdentity,
       "partyIndex": partyIndex,
       "partyTDomain": partyTDomain,
       "partyTAddress": partyTAddress,
       "partyMaxMessageSize": partyMaxMessageSize,
       "partyLocal": partyLocal,
       "partyAuthProtocol": partyAuthProtocol,
       "partyAuthClock": partyAuthClock,
       "partyAuthPrivate": partyAuthPrivate,
       "partyAuthPublic": partyAuthPublic,
       "partyAuthLifetime": partyAuthLifetime,
       "partyPrivProtocol": partyPrivProtocol,
       "partyPrivPrivate": partyPrivPrivate,
       "partyPrivPublic": partyPrivPublic,
       "partyCloneFrom": partyCloneFrom,
       "partyStorageType": partyStorageType,
       "partyStatus": partyStatus,
       "snmpContexts": snmpContexts,
       "contextTable": contextTable,
       "contextEntry": contextEntry,
       "contextIdentity": contextIdentity,
       "contextIndex": contextIndex,
       "contextLocal": contextLocal,
       "contextViewIndex": contextViewIndex,
       "contextLocalEntity": contextLocalEntity,
       "contextLocalTime": contextLocalTime,
       "contextProxyDstParty": contextProxyDstParty,
       "contextProxySrcParty": contextProxySrcParty,
       "contextProxyContext": contextProxyContext,
       "contextStorageType": contextStorageType,
       "contextStatus": contextStatus,
       "snmpAccess": snmpAccess,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclTarget": aclTarget,
       "aclSubject": aclSubject,
       "aclResources": aclResources,
       "aclPrivileges": aclPrivileges,
       "aclStorageType": aclStorageType,
       "aclStatus": aclStatus,
       "snmpViews": snmpViews,
       "viewTable": viewTable,
       "viewEntry": viewEntry,
       "viewIndex": viewIndex,
       "viewSubtree": viewSubtree,
       "viewMask": viewMask,
       "viewType": viewType,
       "viewStorageType": viewStorageType,
       "viewStatus": viewStatus,
       "partyMIBConformance": partyMIBConformance,
       "partyMIBCompliances": partyMIBCompliances,
       "unSecurableCompliance": unSecurableCompliance,
       "partyNoPrivacyCompliance": partyNoPrivacyCompliance,
       "partyPrivacyCompliance": partyPrivacyCompliance,
       "fullPrivacyCompliance": fullPrivacyCompliance,
       "partyMIBGroups": partyMIBGroups,
       "partyMIBGroup": partyMIBGroup}
)
