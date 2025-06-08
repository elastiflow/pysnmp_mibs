# SNMP MIB module (UROAM-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/f5_12276/UROAM-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:59:23 2025
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

uroam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12276)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 10)
)
_VersionID_Type = DisplayString
_VersionID_Object = MibScalar
versionID = _VersionID_Object(
    (1, 3, 6, 1, 4, 1, 12276, 10, 1),
    _VersionID_Type()
)
versionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionID.setStatus("current")
_VersionDate_Type = DisplayString
_VersionDate_Object = MibScalar
versionDate = _VersionDate_Object(
    (1, 3, 6, 1, 4, 1, 12276, 10, 2),
    _VersionDate_Type()
)
versionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionDate.setStatus("current")
_Fp1000_ObjectIdentity = ObjectIdentity
fp1000 = _Fp1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 100)
)


class _Fp1000server_Type(Integer32):
    """Custom type fp1000server based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fp1000server_Type.__name__ = "Integer32"
_Fp1000server_Object = MibScalar
fp1000server = _Fp1000server_Object(
    (1, 3, 6, 1, 4, 1, 12276, 100, 1),
    _Fp1000server_Type()
)
fp1000server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fp1000server.setStatus("current")


class _Fp1000service_Type(Integer32):
    """Custom type fp1000service based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fp1000service_Type.__name__ = "Integer32"
_Fp1000service_Object = MibScalar
fp1000service = _Fp1000service_Object(
    (1, 3, 6, 1, 4, 1, 12276, 100, 2),
    _Fp1000service_Type()
)
fp1000service.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fp1000service.setStatus("current")


class _Fp1000bridge_Type(Integer32):
    """Custom type fp1000bridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fp1000bridge_Type.__name__ = "Integer32"
_Fp1000bridge_Object = MibScalar
fp1000bridge = _Fp1000bridge_Object(
    (1, 3, 6, 1, 4, 1, 12276, 100, 3),
    _Fp1000bridge_Type()
)
fp1000bridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fp1000bridge.setStatus("current")


class _Fp1000ServerSessions_Type(Integer32):
    """Custom type fp1000ServerSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Fp1000ServerSessions_Type.__name__ = "Integer32"
_Fp1000ServerSessions_Object = MibScalar
fp1000ServerSessions = _Fp1000ServerSessions_Object(
    (1, 3, 6, 1, 4, 1, 12276, 100, 4),
    _Fp1000ServerSessions_Type()
)
fp1000ServerSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fp1000ServerSessions.setStatus("current")


class _Fp1000DesktopSessions_Type(Integer32):
    """Custom type fp1000DesktopSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Fp1000DesktopSessions_Type.__name__ = "Integer32"
_Fp1000DesktopSessions_Object = MibScalar
fp1000DesktopSessions = _Fp1000DesktopSessions_Object(
    (1, 3, 6, 1, 4, 1, 12276, 100, 5),
    _Fp1000DesktopSessions_Type()
)
fp1000DesktopSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fp1000DesktopSessions.setStatus("current")
_FailoverInfo_ObjectIdentity = ObjectIdentity
failoverInfo = _FailoverInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 200)
)


class _FailoverConf_Type(Integer32):
    """Custom type failoverConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 0),
          ("firstMember", 1),
          ("secondMember", 2))
    )


_FailoverConf_Type.__name__ = "Integer32"
_FailoverConf_Object = MibScalar
failoverConf = _FailoverConf_Object(
    (1, 3, 6, 1, 4, 1, 12276, 200, 1),
    _FailoverConf_Type()
)
failoverConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverConf.setStatus("current")


class _FailoverStatus_Type(Integer32):
    """Custom type failoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("active", 1),
          ("standby", 2))
    )


_FailoverStatus_Type.__name__ = "Integer32"
_FailoverStatus_Object = MibScalar
failoverStatus = _FailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 12276, 200, 2),
    _FailoverStatus_Type()
)
failoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverStatus.setStatus("current")


class _FailoverSynchStatus_Type(Integer32):
    """Custom type failoverSynchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("Synchronized", 1),
          ("notSynchronized", 2))
    )


_FailoverSynchStatus_Type.__name__ = "Integer32"
_FailoverSynchStatus_Object = MibScalar
failoverSynchStatus = _FailoverSynchStatus_Object(
    (1, 3, 6, 1, 4, 1, 12276, 200, 3),
    _FailoverSynchStatus_Type()
)
failoverSynchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failoverSynchStatus.setStatus("current")
_ClusterInfo_ObjectIdentity = ObjectIdentity
clusterInfo = _ClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 250)
)


class _ClusterConf_Type(Integer32):
    """Custom type clusterConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInCluster", 0),
          ("Master", 1),
          ("Slave", 2))
    )


_ClusterConf_Type.__name__ = "Integer32"
_ClusterConf_Object = MibScalar
clusterConf = _ClusterConf_Object(
    (1, 3, 6, 1, 4, 1, 12276, 250, 1),
    _ClusterConf_Type()
)
clusterConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterConf.setStatus("current")


class _ClusterConfiguredNodesNo_Type(Integer32):
    """Custom type clusterConfiguredNodesNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClusterConfiguredNodesNo_Type.__name__ = "Integer32"
