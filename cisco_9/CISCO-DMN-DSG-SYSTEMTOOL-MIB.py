# SNMP MIB module (CISCO-DMN-DSG-SYSTEMTOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DMN-DSG-SYSTEMTOOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:04:33 2025
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGSystemTool = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8)
)
if mibBuilder.loadTexts:
    ciscoDSGSystemTool.setRevisions(
        ("2010-08-03 09:00",
         "2009-12-20 15:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemTool_ObjectIdentity = ObjectIdentity
systemTool = _SystemTool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1)
)


class _SystemToolBanner_Type(Integer32):
    """Custom type systemToolBanner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SystemToolBanner_Type.__name__ = "Integer32"
_SystemToolBanner_Object = MibScalar
systemToolBanner = _SystemToolBanner_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 1),
    _SystemToolBanner_Type()
)
systemToolBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemToolBanner.setStatus("current")


class _SystemToolReboot_Type(Integer32):
    """Custom type systemToolReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_SystemToolReboot_Type.__name__ = "Integer32"
_SystemToolReboot_Object = MibScalar
systemToolReboot = _SystemToolReboot_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 2),
    _SystemToolReboot_Type()
)
systemToolReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemToolReboot.setStatus("current")


class _SystemToolFactoryReset_Type(Integer32):
    """Custom type systemToolFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_SystemToolFactoryReset_Type.__name__ = "Integer32"
_SystemToolFactoryReset_Object = MibScalar
systemToolFactoryReset = _SystemToolFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 3),
    _SystemToolFactoryReset_Type()
)
systemToolFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemToolFactoryReset.setStatus("current")


class _SystemToolCleanUnusedTables_Type(Integer32):
    """Custom type systemToolCleanUnusedTables based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_SystemToolCleanUnusedTables_Type.__name__ = "Integer32"
_SystemToolCleanUnusedTables_Object = MibScalar
systemToolCleanUnusedTables = _SystemToolCleanUnusedTables_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 4),
    _SystemToolCleanUnusedTables_Type()
)
systemToolCleanUnusedTables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemToolCleanUnusedTables.setStatus("current")


class _SystemToolCAMode_Type(Integer32):
    """Custom type systemToolCAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("open", 2))
    )


_SystemToolCAMode_Type.__name__ = "Integer32"
_SystemToolCAMode_Object = MibScalar
systemToolCAMode = _SystemToolCAMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 5),
    _SystemToolCAMode_Type()
)
systemToolCAMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemToolCAMode.setStatus("current")


class _SystemToolClearLogs_Type(Integer32):
    """Custom type systemToolClearLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_SystemToolClearLogs_Type.__name__ = "Integer32"
_SystemToolClearLogs_Object = MibScalar
systemToolClearLogs = _SystemToolClearLogs_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 6),
    _SystemToolClearLogs_Type()
)
systemToolClearLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemToolClearLogs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-SYSTEMTOOL-MIB",
    **{"ciscoDSGSystemTool": ciscoDSGSystemTool,
       "systemTool": systemTool,
       "systemToolBanner": systemToolBanner,
       "systemToolReboot": systemToolReboot,
       "systemToolFactoryReset": systemToolFactoryReset,
       "systemToolCleanUnusedTables": systemToolCleanUnusedTables,
       "systemToolCAMode": systemToolCAMode,
       "systemToolClearLogs": systemToolClearLogs}
)
