# SNMP MIB module (DOCS-RPHY-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/DOCS-RPHY-STATS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:40:16 2025
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(IfDirection,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "IfDirection")

(docsRphyRpdDevInfoUniqueId,) = mibBuilder.importSymbols(
    "DOCS-RPHY-MIB",
    "docsRphyRpdDevInfoUniqueId")

(IANAPhysicalClass,) = mibBuilder.importSymbols(
    "IANA-ENTITY-MIB",
    "IANAPhysicalClass")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber",
    "InetVersion")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(UUIDorZero,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUIDorZero")


# MODULE-IDENTITY

docsRphyStatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33)
)
if mibBuilder.loadTexts:
    docsRphyStatsMib.setRevisions(
        ("2017-10-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsRphyStatsNotifications_ObjectIdentity = ObjectIdentity
docsRphyStatsNotifications = _DocsRphyStatsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 0)
)
_DocsRphyStatsObjects_ObjectIdentity = ObjectIdentity
docsRphyStatsObjects = _DocsRphyStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1)
)
_DocsRphyStatsRpdMibObjects_ObjectIdentity = ObjectIdentity
docsRphyStatsRpdMibObjects = _DocsRphyStatsRpdMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1)
)
_DocsRphyStatsRpdDsMibObjects_ObjectIdentity = ObjectIdentity
docsRphyStatsRpdDsMibObjects = _DocsRphyStatsRpdDsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1)
)
_DocsRphyStatsRpdDsScQamPerfStatsTable_Object = MibTable
docsRphyStatsRpdDsScQamPerfStatsTable = _DocsRphyStatsRpdDsScQamPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsScQamPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdDsScQamPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdDsScQamPerfStatsEntry = _DocsRphyStatsRpdDsScQamPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 1, 1)
)
docsRphyStatsRpdDsScQamPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsScQamPerfStatsCoreIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsScQamPerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdDsScQamPerfStatsCoreIfIndex_Type = InterfaceIndex
_DocsRphyStatsRpdDsScQamPerfStatsCoreIfIndex_Object = MibTableColumn
docsRphyStatsRpdDsScQamPerfStatsCoreIfIndex = _DocsRphyStatsRpdDsScQamPerfStatsCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 1, 1, 1),
    _DocsRphyStatsRpdDsScQamPerfStatsCoreIfIndex_Type()
)
docsRphyStatsRpdDsScQamPerfStatsCoreIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsScQamPerfStatsCoreIfIndex.setStatus("current")
_DocsRphyStatsRpdDsScQamPerfStatsOutDiscards_Type = Counter64
_DocsRphyStatsRpdDsScQamPerfStatsOutDiscards_Object = MibTableColumn
docsRphyStatsRpdDsScQamPerfStatsOutDiscards = _DocsRphyStatsRpdDsScQamPerfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 1, 1, 2),
    _DocsRphyStatsRpdDsScQamPerfStatsOutDiscards_Type()
)
docsRphyStatsRpdDsScQamPerfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsScQamPerfStatsOutDiscards.setStatus("current")
_DocsRphyStatsRpdDsScQamPerfStatsOutErrors_Type = Counter64
_DocsRphyStatsRpdDsScQamPerfStatsOutErrors_Object = MibTableColumn
docsRphyStatsRpdDsScQamPerfStatsOutErrors = _DocsRphyStatsRpdDsScQamPerfStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 1, 1, 3),
    _DocsRphyStatsRpdDsScQamPerfStatsOutErrors_Type()
)
docsRphyStatsRpdDsScQamPerfStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsScQamPerfStatsOutErrors.setStatus("current")
_DocsRphyStatsRpdDsScQamPerfStatsOutPackets_Type = Counter64
_DocsRphyStatsRpdDsScQamPerfStatsOutPackets_Object = MibTableColumn
docsRphyStatsRpdDsScQamPerfStatsOutPackets = _DocsRphyStatsRpdDsScQamPerfStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 1, 1, 4),
    _DocsRphyStatsRpdDsScQamPerfStatsOutPackets_Type()
)
docsRphyStatsRpdDsScQamPerfStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsScQamPerfStatsOutPackets.setStatus("current")
_DocsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime = _DocsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 1, 1, 5),
    _DocsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime_Type()
)
docsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdDsOfdmPerfStatsTable_Object = MibTable
docsRphyStatsRpdDsOfdmPerfStatsTable = _DocsRphyStatsRpdDsOfdmPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdDsOfdmPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdDsOfdmPerfStatsEntry = _DocsRphyStatsRpdDsOfdmPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 2, 1)
)
docsRphyStatsRpdDsOfdmPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex_Type = InterfaceIndex
_DocsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex = _DocsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 2, 1, 1),
    _DocsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex_Type()
)
docsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex.setStatus("current")
_DocsRphyStatsRpdDsOfdmPerfStatsOutDiscards_Type = Counter64
_DocsRphyStatsRpdDsOfdmPerfStatsOutDiscards_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPerfStatsOutDiscards = _DocsRphyStatsRpdDsOfdmPerfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 2, 1, 2),
    _DocsRphyStatsRpdDsOfdmPerfStatsOutDiscards_Type()
)
docsRphyStatsRpdDsOfdmPerfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPerfStatsOutDiscards.setStatus("current")
_DocsRphyStatsRpdDsOfdmPerfStatsOutErrors_Type = Counter64
_DocsRphyStatsRpdDsOfdmPerfStatsOutErrors_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPerfStatsOutErrors = _DocsRphyStatsRpdDsOfdmPerfStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 2, 1, 3),
    _DocsRphyStatsRpdDsOfdmPerfStatsOutErrors_Type()
)
docsRphyStatsRpdDsOfdmPerfStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPerfStatsOutErrors.setStatus("current")
_DocsRphyStatsRpdDsOfdmPerfStatsOutPackets_Type = Counter64
_DocsRphyStatsRpdDsOfdmPerfStatsOutPackets_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPerfStatsOutPackets = _DocsRphyStatsRpdDsOfdmPerfStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 2, 1, 4),
    _DocsRphyStatsRpdDsOfdmPerfStatsOutPackets_Type()
)
docsRphyStatsRpdDsOfdmPerfStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPerfStatsOutPackets.setStatus("current")
_DocsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime = _DocsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 2, 1, 5),
    _DocsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime_Type()
)
docsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdDsOob551PerfStatsTable_Object = MibTable
docsRphyStatsRpdDsOob551PerfStatsTable = _DocsRphyStatsRpdDsOob551PerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob551PerfStatsTable.setStatus("current")
_DocsRphyStatsRpdDsOob551PerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdDsOob551PerfStatsEntry = _DocsRphyStatsRpdDsOob551PerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 3, 1)
)
docsRphyStatsRpdDsOob551PerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob551PerfStatsCoreIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob551PerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdDsOob551PerfStatsCoreIfIndex_Type = InterfaceIndex
_DocsRphyStatsRpdDsOob551PerfStatsCoreIfIndex_Object = MibTableColumn
docsRphyStatsRpdDsOob551PerfStatsCoreIfIndex = _DocsRphyStatsRpdDsOob551PerfStatsCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 3, 1, 1),
    _DocsRphyStatsRpdDsOob551PerfStatsCoreIfIndex_Type()
)
docsRphyStatsRpdDsOob551PerfStatsCoreIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob551PerfStatsCoreIfIndex.setStatus("current")
_DocsRphyStatsRpdDsOob551PerfStatsOutDiscards_Type = Counter64
_DocsRphyStatsRpdDsOob551PerfStatsOutDiscards_Object = MibTableColumn
docsRphyStatsRpdDsOob551PerfStatsOutDiscards = _DocsRphyStatsRpdDsOob551PerfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 3, 1, 2),
    _DocsRphyStatsRpdDsOob551PerfStatsOutDiscards_Type()
)
docsRphyStatsRpdDsOob551PerfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob551PerfStatsOutDiscards.setStatus("current")
_DocsRphyStatsRpdDsOob551PerfStatsOutErrors_Type = Counter64
_DocsRphyStatsRpdDsOob551PerfStatsOutErrors_Object = MibTableColumn
docsRphyStatsRpdDsOob551PerfStatsOutErrors = _DocsRphyStatsRpdDsOob551PerfStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 3, 1, 3),
    _DocsRphyStatsRpdDsOob551PerfStatsOutErrors_Type()
)
docsRphyStatsRpdDsOob551PerfStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob551PerfStatsOutErrors.setStatus("current")
_DocsRphyStatsRpdDsOob551PerfStatsOutPackets_Type = Counter64
_DocsRphyStatsRpdDsOob551PerfStatsOutPackets_Object = MibTableColumn
docsRphyStatsRpdDsOob551PerfStatsOutPackets = _DocsRphyStatsRpdDsOob551PerfStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 3, 1, 4),
    _DocsRphyStatsRpdDsOob551PerfStatsOutPackets_Type()
)
docsRphyStatsRpdDsOob551PerfStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob551PerfStatsOutPackets.setStatus("current")
_DocsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime = _DocsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 3, 1, 5),
    _DocsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime_Type()
)
docsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdDsOob552PerfStatsTable_Object = MibTable
docsRphyStatsRpdDsOob552PerfStatsTable = _DocsRphyStatsRpdDsOob552PerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob552PerfStatsTable.setStatus("current")
_DocsRphyStatsRpdDsOob552PerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdDsOob552PerfStatsEntry = _DocsRphyStatsRpdDsOob552PerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 4, 1)
)
docsRphyStatsRpdDsOob552PerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob552PerfStatsCoreIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob552PerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdDsOob552PerfStatsCoreIfIndex_Type = InterfaceIndex
_DocsRphyStatsRpdDsOob552PerfStatsCoreIfIndex_Object = MibTableColumn
docsRphyStatsRpdDsOob552PerfStatsCoreIfIndex = _DocsRphyStatsRpdDsOob552PerfStatsCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 4, 1, 1),
    _DocsRphyStatsRpdDsOob552PerfStatsCoreIfIndex_Type()
)
docsRphyStatsRpdDsOob552PerfStatsCoreIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob552PerfStatsCoreIfIndex.setStatus("current")
_DocsRphyStatsRpdDsOob552PerfStatsOutDiscards_Type = Counter64
_DocsRphyStatsRpdDsOob552PerfStatsOutDiscards_Object = MibTableColumn
docsRphyStatsRpdDsOob552PerfStatsOutDiscards = _DocsRphyStatsRpdDsOob552PerfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 4, 1, 2),
    _DocsRphyStatsRpdDsOob552PerfStatsOutDiscards_Type()
)
docsRphyStatsRpdDsOob552PerfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob552PerfStatsOutDiscards.setStatus("current")
_DocsRphyStatsRpdDsOob552PerfStatsOutErrors_Type = Counter64
_DocsRphyStatsRpdDsOob552PerfStatsOutErrors_Object = MibTableColumn
docsRphyStatsRpdDsOob552PerfStatsOutErrors = _DocsRphyStatsRpdDsOob552PerfStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 4, 1, 3),
    _DocsRphyStatsRpdDsOob552PerfStatsOutErrors_Type()
)
docsRphyStatsRpdDsOob552PerfStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob552PerfStatsOutErrors.setStatus("current")
_DocsRphyStatsRpdDsOob552PerfStatsOutPackets_Type = Counter64
_DocsRphyStatsRpdDsOob552PerfStatsOutPackets_Object = MibTableColumn
docsRphyStatsRpdDsOob552PerfStatsOutPackets = _DocsRphyStatsRpdDsOob552PerfStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 4, 1, 4),
    _DocsRphyStatsRpdDsOob552PerfStatsOutPackets_Type()
)
docsRphyStatsRpdDsOob552PerfStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob552PerfStatsOutPackets.setStatus("current")
_DocsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime = _DocsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 4, 1, 5),
    _DocsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime_Type()
)
docsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdDsNdfPerfStatsTable_Object = MibTable
docsRphyStatsRpdDsNdfPerfStatsTable = _DocsRphyStatsRpdDsNdfPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsNdfPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdDsNdfPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdDsNdfPerfStatsEntry = _DocsRphyStatsRpdDsNdfPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 5, 1)
)
docsRphyStatsRpdDsNdfPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsNdfPerfStatsCoreIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsNdfPerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdDsNdfPerfStatsCoreIfIndex_Type = InterfaceIndex
_DocsRphyStatsRpdDsNdfPerfStatsCoreIfIndex_Object = MibTableColumn
docsRphyStatsRpdDsNdfPerfStatsCoreIfIndex = _DocsRphyStatsRpdDsNdfPerfStatsCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 5, 1, 1),
    _DocsRphyStatsRpdDsNdfPerfStatsCoreIfIndex_Type()
)
docsRphyStatsRpdDsNdfPerfStatsCoreIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsNdfPerfStatsCoreIfIndex.setStatus("current")
_DocsRphyStatsRpdDsNdfPerfStatsOutDiscards_Type = Counter64
_DocsRphyStatsRpdDsNdfPerfStatsOutDiscards_Object = MibTableColumn
docsRphyStatsRpdDsNdfPerfStatsOutDiscards = _DocsRphyStatsRpdDsNdfPerfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 5, 1, 2),
    _DocsRphyStatsRpdDsNdfPerfStatsOutDiscards_Type()
)
docsRphyStatsRpdDsNdfPerfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsNdfPerfStatsOutDiscards.setStatus("current")
_DocsRphyStatsRpdDsNdfPerfStatsOutErrors_Type = Counter64
_DocsRphyStatsRpdDsNdfPerfStatsOutErrors_Object = MibTableColumn
docsRphyStatsRpdDsNdfPerfStatsOutErrors = _DocsRphyStatsRpdDsNdfPerfStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 5, 1, 3),
    _DocsRphyStatsRpdDsNdfPerfStatsOutErrors_Type()
)
docsRphyStatsRpdDsNdfPerfStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsNdfPerfStatsOutErrors.setStatus("current")
_DocsRphyStatsRpdDsNdfPerfStatsOutPackets_Type = Counter64
_DocsRphyStatsRpdDsNdfPerfStatsOutPackets_Object = MibTableColumn
docsRphyStatsRpdDsNdfPerfStatsOutPackets = _DocsRphyStatsRpdDsNdfPerfStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 5, 1, 4),
    _DocsRphyStatsRpdDsNdfPerfStatsOutPackets_Type()
)
docsRphyStatsRpdDsNdfPerfStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsNdfPerfStatsOutPackets.setStatus("current")
_DocsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime = _DocsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 5, 1, 5),
    _DocsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime_Type()
)
docsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdDsOfdmPlcPerfStatsTable_Object = MibTable
docsRphyStatsRpdDsOfdmPlcPerfStatsTable = _DocsRphyStatsRpdDsOfdmPlcPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPlcPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdDsOfdmPlcPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdDsOfdmPlcPerfStatsEntry = _DocsRphyStatsRpdDsOfdmPlcPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPlcPerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards_Type = Counter64
_DocsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards = _DocsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 6, 1, 1),
    _DocsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards_Type()
)
docsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards.setStatus("current")
_DocsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors_Type = Counter64
_DocsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors = _DocsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 6, 1, 2),
    _DocsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors_Type()
)
docsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors.setStatus("current")
_DocsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets_Type = Counter64
_DocsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets = _DocsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 6, 1, 3),
    _DocsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets_Type()
)
docsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets.setStatus("current")
_DocsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime = _DocsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 6, 1, 4),
    _DocsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime_Type()
)
docsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdDsOfdmProfilePerfStatsTable_Object = MibTable
docsRphyStatsRpdDsOfdmProfilePerfStatsTable = _DocsRphyStatsRpdDsOfdmProfilePerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmProfilePerfStatsTable.setStatus("current")
_DocsRphyStatsRpdDsOfdmProfilePerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdDsOfdmProfilePerfStatsEntry = _DocsRphyStatsRpdDsOfdmProfilePerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 7, 1)
)
docsRphyStatsRpdDsOfdmProfilePerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmProfilePerfStatsEntry.setStatus("current")


