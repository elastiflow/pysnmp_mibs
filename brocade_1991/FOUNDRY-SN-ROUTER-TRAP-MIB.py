# SNMP MIB module (FOUNDRY-SN-ROUTER-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FOUNDRY-SN-ROUTER-TRAP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:38 2025
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

(snOspfConfigErrorType,
 snOspfExtLsdbLimit,
 snOspfIfStatusIpAddress,
 snOspfIfStatusState,
 snOspfLsdbAreaId,
 snOspfLsdbLsId,
 snOspfLsdbRouterId,
 snOspfLsdbType,
 snOspfNbrIpAddr,
 snOspfNbrRtrId,
 snOspfNbrState,
 snOspfPacketSrc,
 snOspfPacketType,
 snOspfRouterId,
 snOspfVirtIfStatusAreaID,
 snOspfVirtIfStatusNeighbor,
 snOspfVirtIfStatusState,
 snOspfVirtNbrArea,
 snOspfVirtNbrRtrId,
 snOspfVirtNbrState) = mibBuilder.importSymbols(
    "FOUNDRY-SN-OSPF-GROUP-MIB",
    "snOspfConfigErrorType",
    "snOspfExtLsdbLimit",
    "snOspfIfStatusIpAddress",
    "snOspfIfStatusState",
    "snOspfLsdbAreaId",
    "snOspfLsdbLsId",
    "snOspfLsdbRouterId",
    "snOspfLsdbType",
    "snOspfNbrIpAddr",
    "snOspfNbrRtrId",
    "snOspfNbrState",
    "snOspfPacketSrc",
    "snOspfPacketType",
    "snOspfRouterId",
    "snOspfVirtIfStatusAreaID",
    "snOspfVirtIfStatusNeighbor",
    "snOspfVirtIfStatusState",
    "snOspfVirtNbrArea",
    "snOspfVirtNbrRtrId",
    "snOspfVirtNbrState")

(foundry,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "foundry")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

snTrapOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 3)
)
snTrapOspfIfStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusState"))
)
if mibBuilder.loadTexts:
    snTrapOspfIfStateChange.setStatus(
        ""
    )

snTrapOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 4)
)
snTrapOspfVirtIfStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusState"))
)
if mibBuilder.loadTexts:
    snTrapOspfVirtIfStateChange.setStatus(
        ""
    )

snOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 5)
)
snOspfNbrStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrIpAddr"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrState"))
)
if mibBuilder.loadTexts:
    snOspfNbrStateChange.setStatus(
        ""
    )

snOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 6)
)
snOspfVirtNbrStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrArea"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrRtrId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    snOspfVirtNbrStateChange.setStatus(
        ""
    )

snOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 7)
)
snOspfIfConfigError.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfConfigError.setStatus(
        ""
    )

snOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 8)
)
snOspfVirtIfConfigError.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfConfigError.setStatus(
        ""
    )

snOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 9)
)
snOspfIfAuthFailure.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfAuthFailure.setStatus(
        ""
    )

snOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 10)
)
snOspfVirtIfAuthFailure.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfAuthFailure.setStatus(
        ""
    )

snOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 11)
)
snOspfIfRxBadPacket.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfRxBadPacket.setStatus(
        ""
    )

snOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 12)
)
snOspfVirtIfRxBadPacket.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfRxBadPacket.setStatus(
        ""
    )

snOspfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 13)
)
snOspfTxRetransmit.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfTxRetransmit.setStatus(
        ""
    )

ospfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 14)
)
ospfVirtIfTxRetransmit.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfVirtIfTxRetransmit.setStatus(
        ""
    )

snOspfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 15)
)
snOspfOriginateLsa.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfOriginateLsa.setStatus(
        ""
    )

snOspfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 16)
)
snOspfMaxAgeLsa.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfMaxAgeLsa.setStatus(
        ""
    )

snOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 17)
)
snOspfLsdbOverflow.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    snOspfLsdbOverflow.setStatus(
        ""
    )

snOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 18)
)
snOspfLsdbApproachingOverflow.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    snOspfLsdbApproachingOverflow.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-ROUTER-TRAP-MIB",
    **{"snTrapOspfIfStateChange": snTrapOspfIfStateChange,
       "snTrapOspfVirtIfStateChange": snTrapOspfVirtIfStateChange,
       "snOspfNbrStateChange": snOspfNbrStateChange,
       "snOspfVirtNbrStateChange": snOspfVirtNbrStateChange,
       "snOspfIfConfigError": snOspfIfConfigError,
       "snOspfVirtIfConfigError": snOspfVirtIfConfigError,
       "snOspfIfAuthFailure": snOspfIfAuthFailure,
       "snOspfVirtIfAuthFailure": snOspfVirtIfAuthFailure,
       "snOspfIfRxBadPacket": snOspfIfRxBadPacket,
       "snOspfVirtIfRxBadPacket": snOspfVirtIfRxBadPacket,
       "snOspfTxRetransmit": snOspfTxRetransmit,
       "ospfVirtIfTxRetransmit": ospfVirtIfTxRetransmit,
       "snOspfOriginateLsa": snOspfOriginateLsa,
       "snOspfMaxAgeLsa": snOspfMaxAgeLsa,
       "snOspfLsdbOverflow": snOspfLsdbOverflow,
       "snOspfLsdbApproachingOverflow": snOspfLsdbApproachingOverflow}
)
