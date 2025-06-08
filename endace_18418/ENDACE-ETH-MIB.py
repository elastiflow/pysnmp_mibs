# SNMP MIB module (ENDACE-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/endace_18418/ENDACE-ETH-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:13:01 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

(InterfaceIndex,
 moduleInterfaces,
 shogunModuleMIB) = mibBuilder.importSymbols(
    "ENDACE-MODULE-MIB",
    "InterfaceIndex",
    "moduleInterfaces",
    "shogunModuleMIB")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

endaceETHMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 4)
)
if mibBuilder.loadTexts:
    endaceETHMIB.setRevisions(
        ("2011-01-13 00:00",
         "2007-08-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eth1_ObjectIdentity = ObjectIdentity
eth1 = _Eth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2)
)
_EthControlTable_Object = MibTable
ethControlTable = _EthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ethControlTable.setStatus("current")
_EthControlEntry_Object = MibTableRow
ethControlEntry = _EthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1)
)
ethControlEntry.setIndexNames(
    (0, "ENDACE-ETH-MIB", "ethControlIndex"),
)
if mibBuilder.loadTexts:
    ethControlEntry.setStatus("current")
_EthControlIndex_Type = InterfaceIndex
_EthControlIndex_Object = MibTableColumn
ethControlIndex = _EthControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 1),
    _EthControlIndex_Type()
)
ethControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlIndex.setStatus("current")
_EthControlPeerLink_Type = TruthValue
_EthControlPeerLink_Object = MibTableColumn
ethControlPeerLink = _EthControlPeerLink_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 2),
    _EthControlPeerLink_Type()
)
ethControlPeerLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlPeerLink.setStatus("current")
_EthControlRemoteFault_Type = TruthValue
_EthControlRemoteFault_Object = MibTableColumn
ethControlRemoteFault = _EthControlRemoteFault_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 3),
    _EthControlRemoteFault_Type()
)
ethControlRemoteFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlRemoteFault.setStatus("current")
_EthControlLOF_Type = TruthValue
_EthControlLOF_Object = MibTableColumn
ethControlLOF = _EthControlLOF_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 4),
    _EthControlLOF_Type()
)
ethControlLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlLOF.setStatus("current")
_EthControlLOS_Type = TruthValue
_EthControlLOS_Object = MibTableColumn
ethControlLOS = _EthControlLOS_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 5),
    _EthControlLOS_Type()
)
ethControlLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlLOS.setStatus("current")
_EthControlPhysAddress_Type = PhysAddress
_EthControlPhysAddress_Object = MibTableColumn
ethControlPhysAddress = _EthControlPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 6),
    _EthControlPhysAddress_Type()
)
ethControlPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlPhysAddress.setStatus("current")
_EthControlNIC_Type = TruthValue
_EthControlNIC_Object = MibTableColumn
ethControlNIC = _EthControlNIC_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 7),
    _EthControlNIC_Type()
)
ethControlNIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlNIC.setStatus("current")
_EthControlFCSThreshold_Type = Gauge32
_EthControlFCSThreshold_Object = MibTableColumn
ethControlFCSThreshold = _EthControlFCSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 1, 1, 8),
    _EthControlFCSThreshold_Type()
)
ethControlFCSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethControlFCSThreshold.setStatus("current")
_EthStatsTable_Object = MibTable
ethStatsTable = _EthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ethStatsTable.setStatus("current")
_EthStatsEntry_Object = MibTableRow
ethStatsEntry = _EthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 2, 1)
)
ethStatsEntry.setIndexNames(
    (0, "ENDACE-ETH-MIB", "ethStatsIndex"),
)
if mibBuilder.loadTexts:
    ethStatsEntry.setStatus("current")