class _DocsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex_Type(Unsigned32):
    """Custom type docsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex_Type.__name__ = "Unsigned32"
_DocsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex_Object = MibTableColumn
docsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex = _DocsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 7, 1, 1),
    _DocsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex_Type()
)
docsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex.setStatus("current")
_DocsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords_Type = Counter64
_DocsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords_Object = MibTableColumn
docsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords = _DocsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 1, 7, 1, 2),
    _DocsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords_Type()
)
docsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords.setStatus("current")
_DocsRphyStatsRpdUsMibObjects_ObjectIdentity = ObjectIdentity
docsRphyStatsRpdUsMibObjects = _DocsRphyStatsRpdUsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2)
)
_DocsRphyStatsRpdUsOfdmaChanPerfStatsTable_Object = MibTable
docsRphyStatsRpdUsOfdmaChanPerfStatsTable = _DocsRphyStatsRpdUsOfdmaChanPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdUsOfdmaChanPerfStatsEntry = _DocsRphyStatsRpdUsOfdmaChanPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1)
)
docsRphyStatsRpdUsOfdmaChanPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex_Type = InterfaceIndex
_DocsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex = _DocsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1, 1),
    _DocsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex_Type()
)
docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants_Type = Counter64
_DocsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants = _DocsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1, 2),
    _DocsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants_Type()
)
docsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors_Type = Counter64
_DocsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors = _DocsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1, 3),
    _DocsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors_Type()
)
docsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps_Type = Counter64
_DocsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps = _DocsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1, 4),
    _DocsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps_Type()
)
docsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps_Type = Counter64
_DocsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps = _DocsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1, 5),
    _DocsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps_Type()
)
docsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests_Type = Counter64
_DocsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests = _DocsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1, 6),
    _DocsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests_Type()
)
docsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests.setStatus("current")
_DocsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime = _DocsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 1, 1, 7),
    _DocsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime_Type()
)
docsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdUsScQamChanPerfStatsTable_Object = MibTable
docsRphyStatsRpdUsScQamChanPerfStatsTable = _DocsRphyStatsRpdUsScQamChanPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdUsScQamChanPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdUsScQamChanPerfStatsEntry = _DocsRphyStatsRpdUsScQamChanPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1)
)
docsRphyStatsRpdUsScQamChanPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsEntry.setStatus("current")
_DocsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex_Type = InterfaceIndex
_DocsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex_Object = MibTableColumn
docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex = _DocsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1, 1),
    _DocsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex_Type()
)
docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex.setStatus("current")


class _DocsRphyStatsRpdUsScQamChanPerfStatsChanSnr_Type(Unsigned32):
    """Custom type docsRphyStatsRpdUsScQamChanPerfStatsChanSnr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsRphyStatsRpdUsScQamChanPerfStatsChanSnr_Type.__name__ = "Unsigned32"
