# SNMP MIB module (CISCO-SCAS-BB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SCAS-BB-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:57 2025
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

(linkIndex,
 linkModuleIndex,
 pmoduleIndex,
 spvIndex) = mibBuilder.importSymbols(
    "PCUBE-SE-MIB",
    "linkIndex",
    "linkModuleIndex",
    "pmoduleIndex",
    "spvIndex")

(pcubeModules,
 pcubeWorkgroup) = mibBuilder.importSymbols(
    "PCUBE-SMI",
    "pcubeModules",
    "pcubeWorkgroup")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

_PcubeEngageMIB_ObjectIdentity = ObjectIdentity
pcubeEngageMIB = _PcubeEngageMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4)
)
_PcubeEngageConformance_ObjectIdentity = ObjectIdentity
pcubeEngageConformance = _PcubeEngageConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3)
)
_PcubeEngageGroups_ObjectIdentity = ObjectIdentity
pcubeEngageGroups = _PcubeEngageGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1)
)
_PcubeLinkGroup_ObjectIdentity = ObjectIdentity
pcubeLinkGroup = _PcubeLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 2)
)
_PcubePackageGroup_ObjectIdentity = ObjectIdentity
pcubePackageGroup = _PcubePackageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 3)
)
_PcubeSubscriberGroup_ObjectIdentity = ObjectIdentity
pcubeSubscriberGroup = _PcubeSubscriberGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 4)
)
_PcubeServiceCounterGroup_ObjectIdentity = ObjectIdentity
pcubeServiceCounterGroup = _PcubeServiceCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 5)
)
_PcubeEngageCompliances_ObjectIdentity = ObjectIdentity
pcubeEngageCompliances = _PcubeEngageCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 2)
)
_PcubeEngageCompliance_ObjectIdentity = ObjectIdentity
pcubeEngageCompliance = _PcubeEngageCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 2, 1)
)
_PcubeEngageObjs_ObjectIdentity = ObjectIdentity
pcubeEngageObjs = _PcubeEngageObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2)
)
_ServiceGrp_ObjectIdentity = ObjectIdentity
serviceGrp = _ServiceGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 1)
)
_ServiceTable_ObjectIdentity = ObjectIdentity
serviceTable = _ServiceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 1, 1)
)
_LinkGrp_ObjectIdentity = ObjectIdentity
linkGrp = _LinkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2)
)
_LinkServiceUsageTable_Object = MibTable
linkServiceUsageTable = _LinkServiceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    linkServiceUsageTable.setStatus("mandatory")
_LinkServiceUsageEntry_Object = MibTableRow
linkServiceUsageEntry = _LinkServiceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1)
)
linkServiceUsageEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "linkModuleIndex"),
    (0, "PCUBE-SE-MIB", "linkIndex"),
    (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    linkServiceUsageEntry.setStatus("mandatory")
_LinkServiceUsageUpVolume_Type = Counter32
_LinkServiceUsageUpVolume_Object = MibTableColumn
linkServiceUsageUpVolume = _LinkServiceUsageUpVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 1),
    _LinkServiceUsageUpVolume_Type()
)
linkServiceUsageUpVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageUpVolume.setStatus("mandatory")
_LinkServiceUsageDownVolume_Type = Counter32
_LinkServiceUsageDownVolume_Object = MibTableColumn
linkServiceUsageDownVolume = _LinkServiceUsageDownVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 2),
    _LinkServiceUsageDownVolume_Type()
)
linkServiceUsageDownVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageDownVolume.setStatus("mandatory")
_LinkServiceUsageNumSessions_Type = Counter32
_LinkServiceUsageNumSessions_Object = MibTableColumn
linkServiceUsageNumSessions = _LinkServiceUsageNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 3),
    _LinkServiceUsageNumSessions_Type()
)
linkServiceUsageNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageNumSessions.setStatus("mandatory")
_LinkServiceUsageDuration_Type = Counter32
_LinkServiceUsageDuration_Object = MibTableColumn
linkServiceUsageDuration = _LinkServiceUsageDuration_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 4),
    _LinkServiceUsageDuration_Type()
)
linkServiceUsageDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageDuration.setStatus("mandatory")
_LinkServiceUsageConcurrentSessions_Type = Counter32
_LinkServiceUsageConcurrentSessions_Object = MibTableColumn
linkServiceUsageConcurrentSessions = _LinkServiceUsageConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 5),
    _LinkServiceUsageConcurrentSessions_Type()
)
linkServiceUsageConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageConcurrentSessions.setStatus("mandatory")
_LinkServiceUsageActiveSubscribers_Type = Counter32
_LinkServiceUsageActiveSubscribers_Object = MibTableColumn
linkServiceUsageActiveSubscribers = _LinkServiceUsageActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 6),
    _LinkServiceUsageActiveSubscribers_Type()
)
linkServiceUsageActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageActiveSubscribers.setStatus("mandatory")
_LinkServiceUpDroppedPackets_Type = Counter32
_LinkServiceUpDroppedPackets_Object = MibTableColumn
linkServiceUpDroppedPackets = _LinkServiceUpDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 7),
    _LinkServiceUpDroppedPackets_Type()
)
linkServiceUpDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUpDroppedPackets.setStatus("mandatory")
_LinkServiceDownDroppedPackets_Type = Counter32
_LinkServiceDownDroppedPackets_Object = MibTableColumn
linkServiceDownDroppedPackets = _LinkServiceDownDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 8),
    _LinkServiceDownDroppedPackets_Type()
)
linkServiceDownDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceDownDroppedPackets.setStatus("mandatory")
_LinkServiceUpDroppedBytes_Type = Counter32
_LinkServiceUpDroppedBytes_Object = MibTableColumn
linkServiceUpDroppedBytes = _LinkServiceUpDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 9),
    _LinkServiceUpDroppedBytes_Type()
)
linkServiceUpDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUpDroppedBytes.setStatus("mandatory")
_LinkServiceDownDroppedBytes_Type = Counter32
_LinkServiceDownDroppedBytes_Object = MibTableColumn
linkServiceDownDroppedBytes = _LinkServiceDownDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 10),
    _LinkServiceDownDroppedBytes_Type()
)
linkServiceDownDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceDownDroppedBytes.setStatus("mandatory")
_PackageGrp_ObjectIdentity = ObjectIdentity
packageGrp = _PackageGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3)
)
_PackageCounterTable_Object = MibTable
packageCounterTable = _PackageCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    packageCounterTable.setStatus("mandatory")
_PackageCounterEntry_Object = MibTableRow
packageCounterEntry = _PackageCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1)
)
packageCounterEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "packageCounterIndex"),
)
if mibBuilder.loadTexts:
    packageCounterEntry.setStatus("mandatory")


