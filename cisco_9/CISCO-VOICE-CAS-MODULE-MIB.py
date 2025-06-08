# SNMP MIB module (CISCO-VOICE-CAS-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-VOICE-CAS-MODULE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:40 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVoiceCasModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 389)
)
if mibBuilder.loadTexts:
    ciscoVoiceCasModuleMIB.setRevisions(
        ("2004-03-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CvcmCasPatternBitPosition(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dBit", 0),
          ("cBit", 1),
          ("bBit", 2),
          ("aBit", 3))
    )


class CvcmCasBitAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("casBitNoAction", 1),
          ("casBitSetToZero", 2),
          ("casBitSetToOne", 3),
          ("casBitInvertBit", 4),
          ("casBitInvertABit", 5),
          ("casBitInvertBBit", 6),
          ("casBitInvertCBit", 7),
          ("casBitInvertDBit", 8),
          ("casBitABit", 9),
          ("casBitBBit", 10),
          ("casBitCBit", 11),
          ("casBitDBit", 12))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVoiceCasModuleNotifs_ObjectIdentity = ObjectIdentity
ciscoVoiceCasModuleNotifs = _CiscoVoiceCasModuleNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 0)
)
_CiscoVoiceCasModuleObjects_ObjectIdentity = ObjectIdentity
ciscoVoiceCasModuleObjects = _CiscoVoiceCasModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1)
)
_CvcmCasConfig_ObjectIdentity = ObjectIdentity
cvcmCasConfig = _CvcmCasConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1)
)
_CvcmABCDBitTemplateConfigTable_Object = MibTable
cvcmABCDBitTemplateConfigTable = _CvcmABCDBitTemplateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvcmABCDBitTemplateConfigTable.setStatus("current")
_CvcmABCDBitTemplateConfigEntry_Object = MibTableRow
cvcmABCDBitTemplateConfigEntry = _CvcmABCDBitTemplateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1)
)
cvcmABCDBitTemplateConfigEntry.setIndexNames(
    (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmModuleIndex"),
    (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateIndex"),
    (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDPatternIndex"),
)
if mibBuilder.loadTexts:
    cvcmABCDBitTemplateConfigEntry.setStatus("current")


class _CvcmModuleIndex_Type(Unsigned32):
    """Custom type cvcmModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvcmModuleIndex_Type.__name__ = "Unsigned32"
_CvcmModuleIndex_Object = MibTableColumn
cvcmModuleIndex = _CvcmModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 1),
    _CvcmModuleIndex_Type()
)
cvcmModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvcmModuleIndex.setStatus("current")


class _CvcmCasTemplateIndex_Type(Unsigned32):
    """Custom type cvcmCasTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvcmCasTemplateIndex_Type.__name__ = "Unsigned32"
_CvcmCasTemplateIndex_Object = MibTableColumn
cvcmCasTemplateIndex = _CvcmCasTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 2),
    _CvcmCasTemplateIndex_Type()
)
cvcmCasTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvcmCasTemplateIndex.setStatus("current")


class _CvcmABCDPatternIndex_Type(Unsigned32):
    """Custom type cvcmABCDPatternIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CvcmABCDPatternIndex_Type.__name__ = "Unsigned32"
_CvcmABCDPatternIndex_Object = MibTableColumn
cvcmABCDPatternIndex = _CvcmABCDPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 3),
    _CvcmABCDPatternIndex_Type()
)
cvcmABCDPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvcmABCDPatternIndex.setStatus("current")
_CvcmModulePhysicalIndex_Type = EntPhysicalIndexOrZero
_CvcmModulePhysicalIndex_Object = MibTableColumn
cvcmModulePhysicalIndex = _CvcmModulePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 4),
    _CvcmModulePhysicalIndex_Type()
)
cvcmModulePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcmModulePhysicalIndex.setStatus("current")
_CvcmCasTemplateName_Type = SnmpAdminString
_CvcmCasTemplateName_Object = MibTableColumn
cvcmCasTemplateName = _CvcmCasTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 5),
    _CvcmCasTemplateName_Type()
)
cvcmCasTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcmCasTemplateName.setStatus("current")
_CvcmABCDIncomingPattern_Type = CvcmCasPatternBitPosition
_CvcmABCDIncomingPattern_Object = MibTableColumn
cvcmABCDIncomingPattern = _CvcmABCDIncomingPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 6),
    _CvcmABCDIncomingPattern_Type()
)
cvcmABCDIncomingPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcmABCDIncomingPattern.setStatus("current")
_CvcmABCDOutgoingPattern_Type = CvcmCasPatternBitPosition
_CvcmABCDOutgoingPattern_Object = MibTableColumn
cvcmABCDOutgoingPattern = _CvcmABCDOutgoingPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 7),
    _CvcmABCDOutgoingPattern_Type()
)
cvcmABCDOutgoingPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvcmABCDOutgoingPattern.setStatus("current")


class _CvcmCasABitAction_Type(CvcmCasBitAction):
    """Custom type cvcmCasABitAction based on CvcmCasBitAction"""
    defaultValue = 9


_CvcmCasABitAction_Type.__name__ = "CvcmCasBitAction"
_CvcmCasABitAction_Object = MibTableColumn
cvcmCasABitAction = _CvcmCasABitAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 8),
    _CvcmCasABitAction_Type()
)
cvcmCasABitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcmCasABitAction.setStatus("current")


class _CvcmCasBBitAction_Type(CvcmCasBitAction):
    """Custom type cvcmCasBBitAction based on CvcmCasBitAction"""
    defaultValue = 10


_CvcmCasBBitAction_Type.__name__ = "CvcmCasBitAction"
_CvcmCasBBitAction_Object = MibTableColumn
cvcmCasBBitAction = _CvcmCasBBitAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 9),
    _CvcmCasBBitAction_Type()
)
cvcmCasBBitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcmCasBBitAction.setStatus("current")


class _CvcmCasCBitAction_Type(CvcmCasBitAction):
    """Custom type cvcmCasCBitAction based on CvcmCasBitAction"""
    defaultValue = 11


_CvcmCasCBitAction_Type.__name__ = "CvcmCasBitAction"
_CvcmCasCBitAction_Object = MibTableColumn
cvcmCasCBitAction = _CvcmCasCBitAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 10),
    _CvcmCasCBitAction_Type()
)
cvcmCasCBitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcmCasCBitAction.setStatus("current")


class _CvcmCasDBitAction_Type(CvcmCasBitAction):
    """Custom type cvcmCasDBitAction based on CvcmCasBitAction"""
    defaultValue = 12


_CvcmCasDBitAction_Type.__name__ = "CvcmCasBitAction"
_CvcmCasDBitAction_Object = MibTableColumn
cvcmCasDBitAction = _CvcmCasDBitAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 11),
    _CvcmCasDBitAction_Type()
)
cvcmCasDBitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcmCasDBitAction.setStatus("current")
_CvcmCasBitRowStatus_Type = RowStatus
_CvcmCasBitRowStatus_Object = MibTableColumn
cvcmCasBitRowStatus = _CvcmCasBitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 12),
    _CvcmCasBitRowStatus_Type()
)
cvcmCasBitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvcmCasBitRowStatus.setStatus("current")
_CvcmMIBConformance_ObjectIdentity = ObjectIdentity
cvcmMIBConformance = _CvcmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 2)
)
_CvcmMIBGroups_ObjectIdentity = ObjectIdentity
cvcmMIBGroups = _CvcmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1)
)
_CvcmMIBCompliances_ObjectIdentity = ObjectIdentity
cvcmMIBCompliances = _CvcmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2)
)

# Managed Objects groups

cvcmCasBitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1, 1)
)
cvcmCasBitGroup.setObjects(
      *(("CISCO-VOICE-CAS-MODULE-MIB", "cvcmModulePhysicalIndex"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateName"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDIncomingPattern"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDOutgoingPattern"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasABitAction"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBBitAction"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasCBitAction"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasDBitAction"),
        ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitRowStatus"))
)
if mibBuilder.loadTexts:
    cvcmCasBitGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVoiceCasModuleMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2, 1)
)
ciscoVoiceCasModuleMIBCompliance.setObjects(
    ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitGroup")
)
if mibBuilder.loadTexts:
    ciscoVoiceCasModuleMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-CAS-MODULE-MIB",
    **{"CvcmCasPatternBitPosition": CvcmCasPatternBitPosition,
       "CvcmCasBitAction": CvcmCasBitAction,
       "ciscoVoiceCasModuleMIB": ciscoVoiceCasModuleMIB,
       "ciscoVoiceCasModuleNotifs": ciscoVoiceCasModuleNotifs,
       "ciscoVoiceCasModuleObjects": ciscoVoiceCasModuleObjects,
       "cvcmCasConfig": cvcmCasConfig,
       "cvcmABCDBitTemplateConfigTable": cvcmABCDBitTemplateConfigTable,
       "cvcmABCDBitTemplateConfigEntry": cvcmABCDBitTemplateConfigEntry,
       "cvcmModuleIndex": cvcmModuleIndex,
       "cvcmCasTemplateIndex": cvcmCasTemplateIndex,
       "cvcmABCDPatternIndex": cvcmABCDPatternIndex,
       "cvcmModulePhysicalIndex": cvcmModulePhysicalIndex,
       "cvcmCasTemplateName": cvcmCasTemplateName,
       "cvcmABCDIncomingPattern": cvcmABCDIncomingPattern,
       "cvcmABCDOutgoingPattern": cvcmABCDOutgoingPattern,
       "cvcmCasABitAction": cvcmCasABitAction,
       "cvcmCasBBitAction": cvcmCasBBitAction,
       "cvcmCasCBitAction": cvcmCasCBitAction,
       "cvcmCasDBitAction": cvcmCasDBitAction,
       "cvcmCasBitRowStatus": cvcmCasBitRowStatus,
       "cvcmMIBConformance": cvcmMIBConformance,
       "cvcmMIBGroups": cvcmMIBGroups,
       "cvcmCasBitGroup": cvcmCasBitGroup,
       "cvcmMIBCompliances": cvcmMIBCompliances,
       "ciscoVoiceCasModuleMIBCompliance": ciscoVoiceCasModuleMIBCompliance}
)
