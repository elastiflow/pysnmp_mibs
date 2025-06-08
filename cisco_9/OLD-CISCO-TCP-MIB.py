# SNMP MIB module (OLD-CISCO-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/OLD-CISCO-TCP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:08 2025
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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

(tcpConnLocalAddress,
 tcpConnLocalPort,
 tcpConnRemAddress,
 tcpConnRemPort) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnLocalAddress",
    "tcpConnLocalPort",
    "tcpConnRemAddress",
    "tcpConnRemPort")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ltcp_ObjectIdentity = ObjectIdentity
ltcp = _Ltcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 6)
)
_LtcpConnTable_Object = MibTable
ltcpConnTable = _LtcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ltcpConnTable.setStatus("deprecated")
_LtcpConnEntry_Object = MibTableRow
ltcpConnEntry = _LtcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1)
)
ltcpConnEntry.setIndexNames(
    (0, "TCP-MIB", "tcpConnLocalAddress"),
    (0, "TCP-MIB", "tcpConnLocalPort"),
    (0, "TCP-MIB", "tcpConnRemAddress"),
    (0, "TCP-MIB", "tcpConnRemPort"),
)
if mibBuilder.loadTexts:
    ltcpConnEntry.setStatus("deprecated")
_LoctcpConnInBytes_Type = Integer32
_LoctcpConnInBytes_Object = MibTableColumn
loctcpConnInBytes = _LoctcpConnInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 1),
    _LoctcpConnInBytes_Type()
)
loctcpConnInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnInBytes.setStatus("deprecated")
_LoctcpConnOutBytes_Type = Integer32
_LoctcpConnOutBytes_Object = MibTableColumn
loctcpConnOutBytes = _LoctcpConnOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 2),
    _LoctcpConnOutBytes_Type()
)
loctcpConnOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnOutBytes.setStatus("deprecated")
_LoctcpConnInPkts_Type = Integer32
_LoctcpConnInPkts_Object = MibTableColumn
loctcpConnInPkts = _LoctcpConnInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 3),
    _LoctcpConnInPkts_Type()
)
loctcpConnInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnInPkts.setStatus("deprecated")
_LoctcpConnOutPkts_Type = Integer32
_LoctcpConnOutPkts_Object = MibTableColumn
loctcpConnOutPkts = _LoctcpConnOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 4),
    _LoctcpConnOutPkts_Type()
)
loctcpConnOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnOutPkts.setStatus("deprecated")
_LoctcpConnElapsed_Type = TimeTicks
_LoctcpConnElapsed_Object = MibTableColumn
loctcpConnElapsed = _LoctcpConnElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 5),
    _LoctcpConnElapsed_Type()
)
loctcpConnElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnElapsed.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-TCP-MIB",
    **{"ltcp": ltcp,
       "ltcpConnTable": ltcpConnTable,
       "ltcpConnEntry": ltcpConnEntry,
       "loctcpConnInBytes": loctcpConnInBytes,
       "loctcpConnOutBytes": loctcpConnOutBytes,
       "loctcpConnInPkts": loctcpConnInPkts,
       "loctcpConnOutPkts": loctcpConnOutPkts,
       "loctcpConnElapsed": loctcpConnElapsed}
)