_ClusterConfiguredNodesNo_Object = MibScalar
clusterConfiguredNodesNo = _ClusterConfiguredNodesNo_Object(
    (1, 3, 6, 1, 4, 1, 12276, 250, 2),
    _ClusterConfiguredNodesNo_Type()
)
clusterConfiguredNodesNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterConfiguredNodesNo.setStatus("current")
_ClusterSynchTable_Object = MibTable
clusterSynchTable = _ClusterSynchTable_Object(
    (1, 3, 6, 1, 4, 1, 12276, 250, 3)
)
if mibBuilder.loadTexts:
    clusterSynchTable.setStatus("current")
_ClusterSynchEntry_Object = MibTableRow
clusterSynchEntry = _ClusterSynchEntry_Object(
    (1, 3, 6, 1, 4, 1, 12276, 250, 3, 1)
)
clusterSynchEntry.setIndexNames(
    (0, "UROAM-SNMP-MIB", "clusterNodeNo"),
)
if mibBuilder.loadTexts:
    clusterSynchEntry.setStatus("current")


class _ClusterNodeNo_Type(Integer32):
    """Custom type clusterNodeNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClusterNodeNo_Type.__name__ = "Integer32"
_ClusterNodeNo_Object = MibTableColumn
clusterNodeNo = _ClusterNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 12276, 250, 3, 1, 1),
    _ClusterNodeNo_Type()
)
clusterNodeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNodeNo.setStatus("current")
_ClusterNodeName_Type = DisplayString
_ClusterNodeName_Object = MibTableColumn
clusterNodeName = _ClusterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 12276, 250, 3, 1, 2),
    _ClusterNodeName_Type()
)
clusterNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNodeName.setStatus("current")


class _ClusterSynchStatus_Type(Integer32):
    """Custom type clusterSynchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("Synchronized", 1),
          ("notSynchronized", 2))
    )


_ClusterSynchStatus_Type.__name__ = "Integer32"
_ClusterSynchStatus_Object = MibTableColumn
clusterSynchStatus = _ClusterSynchStatus_Object(
    (1, 3, 6, 1, 4, 1, 12276, 250, 3, 1, 3),
    _ClusterSynchStatus_Type()
)
clusterSynchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterSynchStatus.setStatus("current")
_TrapsDefs_ObjectIdentity = ObjectIdentity
trapsDefs = _TrapsDefs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 500)
)

# Managed Objects groups


# Notification objects

trapFailoverSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 500, 0, 10)
)
trapFailoverSwitch.setObjects(
    ("UROAM-SNMP-MIB", "failoverStatus")
)
if mibBuilder.loadTexts:
    trapFailoverSwitch.setStatus(
        ""
    )

trapFailoverNoSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 500, 0, 20)
)
trapFailoverNoSynch.setObjects(
    ("UROAM-SNMP-MIB", "failoverSynch")
)
if mibBuilder.loadTexts:
    trapFailoverNoSynch.setStatus(
        ""
    )

trapClusterNoSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 500, 0, 30)
)
trapClusterNoSynch.setObjects(
    ("UROAM-SNMP-MIB", "clusterSynchTable")
)
if mibBuilder.loadTexts:
    trapClusterNoSynch.setStatus(
        ""
    )

noteFailoverSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 500, 11)
)
noteFailoverSwitch.setObjects(
    ("UROAM-SNMP-MIB", "failoverStatus")
)
if mibBuilder.loadTexts:
    noteFailoverSwitch.setStatus(
        "current"
    )

noteFailoverNoSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 500, 21)
)
noteFailoverNoSynch.setObjects(
    ("UROAM-SNMP-MIB", "failoverSynch")
)
if mibBuilder.loadTexts:
    noteFailoverNoSynch.setStatus(
        "current"
    )

noteClusterNoSynch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12276, 500, 31)
)
noteClusterNoSynch.setObjects(
    ("UROAM-SNMP-MIB", "clusterSynchTable")
)
if mibBuilder.loadTexts:
    noteClusterNoSynch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UROAM-SNMP-MIB",
    **{"uroam": uroam,
       "version": version,
       "versionID": versionID,
       "versionDate": versionDate,
       "fp1000": fp1000,
       "fp1000server": fp1000server,
       "fp1000service": fp1000service,
       "fp1000bridge": fp1000bridge,
       "fp1000ServerSessions": fp1000ServerSessions,
       "fp1000DesktopSessions": fp1000DesktopSessions,
       "failoverInfo": failoverInfo,
       "failoverConf": failoverConf,
       "failoverStatus": failoverStatus,
       "failoverSynchStatus": failoverSynchStatus,
       "clusterInfo": clusterInfo,
       "clusterConf": clusterConf,
       "clusterConfiguredNodesNo": clusterConfiguredNodesNo,
       "clusterSynchTable": clusterSynchTable,
       "clusterSynchEntry": clusterSynchEntry,
       "clusterNodeNo": clusterNodeNo,
       "clusterNodeName": clusterNodeName,
       "clusterSynchStatus": clusterSynchStatus,
       "trapsDefs": trapsDefs,
       "trapFailoverSwitch": trapFailoverSwitch,
       "trapFailoverNoSynch": trapFailoverNoSynch,
       "trapClusterNoSynch": trapClusterNoSynch,
       "noteFailoverSwitch": noteFailoverSwitch,
       "noteFailoverNoSynch": noteFailoverNoSynch,
       "noteClusterNoSynch": noteClusterNoSynch}
)