class _PackageCounterIndex_Type(Integer32):
    """Custom type packageCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PackageCounterIndex_Type.__name__ = "Integer32"
_PackageCounterIndex_Object = MibTableColumn
packageCounterIndex = _PackageCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 1),
    _PackageCounterIndex_Type()
)
packageCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    packageCounterIndex.setStatus("mandatory")


class _PackageCounterStatus_Type(Integer32):
    """Custom type packageCounterStatus based on Integer32"""
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


_PackageCounterStatus_Type.__name__ = "Integer32"
_PackageCounterStatus_Object = MibTableColumn
packageCounterStatus = _PackageCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 2),
    _PackageCounterStatus_Type()
)
packageCounterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageCounterStatus.setStatus("mandatory")
_PackageCounterName_Type = SnmpAdminString
_PackageCounterName_Object = MibTableColumn
packageCounterName = _PackageCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 3),
    _PackageCounterName_Type()
)
packageCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageCounterName.setStatus("mandatory")
_PackageCounterActiveSubscribers_Type = Counter32
_PackageCounterActiveSubscribers_Object = MibTableColumn
packageCounterActiveSubscribers = _PackageCounterActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 4),
    _PackageCounterActiveSubscribers_Type()
)
packageCounterActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageCounterActiveSubscribers.setStatus("mandatory")
_PackageServiceUsageTable_Object = MibTable
packageServiceUsageTable = _PackageServiceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    packageServiceUsageTable.setStatus("mandatory")
_PackageServiceUsageEntry_Object = MibTableRow
packageServiceUsageEntry = _PackageServiceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1)
)
packageServiceUsageEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "packageCounterIndex"),
    (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    packageServiceUsageEntry.setStatus("mandatory")
_PackageServiceUsageUpVolume_Type = Counter32
_PackageServiceUsageUpVolume_Object = MibTableColumn
packageServiceUsageUpVolume = _PackageServiceUsageUpVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 1),
    _PackageServiceUsageUpVolume_Type()
)
packageServiceUsageUpVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageUpVolume.setStatus("mandatory")
_PackageServiceUsageDownVolume_Type = Counter32
_PackageServiceUsageDownVolume_Object = MibTableColumn
packageServiceUsageDownVolume = _PackageServiceUsageDownVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 2),
    _PackageServiceUsageDownVolume_Type()
)
packageServiceUsageDownVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageDownVolume.setStatus("mandatory")
_PackageServiceUsageNumSessions_Type = Counter32
_PackageServiceUsageNumSessions_Object = MibTableColumn
packageServiceUsageNumSessions = _PackageServiceUsageNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 3),
    _PackageServiceUsageNumSessions_Type()
)
packageServiceUsageNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageNumSessions.setStatus("mandatory")
_PackageServiceUsageDuration_Type = Counter32
_PackageServiceUsageDuration_Object = MibTableColumn
packageServiceUsageDuration = _PackageServiceUsageDuration_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 4),
    _PackageServiceUsageDuration_Type()
)
packageServiceUsageDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageDuration.setStatus("mandatory")
_PackageServiceUsageConcurrentSessions_Type = Counter32
_PackageServiceUsageConcurrentSessions_Object = MibTableColumn
packageServiceUsageConcurrentSessions = _PackageServiceUsageConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 5),
    _PackageServiceUsageConcurrentSessions_Type()
)
packageServiceUsageConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageConcurrentSessions.setStatus("mandatory")
_PackageServiceUsageActiveSubscribers_Type = Counter32
_PackageServiceUsageActiveSubscribers_Object = MibTableColumn
packageServiceUsageActiveSubscribers = _PackageServiceUsageActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 6),
    _PackageServiceUsageActiveSubscribers_Type()
)
packageServiceUsageActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageActiveSubscribers.setStatus("mandatory")
_PackageServiceUpDroppedPackets_Type = Counter32
_PackageServiceUpDroppedPackets_Object = MibTableColumn
packageServiceUpDroppedPackets = _PackageServiceUpDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 7),
    _PackageServiceUpDroppedPackets_Type()
)
packageServiceUpDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUpDroppedPackets.setStatus("mandatory")
_PackageServiceDownDroppedPackets_Type = Counter32
_PackageServiceDownDroppedPackets_Object = MibTableColumn
packageServiceDownDroppedPackets = _PackageServiceDownDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 8),
    _PackageServiceDownDroppedPackets_Type()
)
packageServiceDownDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceDownDroppedPackets.setStatus("mandatory")
_PackageServiceUpDroppedBytes_Type = Counter32
_PackageServiceUpDroppedBytes_Object = MibTableColumn
packageServiceUpDroppedBytes = _PackageServiceUpDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 9),
    _PackageServiceUpDroppedBytes_Type()
)
packageServiceUpDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUpDroppedBytes.setStatus("mandatory")
_PackageServiceDownDroppedBytes_Type = Counter32
_PackageServiceDownDroppedBytes_Object = MibTableColumn
packageServiceDownDroppedBytes = _PackageServiceDownDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 10),
    _PackageServiceDownDroppedBytes_Type()
)
packageServiceDownDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceDownDroppedBytes.setStatus("mandatory")
_SubscriberGrp_ObjectIdentity = ObjectIdentity
subscriberGrp = _SubscriberGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4)
)
_SubscribersTable_Object = MibTable
subscribersTable = _SubscribersTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    subscribersTable.setStatus("mandatory")
_SubscribersEntry_Object = MibTableRow
subscribersEntry = _SubscribersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1, 1)
)
subscribersEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "spvIndex"),
)
if mibBuilder.loadTexts:
    subscribersEntry.setStatus("mandatory")


class _SubscriberPackageIndex_Type(Integer32):
    """Custom type subscriberPackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SubscriberPackageIndex_Type.__name__ = "Integer32"
