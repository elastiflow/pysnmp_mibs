# SNMP MIB module (MAILCLEANER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mailcleaner_36661/MAILCLEANER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:19:35 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mailcleaner = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36661)
)
if mibBuilder.loadTexts:
    mailcleaner.setRevisions(
        ("2011-05-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 1)
)
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 1, 1)
)
_FullVersion_Type = DisplayString
_FullVersion_Object = MibScalar
fullVersion = _FullVersion_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 1, 1),
    _FullVersion_Type()
)
fullVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fullVersion.setStatus("current")
_Edition_Type = DisplayString
_Edition_Object = MibScalar
edition = _Edition_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 1, 2),
    _Edition_Type()
)
edition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edition.setStatus("current")
_CurrentVersion_Type = DisplayString
_CurrentVersion_Object = MibScalar
currentVersion = _CurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 1, 3),
    _CurrentVersion_Type()
)
currentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentVersion.setStatus("current")
_PatchLevel_Type = DisplayString
_PatchLevel_Object = MibScalar
patchLevel = _PatchLevel_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 1, 4),
    _PatchLevel_Type()
)
patchLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patchLevel.setStatus("current")
_Spools_ObjectIdentity = ObjectIdentity
spools = _Spools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 1, 2)
)
_SpoolIncoming_Type = Gauge32
_SpoolIncoming_Object = MibScalar
spoolIncoming = _SpoolIncoming_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 2, 1),
    _SpoolIncoming_Type()
)
spoolIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolIncoming.setStatus("current")
_SpoolFiltering_Type = Gauge32
_SpoolFiltering_Object = MibScalar
spoolFiltering = _SpoolFiltering_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 2, 2),
    _SpoolFiltering_Type()
)
spoolFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolFiltering.setStatus("current")
_SpoolOutgoing_Type = Gauge32
_SpoolOutgoing_Object = MibScalar
spoolOutgoing = _SpoolOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 2, 4),
    _SpoolOutgoing_Type()
)
spoolOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolOutgoing.setStatus("current")
_ProcessTable_Object = MibTable
processTable = _ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 3)
)
if mibBuilder.loadTexts:
    processTable.setStatus("current")
_ProcessEntry_Object = MibTableRow
processEntry = _ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 3, 1)
)
processEntry.setIndexNames(
    (0, "MAILCLEANER-MIB", "processIndex"),
)
if mibBuilder.loadTexts:
    processEntry.setStatus("current")