_DocsRphyStatsRpdUsScQamChanPerfStatsChanSnr_Object = MibTableColumn
docsRphyStatsRpdUsScQamChanPerfStatsChanSnr = _DocsRphyStatsRpdUsScQamChanPerfStatsChanSnr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1, 2),
    _DocsRphyStatsRpdUsScQamChanPerfStatsChanSnr_Type()
)
docsRphyStatsRpdUsScQamChanPerfStatsChanSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsChanSnr.setStatus("current")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsChanSnr.setUnits("TenthdB")
_DocsRphyStatsRpdUsScQamChanPerfStatsHcsErrors_Type = Counter64
_DocsRphyStatsRpdUsScQamChanPerfStatsHcsErrors_Object = MibTableColumn
docsRphyStatsRpdUsScQamChanPerfStatsHcsErrors = _DocsRphyStatsRpdUsScQamChanPerfStatsHcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1, 3),
    _DocsRphyStatsRpdUsScQamChanPerfStatsHcsErrors_Type()
)
docsRphyStatsRpdUsScQamChanPerfStatsHcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsHcsErrors.setStatus("current")
_DocsRphyStatsRpdUsScQamChanPerfStatsLateMaps_Type = Counter64
_DocsRphyStatsRpdUsScQamChanPerfStatsLateMaps_Object = MibTableColumn
docsRphyStatsRpdUsScQamChanPerfStatsLateMaps = _DocsRphyStatsRpdUsScQamChanPerfStatsLateMaps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1, 4),
    _DocsRphyStatsRpdUsScQamChanPerfStatsLateMaps_Type()
)
docsRphyStatsRpdUsScQamChanPerfStatsLateMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsLateMaps.setStatus("current")
_DocsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps_Type = Counter64
_DocsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps_Object = MibTableColumn
docsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps = _DocsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1, 5),
    _DocsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps_Type()
)
docsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps.setStatus("current")
_DocsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests_Type = Counter64
_DocsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests_Object = MibTableColumn
docsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests = _DocsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1, 6),
    _DocsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests_Type()
)
docsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests.setStatus("current")
_DocsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime_Type = TimeStamp
_DocsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime_Object = MibTableColumn
docsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime = _DocsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 2, 1, 7),
    _DocsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime_Type()
)
docsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsTable_Object = MibTable
docsRphyStatsRpdUsOfdmaLowIucPerfStatsTable = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdUsOfdmaLowIucPerfStatsEntry = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1)
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsEntry.setStatus("current")