_SubscriberPackageIndex_Object = MibTableColumn
subscriberPackageIndex = _SubscriberPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1, 1, 1),
    _SubscriberPackageIndex_Type()
)
subscriberPackageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberPackageIndex.setStatus("mandatory")
_SubscriberServiceUsageTable_Object = MibTable
subscriberServiceUsageTable = _SubscriberServiceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    subscriberServiceUsageTable.setStatus("mandatory")
_SubscriberServiceUsageEntry_Object = MibTableRow
subscriberServiceUsageEntry = _SubscriberServiceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1)
)
subscriberServiceUsageEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "spvIndex"),
    (0, "CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    subscriberServiceUsageEntry.setStatus("mandatory")
_SubscriberServiceUsageUpVolume_Type = Counter32
_SubscriberServiceUsageUpVolume_Object = MibTableColumn
subscriberServiceUsageUpVolume = _SubscriberServiceUsageUpVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 1),
    _SubscriberServiceUsageUpVolume_Type()
)
subscriberServiceUsageUpVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageUpVolume.setStatus("mandatory")
_SubscriberServiceUsageDownVolume_Type = Counter32
_SubscriberServiceUsageDownVolume_Object = MibTableColumn
subscriberServiceUsageDownVolume = _SubscriberServiceUsageDownVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 2),
    _SubscriberServiceUsageDownVolume_Type()
)
subscriberServiceUsageDownVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageDownVolume.setStatus("mandatory")


