# SNMP MIB module (CISCOTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOTRAP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:13:48 2025
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

(cisco,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "cisco")

(ifDescr,
 ifIndex,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex",
    "ifType")

(locIfReason,) = mibBuilder.importSymbols(
    "OLD-CISCO-INTERFACES-MIB",
    "locIfReason")

(authAddr,
 whyReload) = mibBuilder.importSymbols(
    "OLD-CISCO-SYSTEM-MIB",
    "authAddr",
    "whyReload")

(loctcpConnElapsed,
 loctcpConnInBytes,
 loctcpConnOutBytes) = mibBuilder.importSymbols(
    "OLD-CISCO-TCP-MIB",
    "loctcpConnElapsed",
    "loctcpConnInBytes",
    "loctcpConnOutBytes")

(tsLineUser,
 tslineSesType) = mibBuilder.importSymbols(
    "OLD-CISCO-TS-MIB",
    "tsLineUser",
    "tslineSesType")

(egpNeighAddr,) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "egpNeighAddr")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
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

(tcpConnState,) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnState")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
coldStart.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 2)
)
linkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 3)
)
linkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
authenticationFailure.setObjects(
    ("OLD-CISCO-SYSTEM-MIB", "authAddr")
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

egpNeighborLoss = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 5)
)
egpNeighborLoss.setObjects(
    ("RFC1213-MIB", "egpNeighAddr")
)
if mibBuilder.loadTexts:
    egpNeighborLoss.setStatus(
        ""
    )

reload = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 0, 0)
)
reload.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
)
if mibBuilder.loadTexts:
    reload.setStatus(
        ""
    )

tcpConnectionClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 0, 1)
)
tcpConnectionClose.setObjects(
      *(("OLD-CISCO-TS-MIB", "tslineSesType"),
        ("TCP-MIB", "tcpConnState"),
        ("OLD-CISCO-TCP-MIB", "loctcpConnElapsed"),
        ("OLD-CISCO-TCP-MIB", "loctcpConnInBytes"),
        ("OLD-CISCO-TCP-MIB", "loctcpConnOutBytes"),
        ("OLD-CISCO-TS-MIB", "tsLineUser"))
)
if mibBuilder.loadTexts:
    tcpConnectionClose.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOTRAP-MIB",
    **{"coldStart": coldStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "authenticationFailure": authenticationFailure,
       "egpNeighborLoss": egpNeighborLoss,
       "reload": reload,
       "tcpConnectionClose": tcpConnectionClose}
)
