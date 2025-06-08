# SNMP MIB module (NET-SNMP-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/netsnmp_8072/NET-SNMP-MONITOR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:28:10 2025
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

(netSnmpModuleIDs,
 netSnmpObjects) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmpModuleIDs",
    "netSnmpObjects")

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

netSnmpMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 3)
)
if mibBuilder.loadTexts:
    netSnmpMonitorMIB.setRevisions(
        ("2002-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsProcess_ObjectIdentity = ObjectIdentity
nsProcess = _NsProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 21)
)
_NsDisk_ObjectIdentity = ObjectIdentity
nsDisk = _NsDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 22)
)
_NsFile_ObjectIdentity = ObjectIdentity
nsFile = _NsFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 23)
)
_NsLog_ObjectIdentity = ObjectIdentity
nsLog = _NsLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 24)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-MONITOR-MIB",
    **{"nsProcess": nsProcess,
       "nsDisk": nsDisk,
       "nsFile": nsFile,
       "nsLog": nsLog,
       "netSnmpMonitorMIB": netSnmpMonitorMIB}
)