class _SubscriberServiceUsageNumSessions_Type(Integer32):
    """Custom type subscriberServiceUsageNumSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SubscriberServiceUsageNumSessions_Type.__name__ = "Integer32"
_SubscriberServiceUsageNumSessions_Object = MibTableColumn
subscriberServiceUsageNumSessions = _SubscriberServiceUsageNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 3),
    _SubscriberServiceUsageNumSessions_Type()
)
subscriberServiceUsageNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageNumSessions.setStatus("mandatory")


class _SubscriberServiceUsageDuration_Type(Integer32):
    """Custom type subscriberServiceUsageDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SubscriberServiceUsageDuration_Type.__name__ = "Integer32"
_SubscriberServiceUsageDuration_Object = MibTableColumn
subscriberServiceUsageDuration = _SubscriberServiceUsageDuration_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 4),
    _SubscriberServiceUsageDuration_Type()
)
subscriberServiceUsageDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageDuration.setStatus("mandatory")
_ServiceCounterGrp_ObjectIdentity = ObjectIdentity
serviceCounterGrp = _ServiceCounterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5)
)
_GlobalScopeServiceCounterTable_Object = MibTable
globalScopeServiceCounterTable = _GlobalScopeServiceCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    globalScopeServiceCounterTable.setStatus("mandatory")
_GlobalScopeServiceCounterEntry_Object = MibTableRow
globalScopeServiceCounterEntry = _GlobalScopeServiceCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1)
)
globalScopeServiceCounterEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    globalScopeServiceCounterEntry.setStatus("mandatory")


