# SNMP MIB module (ARISTA-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-IP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetVersion,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetVersion")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

aristaIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27)
)
if mibBuilder.loadTexts:
    aristaIpMIB.setRevisions(
        ("2018-12-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaIpMibObjects_ObjectIdentity = ObjectIdentity
aristaIpMibObjects = _AristaIpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1)
)
_AristaIpIfStatsTable_Object = MibTable
aristaIpIfStatsTable = _AristaIpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1)
)
if mibBuilder.loadTexts:
    aristaIpIfStatsTable.setStatus("current")
_AristaIpIfStatsEntry_Object = MibTableRow
aristaIpIfStatsEntry = _AristaIpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1)
)
aristaIpIfStatsEntry.setIndexNames(
    (0, "ARISTA-IP-MIB", "aristaIpIfStatsIPVersion"),
    (0, "ARISTA-IP-MIB", "aristaIpIfStatsIfIndex"),
)
if mibBuilder.loadTexts:
    aristaIpIfStatsEntry.setStatus("current")
_AristaIpIfStatsIPVersion_Type = InetVersion
_AristaIpIfStatsIPVersion_Object = MibTableColumn
aristaIpIfStatsIPVersion = _AristaIpIfStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 1),
    _AristaIpIfStatsIPVersion_Type()
)
aristaIpIfStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpIfStatsIPVersion.setStatus("current")
_AristaIpIfStatsIfIndex_Type = InterfaceIndex
_AristaIpIfStatsIfIndex_Object = MibTableColumn
aristaIpIfStatsIfIndex = _AristaIpIfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 2),
    _AristaIpIfStatsIfIndex_Type()
)
aristaIpIfStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaIpIfStatsIfIndex.setStatus("current")
_AristaIpIfStatsInPkts_Type = Counter64
_AristaIpIfStatsInPkts_Object = MibTableColumn
aristaIpIfStatsInPkts = _AristaIpIfStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 3),
    _AristaIpIfStatsInPkts_Type()
)
aristaIpIfStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsInPkts.setStatus("current")
_AristaIpIfStatsInOctets_Type = Counter64
_AristaIpIfStatsInOctets_Object = MibTableColumn
aristaIpIfStatsInOctets = _AristaIpIfStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 4),
    _AristaIpIfStatsInOctets_Type()
)
aristaIpIfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsInOctets.setStatus("current")
_AristaIpIfStatsOutPkts_Type = Counter64
_AristaIpIfStatsOutPkts_Object = MibTableColumn
aristaIpIfStatsOutPkts = _AristaIpIfStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 5),
    _AristaIpIfStatsOutPkts_Type()
)
aristaIpIfStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsOutPkts.setStatus("current")
_AristaIpIfStatsOutOctets_Type = Counter64
_AristaIpIfStatsOutOctets_Object = MibTableColumn
aristaIpIfStatsOutOctets = _AristaIpIfStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 6),
    _AristaIpIfStatsOutOctets_Type()
)
aristaIpIfStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsOutOctets.setStatus("current")
_AristaIpIfStatsInUcastPkts_Type = Counter64
_AristaIpIfStatsInUcastPkts_Object = MibTableColumn
aristaIpIfStatsInUcastPkts = _AristaIpIfStatsInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 7),
    _AristaIpIfStatsInUcastPkts_Type()
)
aristaIpIfStatsInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsInUcastPkts.setStatus("current")
_AristaIpIfStatsInUcastOctets_Type = Counter64
_AristaIpIfStatsInUcastOctets_Object = MibTableColumn
aristaIpIfStatsInUcastOctets = _AristaIpIfStatsInUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 8),
    _AristaIpIfStatsInUcastOctets_Type()
)
aristaIpIfStatsInUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsInUcastOctets.setStatus("current")
_AristaIpIfStatsOutUcastPkts_Type = Counter64
_AristaIpIfStatsOutUcastPkts_Object = MibTableColumn
aristaIpIfStatsOutUcastPkts = _AristaIpIfStatsOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 9),
    _AristaIpIfStatsOutUcastPkts_Type()
)
aristaIpIfStatsOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsOutUcastPkts.setStatus("current")
_AristaIpIfStatsOutUcastOctets_Type = Counter64
_AristaIpIfStatsOutUcastOctets_Object = MibTableColumn
aristaIpIfStatsOutUcastOctets = _AristaIpIfStatsOutUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 10),
    _AristaIpIfStatsOutUcastOctets_Type()
)
aristaIpIfStatsOutUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsOutUcastOctets.setStatus("current")
_AristaIpIfStatsInMcastPkts_Type = Counter64
_AristaIpIfStatsInMcastPkts_Object = MibTableColumn
aristaIpIfStatsInMcastPkts = _AristaIpIfStatsInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 11),
    _AristaIpIfStatsInMcastPkts_Type()
)
aristaIpIfStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsInMcastPkts.setStatus("current")
_AristaIpIfStatsInMcastOctets_Type = Counter64
_AristaIpIfStatsInMcastOctets_Object = MibTableColumn
aristaIpIfStatsInMcastOctets = _AristaIpIfStatsInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 12),
    _AristaIpIfStatsInMcastOctets_Type()
)
aristaIpIfStatsInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsInMcastOctets.setStatus("current")
_AristaIpIfStatsOutMcastPkts_Type = Counter64
_AristaIpIfStatsOutMcastPkts_Object = MibTableColumn
aristaIpIfStatsOutMcastPkts = _AristaIpIfStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 13),
    _AristaIpIfStatsOutMcastPkts_Type()
)
aristaIpIfStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsOutMcastPkts.setStatus("current")
_AristaIpIfStatsOutMcastOctets_Type = Counter64
_AristaIpIfStatsOutMcastOctets_Object = MibTableColumn
aristaIpIfStatsOutMcastOctets = _AristaIpIfStatsOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 14),
    _AristaIpIfStatsOutMcastOctets_Type()
)
aristaIpIfStatsOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsOutMcastOctets.setStatus("current")
_AristaIpIfStatsDiscontinuityTime_Type = TimeStamp
_AristaIpIfStatsDiscontinuityTime_Object = MibTableColumn
aristaIpIfStatsDiscontinuityTime = _AristaIpIfStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 15),
    _AristaIpIfStatsDiscontinuityTime_Type()
)
aristaIpIfStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsDiscontinuityTime.setStatus("current")
_AristaIpIfStatsRefreshRate_Type = Unsigned32
_AristaIpIfStatsRefreshRate_Object = MibTableColumn
aristaIpIfStatsRefreshRate = _AristaIpIfStatsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 1, 1, 1, 16),
    _AristaIpIfStatsRefreshRate_Type()
)
aristaIpIfStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpIfStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    aristaIpIfStatsRefreshRate.setUnits("milli-seconds")
_AristaIpMibConformance_ObjectIdentity = ObjectIdentity
aristaIpMibConformance = _AristaIpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 2)
)
_AristaIpMibCompliances_ObjectIdentity = ObjectIdentity
aristaIpMibCompliances = _AristaIpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 2, 1)
)
_AristaIpMibGroups_ObjectIdentity = ObjectIdentity
aristaIpMibGroups = _AristaIpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 2, 2)
)