_EthStatsIndex_Type = InterfaceIndex
_EthStatsIndex_Object = MibTableColumn
ethStatsIndex = _EthStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 2, 1, 1),
    _EthStatsIndex_Type()
)
ethStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsIndex.setStatus("current")
_EthStatsFCSErrors_Type = Counter32
_EthStatsFCSErrors_Object = MibTableColumn
ethStatsFCSErrors = _EthStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 2, 1, 2),
    _EthStatsFCSErrors_Type()
)
ethStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsFCSErrors.setStatus("current")
_EthStatsAlignmentErrors_Type = Counter32
_EthStatsAlignmentErrors_Object = MibTableColumn
ethStatsAlignmentErrors = _EthStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 2, 1, 3),
    _EthStatsAlignmentErrors_Type()
)
ethStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsAlignmentErrors.setStatus("current")
_EthStatsRemoteErrors_Type = Counter64
_EthStatsRemoteErrors_Object = MibTableColumn
ethStatsRemoteErrors = _EthStatsRemoteErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 2, 1, 4),
    _EthStatsRemoteErrors_Type()
)
ethStatsRemoteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatsRemoteErrors.setStatus("current")
_EthHCStatsTable_Object = MibTable
ethHCStatsTable = _EthHCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ethHCStatsTable.setStatus("current")
_EthHCStatsEntry_Object = MibTableRow
ethHCStatsEntry = _EthHCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1)
)
ethHCStatsEntry.setIndexNames(
    (0, "ENDACE-ETH-MIB", "ethHCStatsIndex"),
)
if mibBuilder.loadTexts:
    ethHCStatsEntry.setStatus("current")
_EthHCStatsIndex_Type = InterfaceIndex
_EthHCStatsIndex_Object = MibTableColumn
ethHCStatsIndex = _EthHCStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1, 1),
    _EthHCStatsIndex_Type()
)
ethHCStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethHCStatsIndex.setStatus("current")
_EthHCFCSErrors_Type = Counter64
_EthHCFCSErrors_Object = MibTableColumn
ethHCFCSErrors = _EthHCFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1, 2),
    _EthHCFCSErrors_Type()
)
ethHCFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethHCFCSErrors.setStatus("current")
_EthHCInFaults_Type = Counter64
_EthHCInFaults_Object = MibTableColumn
ethHCInFaults = _EthHCInFaults_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1, 3),
    _EthHCInFaults_Type()
)
ethHCInFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethHCInFaults.setStatus("current")
_EthHCOutFaults_Type = Counter64
_EthHCOutFaults_Object = MibTableColumn
ethHCOutFaults = _EthHCOutFaults_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1, 4),
    _EthHCOutFaults_Type()
)
ethHCOutFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethHCOutFaults.setStatus("current")
_EthHCBERErrors_Type = Counter64
_EthHCBERErrors_Object = MibTableColumn
ethHCBERErrors = _EthHCBERErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1, 5),
    _EthHCBERErrors_Type()
)
ethHCBERErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethHCBERErrors.setStatus("current")
_EthHCShortPacketErrors_Type = Counter64
_EthHCShortPacketErrors_Object = MibTableColumn
ethHCShortPacketErrors = _EthHCShortPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1, 6),
    _EthHCShortPacketErrors_Type()
)
ethHCShortPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethHCShortPacketErrors.setStatus("current")
_EthHCLongPacketErrors_Type = Counter64
_EthHCLongPacketErrors_Object = MibTableColumn
ethHCLongPacketErrors = _EthHCLongPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 2, 3, 1, 7),
    _EthHCLongPacketErrors_Type()
)
ethHCLongPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethHCLongPacketErrors.setStatus("current")
_EthConformance_ObjectIdentity = ObjectIdentity
ethConformance = _EthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3)
)
_EthGroups_ObjectIdentity = ObjectIdentity
ethGroups = _EthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 1)
)
_EthCompliances_ObjectIdentity = ObjectIdentity
ethCompliances = _EthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 2)
)

# Managed Objects groups

ethControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 1, 1)
)
ethControlGroup.setObjects(
      *(("ENDACE-ETH-MIB", "ethControlIndex"),
        ("ENDACE-ETH-MIB", "ethControlPeerLink"),
        ("ENDACE-ETH-MIB", "ethControlRemoteFault"),
        ("ENDACE-ETH-MIB", "ethControlPhysAddress"),
        ("ENDACE-ETH-MIB", "ethControlFCSThreshold"))
)
if mibBuilder.loadTexts:
    ethControlGroup.setStatus("current")

ethStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 1, 2)
)
ethStatsGroup.setObjects(
      *(("ENDACE-ETH-MIB", "ethStatsFCSErrors"),
        ("ENDACE-ETH-MIB", "ethStatsRemoteErrors"))
)
if mibBuilder.loadTexts:
    ethStatsGroup.setStatus("current")

ethHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 1, 3)
)
ethHCStatsGroup.setObjects(
      *(("ENDACE-ETH-MIB", "ethHCFCSErrors"),
        ("ENDACE-ETH-MIB", "ethHCInFaults"),
        ("ENDACE-ETH-MIB", "ethHCOutFaults"))
)
if mibBuilder.loadTexts:
    ethHCStatsGroup.setStatus("current")

ethHCStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 1, 4)
)
ethHCStatsGroup2.setObjects(
      *(("ENDACE-ETH-MIB", "ethHCBERErrors"),
        ("ENDACE-ETH-MIB", "ethHCShortPacketErrors"),
        ("ENDACE-ETH-MIB", "ethHCLongPacketErrors"),
        ("ENDACE-ETH-MIB", "ethStatsAlignmentErrors"))
)
if mibBuilder.loadTexts:
    ethHCStatsGroup2.setStatus("current")

ethControlGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 1, 5)
)
ethControlGroup2.setObjects(
      *(("ENDACE-ETH-MIB", "ethControlNIC"),
        ("ENDACE-ETH-MIB", "ethControlRemoteFault"),
        ("ENDACE-ETH-MIB", "ethControlLOF"),
        ("ENDACE-ETH-MIB", "ethControlLOS"))
)
if mibBuilder.loadTexts:
    ethControlGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ethCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 2, 3, 2, 1)
)
ethCompliance1.setObjects(
      *(("ENDACE-ETH-MIB", "ethControlGroup"),
        ("ENDACE-ETH-MIB", "ethStatsGroup"),
        ("ENDACE-ETH-MIB", "ethControlGroup2"),
        ("ENDACE-ETH-MIB", "ethHCStatsGroup"),
        ("ENDACE-ETH-MIB", "ethHCStatsGroup2"))
)
if mibBuilder.loadTexts:
    ethCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-ETH-MIB",
    **{"eth1": eth1,
       "ethControlTable": ethControlTable,
       "ethControlEntry": ethControlEntry,
       "ethControlIndex": ethControlIndex,
       "ethControlPeerLink": ethControlPeerLink,
       "ethControlRemoteFault": ethControlRemoteFault,
       "ethControlLOF": ethControlLOF,
       "ethControlLOS": ethControlLOS,
       "ethControlPhysAddress": ethControlPhysAddress,
       "ethControlNIC": ethControlNIC,
       "ethControlFCSThreshold": ethControlFCSThreshold,
       "ethStatsTable": ethStatsTable,
       "ethStatsEntry": ethStatsEntry,
       "ethStatsIndex": ethStatsIndex,
       "ethStatsFCSErrors": ethStatsFCSErrors,
       "ethStatsAlignmentErrors": ethStatsAlignmentErrors,
       "ethStatsRemoteErrors": ethStatsRemoteErrors,
       "ethHCStatsTable": ethHCStatsTable,
       "ethHCStatsEntry": ethHCStatsEntry,
       "ethHCStatsIndex": ethHCStatsIndex,
       "ethHCFCSErrors": ethHCFCSErrors,
       "ethHCInFaults": ethHCInFaults,
       "ethHCOutFaults": ethHCOutFaults,
       "ethHCBERErrors": ethHCBERErrors,
       "ethHCShortPacketErrors": ethHCShortPacketErrors,
       "ethHCLongPacketErrors": ethHCLongPacketErrors,
       "ethConformance": ethConformance,
       "ethGroups": ethGroups,
       "ethControlGroup": ethControlGroup,
       "ethStatsGroup": ethStatsGroup,
       "ethHCStatsGroup": ethHCStatsGroup,
       "ethHCStatsGroup2": ethHCStatsGroup2,
       "ethControlGroup2": ethControlGroup2,
       "ethCompliances": ethCompliances,
       "ethCompliance1": ethCompliance1,
       "endaceETHMIB": endaceETHMIB}
)