class _GlobalScopeServiceCounterIndex_Type(Integer32):
    """Custom type globalScopeServiceCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GlobalScopeServiceCounterIndex_Type.__name__ = "Integer32"
_GlobalScopeServiceCounterIndex_Object = MibTableColumn
globalScopeServiceCounterIndex = _GlobalScopeServiceCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 1),
    _GlobalScopeServiceCounterIndex_Type()
)
globalScopeServiceCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalScopeServiceCounterIndex.setStatus("mandatory")


class _GlobalScopeServiceCounterStatus_Type(Integer32):
    """Custom type globalScopeServiceCounterStatus based on Integer32"""
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


_GlobalScopeServiceCounterStatus_Type.__name__ = "Integer32"
_GlobalScopeServiceCounterStatus_Object = MibTableColumn
globalScopeServiceCounterStatus = _GlobalScopeServiceCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 2),
    _GlobalScopeServiceCounterStatus_Type()
)
globalScopeServiceCounterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalScopeServiceCounterStatus.setStatus("mandatory")
_GlobalScopeServiceCounterName_Type = SnmpAdminString
_GlobalScopeServiceCounterName_Object = MibTableColumn
globalScopeServiceCounterName = _GlobalScopeServiceCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 3),
    _GlobalScopeServiceCounterName_Type()
)
globalScopeServiceCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalScopeServiceCounterName.setStatus("mandatory")
_SubscriberScopeServiceCounterTable_Object = MibTable
subscriberScopeServiceCounterTable = _SubscriberScopeServiceCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2)
)
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterTable.setStatus("mandatory")
_SubscriberScopeServiceCounterEntry_Object = MibTableRow
subscriberScopeServiceCounterEntry = _SubscriberScopeServiceCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1)
)
subscriberScopeServiceCounterEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterEntry.setStatus("mandatory")


class _SubscriberScopeServiceCounterIndex_Type(Integer32):
    """Custom type subscriberScopeServiceCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SubscriberScopeServiceCounterIndex_Type.__name__ = "Integer32"
_SubscriberScopeServiceCounterIndex_Object = MibTableColumn
subscriberScopeServiceCounterIndex = _SubscriberScopeServiceCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 1),
    _SubscriberScopeServiceCounterIndex_Type()
)
subscriberScopeServiceCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterIndex.setStatus("mandatory")


class _SubscriberScopeServiceCounterStatus_Type(Integer32):
    """Custom type subscriberScopeServiceCounterStatus based on Integer32"""
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