class _ProcessIndex_Type(Integer32):
    """Custom type processIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ProcessIndex_Type.__name__ = "Integer32"
_ProcessIndex_Object = MibTableColumn
processIndex = _ProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 3, 1, 1),
    _ProcessIndex_Type()
)
processIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processIndex.setStatus("current")
_ProcessName_Type = DisplayString
_ProcessName_Object = MibTableColumn
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 3, 1, 2),
    _ProcessName_Type()
)
processName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processName.setStatus("current")
_ProcessCount_Type = Gauge32
_ProcessCount_Object = MibTableColumn
processCount = _ProcessCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 3, 1, 3),
    _ProcessCount_Type()
)
processCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCount.setStatus("current")
_ProcessStatus_Type = DisplayString
_ProcessStatus_Object = MibTableColumn
processStatus = _ProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 36661, 1, 3, 1, 4),
    _ProcessStatus_Type()
)
processStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processStatus.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 2)
)
_ConfigIsMaster_Type = Integer32
_ConfigIsMaster_Object = MibScalar
configIsMaster = _ConfigIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 36661, 2, 1),
    _ConfigIsMaster_Type()
)
configIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configIsMaster.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 3)
)
_GlobalStatistics_ObjectIdentity = ObjectIdentity
globalStatistics = _GlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1)
)
_GlobalProcessesStatistics_ObjectIdentity = ObjectIdentity
globalProcessesStatistics = _GlobalProcessesStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1)
)
_GlobalMsgCount_Type = Counter32
_GlobalMsgCount_Object = MibScalar
globalMsgCount = _GlobalMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 1),
    _GlobalMsgCount_Type()
)
globalMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalMsgCount.setStatus("current")
_GlobalCleanCount_Type = Counter32
_GlobalCleanCount_Object = MibScalar
globalCleanCount = _GlobalCleanCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 2),
    _GlobalCleanCount_Type()
)
globalCleanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCleanCount.setStatus("current")
_GlobalSpamCount_Type = Counter32
_GlobalSpamCount_Object = MibScalar
globalSpamCount = _GlobalSpamCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 3),
    _GlobalSpamCount_Type()
)
globalSpamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalSpamCount.setStatus("current")
_GlobalVirusCount_Type = Counter32
_GlobalVirusCount_Object = MibScalar
globalVirusCount = _GlobalVirusCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 4),
    _GlobalVirusCount_Type()
)
globalVirusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalVirusCount.setStatus("current")
_GlobalNameCount_Type = Counter32
_GlobalNameCount_Object = MibScalar
globalNameCount = _GlobalNameCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 5),
    _GlobalNameCount_Type()
)
globalNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalNameCount.setStatus("current")
_GlobalOtherCount_Type = Counter32
_GlobalOtherCount_Object = MibScalar
globalOtherCount = _GlobalOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 6),
    _GlobalOtherCount_Type()
)
globalOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalOtherCount.setStatus("current")
_GlobalSizeCount_Type = Counter32
_GlobalSizeCount_Object = MibScalar
globalSizeCount = _GlobalSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 7),
    _GlobalSizeCount_Type()
)
globalSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalSizeCount.setStatus("current")
_GlobalUserCount_Type = Counter32
_GlobalUserCount_Object = MibScalar
globalUserCount = _GlobalUserCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 8),
    _GlobalUserCount_Type()
)
globalUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalUserCount.setStatus("current")
_GlobalDomainCount_Type = Counter32
_GlobalDomainCount_Object = MibScalar
globalDomainCount = _GlobalDomainCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 1, 9),
    _GlobalDomainCount_Type()
)
globalDomainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDomainCount.setStatus("current")
_GlobalRefusedStatistics_ObjectIdentity = ObjectIdentity
globalRefusedStatistics = _GlobalRefusedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2)
)
_GlobalRefusedCount_Type = Counter32
_GlobalRefusedCount_Object = MibScalar
globalRefusedCount = _GlobalRefusedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 1),
    _GlobalRefusedCount_Type()
)
globalRefusedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedCount.setStatus("current")
_GlobalRefusedRBLCount_Type = Counter32
_GlobalRefusedRBLCount_Object = MibScalar
globalRefusedRBLCount = _GlobalRefusedRBLCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 2),
    _GlobalRefusedRBLCount_Type()
)
globalRefusedRBLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedRBLCount.setStatus("current")
_GlobalRefusedHostCount_Type = Counter32
_GlobalRefusedHostCount_Object = MibScalar
globalRefusedHostCount = _GlobalRefusedHostCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 3),
    _GlobalRefusedHostCount_Type()
)
globalRefusedHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedHostCount.setStatus("current")
_GlobalRefusedRelayCount_Type = Counter32
_GlobalRefusedRelayCount_Object = MibScalar
globalRefusedRelayCount = _GlobalRefusedRelayCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 4),
    _GlobalRefusedRelayCount_Type()
)
globalRefusedRelayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedRelayCount.setStatus("current")
_GlobalRefusedLocalpartCount_Type = Counter32
_GlobalRefusedLocalpartCount_Object = MibScalar
globalRefusedLocalpartCount = _GlobalRefusedLocalpartCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 5),
    _GlobalRefusedLocalpartCount_Type()
)
globalRefusedLocalpartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedLocalpartCount.setStatus("current")
_GlobalRefusedBATVCount_Type = Counter32
_GlobalRefusedBATVCount_Object = MibScalar
globalRefusedBATVCount = _GlobalRefusedBATVCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 6),
    _GlobalRefusedBATVCount_Type()
)
globalRefusedBATVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedBATVCount.setStatus("current")
_GlobalRefusedBlacklistedSenderCount_Type = Counter32
_GlobalRefusedBlacklistedSenderCount_Object = MibScalar
globalRefusedBlacklistedSenderCount = _GlobalRefusedBlacklistedSenderCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 7),
    _GlobalRefusedBlacklistedSenderCount_Type()
)
globalRefusedBlacklistedSenderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedBlacklistedSenderCount.setStatus("current")
_GlobalRefusedSpoofingCount_Type = Counter32
_GlobalRefusedSpoofingCount_Object = MibScalar
globalRefusedSpoofingCount = _GlobalRefusedSpoofingCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 8),
    _GlobalRefusedSpoofingCount_Type()
)
globalRefusedSpoofingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedSpoofingCount.setStatus("current")
_GlobalRefusedCalloutCount_Type = Counter32
_GlobalRefusedCalloutCount_Object = MibScalar
globalRefusedCalloutCount = _GlobalRefusedCalloutCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 9),
    _GlobalRefusedCalloutCount_Type()
)
globalRefusedCalloutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedCalloutCount.setStatus("current")
_GlobalRefusedBadSenderCount_Type = Counter32
_GlobalRefusedBadSenderCount_Object = MibScalar
globalRefusedBadSenderCount = _GlobalRefusedBadSenderCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 10),
    _GlobalRefusedBadSenderCount_Type()
)
globalRefusedBadSenderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedBadSenderCount.setStatus("current")
_GlobalRefusedBackscatterCount_Type = Counter32
_GlobalRefusedBackscatterCount_Object = MibScalar
globalRefusedBackscatterCount = _GlobalRefusedBackscatterCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 11),
    _GlobalRefusedBackscatterCount_Type()
)
globalRefusedBackscatterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedBackscatterCount.setStatus("current")
_GlobalRefusedUnauthenticatedCount_Type = Counter32
_GlobalRefusedUnauthenticatedCount_Object = MibScalar
globalRefusedUnauthenticatedCount = _GlobalRefusedUnauthenticatedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 12),
    _GlobalRefusedUnauthenticatedCount_Type()
)
globalRefusedUnauthenticatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedUnauthenticatedCount.setStatus("current")
_GlobalRefusedUnencryptedCount_Type = Counter32
_GlobalRefusedUnencryptedCount_Object = MibScalar
globalRefusedUnencryptedCount = _GlobalRefusedUnencryptedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 13),
    _GlobalRefusedUnencryptedCount_Type()
)
globalRefusedUnencryptedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedUnencryptedCount.setStatus("current")
_GlobalRefusedBadDomainCount_Type = Counter32
_GlobalRefusedBadDomainCount_Object = MibScalar
globalRefusedBadDomainCount = _GlobalRefusedBadDomainCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 14),
    _GlobalRefusedBadDomainCount_Type()
)
globalRefusedBadDomainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedBadDomainCount.setStatus("current")
_GlobalRefusedBadSPFCount_Type = Counter32
_GlobalRefusedBadSPFCount_Object = MibScalar
globalRefusedBadSPFCount = _GlobalRefusedBadSPFCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 15),
    _GlobalRefusedBadSPFCount_Type()
)
globalRefusedBadSPFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedBadSPFCount.setStatus("current")
_GlobalRefusedBadRDNSCount_Type = Counter32
_GlobalRefusedBadRDNSCount_Object = MibScalar
globalRefusedBadRDNSCount = _GlobalRefusedBadRDNSCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 2, 16),
    _GlobalRefusedBadRDNSCount_Type()
)
globalRefusedBadRDNSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRefusedBadRDNSCount.setStatus("current")
_GlobalDelayedStatistics_ObjectIdentity = ObjectIdentity
globalDelayedStatistics = _GlobalDelayedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 3)
)
_GlobalDelayedCount_Type = Counter32
_GlobalDelayedCount_Object = MibScalar
globalDelayedCount = _GlobalDelayedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 3, 1),
    _GlobalDelayedCount_Type()
)
globalDelayedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDelayedCount.setStatus("current")
_GlobalDelayedRatelimitCount_Type = Counter32
_GlobalDelayedRatelimitCount_Object = MibScalar
globalDelayedRatelimitCount = _GlobalDelayedRatelimitCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 3, 2),
    _GlobalDelayedRatelimitCount_Type()
)
globalDelayedRatelimitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDelayedRatelimitCount.setStatus("current")
_GlobalDelayedGreylistCount_Type = Counter32
_GlobalDelayedGreylistCount_Object = MibScalar
globalDelayedGreylistCount = _GlobalDelayedGreylistCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 3, 3),
    _GlobalDelayedGreylistCount_Type()
)
globalDelayedGreylistCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDelayedGreylistCount.setStatus("current")
_GlobalRelayedStatistics_ObjectIdentity = ObjectIdentity
globalRelayedStatistics = _GlobalRelayedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 4)
)
_GlobalRelayedCount_Type = Counter32
_GlobalRelayedCount_Object = MibScalar
globalRelayedCount = _GlobalRelayedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 4, 1),
    _GlobalRelayedCount_Type()
)
globalRelayedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRelayedCount.setStatus("current")
_GlobalRelayedHostCount_Type = Counter32
_GlobalRelayedHostCount_Object = MibScalar
globalRelayedHostCount = _GlobalRelayedHostCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 4, 2),
    _GlobalRelayedHostCount_Type()
)
globalRelayedHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRelayedHostCount.setStatus("current")
_GlobalRelayedAuthenticatedCount_Type = Counter32
_GlobalRelayedAuthenticatedCount_Object = MibScalar
globalRelayedAuthenticatedCount = _GlobalRelayedAuthenticatedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 4, 3),
    _GlobalRelayedAuthenticatedCount_Type()
)
globalRelayedAuthenticatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRelayedAuthenticatedCount.setStatus("current")
_GlobalRelayedRefusedCount_Type = Counter32
_GlobalRelayedRefusedCount_Object = MibScalar
globalRelayedRefusedCount = _GlobalRelayedRefusedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 4, 4),
    _GlobalRelayedRefusedCount_Type()
)
globalRelayedRefusedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRelayedRefusedCount.setStatus("current")
_GlobalRelayedVirusCount_Type = Counter32
_GlobalRelayedVirusCount_Object = MibScalar
globalRelayedVirusCount = _GlobalRelayedVirusCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 4, 5),
    _GlobalRelayedVirusCount_Type()
)
globalRelayedVirusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRelayedVirusCount.setStatus("current")
_GlobalAcceptedStatistics_ObjectIdentity = ObjectIdentity
globalAcceptedStatistics = _GlobalAcceptedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 5)
)
_GlobalAcceptedCount_Type = Counter32
_GlobalAcceptedCount_Object = MibScalar
globalAcceptedCount = _GlobalAcceptedCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 1, 5, 1),
    _GlobalAcceptedCount_Type()
)
globalAcceptedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAcceptedCount.setStatus("current")
_DomainStatisticsTable_Object = MibTable
domainStatisticsTable = _DomainStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2)
)
if mibBuilder.loadTexts:
    domainStatisticsTable.setStatus("current")
_DomainStatisticsEntry_Object = MibTableRow
domainStatisticsEntry = _DomainStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1)
)
domainStatisticsEntry.setIndexNames(
    (0, "MAILCLEANER-MIB", "domainIndex"),
)
if mibBuilder.loadTexts:
    domainStatisticsEntry.setStatus("current")


class _DomainIndex_Type(Integer32):
    """Custom type domainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DomainIndex_Type.__name__ = "Integer32"