class _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc_Type(Unsigned32):
    """Custom type docsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc_Type.__name__ = "Unsigned32"
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 1),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 2),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 3),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 4),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 5),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 6),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 7),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 8),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 9),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 10),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 11),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy.setStatus("current")
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors_Type = Counter64
_DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors = _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 3, 1, 12),
    _DocsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors_Type()
)
docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsTable_Object = MibTable
docsRphyStatsRpdUsOfdmaHighIucPerfStatsTable = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdUsOfdmaHighIucPerfStatsEntry = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1)
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsEntry.setStatus("current")


class _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc_Type(Unsigned32):
    """Custom type docsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc_Type.__name__ = "Unsigned32"
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 1),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 2),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 3),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 4),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 5),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 6),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 7),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 8),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts.setStatus("current")
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts_Type = Counter64
_DocsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts_Object = MibTableColumn
docsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts = _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 4, 1, 9),
    _DocsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts_Type()
)
docsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsTable_Object = MibTable
docsRphyStatsRpdUsScQamLowIucPerfStatsTable = _DocsRphyStatsRpdUsScQamLowIucPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdUsScQamLowIucPerfStatsEntry = _DocsRphyStatsRpdUsScQamLowIucPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1)
)
docsRphyStatsRpdUsScQamLowIucPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsEntry.setStatus("current")


