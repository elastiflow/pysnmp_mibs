# SNMP MIB module (ONEFS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/isilon_12124/ONEFS-TRAP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:26:34 2025
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

(TimeTicks64,
 onefs) = mibBuilder.importSymbols(
    "ONEFS-MIB",
    "TimeTicks64",
    "onefs")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oneFSTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 251)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OneFSTrapByPriority_ObjectIdentity = ObjectIdentity
oneFSTrapByPriority = _OneFSTrapByPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 251, 1)
)
_OneFSTrapByFacility_ObjectIdentity = ObjectIdentity
oneFSTrapByFacility = _OneFSTrapByFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2)
)

# Managed Objects groups


# Notification objects

oneFSTrapCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 1, 1)
)
if mibBuilder.loadTexts:
    oneFSTrapCrit.setStatus(
        "current"
    )

oneFSTrapWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 1, 2)
)
if mibBuilder.loadTexts:
    oneFSTrapWarn.setStatus(
        "current"
    )

oneFSTrapInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 1, 3)
)
if mibBuilder.loadTexts:
    oneFSTrapInfo.setStatus(
        "current"
    )

oneFSTrapEmrg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 1, 4)
)
if mibBuilder.loadTexts:
    oneFSTrapEmrg.setStatus(
        "current"
    )

oneFSTrapDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 1)
)
if mibBuilder.loadTexts:
    oneFSTrapDefault.setStatus(
        "current"
    )

oneFSTrapNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 2)
)
if mibBuilder.loadTexts:
    oneFSTrapNode.setStatus(
        "current"
    )

oneFSTrapWindowsNetworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 3)
)
if mibBuilder.loadTexts:
    oneFSTrapWindowsNetworking.setStatus(
        "current"
    )

oneFSTrapProcesses = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 4)
)
if mibBuilder.loadTexts:
    oneFSTrapProcesses.setStatus(
        "current"
    )

oneFSTrapPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 5)
)
if mibBuilder.loadTexts:
    oneFSTrapPower.setStatus(
        "current"
    )

oneFSTrapSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 6)
)
if mibBuilder.loadTexts:
    oneFSTrapSpace.setStatus(
        "current"
    )

oneFSTrapRestripe = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 7)
)
if mibBuilder.loadTexts:
    oneFSTrapRestripe.setStatus(
        "current"
    )

oneFSTrapGeneral = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 8)
)
if mibBuilder.loadTexts:
    oneFSTrapGeneral.setStatus(
        "current"
    )

oneFSTrapNVRAM = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 9)
)
if mibBuilder.loadTexts:
    oneFSTrapNVRAM.setStatus(
        "current"
    )

oneFSTrapTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 10)
)
if mibBuilder.loadTexts:
    oneFSTrapTemp.setStatus(
        "current"
    )

oneFSTrapFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 11)
)
if mibBuilder.loadTexts:
    oneFSTrapFan.setStatus(
        "current"
    )

oneFSTrapFilesystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 12)
)
if mibBuilder.loadTexts:
    oneFSTrapFilesystem.setStatus(
        "current"
    )

oneFSTrapDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 13)
)
if mibBuilder.loadTexts:
    oneFSTrapDisk.setStatus(
        "current"
    )

oneFSTrapCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 14)
)
if mibBuilder.loadTexts:
    oneFSTrapCPU.setStatus(
        "current"
    )

oneFSTrapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 15)
)
if mibBuilder.loadTexts:
    oneFSTrapTest.setStatus(
        "current"
    )

oneFSTrapLicensing = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 16)
)
if mibBuilder.loadTexts:
    oneFSTrapLicensing.setStatus(
        "current"
    )

oneFSTrapSnapshots = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 17)
)
if mibBuilder.loadTexts:
    oneFSTrapSnapshots.setStatus(
        "current"
    )

oneFSTrapSmartQuotas = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 251, 2, 18)
)
if mibBuilder.loadTexts:
    oneFSTrapSmartQuotas.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEFS-TRAP-MIB",
    **{"oneFSTraps": oneFSTraps,
       "oneFSTrapByPriority": oneFSTrapByPriority,
       "oneFSTrapCrit": oneFSTrapCrit,
       "oneFSTrapWarn": oneFSTrapWarn,
       "oneFSTrapInfo": oneFSTrapInfo,
       "oneFSTrapEmrg": oneFSTrapEmrg,
       "oneFSTrapByFacility": oneFSTrapByFacility,
       "oneFSTrapDefault": oneFSTrapDefault,
       "oneFSTrapNode": oneFSTrapNode,
       "oneFSTrapWindowsNetworking": oneFSTrapWindowsNetworking,
       "oneFSTrapProcesses": oneFSTrapProcesses,
       "oneFSTrapPower": oneFSTrapPower,
       "oneFSTrapSpace": oneFSTrapSpace,
       "oneFSTrapRestripe": oneFSTrapRestripe,
       "oneFSTrapGeneral": oneFSTrapGeneral,
       "oneFSTrapNVRAM": oneFSTrapNVRAM,
       "oneFSTrapTemp": oneFSTrapTemp,
       "oneFSTrapFan": oneFSTrapFan,
       "oneFSTrapFilesystem": oneFSTrapFilesystem,
       "oneFSTrapDisk": oneFSTrapDisk,
       "oneFSTrapCPU": oneFSTrapCPU,
       "oneFSTrapTest": oneFSTrapTest,
       "oneFSTrapLicensing": oneFSTrapLicensing,
       "oneFSTrapSnapshots": oneFSTrapSnapshots,
       "oneFSTrapSmartQuotas": oneFSTrapSmartQuotas}
)
