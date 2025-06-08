# SNMP MIB module (ZYXEL-CPU-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-CPU-PROTECTION-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:26:15 2025
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelCpuProtection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelCpuProtectionSetup_ObjectIdentity = ObjectIdentity
zyxelCpuProtectionSetup = _ZyxelCpuProtectionSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1)
)
_ZyxelCpuProtectionTable_Object = MibTable
zyxelCpuProtectionTable = _ZyxelCpuProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelCpuProtectionTable.setStatus("current")
_ZyxelCpuProtectionEntry_Object = MibTableRow
zyxelCpuProtectionEntry = _ZyxelCpuProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1)
)
zyxelCpuProtectionEntry.setIndexNames(
    (0, "ZYXEL-CPU-PROTECTION-MIB", "zyCpuProtectionPort"),
    (0, "ZYXEL-CPU-PROTECTION-MIB", "zyCpuProtectionReasonType"),
)
if mibBuilder.loadTexts:
    zyxelCpuProtectionEntry.setStatus("current")
_ZyCpuProtectionPort_Type = Integer32
_ZyCpuProtectionPort_Object = MibTableColumn
zyCpuProtectionPort = _ZyCpuProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 1),
    _ZyCpuProtectionPort_Type()
)
zyCpuProtectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyCpuProtectionPort.setStatus("current")


class _ZyCpuProtectionReasonType_Type(Integer32):
    """Custom type zyCpuProtectionReasonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3))
    )


_ZyCpuProtectionReasonType_Type.__name__ = "Integer32"
_ZyCpuProtectionReasonType_Object = MibTableColumn
zyCpuProtectionReasonType = _ZyCpuProtectionReasonType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 2),
    _ZyCpuProtectionReasonType_Type()
)
zyCpuProtectionReasonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyCpuProtectionReasonType.setStatus("current")


class _ZyCpuProtectionRateLimit_Type(Integer32):
    """Custom type zyCpuProtectionRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ZyCpuProtectionRateLimit_Type.__name__ = "Integer32"
_ZyCpuProtectionRateLimit_Object = MibTableColumn
zyCpuProtectionRateLimit = _ZyCpuProtectionRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 3),
    _ZyCpuProtectionRateLimit_Type()
)
zyCpuProtectionRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCpuProtectionRateLimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-CPU-PROTECTION-MIB",
    **{"zyxelCpuProtection": zyxelCpuProtection,
       "zyxelCpuProtectionSetup": zyxelCpuProtectionSetup,
       "zyxelCpuProtectionTable": zyxelCpuProtectionTable,
       "zyxelCpuProtectionEntry": zyxelCpuProtectionEntry,
       "zyCpuProtectionPort": zyCpuProtectionPort,
       "zyCpuProtectionReasonType": zyCpuProtectionReasonType,
       "zyCpuProtectionRateLimit": zyCpuProtectionRateLimit}
)