class _DocsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc_Type(Unsigned32):
    """Custom type docsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc_Type.__name__ = "Unsigned32"
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc = _DocsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 1),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw = _DocsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 2),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw = _DocsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 3),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw = _DocsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 4),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities = _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 5),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions = _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 6),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy = _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 7),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors = _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 8),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities = _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 9),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions = _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 10),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy = _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 11),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy.setStatus("current")
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors_Type = Counter64
_DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors_Object = MibTableColumn
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors = _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 5, 1, 12),
    _DocsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors_Type()
)
docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsTable_Object = MibTable
docsRphyStatsRpdUsScQamHighIucPerfStatsTable = _DocsRphyStatsRpdUsScQamHighIucPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsTable.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsEntry_Object = MibTableRow
docsRphyStatsRpdUsScQamHighIucPerfStatsEntry = _DocsRphyStatsRpdUsScQamHighIucPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1)
)
docsRphyStatsRpdUsScQamHighIucPerfStatsEntry.setIndexNames(
    (0, "DOCS-RPHY-MIB", "docsRphyRpdDevInfoUniqueId"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex"),
    (0, "DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc"),
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsEntry.setStatus("current")


class _DocsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc_Type(Unsigned32):
    """Custom type docsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc_Type.__name__ = "Unsigned32"
_DocsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc = _DocsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 1),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw_Type = Counter64
_DocsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw = _DocsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 2),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw_Type = Counter64
_DocsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw = _DocsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 3),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw_Type = Counter64
_DocsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw = _DocsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 4),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants_Type = Counter64
_DocsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants = _DocsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 5),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts_Type = Counter64
_DocsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts = _DocsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 6),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts_Type = Counter64
_DocsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts = _DocsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 7),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts.setStatus("current")
_DocsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts_Type = Counter64
_DocsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts_Object = MibTableColumn
docsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts = _DocsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 1, 2, 6, 1, 8),
    _DocsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts_Type()
)
docsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts.setStatus("current")
_DocsRphyStatsCcapMibObjects_ObjectIdentity = ObjectIdentity
docsRphyStatsCcapMibObjects = _DocsRphyStatsCcapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 1, 2)
)
_DocsRphyStatsConformance_ObjectIdentity = ObjectIdentity
docsRphyStatsConformance = _DocsRphyStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 2)
)
_DocsRphyStatsCompliances_ObjectIdentity = ObjectIdentity
docsRphyStatsCompliances = _DocsRphyStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 2, 1)
)
_DocsRphyStatsGroups_ObjectIdentity = ObjectIdentity
docsRphyStatsGroups = _DocsRphyStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 2, 2)
)
docsRphyStatsRpdDsOfdmPerfStatsEntry.registerAugmentions(
    ("DOCS-RPHY-STATS-MIB",
     "docsRphyStatsRpdDsOfdmPlcPerfStatsEntry")
)
docsRphyStatsRpdDsOfdmPlcPerfStatsEntry.setIndexNames(*docsRphyStatsRpdDsOfdmPerfStatsEntry.getIndexNames())

# Managed Objects groups

docsRphyStatsRpdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 2, 2, 1)
)
docsRphyStatsRpdGroup.setObjects(
      *(("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsScQamPerfStatsOutDiscards"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsScQamPerfStatsOutErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsScQamPerfStatsOutPackets"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPerfStatsOutDiscards"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPerfStatsOutErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPerfStatsOutPackets"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob551PerfStatsOutDiscards"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob551PerfStatsOutErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob551PerfStatsOutPackets"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob552PerfStatsOutDiscards"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob552PerfStatsOutErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob552PerfStatsOutPackets"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsNdfPerfStatsOutDiscards"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsNdfPerfStatsOutErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsNdfPerfStatsOutPackets"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsChanSnr"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsHcsErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsLateMaps"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts"),
        ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts"))
)
if mibBuilder.loadTexts:
    docsRphyStatsRpdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsRphyStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 33, 2, 1, 1)
)
docsRphyStatsCompliance.setObjects(
    ("DOCS-RPHY-STATS-MIB", "docsRphyStatsRpdGroup")
)
if mibBuilder.loadTexts:
    docsRphyStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-RPHY-STATS-MIB",
    **{"docsRphyStatsMib": docsRphyStatsMib,
       "docsRphyStatsNotifications": docsRphyStatsNotifications,
       "docsRphyStatsObjects": docsRphyStatsObjects,
       "docsRphyStatsRpdMibObjects": docsRphyStatsRpdMibObjects,
       "docsRphyStatsRpdDsMibObjects": docsRphyStatsRpdDsMibObjects,
       "docsRphyStatsRpdDsScQamPerfStatsTable": docsRphyStatsRpdDsScQamPerfStatsTable,
       "docsRphyStatsRpdDsScQamPerfStatsEntry": docsRphyStatsRpdDsScQamPerfStatsEntry,
       "docsRphyStatsRpdDsScQamPerfStatsCoreIfIndex": docsRphyStatsRpdDsScQamPerfStatsCoreIfIndex,
       "docsRphyStatsRpdDsScQamPerfStatsOutDiscards": docsRphyStatsRpdDsScQamPerfStatsOutDiscards,
       "docsRphyStatsRpdDsScQamPerfStatsOutErrors": docsRphyStatsRpdDsScQamPerfStatsOutErrors,
       "docsRphyStatsRpdDsScQamPerfStatsOutPackets": docsRphyStatsRpdDsScQamPerfStatsOutPackets,
       "docsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime": docsRphyStatsRpdDsScQamPerfStatsRpdDsCounterDiscTime,
       "docsRphyStatsRpdDsOfdmPerfStatsTable": docsRphyStatsRpdDsOfdmPerfStatsTable,
       "docsRphyStatsRpdDsOfdmPerfStatsEntry": docsRphyStatsRpdDsOfdmPerfStatsEntry,
       "docsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex": docsRphyStatsRpdDsOfdmPerfStatsCoreIfIndex,
       "docsRphyStatsRpdDsOfdmPerfStatsOutDiscards": docsRphyStatsRpdDsOfdmPerfStatsOutDiscards,
       "docsRphyStatsRpdDsOfdmPerfStatsOutErrors": docsRphyStatsRpdDsOfdmPerfStatsOutErrors,
       "docsRphyStatsRpdDsOfdmPerfStatsOutPackets": docsRphyStatsRpdDsOfdmPerfStatsOutPackets,
       "docsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime": docsRphyStatsRpdDsOfdmPerfStatsRpdDsCounterDiscTime,
       "docsRphyStatsRpdDsOob551PerfStatsTable": docsRphyStatsRpdDsOob551PerfStatsTable,
       "docsRphyStatsRpdDsOob551PerfStatsEntry": docsRphyStatsRpdDsOob551PerfStatsEntry,
       "docsRphyStatsRpdDsOob551PerfStatsCoreIfIndex": docsRphyStatsRpdDsOob551PerfStatsCoreIfIndex,
       "docsRphyStatsRpdDsOob551PerfStatsOutDiscards": docsRphyStatsRpdDsOob551PerfStatsOutDiscards,
       "docsRphyStatsRpdDsOob551PerfStatsOutErrors": docsRphyStatsRpdDsOob551PerfStatsOutErrors,
       "docsRphyStatsRpdDsOob551PerfStatsOutPackets": docsRphyStatsRpdDsOob551PerfStatsOutPackets,
       "docsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime": docsRphyStatsRpdDsOob551PerfStatsRpdDsCounterDiscTime,
       "docsRphyStatsRpdDsOob552PerfStatsTable": docsRphyStatsRpdDsOob552PerfStatsTable,
       "docsRphyStatsRpdDsOob552PerfStatsEntry": docsRphyStatsRpdDsOob552PerfStatsEntry,
       "docsRphyStatsRpdDsOob552PerfStatsCoreIfIndex": docsRphyStatsRpdDsOob552PerfStatsCoreIfIndex,
       "docsRphyStatsRpdDsOob552PerfStatsOutDiscards": docsRphyStatsRpdDsOob552PerfStatsOutDiscards,
       "docsRphyStatsRpdDsOob552PerfStatsOutErrors": docsRphyStatsRpdDsOob552PerfStatsOutErrors,
       "docsRphyStatsRpdDsOob552PerfStatsOutPackets": docsRphyStatsRpdDsOob552PerfStatsOutPackets,
       "docsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime": docsRphyStatsRpdDsOob552PerfStatsRpdDsCounterDiscTime,
       "docsRphyStatsRpdDsNdfPerfStatsTable": docsRphyStatsRpdDsNdfPerfStatsTable,
       "docsRphyStatsRpdDsNdfPerfStatsEntry": docsRphyStatsRpdDsNdfPerfStatsEntry,
       "docsRphyStatsRpdDsNdfPerfStatsCoreIfIndex": docsRphyStatsRpdDsNdfPerfStatsCoreIfIndex,
       "docsRphyStatsRpdDsNdfPerfStatsOutDiscards": docsRphyStatsRpdDsNdfPerfStatsOutDiscards,
       "docsRphyStatsRpdDsNdfPerfStatsOutErrors": docsRphyStatsRpdDsNdfPerfStatsOutErrors,
       "docsRphyStatsRpdDsNdfPerfStatsOutPackets": docsRphyStatsRpdDsNdfPerfStatsOutPackets,
       "docsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime": docsRphyStatsRpdDsNdfPerfStatsRpdDsCounterDiscTime,
       "docsRphyStatsRpdDsOfdmPlcPerfStatsTable": docsRphyStatsRpdDsOfdmPlcPerfStatsTable,
       "docsRphyStatsRpdDsOfdmPlcPerfStatsEntry": docsRphyStatsRpdDsOfdmPlcPerfStatsEntry,
       "docsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards": docsRphyStatsRpdDsOfdmPlcPerfStatsOutDiscards,
       "docsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors": docsRphyStatsRpdDsOfdmPlcPerfStatsOutErrors,
       "docsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets": docsRphyStatsRpdDsOfdmPlcPerfStatsOutPackets,
       "docsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime": docsRphyStatsRpdDsOfdmPlcPerfStatsRpdDsCounterDiscTime,
       "docsRphyStatsRpdDsOfdmProfilePerfStatsTable": docsRphyStatsRpdDsOfdmProfilePerfStatsTable,
       "docsRphyStatsRpdDsOfdmProfilePerfStatsEntry": docsRphyStatsRpdDsOfdmProfilePerfStatsEntry,
       "docsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex": docsRphyStatsRpdDsOfdmProfilePerfStatsProfileIndex,
       "docsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords": docsRphyStatsRpdDsOfdmProfilePerfStatsOutCodewords,
       "docsRphyStatsRpdUsMibObjects": docsRphyStatsRpdUsMibObjects,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsTable": docsRphyStatsRpdUsOfdmaChanPerfStatsTable,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsEntry": docsRphyStatsRpdUsOfdmaChanPerfStatsEntry,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex": docsRphyStatsRpdUsOfdmaChanPerfStatsCoreIfIndex,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants": docsRphyStatsRpdUsOfdmaChanPerfStatsProbeGrants,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors": docsRphyStatsRpdUsOfdmaChanPerfStatsHcsErrors,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps": docsRphyStatsRpdUsOfdmaChanPerfStatsLateMaps,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps": docsRphyStatsRpdUsOfdmaChanPerfStatsIllegalMaps,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests": docsRphyStatsRpdUsOfdmaChanPerfStatsDiscardedRequests,
       "docsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime": docsRphyStatsRpdUsOfdmaChanPerfStatsRpdUsCounterDiscTime,
       "docsRphyStatsRpdUsScQamChanPerfStatsTable": docsRphyStatsRpdUsScQamChanPerfStatsTable,
       "docsRphyStatsRpdUsScQamChanPerfStatsEntry": docsRphyStatsRpdUsScQamChanPerfStatsEntry,
       "docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex": docsRphyStatsRpdUsScQamChanPerfStatsCoreIfIndex,
       "docsRphyStatsRpdUsScQamChanPerfStatsChanSnr": docsRphyStatsRpdUsScQamChanPerfStatsChanSnr,
       "docsRphyStatsRpdUsScQamChanPerfStatsHcsErrors": docsRphyStatsRpdUsScQamChanPerfStatsHcsErrors,
       "docsRphyStatsRpdUsScQamChanPerfStatsLateMaps": docsRphyStatsRpdUsScQamChanPerfStatsLateMaps,
       "docsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps": docsRphyStatsRpdUsScQamChanPerfStatsIllegalMaps,
       "docsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests": docsRphyStatsRpdUsScQamChanPerfStatsDiscardedRequests,
       "docsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime": docsRphyStatsRpdUsScQamChanPerfStatsRpdUsCounterDiscTime,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsTable": docsRphyStatsRpdUsOfdmaLowIucPerfStatsTable,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsEntry": docsRphyStatsRpdUsOfdmaLowIucPerfStatsEntry,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc": docsRphyStatsRpdUsOfdmaLowIucPerfStatsUsIuc,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass": docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPredecodePass,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass": docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodePass,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail": docsRphyStatsRpdUsOfdmaLowIucPerfStatsNumPostdecodeFail,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities": docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpportunities,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions": docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpCollisions,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy": docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpNoEnergy,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors": docsRphyStatsRpdUsOfdmaLowIucPerfStatsUnicastOpErrors,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities": docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpportunities,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions": docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpCollisions,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy": docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpNoEnergy,
       "docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors": docsRphyStatsRpdUsOfdmaLowIucPerfStatsMulticastOpErrors,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsTable": docsRphyStatsRpdUsOfdmaHighIucPerfStatsTable,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsEntry": docsRphyStatsRpdUsOfdmaHighIucPerfStatsEntry,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc": docsRphyStatsRpdUsOfdmaHighIucPerfStatsUsIuc,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer": docsRphyStatsRpdUsOfdmaHighIucPerfStatsAverageMer,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass": docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPredecodePass,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass": docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodePass,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail": docsRphyStatsRpdUsOfdmaHighIucPerfStatsNumPostdecodeFail,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants": docsRphyStatsRpdUsOfdmaHighIucPerfStatsScheduledGrants,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts": docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoEnergyBursts,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts": docsRphyStatsRpdUsOfdmaHighIucPerfStatsNoPreambleBursts,
       "docsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts": docsRphyStatsRpdUsOfdmaHighIucPerfStatsErrorBursts,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsTable": docsRphyStatsRpdUsScQamLowIucPerfStatsTable,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsEntry": docsRphyStatsRpdUsScQamLowIucPerfStatsEntry,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc": docsRphyStatsRpdUsScQamLowIucPerfStatsUsIuc,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw": docsRphyStatsRpdUsScQamLowIucPerfStatsGoodFecCw,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw": docsRphyStatsRpdUsScQamLowIucPerfStatsCorrectedFecCw,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw": docsRphyStatsRpdUsScQamLowIucPerfStatsUncorrectedFecCw,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities": docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpportunities,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions": docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpCollisions,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy": docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpNoEnergy,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors": docsRphyStatsRpdUsScQamLowIucPerfStatsUnicastOpErrors,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities": docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpportunities,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions": docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpCollisions,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy": docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpNoEnergy,
       "docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors": docsRphyStatsRpdUsScQamLowIucPerfStatsMulticastOpErrors,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsTable": docsRphyStatsRpdUsScQamHighIucPerfStatsTable,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsEntry": docsRphyStatsRpdUsScQamHighIucPerfStatsEntry,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc": docsRphyStatsRpdUsScQamHighIucPerfStatsUsIuc,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw": docsRphyStatsRpdUsScQamHighIucPerfStatsGoodFecCw,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw": docsRphyStatsRpdUsScQamHighIucPerfStatsCorrectedFecCw,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw": docsRphyStatsRpdUsScQamHighIucPerfStatsUncorrectedFecCw,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants": docsRphyStatsRpdUsScQamHighIucPerfStatsScheduledGrants,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts": docsRphyStatsRpdUsScQamHighIucPerfStatsNoEnergyBursts,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts": docsRphyStatsRpdUsScQamHighIucPerfStatsNoPreambleBursts,
       "docsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts": docsRphyStatsRpdUsScQamHighIucPerfStatsErrorBursts,
       "docsRphyStatsCcapMibObjects": docsRphyStatsCcapMibObjects,
       "docsRphyStatsConformance": docsRphyStatsConformance,
       "docsRphyStatsCompliances": docsRphyStatsCompliances,
       "docsRphyStatsCompliance": docsRphyStatsCompliance,
       "docsRphyStatsGroups": docsRphyStatsGroups,
       "docsRphyStatsRpdGroup": docsRphyStatsRpdGroup}
)