_DomainIndex_Object = MibTableColumn
domainIndex = _DomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 1),
    _DomainIndex_Type()
)
domainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainIndex.setStatus("current")
_DomainName_Type = DisplayString
_DomainName_Object = MibTableColumn
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 2),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("current")
_DomainMsgCount_Type = Counter32
_DomainMsgCount_Object = MibTableColumn
domainMsgCount = _DomainMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 3),
    _DomainMsgCount_Type()
)
domainMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainMsgCount.setStatus("current")
_DomainCleanCount_Type = Counter32
_DomainCleanCount_Object = MibTableColumn
domainCleanCount = _DomainCleanCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 4),
    _DomainCleanCount_Type()
)
domainCleanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainCleanCount.setStatus("current")
_DomainSpamCount_Type = Counter32
_DomainSpamCount_Object = MibTableColumn
domainSpamCount = _DomainSpamCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 5),
    _DomainSpamCount_Type()
)
domainSpamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainSpamCount.setStatus("current")
_DomainVirusCount_Type = Counter32
_DomainVirusCount_Object = MibTableColumn
domainVirusCount = _DomainVirusCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 6),
    _DomainVirusCount_Type()
)
domainVirusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainVirusCount.setStatus("current")
_DomainNameCount_Type = Counter32
_DomainNameCount_Object = MibTableColumn
domainNameCount = _DomainNameCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 7),
    _DomainNameCount_Type()
)
domainNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainNameCount.setStatus("current")
_DomainOtherCount_Type = Counter32
_DomainOtherCount_Object = MibTableColumn
domainOtherCount = _DomainOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 8),
    _DomainOtherCount_Type()
)
domainOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainOtherCount.setStatus("current")
_DomainSizeCount_Type = Counter32
_DomainSizeCount_Object = MibTableColumn
domainSizeCount = _DomainSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 9),
    _DomainSizeCount_Type()
)
domainSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainSizeCount.setStatus("current")
_DomainUserCount_Type = Counter32
_DomainUserCount_Object = MibTableColumn
domainUserCount = _DomainUserCount_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 10),
    _DomainUserCount_Type()
)
domainUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainUserCount.setStatus("current")
_DomainRefused_Type = Counter32
_DomainRefused_Object = MibTableColumn
domainRefused = _DomainRefused_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 11),
    _DomainRefused_Type()
)
domainRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefused.setStatus("current")
_DomainRefusedBATV_Type = Counter32
_DomainRefusedBATV_Object = MibTableColumn
domainRefusedBATV = _DomainRefusedBATV_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 12),
    _DomainRefusedBATV_Type()
)
domainRefusedBATV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefusedBATV.setStatus("current")
_DomainRefusedSpoof_Type = Counter32
_DomainRefusedSpoof_Object = MibTableColumn
domainRefusedSpoof = _DomainRefusedSpoof_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 13),
    _DomainRefusedSpoof_Type()
)
domainRefusedSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefusedSpoof.setStatus("current")
_DomainRefusedCallout_Type = Counter32
_DomainRefusedCallout_Object = MibTableColumn
domainRefusedCallout = _DomainRefusedCallout_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 14),
    _DomainRefusedCallout_Type()
)
domainRefusedCallout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefusedCallout.setStatus("current")
_DomainRefusedSender_Type = Counter32
_DomainRefusedSender_Object = MibTableColumn
domainRefusedSender = _DomainRefusedSender_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 15),
    _DomainRefusedSender_Type()
)
domainRefusedSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefusedSender.setStatus("current")
_DomainRefusedRBL_Type = Counter32
_DomainRefusedRBL_Object = MibTableColumn
domainRefusedRBL = _DomainRefusedRBL_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 16),
    _DomainRefusedRBL_Type()
)
domainRefusedRBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefusedRBL.setStatus("current")
_DomainRefusedBRBL_Type = Counter32
_DomainRefusedBRBL_Object = MibTableColumn
domainRefusedBRBL = _DomainRefusedBRBL_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 17),
    _DomainRefusedBRBL_Type()
)
domainRefusedBRBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefusedBRBL.setStatus("current")
_DomainDelayed_Type = Counter32
_DomainDelayed_Object = MibTableColumn
domainDelayed = _DomainDelayed_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 18),
    _DomainDelayed_Type()
)
domainDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainDelayed.setStatus("current")
_DomainDelayedGreylist_Type = Counter32
_DomainDelayedGreylist_Object = MibScalar
domainDelayedGreylist = _DomainDelayedGreylist_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 19),
    _DomainDelayedGreylist_Type()
)
domainDelayedGreylist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainDelayedGreylist.setStatus("current")
_DomainRefusedRDNS_Type = Counter32
_DomainRefusedRDNS_Object = MibScalar
domainRefusedRDNS = _DomainRefusedRDNS_Object(
    (1, 3, 6, 1, 4, 1, 36661, 3, 2, 1, 20),
    _DomainRefusedRDNS_Type()
)
domainRefusedRDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainRefusedRDNS.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAILCLEANER-MIB",
    **{"mailcleaner": mailcleaner,
       "status": status,
       "version": version,
       "fullVersion": fullVersion,
       "edition": edition,
       "currentVersion": currentVersion,
       "patchLevel": patchLevel,
       "spools": spools,
       "spoolIncoming": spoolIncoming,
       "spoolFiltering": spoolFiltering,
       "spoolOutgoing": spoolOutgoing,
       "processTable": processTable,
       "processEntry": processEntry,
       "processIndex": processIndex,
       "processName": processName,
       "processCount": processCount,
       "processStatus": processStatus,
       "configuration": configuration,
       "configIsMaster": configIsMaster,
       "statistics": statistics,
       "globalStatistics": globalStatistics,
       "globalProcessesStatistics": globalProcessesStatistics,
       "globalMsgCount": globalMsgCount,
       "globalCleanCount": globalCleanCount,
       "globalSpamCount": globalSpamCount,
       "globalVirusCount": globalVirusCount,
       "globalNameCount": globalNameCount,
       "globalOtherCount": globalOtherCount,
       "globalSizeCount": globalSizeCount,
       "globalUserCount": globalUserCount,
       "globalDomainCount": globalDomainCount,
       "globalRefusedStatistics": globalRefusedStatistics,
       "globalRefusedCount": globalRefusedCount,
       "globalRefusedRBLCount": globalRefusedRBLCount,
       "globalRefusedHostCount": globalRefusedHostCount,
       "globalRefusedRelayCount": globalRefusedRelayCount,
       "globalRefusedLocalpartCount": globalRefusedLocalpartCount,
       "globalRefusedBATVCount": globalRefusedBATVCount,
       "globalRefusedBlacklistedSenderCount": globalRefusedBlacklistedSenderCount,
       "globalRefusedSpoofingCount": globalRefusedSpoofingCount,
       "globalRefusedCalloutCount": globalRefusedCalloutCount,
       "globalRefusedBadSenderCount": globalRefusedBadSenderCount,
       "globalRefusedBackscatterCount": globalRefusedBackscatterCount,
       "globalRefusedUnauthenticatedCount": globalRefusedUnauthenticatedCount,
       "globalRefusedUnencryptedCount": globalRefusedUnencryptedCount,
       "globalRefusedBadDomainCount": globalRefusedBadDomainCount,
       "globalRefusedBadSPFCount": globalRefusedBadSPFCount,
       "globalRefusedBadRDNSCount": globalRefusedBadRDNSCount,
       "globalDelayedStatistics": globalDelayedStatistics,
       "globalDelayedCount": globalDelayedCount,
       "globalDelayedRatelimitCount": globalDelayedRatelimitCount,
       "globalDelayedGreylistCount": globalDelayedGreylistCount,
       "globalRelayedStatistics": globalRelayedStatistics,
       "globalRelayedCount": globalRelayedCount,
       "globalRelayedHostCount": globalRelayedHostCount,
       "globalRelayedAuthenticatedCount": globalRelayedAuthenticatedCount,
       "globalRelayedRefusedCount": globalRelayedRefusedCount,
       "globalRelayedVirusCount": globalRelayedVirusCount,
       "globalAcceptedStatistics": globalAcceptedStatistics,
       "globalAcceptedCount": globalAcceptedCount,
       "domainStatisticsTable": domainStatisticsTable,
       "domainStatisticsEntry": domainStatisticsEntry,
       "domainIndex": domainIndex,
       "domainName": domainName,
       "domainMsgCount": domainMsgCount,
       "domainCleanCount": domainCleanCount,
       "domainSpamCount": domainSpamCount,
       "domainVirusCount": domainVirusCount,
       "domainNameCount": domainNameCount,
       "domainOtherCount": domainOtherCount,
       "domainSizeCount": domainSizeCount,
       "domainUserCount": domainUserCount,
       "domainRefused": domainRefused,
       "domainRefusedBATV": domainRefusedBATV,
       "domainRefusedSpoof": domainRefusedSpoof,
       "domainRefusedCallout": domainRefusedCallout,
       "domainRefusedSender": domainRefusedSender,
       "domainRefusedRBL": domainRefusedRBL,
       "domainRefusedBRBL": domainRefusedBRBL,
       "domainDelayed": domainDelayed,
       "domainDelayedGreylist": domainDelayedGreylist,
       "domainRefusedRDNS": domainRefusedRDNS}
)