_SubscriberScopeServiceCounterStatus_Type.__name__ = "Integer32"
_SubscriberScopeServiceCounterStatus_Object = MibTableColumn
subscriberScopeServiceCounterStatus = _SubscriberScopeServiceCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 2),
    _SubscriberScopeServiceCounterStatus_Type()
)
subscriberScopeServiceCounterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterStatus.setStatus("mandatory")
_SubscriberScopeServiceCounterName_Type = SnmpAdminString
_SubscriberScopeServiceCounterName_Object = MibTableColumn
subscriberScopeServiceCounterName = _SubscriberScopeServiceCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 3),
    _SubscriberScopeServiceCounterName_Type()
)
subscriberScopeServiceCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SCAS-BB-MIB",
    **{"pcubeEngageMIB": pcubeEngageMIB,
       "pcubeEngageConformance": pcubeEngageConformance,
       "pcubeEngageGroups": pcubeEngageGroups,
       "pcubeLinkGroup": pcubeLinkGroup,
       "pcubePackageGroup": pcubePackageGroup,
       "pcubeSubscriberGroup": pcubeSubscriberGroup,
       "pcubeServiceCounterGroup": pcubeServiceCounterGroup,
       "pcubeEngageCompliances": pcubeEngageCompliances,
       "pcubeEngageCompliance": pcubeEngageCompliance,
       "pcubeEngageObjs": pcubeEngageObjs,
       "serviceGrp": serviceGrp,
       "serviceTable": serviceTable,
       "linkGrp": linkGrp,
       "linkServiceUsageTable": linkServiceUsageTable,
       "linkServiceUsageEntry": linkServiceUsageEntry,
       "linkServiceUsageUpVolume": linkServiceUsageUpVolume,
       "linkServiceUsageDownVolume": linkServiceUsageDownVolume,
       "linkServiceUsageNumSessions": linkServiceUsageNumSessions,
       "linkServiceUsageDuration": linkServiceUsageDuration,
       "linkServiceUsageConcurrentSessions": linkServiceUsageConcurrentSessions,
       "linkServiceUsageActiveSubscribers": linkServiceUsageActiveSubscribers,
       "linkServiceUpDroppedPackets": linkServiceUpDroppedPackets,
       "linkServiceDownDroppedPackets": linkServiceDownDroppedPackets,
       "linkServiceUpDroppedBytes": linkServiceUpDroppedBytes,
       "linkServiceDownDroppedBytes": linkServiceDownDroppedBytes,
       "packageGrp": packageGrp,
       "packageCounterTable": packageCounterTable,
       "packageCounterEntry": packageCounterEntry,
       "packageCounterIndex": packageCounterIndex,
       "packageCounterStatus": packageCounterStatus,
       "packageCounterName": packageCounterName,
       "packageCounterActiveSubscribers": packageCounterActiveSubscribers,
       "packageServiceUsageTable": packageServiceUsageTable,
       "packageServiceUsageEntry": packageServiceUsageEntry,
       "packageServiceUsageUpVolume": packageServiceUsageUpVolume,
       "packageServiceUsageDownVolume": packageServiceUsageDownVolume,
       "packageServiceUsageNumSessions": packageServiceUsageNumSessions,
       "packageServiceUsageDuration": packageServiceUsageDuration,
       "packageServiceUsageConcurrentSessions": packageServiceUsageConcurrentSessions,
       "packageServiceUsageActiveSubscribers": packageServiceUsageActiveSubscribers,
       "packageServiceUpDroppedPackets": packageServiceUpDroppedPackets,
       "packageServiceDownDroppedPackets": packageServiceDownDroppedPackets,
       "packageServiceUpDroppedBytes": packageServiceUpDroppedBytes,
       "packageServiceDownDroppedBytes": packageServiceDownDroppedBytes,
       "subscriberGrp": subscriberGrp,
       "subscribersTable": subscribersTable,
       "subscribersEntry": subscribersEntry,
       "subscriberPackageIndex": subscriberPackageIndex,
       "subscriberServiceUsageTable": subscriberServiceUsageTable,
       "subscriberServiceUsageEntry": subscriberServiceUsageEntry,
       "subscriberServiceUsageUpVolume": subscriberServiceUsageUpVolume,
       "subscriberServiceUsageDownVolume": subscriberServiceUsageDownVolume,
       "subscriberServiceUsageNumSessions": subscriberServiceUsageNumSessions,
       "subscriberServiceUsageDuration": subscriberServiceUsageDuration,
       "serviceCounterGrp": serviceCounterGrp,
       "globalScopeServiceCounterTable": globalScopeServiceCounterTable,
       "globalScopeServiceCounterEntry": globalScopeServiceCounterEntry,
       "globalScopeServiceCounterIndex": globalScopeServiceCounterIndex,
       "globalScopeServiceCounterStatus": globalScopeServiceCounterStatus,
       "globalScopeServiceCounterName": globalScopeServiceCounterName,
       "subscriberScopeServiceCounterTable": subscriberScopeServiceCounterTable,
       "subscriberScopeServiceCounterEntry": subscriberScopeServiceCounterEntry,
       "subscriberScopeServiceCounterIndex": subscriberScopeServiceCounterIndex,
       "subscriberScopeServiceCounterStatus": subscriberScopeServiceCounterStatus,
       "subscriberScopeServiceCounterName": subscriberScopeServiceCounterName}
)