# Managed Objects groups

aristaIpIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 2, 2, 1)
)
aristaIpIfStatsGroup.setObjects(
      *(("ARISTA-IP-MIB", "aristaIpIfStatsInPkts"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsInOctets"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsOutPkts"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsOutOctets"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsInUcastPkts"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsInUcastOctets"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsOutUcastPkts"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsOutUcastOctets"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsInMcastPkts"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsInMcastOctets"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsOutMcastPkts"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsOutMcastOctets"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsDiscontinuityTime"),
        ("ARISTA-IP-MIB", "aristaIpIfStatsRefreshRate"))
)
if mibBuilder.loadTexts:
    aristaIpIfStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaIpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 27, 2, 1, 1)
)
aristaIpMibCompliance.setObjects(
    ("ARISTA-IP-MIB", "aristaIpIfStatsGroup")
)
if mibBuilder.loadTexts:
    aristaIpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-IP-MIB",
    **{"aristaIpMIB": aristaIpMIB,
       "aristaIpMibObjects": aristaIpMibObjects,
       "aristaIpIfStatsTable": aristaIpIfStatsTable,
       "aristaIpIfStatsEntry": aristaIpIfStatsEntry,
       "aristaIpIfStatsIPVersion": aristaIpIfStatsIPVersion,
       "aristaIpIfStatsIfIndex": aristaIpIfStatsIfIndex,
       "aristaIpIfStatsInPkts": aristaIpIfStatsInPkts,
       "aristaIpIfStatsInOctets": aristaIpIfStatsInOctets,
       "aristaIpIfStatsOutPkts": aristaIpIfStatsOutPkts,
       "aristaIpIfStatsOutOctets": aristaIpIfStatsOutOctets,
       "aristaIpIfStatsInUcastPkts": aristaIpIfStatsInUcastPkts,
       "aristaIpIfStatsInUcastOctets": aristaIpIfStatsInUcastOctets,
       "aristaIpIfStatsOutUcastPkts": aristaIpIfStatsOutUcastPkts,
       "aristaIpIfStatsOutUcastOctets": aristaIpIfStatsOutUcastOctets,
       "aristaIpIfStatsInMcastPkts": aristaIpIfStatsInMcastPkts,
       "aristaIpIfStatsInMcastOctets": aristaIpIfStatsInMcastOctets,
       "aristaIpIfStatsOutMcastPkts": aristaIpIfStatsOutMcastPkts,
       "aristaIpIfStatsOutMcastOctets": aristaIpIfStatsOutMcastOctets,
       "aristaIpIfStatsDiscontinuityTime": aristaIpIfStatsDiscontinuityTime,
       "aristaIpIfStatsRefreshRate": aristaIpIfStatsRefreshRate,
       "aristaIpMibConformance": aristaIpMibConformance,
       "aristaIpMibCompliances": aristaIpMibCompliances,
       "aristaIpMibCompliance": aristaIpMibCompliance,
       "aristaIpMibGroups": aristaIpMibGroups,
       "aristaIpIfStatsGroup": aristaIpIfStatsGroup}
)
